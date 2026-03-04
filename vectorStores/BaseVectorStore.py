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
    def get_relevant_documents(self, query: str) -> List[Document]:
        """
        Retrieves the most relevant documents based on a query.

        Args:
            query (str): The user's search query.

        Returns:
            List[Document]: The most relevant document chunks.
        """
        pass