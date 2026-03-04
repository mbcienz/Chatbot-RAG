from .BaseVectorStore import BaseVectorStore
from .FaissVectorStore import FaissVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

class VectorStoresFactory:
    """
    Factory class to instantiate the appropriate Vector Store.
    """

    @staticmethod
    def get_vector_store(store_type: str, k: int) -> BaseVectorStore:
        """
        Returns an instance of a specific vector store.

        Args:
            store_type (str): The identifier ('faiss').
            k (int): The number of documents to retrieve.

        Returns:
            BaseVectorStore: An initialized vector store instance.

        Raises:
            ValueError: If the store_type is not supported.
        """
        normalized_type = store_type.lower().strip()
        embeddings = HuggingFaceEmbeddings(model_name = "BAAI/bge-small-en-v1.5", encode_kwargs = {'normalize_embeddings': True}) # This can be made more flexible by allowing the model name to be passed as an argument.

        if normalized_type == "faiss":
            return FaissVectorStore(embeddings, k)
        else:
            raise ValueError(f"Vector Store type '{store_type}' is not supported.")