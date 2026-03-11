import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from chatModel.BaseModel import BaseModel

class LangChainModel(BaseModel):
    def __init__(self, model_id="google_genai:gemini-2.5-flash-lite", max_tokens=1000, temperature=0.3):
        self.model_id = model_id
        self.max_tokens = max_tokens
        self.temperature = temperature

        # Load environment variables
        load_dotenv()
        
        # If the model is from Google, set the GOOGLE_API_KEY environment variable
        if "google" in self.model_id.lower():
            google_key = os.getenv("GOOGLE_API_KEY")
            if google_key:
                os.environ["GOOGLE_API_KEY"] = google_key
            else:
                print("Warning: Google API key not found. Please insert 'GOOGLE_API_KEY' in your .env file.")
                os.environ["GOOGLE_API_KEY"] = ""

        self.chat_model = init_chat_model(
            model = self.model_id,
            temperature = self.temperature,
            max_tokens = self.max_tokens
        )

    def get_chat_model(self):
        """Return the chat model.

        Returns:
            BaseChatModel: chat model.
        """
        return self.chat_model

    def get_model_name(self):
        """get the model name

        Returns:
            str: the model name
        """
        return self.model_id 

        