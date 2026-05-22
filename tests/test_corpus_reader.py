import os

from app.rag.corpus.reader import reader


def test_dir_reader(tmp_doc_dir, tmp_pdf_file):
    pdf_path = os.path.join(tmp_doc_dir, "test_document.pdf")
    tmp_pdf_file(pdf_path)

    docs = reader(input_dir=tmp_doc_dir)
    assert len(docs) >= 1
