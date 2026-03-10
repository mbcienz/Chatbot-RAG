# Chatbot-RAG
A modular Retrieval-Augmented Generation (RAG) chatbot framework designed to provide grounded and context-aware responses by integrating external document retrieval with Large Language Models using LangChain framework.

---

## Project Overview

This project implements a complete RAG pipeline, allowing users to query their own documents and receive answers based strictly on the provided data. The system is designed with a focus on scalability and flexibility, ensuring that individual components can be swapped or upgraded without refactoring the entire codebase.

## System Architecture

The following UML class diagram illustrates the modular design of the system, highlighting the use of Factory and Strategy patterns to decouple document loading, vector storage, and model integration.

![System Architecture UML Diagram](uml_diagram.png)

## Project Structure and Modularity

The repository follows a strict modular design pattern to separate concerns and facilitate maintenance:

### 1. Ingestion and Multi-Format Support
The ingestion module is built to be extensible through the `DocumentLoaderFactory`.
* **Currently Supported**: The system is pre-configured with `PDFLoader` and `PDFDirectoryLoader` to handle PDF documents.
* **Extensibility**: By extending the `BaseLoader` abstract class, support for new formats (such as .txt, .docx, or .md) can be added without modifying the core `ChatbotManager`.

### 2. Model Factory and LLM Integration
The `ChatModelFactory` manages the instantiation of different language models. 
* **Supported Providers**: Current implementations include `HuggingFaceModel` and `LangChainModel` providers.

### 3. Vector Database Management
The `VectorStoresFactory` handles the creation of storage solutions. 
* **Current Implementation**: Uses `FaissVectorStore` (based on FAISS) for efficient similarity search.
* The system is designed to support any vector database that implements the `BaseVectorStore` interface.

### 4. Chatbot Manager and Chain Logic
The `ChatbotManager` acts as the orchestrator, utilizing a `Chain` component to manage the flow of information between the retriever and the generative model.

---

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/mbcienz/Chatbot-RAG.git
    cd Chatbot-RAG

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

---

## Usage

### Data Preparation

To index your documents (currently supporting PDF files), place your source files in the designated data directory.
### Running the Application

To start the chatbot interface or CLI:
```bash
    python main.py
```

## Technical Features

* **Abstract Factory Pattern**: Ensures that components (Models, Loaders, Vector Stores) are created consistently and are easily swappable.
* **Flexible Document Parsing**: Designed to support multiple data sources beyond the current PDF implementation.
* **Customizable Chunking**: Uses `RecursiveCharacterSplitter` via `DocumentSplittersFactory` for optimal context window management.
* **Agnostic LLM Integration**: Decoupled from specific providers to prevent vendor lock-in, supporting both HuggingFace and LangChain providers.

## License

Refer to the LICENSE file in the repository for details on usage rights and restrictions.