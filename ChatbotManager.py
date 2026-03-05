class ChatbotManager:
    """
    Connects Retrieval logic with LLM Generation.
    """

    def __init__(self, loader, splitter, vector_store, chat_model):
        self.system_prompt = self._get_system_prompt()
        self.loader = loader
        self.splitter = splitter
        self.vector_store = vector_store
        self.chat_model = chat_model
        self._initialize_knowledge_base()

    def _get_system_prompt(self):
        """Defines the system prompt for the LLM."""
        system_prompt = """
            You are an agent specialized in Natural Language Processing. 
            Use the following pieces of context to answer the question after.
            Do NOT provide any explaination if something is not present in the context!

            Please follow these rules:
            1. Avoid offensive language.
            2. Answer in proper English.
            Give me only 1 complete result.
        """
        return system_prompt
    
    def _initialize_knowledge_base(self):
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