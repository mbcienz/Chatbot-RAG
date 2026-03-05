from .BaseVectorStore import BaseVectorStore
from typing import List, Optional
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

class FaissVectorStore(BaseVectorStore):
    """
    Concrete implementation of a Vector Store using FAISS.
    """

    def __init__(self, embeddings: Embeddings, k: int = 3, faiss_index: str = "faiss_index"):
        """
        Initializes the FAISS store with a specific embedding model.

        Args:
            embeddings (Embeddings): The LangChain embedding model to use.
            k (int): The number of documents to retrieve.
        """
        self.embeddings = embeddings
        self.k = k
        self.faiss_index = faiss_index
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
        self.vectorstore.save_local(self.faiss_index)

        # Initialize the retriever with default search parameters
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": self.k})

    def get_retriever(self):
        """
        Returns the retriever for querying the FAISS index.

        Returns:
            The retriever object for querying the FAISS index.
        """
        if self.retriever is None:
            raise ValueError("The FAISS index has not been created. Please ingest documents first.")
        return self.retriever