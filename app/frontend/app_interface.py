import streamlit as st
from pipeline.indexer import indexer
from pipeline.queries import query

def render_chat():
    st.title("📚 Local RAG")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "index" not in st.session_state:
        with st.spinner("Cargando índice..."):
            st.session_state.index = indexer()
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Pregunta algo..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                response = query(prompt)
            st.markdown(response)
    
        st.session_state.messages.append({"role": "assistant", "content": str(response)})
