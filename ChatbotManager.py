class ChatbotManager:
    """
    Connects Retrieval logic with LLM Generation.
    """

    def __init__(self, system_prompt, loader, splitter, vector_store, chat_model):
        self.system_prompt = system_prompt
        self.loader = loader
        self.splitter = splitter
        self.vector_store = vector_store
        self.chat_model = chat_model

    def initialize_knowledge_base(self):
        """Prepares the vector database."""
        raw_docs = self.loader.load()
        chunks = self.splitter.split(raw_docs)
        self.vector_store.ingest_documents(chunks)

    def generate_response(self, message: str, history: list):
        """
        The RAG Loop: 
        1. Retrieve relevant chunks.
        2. Construct the prompt with Context.
        3. Generate answer via ChatModel.
        """
        # 1. Retrieval

        # 2. Prompt Engineering (Basic Example)

        # 3. Generation
        response = "Hello!"
        
        return response