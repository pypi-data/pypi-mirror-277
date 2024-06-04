from typing import BinaryIO, cast, Optional, List, Any, Dict, Union
from flexidata.utils.constants import FileReaderSource, FileType
from flexidata.reader.handlers import FileHandler
import docx
from flexidata.text_processing.text_block import TextBlockMetadata, TextBlock
from flexidata.text_processing.classification import TextType
from flexidata.ocr.agent import OCRAgentFactory
from docx import table
from flexidata.utils.constants import FileType
from flexidata.utils.decorators import validate_file_type_method
import numpy as np
from PIL import Image
import io
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.table import _Cell
import copy
from xml.etree import ElementTree
from io import StringIO
from flexidata.utils.tables import (
    extract_inner_tables,
    remove_inner_tables,
    table_dict_to_html_table,
    table_dict_to_plain_text,
)


class DocxParser(FileHandler):
    """
    A specialized parser for handling DOCX files that extends the generic FileHandler class.
    
    This parser is designed to extract textual and tabular data from DOCX files, with optional
    capabilities to handle embedded images and separate inner tables within those documents.
    
    Attributes:
        extract_table (bool): Flag to determine whether to extract tables from the document.
        extract_image (bool): Flag to determine whether to process and extract text from images within the document.
        table_dict_in_metadata (bool): Indicates if table dictionaries should be included in metadata outputs.
        separate_inner_tables (bool): Determines if inner tables should be processed separately from the main tables.
        text_extractable (bool): Flag to track if text is extractable, initialized as False and set based on file processing.
        document (Any): Holds the loaded DOCX document object; initialized as None.
        page_number (int): Tracks the current page number for processing; defaults to 1.
        text_blocks (list): Accumulates processed text blocks from the document.
    """

    def __init__(
        self,
        file_path: Optional[str] = None,
        file_url: Optional[str] = None,
        source: FileReaderSource = FileReaderSource.LOCAL,
        extract_table: bool = False,
        extract_image: bool = False,
        bucket_name: Optional[str] = None,
        file_key: Optional[str] = None,
        table_dict_in_metadata: bool = False,
        separate_inner_tables: bool = True,
        **kwargs,
    ) -> None:
        super().__init__(source, file_path, file_url, bucket_name, file_key)
        self.extract_table = extract_table
        self.extract_image = extract_image
        self.table_dict_in_metadata = table_dict_in_metadata
        self.separate_inner_tables = separate_inner_tables
        self.text_extractable = False
        self.document = None
        self.page_number = 1
        self.text_blocks = []

    def is_document_has_section(self):
        """
        Check if the document contains any sections.

        Returns:
            bool: True if the document has one or more sections, False otherwise.
        """
        return bool(self.document.sections)

    def _parse_document_with_section(self):
        """
        Parses each section of a document, processing both paragraphs and tables.

        This internal method iterates through each section of the document,
        further iterating through each content item within these sections.
        It identifies the type of each content item and dispatches it to the
        appropriate parsing method based on whether the item is a paragraph or a table.

        The function assumes that `self.document.sections` is iterable and that
        each section has an `iter_inner_content` method which also produces iterable content.

        No return value as changes are made directly to the class state or other side effects.
        """
        for section in self.document.sections:
            for item in section.iter_inner_content():
                if isinstance(item, Paragraph):
                    self._parse_paragraph(item)
                elif isinstance(item, Table):
                    self._parse_table(item)

    def _parse_document_without_section(self):
        """
        Parses a document's content that is not organized into sections.

        This method iterates through the document's content directly, handling each item it encounters.
        It distinguishes between different types of content, such as paragraphs and tables, and
        processes them with the appropriate parsing methods. This approach is used when the document
        does not contain discrete sections or when such distinctions are irrelevant for the processing task.

        Each content type is handled by a dedicated parsing method, ensuring modularity and clarity in
        content processing operations.

        No return value as changes are made directly to the class state or through other side effects.
        """
        for item in self.document.iter_inner_content():
            if isinstance(item, Paragraph):
                self._parse_paragraph(item)
            elif isinstance(item, Table):
                self._parse_table(item)

    def _parse_table(self, doc_table: Table):
        """
        Parses a table from a document, extracting it into a dictionary format and processing it
        depending on whether inner tables are to be separated or not.

        Args:
            doc_table (Table): A table object from a DOCX file, typically handled by python-docx.

        Description:
            This method first converts the provided table into a dictionary representation.
            If `separate_inner_tables` is enabled, it separates the inner tables from the main table,
            processes the main table, and then processes each of the inner tables individually.
            If `separate_inner_tables` is not enabled, it processes the table dictionary directly.
        """
        table_dict = self.convert_table_to_dict(doc_table)
        if self.separate_inner_tables:
            main_table = remove_inner_tables(table_dict)
            self._process_table_dict(main_table)
            inner_tables = extract_inner_tables(table_dict)
            for table in inner_tables:
                self._process_table_dict(table)
        else:
            self._process_table_dict(table_dict)




    def _process_table_dict(self, table_dict: Dict):
        """
        Processes a table dictionary to generate plain text and HTML representations,
        create metadata, and append a text block to the document's text blocks collection.

        Args:
            table_dict (Dict): The dictionary representation of a table that includes data
                               necessary to render text and HTML formats.

        Description:
            The function converts a table dictionary into plain text and HTML formats,
            generates metadata based on the HTML and potentially the table dictionary itself,
            and then creates and appends a new text block to the document's collection of text blocks.
        """
        text_table = table_dict_to_plain_text(table_dict)
        html_table = table_dict_to_html_table(table_dict)
        
        metadata = self._create_metadata(html_table, table_dict if self.table_dict_in_metadata else None)
        
        text_block = TextBlock(text_table, metadata, TextType.TABLES)
        self.text_blocks.append(text_block)

    def _create_metadata(self, html_table: str, table_dict: Optional[Dict] = None):
        """
        Creates metadata for a table, optionally including the table dictionary itself.

        Args:
            html_table (str): The HTML representation of the table to include in the metadata.
            table_dict (Optional[Dict]): The original table dictionary to optionally include in the metadata.

        Returns:
            An instance of a metadata class containing the metadata information.
        """
        metadata_details = {
            "text_as_html": html_table,
            "file_path": self.get_file_path_by_source(),
            "languages": ["eng"],
            "filetype": FileType.DOCX,
            "page_number": self.page_number,
            "extraction_source": "docx",
        }
        if table_dict is not None:
            metadata_details["table_dict"] = table_dict

        return TextBlockMetadata(**metadata_details)


    def _parse_paragraph(self, paragraph: Paragraph):
        """
        Parses a paragraph and processes any contained images if applicable. Adds the extracted text
        and images as TextBlocks to the document's text blocks collection.

        Parameters:
            paragraph (Paragraph): The paragraph object to be parsed.

        Description:
            This method handles paragraphs by:
            - Optionally processing and extracting text from images contained within the paragraph if `extract_image` is enabled.
            - Extracting text directly from the paragraph if there is any non-whitespace content.
            - Associating extracted content with metadata including file path, language, file type, page number, and source.
            - Determining the text type based on the paragraph's style and creating a corresponding TextBlock.
            - Appending each new TextBlock to the document's list of text blocks for further processing or output.

        Processes:
            - Checks if image extraction is enabled and processes images.
            - Extracts and trims paragraph text.
            - Constructs metadata for the paragraph.
            - Determines the type of text based on paragraph style.
            - Creates and appends TextBlock to the document's text blocks.
        """
        if self.extract_image:
            image_texts = self._process_image(paragraph, format='list')
            self.text_blocks.extend(image_texts)
        if len(paragraph.text.strip()):
            metadata = TextBlockMetadata(
                file_path=self.get_file_path_by_source(),
                languages=["eng"],
                filetype=FileType.DOCX,
                page_number=self.page_number,
                extraction_source="docx",
            )
            text_type = TextType.get_text_type_by_docx_style(
                paragraph.style.name if paragraph.style else None
            )
            text_block = TextBlock(paragraph.text.strip(), metadata, text_type)
            self.text_blocks.append(text_block)

    @validate_file_type_method([FileType.DOCX])
    def parse(self, extract_image: bool = False) -> List[TextBlock]:
        """
        Parses the DOCX file to extract text and possibly tables and images,
        depending on configuration.

        Parameters:
            extract_image (bool, optional): If set to True, images within the document
            will be processed to extract embedded text. Defaults to False.

        Returns:
            List[TextBlock]: A list of TextBlock objects containing the extracted data
            from text, tables, and possibly images within the document.

        Description:
            The function initializes document parsing by loading the DOCX file into memory,
            setting up the image extraction preference, and determining whether the document
            contains sections. It then delegates the parsing to specific methods depending
            on the document's structure (with sections or without sections). Finally, it
            returns a list of text blocks that have been populated during the parsing process.
        """
        if extract_image:
            self.extract_image = extract_image
        self.document = docx.Document(cast(BinaryIO, self.get_file_content()))
        # Determine the parsing strategy based on the document structure and parse accordingly
        if self.is_document_has_section():
            self._parse_document_with_section()
        else:
            self._parse_document_without_section()

        return self.text_blocks

    def _check_page_break(self, element) -> bool:
        """Check if the given element represents a page break in the document.

        Args:
            element: The element to check.

        Returns:
            bool: True if the element is a page break, False otherwise.
        """
        page_break_indicators = [["w:br", 'type="page"'], ["lastRenderedPageBreak"]]
        if hasattr(element, "xml"):
            for indicators in page_break_indicators:
                if all(indicator in element.xml for indicator in indicators):
                    return True
        return False

    def convert_table_to_dict(self, table: table.Table, table_dict: Optional[Dict[str, List]] = None, inner_tables: Optional[List[Dict]] = None, inner_table_count: int = 0) -> Dict:
        """
        Converts a Word table into a dictionary representation, handling nested tables and text content.

        Args:
            table (DocxTable): The table object from python-docx to convert.
            table_dict (Optional[Dict[str, List]], optional): The dictionary to which table rows will be added.
                Initializes to a new dictionary with 'rows' key if None. Defaults to None.
            inner_tables (Optional[List[Dict]], optional): List to track inner tables' dictionaries.
                Initializes to an empty list if None. Defaults to None.
            inner_table_count (int, optional): Counter to track the number of nested tables processed. Defaults to 0.

        Returns:
            Dict: A dictionary representation of the table with rows as keys and each cell as a nested dictionary,
            which includes the cell's content, row span, and column span, along with any nested tables.
        """
        # Initialize the table dictionary and inner tables list if they are None
        if table_dict is None:
            table_dict = {'rows':[]}
            inner_tables = []
        
        # Iterate over each row in the table
        for row in table.rows:
            columns = {}
            for column_index, table_cell in enumerate(row._tr.tc_lst):
                column = {'value': '', 'row_span': 0, 'col_span': 0}
                
                # Create a cell object to handle its content and properties
                cell = _Cell(table_cell, table)
                cell_content = ""
                inner_table = None

                # Iterate over the cell's content to extract text and detect inner tables
                for cell_item in cell.iter_inner_content():
                    if isinstance(cell_item, Paragraph):
                        cell_content += cell_item.text.strip() + "\n"
                        if self.extract_image:
                            image_text = self._process_image(cell_item)
                            if image_text:
                               cell_content += image_text + "\n"
                    elif isinstance(cell_item, Table):
                        inner_table_count = inner_table_count + 1
                        inner_table = self.convert_table_to_dict(
                            cell_item,
                            inner_table_count=inner_table_count,
                            inner_tables=inner_tables
                        )
                        inner_tables.append(inner_table)
                    
                # Prepare cell content by removing trailing new lines
                column_text = cell_content.rstrip("\n")
                column[f'value'] =  column_text if column_text else ""

                # Handle inner tables within the cell
                if inner_table:
                    column.setdefault('inner_tables', []).append(inner_tables)
                    inner_tables = []
                

                # Calculate column span from the cell properties
                cell_span_count = int(table_cell.tcPr.gridSpan.val) if table_cell.tcPr.gridSpan is not None else 0
                if cell_span_count:
                    column['col_span'] = cell_span_count

                # Calculate row span from the cell properties
                if table_cell.tcPr.vMerge is not None and table_cell.tcPr.vMerge.val != "restart":
                    column['row_span'] = column['row_span'] + 1 if 'row_span' in column else 1

                # Add column dictionary to columns using the current column index
                columns[f'column_{column_index}'] = column
            
            # Append columns dictionary to table_dict's rows list
            table_dict['rows'].append(columns)

        return table_dict
    
    
    
    def add_empty_value(self, cells_data: List[str], count: int) -> None:
        """
        Append empty strings to the cells data to account for spanned columns or rows.

        Parameters:
        - cells_data (List[str]): List containing the data of cells in a row.
        - count (int): Number of empty strings to add.
        """
        cells_data.extend(
            [""] * count
        )  # Append 'count' number of empty strings to the cells data

    def paragragph_contains_image(self, paragraph: Paragraph) -> bool:
        return bool(
            paragraph._p.xpath(
                "./w:r/w:drawing/*[self::wp:inline | self::wp:anchor]/a:graphic/a:graphicData/pic:pic"
            )
        )

    def _process_image(self, paragraph: Any, format: str='plain') -> Union[str, List[TextBlock]]:
        """
        Extracts images from a paragraph and converts them to text using OCR.

        Args:
            paragraph (Any): A paragraph object from a Word document. The type is generic
                             because the exact class depends on the library used for DOCX handling.
            format (str, optional): Specifies the format of the returned OCR text.
                                    'plain' returns a single string. 'list' returns a list of strings.
                                    Defaults to 'plain'.

        Returns:
            Union[str, List[TextBlock]]: Depending on the 'format' parameter, this function returns either
                                    a single string containing all OCR'd text or a list of TextBlock with OCR'd text.

        Processes:
            - Checks if the paragraph contains an image.
            - Extracts XML data from image-containing runs.
            - Parses XML to find image data and uses OCR to convert image to text.
            - Depending on the 'format', compiles text results into a single string or a list of strings.
        """
        image_texts = []
        image_text = ''
        if self.paragragph_contains_image(paragraph):
            for run in paragraph.runs:
                if run.text == "":
                    xmlstr = str(run.element.xml)
                    my_namespaces = dict([node for _, node in ElementTree.iterparse(StringIO(xmlstr), events=['start-ns'])])
                    root = ElementTree.fromstring(xmlstr)
                    if 'pic:pic' in xmlstr:
                        for pic in root.findall('.//pic:pic', my_namespaces):
                            cNvPr_elem = pic.find("pic:nvPicPr/pic:cNvPr", my_namespaces)
                            name_attr = cNvPr_elem.get("name")
                            blip_elem = pic.find("pic:blipFill/a:blip", my_namespaces)
                            embed_attr = blip_elem.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
                            imgData = self.document.part.related_parts[embed_attr].blob
                            image = np.array(Image.open(io.BytesIO(imgData)))
                            ocr_factory = OCRAgentFactory()
                            ocr_agent = ocr_factory.get_ocr_agent()
                            elements = ocr_agent.image_to_text(
                                np.array(image),
                                lang="eng",
                                page_number=self.page_number,
                                file_path=self.get_file_path_by_source(),
                                filetype=FileType.DOCX,
                            )
                            if format == 'plain':
                                for element in elements:
                                    image_text += element.text + "\n"
                            if format == 'list':
                                image_texts.extend(elements)
        return image_text if format == 'plain' else image_texts

    def convert_list_table_to_dict(self, table):
        table_dict = {"rows": []}
        for rows in table:
            columns_dict = {}
            for index, column in enumerate(rows):
                columns_dict[f"column_{index}"] = column
            table_dict["rows"].append([columns_dict])
        return table_dict
    

    # try:
                #     if 'pic:pic' in str(run.element.xml):
                #         contentID = Patterns.DOCX_IMAGE_PATTERN.search(
                #             run.element.xml
                #         ).group(0)
                #         print(f"content_id={contentID}")
                #         contentType = self.document.part.related_parts[
                #             contentID
                #         ].content_type
                #         print(f"contentType={contentType}")
                # except KeyError as e:
                #     print(e)
                #     continue
                # except Exception as e:
                #     print(e)
                #     continue
                # if not contentType.startswith("image"):
                #     continue
                # imgName = basename(self.document.part.related_parts[contentID].partname)
                # imgData = self.document.part.related_parts[contentID].blob
                # if contentType != "image/x-wmf":
                #     image = np.array(Image.open(io.BytesIO(imgData)))
                #     ocr_factory = OCRAgentFactory()
                #     ocr_agent = ocr_factory.get_ocr_agent()
                #     elements = ocr_agent.image_to_text(
                #         np.array(image),
                #         lang="eng",
                #         page_number=self.page_number,
                #         file_path=self.get_file_path_by_source(),
                #         filetype=FileType.DOCX,
                #     )
                #     image_texts.extend(elements)
