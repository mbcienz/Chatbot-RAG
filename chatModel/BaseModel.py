from abc import ABC, abstractmethod

class BaseModel(ABC):

    @abstractmethod
    def get_chat_model(self):
        """Return the chat model.
        """
        pass

    @abstractmethod
    def get_model_name(self):
        """Get the model name.
        """
        pass

