from constants import ROOT_URL
from llama_index.core import Document, SimpleDirectoryReader


# For beginning the first connection, we're going to use the first built functions
# in LlamaIndex, Knowing we have limited uses for important metadata in each chunk
#
def dir_corpus_reader(input_dir=ROOT_URL, **kwargs) -> list[Document]:
    docs = SimpleDirectoryReader(input_dir, recursive=True, **kwargs)
    return docs.load_data(show_progress=True)
