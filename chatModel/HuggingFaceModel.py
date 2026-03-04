from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from chatModel.BaseModel import BaseModel

class HuggingFaceModel(BaseModel):
    def __init__(self, model_id = "Qwen/Qwen3-Coder-Next", max_tokens = 1000, temperature = 0.3):
        """init method

        Args:
            model_id (str, optional): Model id from huggingface. Defaults to "Qwen/Qwen3-Coder-Next".
            max_tokens (int, optional): Maximum number of generated token. Defaults to 1000.
            task (str, optional): Task type. Defaults to "text-generation".
        """
        self.model_id = model_id
        self.max_tokens = max_tokens
        self.temperature = temperature

        self.llm = HuggingFaceEndpoint(
            repo_id = self.model_id,
            temperature = self.temperature,
            max_new_tokens = self.max_tokens
        )

        self.chat_model = ChatHuggingFace(llm = self.llm)

    def get_chat_model(self):
        """Return the chat model.

        Returns:
            ChatHuggingFace: chat model.
        """
        return self.chat_model

    def get_model_name(self):
        """Get the model name

        Returns:
            str: name of the model
        """
        return self.model_id
