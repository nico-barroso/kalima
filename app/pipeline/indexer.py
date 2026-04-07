from llama_index.core.indices.vector_store.base import VectorStoreIndex
from rag.chunks.splitter import document_splitter
from rag.corpus.reader import reader
from rag.vectorstore.store import init_store, load_store


def build_index() -> VectorStoreIndex:
    """Orchestrates the generation of the vector index and creates the vector store.

    Note:
        1. Reads the corpus.
        2. Split the corpus into nodes.
        3. Pass them to the vector store and initialize it
    """
    docs = reader()
    print(f"Loaded {len(docs)} docs")
    nodes = document_splitter(docs)
    print(f"Split into {len(nodes)} nodes")
    index = init_store(nodes)
    return index


def load_index() -> VectorStoreIndex:
    """Initialize a vector store already indexed"""
    index = load_store()
    print("Index loaded correctly")
    return index
