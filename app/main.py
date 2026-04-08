import streamlit as st
import time
from pathlib import Path
<<<<<<< HEAD

import streamlit as st
from constants import VECTOR_STORE_PATH  # Renombrado para mayor claridad
=======
from constants import VECTOR_STORE_PATH
>>>>>>> f771d17 (fix(commit_not_merged): one of the fix was not merged correctly to the)
from frontend.run_chat import run_chat
from pipeline.indexer import build_index, load_index
from pipeline.query import reranker as build_reranker
from rag.embeddings.initialize_embedding import initialize_embedding

STORE_PATH = Path(VECTOR_STORE_PATH)


<<<<<<< HEAD
@st.cache_resource
def get_index():
=======
def _load_or_build_index():
>>>>>>> f771d17 (fix(commit_not_merged): one of the fix was not merged correctly to the)
    initialize_embedding()

    if (STORE_PATH / "chroma.sqlite3").exists():
        try:
            return load_index()
        except Exception as e:
            st.error(f"Error loading the index {e}. Rebuilding...")
            return build_index()

    return build_index()


@st.cache_resource
<<<<<<< HEAD
def get_reranker():

=======
def get_index():
    return _load_or_build_index()


@st.cache_resource
def get_reranker():
>>>>>>> f771d17 (fix(commit_not_merged): one of the fix was not merged correctly to the)
    return build_reranker()


def main():
<<<<<<< HEAD
    index = get_index()
    reranker = get_reranker()
    run_chat(index, reranker)
=======
    st.set_page_config(page_title="Kalima", page_icon="☁️")

    if "initialized" not in st.session_state:
        st.markdown("""
            <style>
            .loading-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 80vh;
                gap: 20px;
            }
            .loading-spinner {
                width: 50px;
                height: 50px;
                border: 4px solid #e0e0e0;
                border-top: 4px solid #4A90D9;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            .loading-text {
                font-size: 18px;
                color: #666;
            }
            </style>
            <div class="loading-container">
                <div class="loading-spinner"></div>
                <div class="loading-text">Cargando sistema RAG...</div>
            </div>
        """, unsafe_allow_html=True)

        with st.spinner("Cargando índice..."):
            index = get_index()
        with st.spinner("Inicializando reranker..."):
            reranker = get_reranker()

        st.session_state.index = index
        st.session_state.reranker = reranker
        st.session_state.initialized = True
        st.rerun()

    run_chat(st.session_state.index, st.session_state.reranker)
>>>>>>> f771d17 (fix(commit_not_merged): one of the fix was not merged correctly to the)


if __name__ == "__main__":
    main()