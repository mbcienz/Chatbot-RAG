from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseVectorStore(ABC):
    """
    Abstract interface for all vector store implementations.
    """

    @abstractmethod
    def ingest_documents(self, documents: List[Document]) -> None:
        """
        Processes and stores documents in the vector database.

        Args:
            documents (List[Document]): The list of document chunks to store.
        """
        pass

    @abstractmethod
    def get_retriever(self):
        """
        Returns the retriever for querying the vector database.

        Returns:
            The retriever object for querying the vector database.
        """
        pass