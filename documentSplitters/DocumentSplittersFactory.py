from .BaseSplitter import BaseSplitter
from .RecursiveCharacterSplitter import RecursiveCharacterSplitter

class DocumentSplittersFactory:
    """
    Factory class to instantiate the appropriate document splitter.
    """

    @staticmethod
    def get_splitter(splitter_type: str, **kwargs) -> BaseSplitter:
        """
        Returns an instance of a specific splitter.

        Args:
            splitter_type (str): The identifier for the splitter (e.g., 'recursive_character').
            **kwargs: Optional keyword arguments for the constructor (chunk_size, chunk_overlap).

        Returns:
            BaseSplitter: An initialized instance of the requested splitter.

        Raises:
            ValueError: If the splitter_type is not supported.
        """
        normalized_type = splitter_type.lower().strip()

        if normalized_type == "recursive_character":
            return RecursiveCharacterSplitter(
                chunk_size=kwargs.get("chunk_size", 700),
                chunk_overlap=kwargs.get("chunk_overlap", 50)
            )
        else:
            raise ValueError(f"Splitter type '{splitter_type}' is not supported.")