import gradio as gr
from ChatbotManager import ChatbotManager

def launch_app(bot_manager):
    """
    Configures and starts the Gradio web interface.
    """
    # Create the interface using the ChatInterface high-level component
    view = gr.ChatInterface(
        fn=bot_manager.generate_response,
        title="RAG Chatbot",
        description="""
        ### Welcome! 
        I am a **RAG-powered chatbot**. Unlike standard AI, I have access to a specific **Knowledge Base**.
        
        **Instructions:** Please ask questions about the documents or data I've been trained on. 
        I will retrieve the most relevant information to provide accurate, grounded answers.
        """,
        fill_height=True
    ).launch()


def main():
    # Define the chatbot's configuration
    system_prompt = """
    You are a helpful assistant. Answer the user's questions based on the conversation history.
    """
    temperature = 0.7
    kb_path = "./knowledgeBase/"  # Path to the knowledge base for RAG
    
    # Instantiate the manager globally
    bot_manager = ChatbotManager(
        system_prompt=system_prompt, 
        temperature=temperature,
        kb_path=kb_path)

    # Start the Gradio app with the chatbot manager
    launch_app(bot_manager)

if __name__ == "__main__":
    main()