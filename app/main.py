from pathlib import Path

import streamlit as st
from constants import VECTOR_STORE_PATH
from frontend.components.loader.loader import loader
from frontend.run_chat import run_chat
from pipeline.indexer import build_index, load_index
from pipeline.model_checker import get_missing_models, missing_models_dialog
from pipeline.query import reranker as build_reranker
from rag.embeddings.initialize_embedding import initialize_embedding

STORE_PATH = Path(VECTOR_STORE_PATH)


@st.cache_resource
def get_index():
    initialize_embedding()
    if (STORE_PATH / "chroma.sqlite3").exists():
        try:
            return load_index()
        except Exception as e:
            st.error(f"Error loading the index: {e}. Rebuilding...")
            return build_index()
    return build_index()


@st.cache_resource
def get_reranker():
    return build_reranker()


def main():
    st.set_page_config(
        page_title="Kalima", page_icon="☁️", initial_sidebar_state="collapsed"
    )

    model_missing = get_missing_models()
    if model_missing:
        missing_models_dialog(model_missing)

    if "initialized" not in st.session_state:
        loader()
        with st.spinner("Cargando..."):
            st.session_state.index = get_index()
            st.session_state.reranker = get_reranker()
            st.session_state.initialized = True
        st.rerun()

    run_chat(st.session_state.index, st.session_state.reranker)


if __name__ == "__main__":
    main()
