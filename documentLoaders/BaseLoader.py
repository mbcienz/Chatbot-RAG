from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseLoader(ABC):
    """
    Abstract interface that defines the contract for all document loaders.
    """

    @abstractmethod
    def load(self) -> List[Document]:
        """
        Extracts data from the source and returns a list of LangChain Documents.

        Returns:
            List[Document]: A list of documents containing page content and metadata.
        """
        pass