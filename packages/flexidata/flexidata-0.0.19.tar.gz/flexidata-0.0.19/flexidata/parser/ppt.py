from typing import BinaryIO, cast, Optional, List
from flexidata.utils.constants import FileReaderSource, FileType
from flexidata.reader.handlers import FileHandler
from flexidata.text_processing.text_block import TextBlock
from flexidata.parser.pptx import PptxParser
from flexidata.text_processing.convert_file import FileConversion
from flexidata.utils.constants import FileType
from flexidata.utils.decorators import validate_file_type_method
import os


class PptParser(FileHandler):
    
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
        separate_inner_tables: bool = False,
        **kwargs,
    ) -> None:
        super().__init__(source, file_path, file_url, bucket_name, file_key)
        self.extract_table = extract_table
        self.extract_image = extract_image
        self.table_dict_in_metadata = table_dict_in_metadata
        self.separate_inner_tables = separate_inner_tables
        self.text_extractable = False

    @validate_file_type_method([FileType.PPT])
    def parse(self, extract_image: bool = False) -> List[TextBlock]:
        """Parse the Doc file to extract text and possibly tables.

        Returns:
            List[TextBlock]: A list of TextBlock objects containing the extracted data.
        """
        if extract_image:
            self.extract_image = extract_image
        temp_directory = self._create_temp_directory()
        FileConversion.convet_ppt_to_pptx(self.file_path, temp_directory.name)
        _, filename_no_path = os.path.split(os.path.abspath(self.file_path))
        base_filename, _ = os.path.splitext(filename_no_path)
        target_file_path = os.path.join(temp_directory.name, f"{base_filename}.pptx")
        parser = PptxParser(
            file_path=target_file_path,
            source=self.source,
            extract_table=self.extract_table,
            extract_image=self.extract_image,
            table_dict_in_metadata = self.table_dict_in_metadata,
            separate_inner_tables = self.separate_inner_tables,
            bucket_name=self.bucket_name,
            file_key=self.file_key,
        )
        elements = parser.parse()
        self._delete_temp_directory(temp_directory)
        return elements
