from unittest.mock import MagicMock

from llama_index.core import PromptTemplate
from pipeline.query import qa_prompt, query


def test_qa_prompt_returns_prompt_template():
    result = qa_prompt()
    assert isinstance(result, PromptTemplate)


def test_query_passes_prompt_template_instance_not_callable():
    mock_index = MagicMock()
    mock_reranker = MagicMock()

    mock_response = MagicMock()
    mock_response.response_gen = iter([])
    mock_response.source_nodes = []

    mock_chat_engine = MagicMock()
    mock_chat_engine.stream_chat.return_value = mock_response
    mock_index.as_chat_engine.return_value = mock_chat_engine

    query(mock_index, "¿qué dice el documento?", mock_reranker)

    _, kwargs = mock_index.as_chat_engine.call_args
    template = kwargs["text_qa_template"]

    assert isinstance(template, PromptTemplate), (
        f"text_qa_template debe ser PromptTemplate, no {type(template)}"
    )
    assert not callable(template), "text_qa_template no debe ser la función qa_prompt sin llamar"
