from .BaseSplitter import BaseSplitter
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class RecursiveCharacterSplitter(BaseSplitter):
    """
    Implementation of a document splitter that splits text recursively 
    based on a set of characters (paragraphs, lines, spaces).
    """

    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        """
        Initializes the RecursiveCharacterTextSplitter with specific parameters.

        Args:
            chunk_size (int): The maximum size of each chunk (in characters).
            chunk_overlap (int): The number of characters to overlap between chunks.
        """
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split(self, documents: List[Document]) -> List[Document]:
        """
        Executes the splitting logic on the provided documents.

        Args:
            documents (List[Document]): Documents loaded by a DocumentLoader.

        Returns:
            List[Document]: The resulting list of smaller document chunks.
        """
        return self.splitter.split_documents(documents)