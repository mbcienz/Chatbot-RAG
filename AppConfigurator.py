import json
from typing import Any, Dict
from langchain_huggingface import HuggingFaceEmbeddings
from documentLoaders.DocumentLoadersFactory import DocumentLoadersFactory
from documentSplitters.DocumentSplittersFactory import DocumentSplittersFactory
from vectorStores.VectorStoresFactory import VectorStoresFactory
from chatModel.ChatModelFactory import ChatModelFactory
from ChatbotManager import ChatbotManager

class AppConfigurator:
    """
    Orchestrates the instantiation of the entire RAG system based on JSON config.
    """

    @staticmethod
    def read_config(config_path: str) -> Dict[str, Any]:
        """Reads the JSON configuration file with UTF-8 encoding."""
        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def create_manager_from_config(config: Dict[str, Any]) -> ChatbotManager:
        """
        Builds the ChatbotManager by injecting all required modular dependencies.
        """
        # 1. Document Loader
        loader = DocumentLoadersFactory.get_loader(
            loader_type=config["loader"]["type"],
            source_path=config["loader"]["path"]
        )

        # 2. Document Splitter
        splitter = DocumentSplittersFactory.get_splitter(
            splitter_type=config["splitter"]["type"],
            chunk_size=config["splitter"]["chunk_size"],
            chunk_overlap=config["splitter"]["chunk_overlap"]
        )

        # 3. Vector Store & Embeddings (default in vector store factory)
        vector_store = VectorStoresFactory.get_vector_store(
            store_type=config["vector_store"]["type"],
            k=config["vector_store"]["k"]
        )

        # 4. Chat Model (The LLM)
        chat_model = ChatModelFactory.create_chat_model(
            provider=config["chat_model"]["provider"],
            model_id=config["chat_model"]["model_id"],
            max_tokens=config["chat_model"]["max_tokens"],
            temperature=config["chat_model"]["temperature"]
        )

        # 5. Assemble the Manager
        return ChatbotManager(
            system_prompt=config["chatbot"]["system_prompt"],
            loader=loader,
            splitter=splitter,
            vector_store=vector_store,
            chat_model=chat_model
        )