from chain.Chain import Chain
from langchain_core.runnables import RunnablePassthrough


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
        self.chain = self._build_chain()


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


    def _build_prompt(self, data):
        """Format the prompt given the contex and question data in a dictionary. 
        The prompt will be formatted in the following way:
            - system prompt
            - context : all the relevant document 
            - question : the user query 

        Args:
            data (dict): dictionary containing context and question
        
        Returns:
            str: return the prompt to submit to the chatbot
        """
        context_text = "\n\n".join([doc.page_content for doc in data["context"]])
        question = data["question"]

        return f"""{self.system_prompt}

        Context:
        {context_text}

        Question:
        {question}
        """


    def _build_chain(self):
        """Private method to build the chain.

        Returns:
            Chain: return the object chain after the build.
        """
        retriever = self.vector_store.get_retriever()
        chain = Chain() 

        chain.add({"context": retriever, "question": RunnablePassthrough()})
        chain.add(self._build_prompt)
        chain.add(self.chat_model.get_chat_model())

        chain.build()
        return chain


    def generate_response(self, message: str, history: list):
        """
        Invoke the chain to retrieve relevant documents and generate the response
        """
        response = self.chain.invoke(message)
        if hasattr(response, 'content'):
            return response.content
               
        return str(response)