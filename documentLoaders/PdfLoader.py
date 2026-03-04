from .BaseLoader import BaseLoader
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

class PdfLoader(BaseLoader):
    """
    Concrete implementation for loading a single PDF file using LangChain.
    """

    def __init__(self, source_path: str):
        """
        Initializes the PyPDFLoader with the given file path.

        Args:
            source_path (str): The full path to the PDF file.
        """
        self.source_path = source_path
        self.loader = PyPDFLoader(self.source_path)

    def load(self) -> List[Document]:
        """
        Executes the loading process for the single PDF.

        Returns:
            List[Document]: Processed content of the PDF.
        """
        return self.loader.load()