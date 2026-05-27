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

# Configure a module-level logger for the application.
import logging

logger = logging.getLogger(PROJECT_NAME)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
logger.setLevel(logging.INFO)
