from .BaseLoader import BaseLoader
from typing import List
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.documents import Document

class PdfDirectoryLoader(BaseLoader):
    """
    Concrete implementation for loading all PDFs from a directory using LangChain.
    """

    def __init__(self, source_path: str):
        """
        Initializes the PyPDFDirectoryLoader with the given directory path.

        Args:
            source_path (str): The path to the folder containing PDF files.
        """
        self.source_path = source_path
        self.loader = PyPDFDirectoryLoader(self.source_path)

    def load(self) -> List[Document]:
        """
        Executes the loading process for all PDFs found in the directory.

        Returns:
            List[Document]: Aggregated content from all PDFs in the folder.
        """
        return self.loader.load()