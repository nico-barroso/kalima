# RAG Local — Sistema de Pregunta-Respuesta

Sistema de Retrieval-Augmented Generation completamente local, sin dependencias de APIs externas. Permite hacer preguntas sobre un corpus de documentos propios usando modelos de lenguaje open-source.

## Stack

- **LLM**: Ollama (`gemma3:12b`)
- **Embeddings**: Ollama (`nomic-embed-text`)
- **Vector DB**: ChromaDB
- **Orquestación**: LlamaIndex
- **Frontend**: Streamlit

## Requisitos

- [Ollama](https://ollama.com) instalado y corriendo en el host
- Docker y Docker Compose
- 8GB+ RAM recomendado

## Instalación

### 1. Descargar modelos

```bash
ollama pull gemma3:12b
ollama pull nomic-embed-text
```

### 2. Clonar el repositorio

```bash
git clone https://github.com/nico-barroso/rag-local
cd rag-local
```

### 3. Añadir documentos

Coloca tus documentos (`.pdf`, `.txt`) en la carpeta `docs/`.

### 4. Levantar la app

```bash
docker compose up --build
```

Accede a la interfaz en `http://localhost:8501`.
