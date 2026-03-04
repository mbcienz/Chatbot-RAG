from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseSplitter(ABC):
    """
    Abstract interface defining the contract for all document splitters.
    """

    @abstractmethod
    def split(self, documents: List[Document]) -> List[Document]:
        """
        Splits a list of documents into smaller chunks.

        Args:
            documents (List[Document]): The list of raw documents to be split.

        Returns:
            List[Document]: A list of fragmented documents (chunks).
        """
        pass