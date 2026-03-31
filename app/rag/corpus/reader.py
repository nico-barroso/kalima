# from pathlib import Path

# import fitz  # type: ignore
from constants import ROOT_URL
from llama_index.core import Document, SimpleDirectoryReader


# For beginning the first connection, we're going to use the first built functions
# in LlamaIndex, Knowing we have limited uses for important metadata in each chunk
#
def simple_reader():
    docs = SimpleDirectoryReader(input_dir=ROOT_URL, recursive=True)
    return docs.load_data(show_progress=True)


# After this line, there's another approach builded for handle metadata, WIP


# def get_path(url: str) -> list[str]:
#     path = Path(url)

#     # Validations
#     if not path.exists():
#         raise FileNotFoundError(f"File not found: {url}")
#     if not path.is_dir():
#         raise NotADirectoryError(f"Not a directory: {url}")

#     return [str(p) for p in path.glob("*.pdf")]


# def load_pdf(urls: list[str]) -> list[dict]:
#     try:
#         pages = []
#         for path in urls:
#             doc = fitz.open(path)
#             for page in doc:
#                 pages.append(
#                     {
#                         "doc_path": path,
#                         "page": page.number + 1,
#                         "text": page.get_text(),
#                     }
#                 )
#             doc.close()
#         return pages
#     except Exception as e:
#         print("There was an error", e)
#         return [{}]

#     def to_documents(pages: list[dict]) -> list[Document]:
#         return [
#             Document(text=page["text"], matadata={"page": page["page"]})
#             for page in pages
#         ]
