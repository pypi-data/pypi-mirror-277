from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTImage
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
import re
from typing import BinaryIO, cast, Optional, List, Dict, Any, Tuple
from pdf2image import convert_from_path, pdfinfo_from_path
import tempfile
from flexidata.models.base import get_model
from PIL import Image
import layoutparser as lp
from flexidata.utils.constants import (
    ParserMethod,
    FileType,
    Patterns,
    FileReaderSource,
    EXTRACTIONSOURCE,
)
from flexidata.utils.pdf import rect_to_bbox, normalize_whitespace
from pdfminer.pdftypes import PDFObjRef
from flexidata.Logger import Logger
from flexidata.reader.factory import get_file_reader
from flexidata.ocr.agent import OCRAgentFactory
from pdfminer.layout import LTContainer
import numpy as np
from PIL import Image
from flexidata.text_processing.text_block import TextBlock, TextBlockMetadata
from flexidata.reader.handlers import FileHandler
from PIL import Image as PILImage
from flexidata.utils.constants import FileType
from flexidata.utils.decorators import validate_file_type_method


logger = Logger()

PDF_LOSSY_COMPRESSION_FILTERS = ["DCTDecode", "DCT", "JPXDecode"]
PDF_LOSSLESS_COMPRESSION_FILTERS = [
    "LZWDecode",
    "LZW",
    "FlateDecode",
    "Fl",
    "ASCII85Decode",
    "A85",
    "ASCIIHexDecode",
    "AHx",
    "RunLengthDecode",
    "RL",
    "CCITTFaxDecode",
    "CCF",
    "JBIG2Decode",
]


