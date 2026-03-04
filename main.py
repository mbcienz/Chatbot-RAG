import gradio as gr
from AppConfigurator import AppConfigurator

def launch_app(bot_manager, ui_config):
    """
    Starts the Gradio web interface using UI settings from config.
    """
    # Pre-process the knowledge base
    bot_manager.initialize_knowledge_base()

    # Setup the interface
    view = gr.ChatInterface(
        fn=bot_manager.generate_response,
        title=ui_config.get("title", "AI Assistant"),
        description=ui_config.get("description", ""),
        fill_height=True
    )

    view.launch()

def main():
    # 1. Load the master configuration
    config = AppConfigurator.read_config("config.json")
    
    # 2. Build the system core
    bot_manager = AppConfigurator.create_manager_from_config(config)
    
    # 3. Run the application with UI parameters
    launch_app(bot_manager, config["ui"])

if __name__ == "__main__":
    main()