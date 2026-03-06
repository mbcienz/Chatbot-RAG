from operator import itemgetter
from chain.Chain import Chain
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import get_buffer_string

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
            You are a specialized Assistant in Natural Language Processing.
            Your task is to answer the user's question based strictly on the provided Context and Chat History.

            Follow these operational rules:
            1. CONTEXT & HISTORY: Use the provided context and previous chat history to formulate your response. 
            2. STRICTNESS: If the answer is not explicitly contained within the provided context, state that you do not have enough information. Do NOT provide external explanations or hallucinate details.
            3. LANGUAGE: Always respond in clear, professional English.
            4. CONDUCT: Avoid any offensive or inappropriate language.
            5. OUTPUT: Provide exactly one complete result.
        """
        return system_prompt
    
    def _format_chat_history(self, chat_history):
        """
        Converts the Gradio chat history (list of complex dicts) 
        into a clean string format for the prompt.
        """
        if not chat_history:
            return "No previous conversation."

        formatted_messages = []
        
        for message in chat_history:
            # Extract and capitalize the role (e.g., 'user' -> 'User')
            role = message.get("role", "Unknown").capitalize()
            
            # Extract text from the 'content' list
            # Expected structure: [{'text': 'Hello', 'type': 'text'}]
            content_items = message.get("content", [])
            text_parts = [item.get("text", "") for item in content_items if isinstance(item, dict)]
            full_text = " ".join(text_parts).strip()
            
            if full_text:
                formatted_messages.append(f"{role}: {full_text}")

        return "\n".join(formatted_messages)
    
    def _initialize_knowledge_base(self):
        """Prepares the vector database."""
        raw_docs = self.loader.load()
        chunks = self.splitter.split(raw_docs)
        self.vector_store.ingest_documents(chunks)
        self.retriever = self.vector_store.get_retriever()


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
        # 1. Context
        docs = data.get("context", [])
        context_text = "\n\n".join([doc.page_content for doc in docs]) if docs else "No relevant context found."
        
        # 2. History
        history = data.get("history", "")
        history_section = f"HISTORY:\n{history}" if history else "No previous history."

        # 3. Build the final prompt
        prompt_template = f"""
        {self.system_prompt}

        ---
        {history_section}

        ---
        CONTEXT (Knowledge Base):
        {context_text}

        ---
        QUESTION: {data.get("question", "")}
        
        ANSWER:
        """
        final_prompt = prompt_template
        print("--- DEBUG PROMPT START ---\n", final_prompt, "\n--- DEBUG PROMPT END ---")
        return final_prompt


    def _build_chain(self):
        """Private method to build the chain.

        Returns:
            Chain: return the object chain after the build.
        """
        chain = Chain() 

        chain.add({"context": itemgetter("question") | self.retriever,
                    "question": itemgetter("question"),
                    "history": itemgetter("history")
            })
        chain.add(self._build_prompt)
        chain.add(self.chat_model.get_chat_model())

        chain.build()
        return chain


    def generate_response(self, message: str, history: list):
        """
        Invoke the chain to retrieve relevant documents and generate the response
        """
        formatted_history = self._format_chat_history(history)
        inputs = {"question": message, "history": formatted_history}
        response = self.chain.invoke(inputs)
        
        return response.content if hasattr(response, 'content') else str(response)