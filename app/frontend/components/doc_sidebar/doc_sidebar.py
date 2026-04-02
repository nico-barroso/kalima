import os

import streamlit as st
from frontend.utils.utils import styles_file_opener


def doc_sidebar():
    """Generates a curated sidebar that contains the documents in the /docs root folder"""
    st.markdown(
        f"<style>{styles_file_opener(__file__)}</style>", unsafe_allow_html=True
    )
    with st.sidebar:
        with st.container(key="uploader-container"):
            st.caption(
                "Here you can upload your own documents. Remember that the model need to index each time you upload a document."
            )
            uploaded = st.file_uploader(
                "Subir documento",
                type=["pdf", "txt"],
                accept_multiple_files=True,
                key="uploader",
            )
            st.header("Documentos activos")

        if uploaded:
            for file in uploaded:
                with open(f"./docs/{file.name}", "wb") as out:
                    out.write(file.read())
                st.success(f"{file.name} añadido")

        files = sorted(
            os.scandir("./docs"), key=lambda f: f.stat().st_mtime, reverse=True
        )

        cards_html = '<div class="document-container">'
        for filename in files:
            cards_html += f"""
                <div class="document-card">
                    <span class="document-img">📄</span>
                    <p>{filename.name}</p>
                </div>
            """
        cards_html += "</div>"
        st.html(cards_html)