class PDFParser(FileHandler):
    """_summary_"""

    def __init__(
        self,
        file_path: Optional[str] = None,
        file_url: Optional[str] = None,
        source: FileReaderSource = FileReaderSource.LOCAL,
        method: ParserMethod = ParserMethod.AUTO,
        extract_table: bool = False,
        extract_image: bool = False,
        bucket_name: Optional[str] = None,
        file_key: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Initialize the PDF parser with specified parameters.

        Args:
            file_path (Optional[str]): Local path to the PDF file.
            file_url (Optional[str]): URL to a PDF file for web-based reading.
            source (FileReaderSource): The source type of the file.
            method (ParserMethod): The parsing method to be used.
            extract_table (bool): Flag to indicate if tables should be extracted.
            extract_image (bool): Flag to indicate if images should be extracted.
            output_folder (Optional[str]): Folder path for storing output.
            bucket_name (Optional[str]): Name of the S3 bucket (for S3 sources).
            file_key (Optional[str]): File key within the S3 bucket.
            **kwargs: Additional keyword arguments for future extensibility.
        """
        super().__init__(source, file_path, file_url, bucket_name, file_key)
        self.pdf_resource_manager = PDFResourceManager()
        self.la_params = LAParams()
        try:
            self.device = PDFPageAggregator(
                self.pdf_resource_manager, laparams=self.la_params
            )
            self.interpreter = PDFPageInterpreter(
                self.pdf_resource_manager, self.device
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize PDF parsing resources: {str(e)}")
        self.method = method
        self.starting_page_number = 1
        self.extract_table = extract_table
        self.extract_image = extract_image
        self.text_extractable = False

    def set_parser_auto_method(self):
        """
        Automatically sets the parsing method based on the content characteristics of the PDF.

        This method determines the optimal parsing method by evaluating whether the PDF contains
        images or tables that need extraction or whether text is readily extractable. It sets the
        parsing method to MODEL if image or table extraction is necessary, to FAST if text is
        easily extractable, and to OCR if the text is not directly extractable (likely due to
        text being embedded within images).

        Returns:
            ParserMethod: The determined parser method (e.g., MODEL, FAST, OCR) after evaluating the PDF content.
        """
        # Determine the parsing method based on the presence of images or tables
        if self.extract_image or self.extract_table:
            self.method = (
                ParserMethod.MODEL
            )  # Use MODEL method for complex content like images/tables
        # If text is extractable, set to FAST for quick text extraction
        elif self.text_extractable:
            self.method = ParserMethod.FAST
        # If no text is directly extractable, fall back to OCR
        else:
            self.method = ParserMethod.OCR

        return self.method  # Return the selected method
    
    @validate_file_type_method([FileType.PDF])
    def parse(self, extract_image: bool = False) -> List[List[Dict[str, Any]]]:
        """
        Parses the document based on the specified method set in `self.method`.

        Args:
            extract_image (bool): If True, image extraction mode is enabled.

        Returns:
           List[List[Dict[str, Any]]]: A list of elements parsed from the document according to the chosen parser method.
        """
        if extract_image:
            self.extract_image = extract_image

        elements: List[List[Dict[str, Any]]] = []

        if self.method == ParserMethod.AUTO:
            self.set_parser_auto_method()

        if self.source is not FileReaderSource.LOCAL:
            self.file_path = self.create_temp_file(cast(BinaryIO, self.get_file_content()))

        if self.method == ParserMethod.FAST:
            self.text_extractable, elements = self.parse_by_pdfminer()
        elif self.method == ParserMethod.MODEL:
            elements = self.parse_by_model()
        elif self.method == ParserMethod.OCR:
            elements = self.parse_by_ocr()
        
        if self.source is not FileReaderSource.LOCAL:
            self._delete_temp_file(self.file_path)
        return elements

    def parse_by_model(self, is_image=False):
        """_summary_"""
        pages_image = self.convert_pdf_to_image(self.file_path, self.output_folder)
        self.process_images(pages_image=pages_image)

    def parse_by_ocr(self, is_image: bool = False) -> List[List[TextBlock]]:
        """
        Parses the PDF by converting it to images and applying OCR to extract text elements.
        If 'is_image' is set to True, treats the source file as an image directly instead of a PDF.

        Args:
            is_image (bool): Flag indicating whether the source file is an image.

        Returns:
            List[List[TextBlock]]: A nested list where each sublist represents OCR'd text blocks
            from each page or image, along with their metadata.
        """
        ocr_factory = OCRAgentFactory()
        ocr_agent = ocr_factory.get_ocr_agent()  # Get the OCR agent instance
        elements: List[List[TextBlock]] = (
            []
        )  # Initialize the list to hold all OCR'd elements

        # Handle direct image OCR if the source file is an image
        if is_image:
            if self.source is not FileReaderSource.LOCAL:
                self.file_path = self.create_temp_file(cast(BinaryIO, self.get_file_content()))
            images = []
            image = PILImage.open(self.file_path)
            images.append(image)
            for page_number, image in enumerate(images, start=1):
                page_elements = ocr_agent.image_to_text(
                    np.array(image),
                    lang="eng",
                    page_number=page_number,
                    file_path=self.get_file_path_by_source(),
                    filetype=FileType.PDF,
                )
                elements.append(page_elements)
            if self.source is not FileReaderSource.LOCAL:
                self._delete_temp_file(self.file_path)
        else:
            # Process each page of the PDF converted to images
            # Enumerate over each image page, starting from the specified page number
            for page_number, image in enumerate(
                self.convert_pdf_to_image(), start=self.starting_page_number
            ):
                # Convert image to numpy array and perform OCR
                page_elements = ocr_agent.image_to_text(
                    np.array(image),
                    lang="eng",
                    page_number=page_number,
                    file_path=self.get_file_path_by_source(),
                    filetype=FileType.PDF,
                )
                elements.append(page_elements)
        return elements

    def get_pdf_info(self):
        """
        Get the information about the PDF file.

        Returns:
            dict: A dictionary containing the PDF file information.
        """
        return pdfinfo_from_path(self.file_path)

    def convert_pdf_to_image(self, pages_per_chunk=10):
        """
        Convert PDF file to images in chunks, yielding images page by page.

        This method divides the PDF into chunks of pages and converts each chunk into images,
        which are then yielded one at a time. This is useful for processing large PDFs or
        when memory management is a concern.

        Args:
            pages_per_chunk (int): Number of pages to process in each chunk.

        Yields:
            str: Path to the converted image if output_folder is specified, else PIL image object.
        """
        pdf_info = self.get_pdf_info()

        # Iterate over each chunk of pages
        for start_page in range(1, pdf_info["Pages"] + 1, pages_per_chunk):
            end_page = min(start_page + pages_per_chunk - 1, pdf_info["Pages"])

            # Convert pages from start_page to end_page
            if self.output_folder:
                # Store images directly to the specified folder and return paths
                page_images = convert_from_path(
                    self.file_path,
                    output_folder=self.output_folder,
                    paths_only=True,
                    first_page=start_page,
                    last_page=end_page,
                )
            else:
                # Return image objects directly
                page_images = convert_from_path(
                    self.file_path, first_page=start_page, last_page=end_page
                )

            # Yield each image from the current chunk
            for image in page_images:
                yield image

    def process_images(self, pages_image):
        """_summary_

        Args:
            pages_image (_type_): _description_
        """
        model = get_model()
        for image_path in pages_image:
            print(image_path)
            with Image.open(image_path) as image:
                layouts = model.predict(image)
                lp.draw_box(image, layouts, box_width=3).save(
                    image_path.replace(".ppm", ".png")
                )

    def annotation_resolve(self, annotation):
        """
        Resolves a PDF annotation object, typically used to dereference indirect objects to their direct values.

        In PDF processing, many objects like annotations can be indirect references. This method attempts
        to resolve such references to their actual content. If the resolution fails due to any error (e.g.,
        the object is not an indirect object or the resolution process encounters an issue), it safely
        returns the original object.

        Args:
            annotation (PDFObjRef or any PDF object): The PDF annotation or object to resolve.

        Returns:
            PDF object: The resolved PDF object if possible, or the original object if resolution fails.
        """
        try:
            # Attempt to resolve the annotation to its direct object.
            return annotation.resolve()
        except:
            # Return the original annotation if the resolve attempt fails.
            return annotation

    def get_urls(self, annots, page_number, height):
        """
        Extracts URLs from PDF annotations on a given page.

        This method iterates through annotation objects in the PDF, filtering for link annotations,
        resolving references as needed, and extracting URL details. It returns a list of dictionaries,
        each containing the URL, its bounding box, the annotation type, and the page number.

        Args:
            annots (list): A list of annotation objects from a PDF page.
            page_number (int): The number of the current PDF page being processed.
            height (int): The height of the PDF page, needed for coordinate transformations.

        Returns:
            list: A list of dictionaries with details about each URL found in the annotations.
        """
        url = ""  # Initialize an empty string for URLs.
        annot_list = []  # List to hold the details of each URL annotation.

        for annot in annots:
            # Resolve the annotation to a dictionary to access its properties.
            annotation_dict = self.annotation_resolve(annot)

            # Get the subtype of the annotation to filter for link annotations.
            sub_type = annotation_dict.get("Subtype", None)
            # Get the rectangle which specifies the annotation's position on the page.
            rect = annotation_dict.get("Rect", None)

            # Continue to next annotation if it's not a link or if the rectangle is not well defined.
            if isinstance(sub_type, PDFObjRef) or str(sub_type) != "/'Link'":
                continue
            if not rect or isinstance(rect, PDFObjRef) or len(rect) != 4:
                continue

            # Convert PDF rectangle to a bounding box with coordinates adjusted for a top-left origin.
            x1, y1, x2, y2 = rect_to_bbox(rect, height)

            # Check if there is an action associated with the annotation; skip if not.
            if "A" not in annotation_dict:
                continue

            # Resolve the action dictionary from the annotation.
            url_dict = self.annotation_resolve(annotation_dict["A"])
            url_type = None

            # Determine the type of action (e.g., URI link or internal document link).
            if "S" in url_dict and not isinstance(url_dict["S"], PDFObjRef):
                url_type = str(url_dict["S"])

            url = None  # Reset URL for each annotation.
            try:
                # Extract the URL if the action type is a URI.
                if url_type == "/'URI'":
                    url = self.annotation_resolve(
                        self.annotation_resolve(url_dict["URI"])
                    ).decode("utf-8")

                # Handle internal document links if the action type is 'GoTo'.
                if url_type == "/'GoTo'":
                    url = self.annotation_resolve(
                        self.annotation_resolve(url_dict["D"])
                    ).decode("utf-8")
            except Exception as e:
                # Print any exceptions encountered while resolving URLs.
                print(e)
                pass

            # Append the URL and its details to the list.
            annot_list.append(
                {
                    "url": url,
                    "bbox": (x1, y1, x2, y2),
                    "type": url_type,
                    "page_number": page_number,
                }
            )

        return annot_list  # Return the list of URLs and their details.

    def extract_text_from_img_with_rapidocr(self, images):
        """
        Extracts text from a list of image objects using the RapidOCR library, which is based
        on the ONNX runtime.

        This function dynamically imports the RapidOCR library, initializes the OCR engine,
        and processes each image to extract text. The extracted text from all images is concatenated
        and returned as a single string, with each image's text separated by a newline.

        Args:
            images (list): A list of image objects that the OCR should process.

        Returns:
            str: A string containing the concatenated text extracted from all images.

        Raises:
            ImportError: If the `rapidocr-onnxruntime` package is not installed.
        """
        try:
            # Attempt to import the RapidOCR library
            from rapidocr_onnxruntime import RapidOCR
        except ImportError:
            # Raise an informative error if the library is not installed
            raise ImportError(
                "`rapidocr-onnxruntime` package not found, please install it with "
                "`pip install rapidocr-onnxruntime`"
            )

        # Initialize the OCR engine
        ocr_engine = RapidOCR()
        text = ""  # Initialize a string to accumulate the results

        for img in images:
            # Process each image with the OCR engine
            result, _ = ocr_engine(img)
            if result:
                # Extract text from the results, result is a list of tuples where the second element is the text
                result = [text[1] for text in result]
                # Join all recognized text segments from this image and append to the overall text
                text += "\n".join(result)

        # Return the concatenated text from all images
        return text

    def parse_by_pdfminer(self)-> Tuple[bool, List[List[TextBlock]]]:
        """
        Parses the PDF file using pdfminer, extracting text blocks and their metadata.

        Returns:
            Tuple[bool, List[List[TextBlock]]]: A tuple containing a boolean indicating if text was extractable,
            and a list of lists of TextBlock instances for each page.
        """
        text_extractable = False
        elements = []
        fp = cast(BinaryIO, self.get_file_content())
        for page_number, (page, page_layout) in enumerate(
            self.get_pdfminer_pages(fp), start=self.starting_page_number
        ):
            page_elements = []
            width, height = page_layout.width, page_layout.height
            # if page.annots:
            #     logger.info(f"page_number={page_number} has a annotation")
            #     urls = self.get_urls(page.annots, page_number, height)
            for element_obj in page_layout:
                element_bbox = rect_to_bbox(element_obj.bbox, height)
                if hasattr(element_obj, "get_text"):
                    texts = [element_obj.get_text()]
                else:
                    text = self.extract_text(element_obj)
                    texts = re.split(Patterns.WHITESPACE_NEWLINE_PATTERN, text)
                for text in texts:
                    text = normalize_whitespace(text)
                    if text:
                        metadata = TextBlockMetadata(
                            file_path=self.get_file_path_by_source(),
                            languages=["eng"],
                            filetype=FileType.PDF,
                            page_number=page_number,
                            bbox=element_bbox,
                            layout_height=height,
                            layout_width=width,
                            extraction_source=EXTRACTIONSOURCE.PDF_MINER,
                        )
                        element = TextBlock(text=text, metadata=metadata)
                        text_extractable = True
                        page_elements.append(element)
            elements.append(page_elements)
        return text_extractable, elements

    def extract_text(self, element):
        """
        Recursively extract text from a layout element of a PDF page.

        This function checks the type of the element and appropriately extracts text. If the element
        has the 'get_text' method, it directly returns the text. For container elements (LTContainer),
        it recursively accumulates text from all child elements. If the element does not contain text
        or is neither a text element, container, it returns a newline as a placeholder.

        Args:
            element (LTItem): The layout element from which to extract text.

        Returns:
            str: The extracted text from the element, including all child elements, or a newline for non-textual.
        """
        # Check if the element has the 'get_text' method (likely an LTText element)
        if hasattr(element, "get_text"):
            return element.get_text()

        elif self.extract_image and isinstance(element, LTImage):
            if element.stream["Filter"].name in PDF_LOSSY_COMPRESSION_FILTERS:
                image_text = self.extract_text_from_img_with_rapidocr(
                    [element.stream.get_data()]
                )
                logger.info(
                    f"Extracted text from image with potential data loss: {image_text}"
                )
                return image_text
            elif element.stream["Filter"].name in PDF_LOSSLESS_COMPRESSION_FILTERS:
                image_data = np.frombuffer(element.stream.get_data(), dtype=np.uint8)
                image_data = image_data.reshape(
                    element.stream["Height"], element.stream["Width"], -1
                )
                image_text = self.extract_text_from_img_with_rapidocr([image_data])
                logger.info(f"Extracted text from lossless image: {image_text}")
                return image_text
            else:
                return "\n"

        # If the element is a container, recurse on its children to accumulate text
        elif isinstance(element, LTContainer):
            text = ""  # Initialize an empty string to collect text
            for child_element in element:
                # Recursively accumulate text from child elements, adding nothing if None
                text += self.extract_text(child_element) or ""
            return text

        # Return a newline for elements that are neither text elements nor containers
        return "\n"

    def get_pdfminer_pages(self, fp):
        """
        Extract pages and their layouts from a PDF file using PDFMiner.

        This function iterates through each page of a PDF file, processes it to extract
        layout information, and yields both the page and its layout.

        Args:
            fp (file object): A file-like object representing the PDF file.

        Yields:
            tuple: A tuple containing a PDFPage object and its corresponding layout object.
        """
        try:
            pages = PDFPage.get_pages(fp)
            for index, page in enumerate(pages):
                try:
                    self.interpreter.process_page(page)
                    page_layout = self.device.get_result()
                    yield page, page_layout
                except Exception as e:
                    logger.error(f"Error processing page {index + 1}: {e}")
                continue
        except Exception as e:
            raise IOError(f"Failed to read or process PDF file: {str(e)}")
