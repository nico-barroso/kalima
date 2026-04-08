import os

DOC_FOLDER_URL = "./docs"
VECTOR_STORE_PATH = "./chroma_db"
PROJECT_NAME = "kalima"
THINKING_MESSAGES = [
    "Pensando...",
    "Creando una respuesta...",
    "Re-pensando...",
    "Navegando entre documentos...",
    "Conectando los puntos...",
    "Leyendo detenidamente...",
    "Casi termino...",
    "Procesando...",
]
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
