from .PdfLoader import PdfLoader
from .PdfDirectoryLoader import PdfDirectoryLoader
from .BaseLoader import BaseLoader

class DocumentLoadersFactory:
    """
    Factory class to instantiate the appropriate loader based on the source type.
    """

    @staticmethod
    def get_loader(loader_type: str, source_path: str) -> BaseLoader:
        """
        Returns an instance of a specific loader.

        Args:
            loader_type (str): The type of loader ('pdf' or 'pdf_directory').
            source_path (str): The path to the file or directory.

        Returns:
            BaseLoader: An initialized loader instance.

        Raises:
            ValueError: If the loader_type is not supported.
        """
        normalized_type = loader_type.lower().strip()

        if normalized_type == "pdf":
            return PdfLoader(source_path)
        elif normalized_type == "pdf_directory":
            return PdfDirectoryLoader(source_path)
        else:
            raise ValueError(f"Loader type '{loader_type}' is not supported.")