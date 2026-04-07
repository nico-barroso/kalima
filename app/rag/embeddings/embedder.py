from llama_index.core import Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama


def embed_text():
    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")


def gemma3_4b():
    Settings.llm = Ollama(
        model="gemma3:4b", request_timeout=60.0, additional_kwargs={"num_predict": 5024}
    )


def gemma3_12b():
    Settings.llm = Ollama(
        model="gemma3:12b",
        request_timeout=60.0,
        additional_kwargs={"num_predict": 5024},
    )


def initialize_embedding():
    embed_text()
    gemma3_4b()
