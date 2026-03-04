class ChatModelFactory():
    
    @staticmethod
    def create_chat_model(provider, **kwargs):
        """static method for creating the chat model. Supporter provider are [hf, langchain].

        Args:
            provider (str): the name of the provider. It can be [hf, langchain]

        Raises:
            ValueError: This exception is raised when an unsupported provider is given.
        """
        if provider == "hf":
            from chatModel.HuggingFaceModel import HuggingFaceModel
            return HuggingFaceModel(kwargs["repo_id"], kwargs["max_tokens"], kwargs["task"])
        elif provider == "langchain":
            from chatModel.LangChainModel import LangChainModel
            return LangChainModel(kwargs["model_id"], kwargs["max_tokens"], kwargs["temperature"])
        else:
            raise ValueError(f"Provider {provider} not supported yet. Supported provider are [hf, langchain]!\n")
