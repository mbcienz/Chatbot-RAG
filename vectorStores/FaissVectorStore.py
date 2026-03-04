from .BaseVectorStore import BaseVectorStore
from typing import List, Optional
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

class FaissVectorStore(BaseVectorStore):
    """
    Concrete implementation of a Vector Store using FAISS.
    """

    def __init__(self, embeddings: Embeddings, k: int = 3):
        """
        Initializes the FAISS store with a specific embedding model.

        Args:
            embeddings (Embeddings): The LangChain embedding model to use.
            k (int): The number of documents to retrieve.
        """
        self.embeddings = embeddings
        self.k = k
        self.vectorstore: Optional[FAISS] = None
        self.retriever = None

    def ingest_documents(self, documents: List[Document]) -> None:
        """
        Creates a FAISS index from documents and sets up the retriever.

        Args:
            documents (List[Document]): Document chunks.
        """
        if not documents:
            return

        self.vectorstore = FAISS.from_documents(documents, self.embeddings)
        # Initialize the retriever with default search parameters
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": self.k})

    def get_relevant_documents(self, query: str) -> List[Document]:
        """
        Uses the retriever to find documents similar to the query.

        Args:
            query (str): User question.

        Returns:
            List[Document]: Relevant chunks found in FAISS.
        """
        if not self.retriever:
            return []
        
        return self.retriever.get_relevant_documents(query)