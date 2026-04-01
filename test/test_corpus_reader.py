import os
import tempfile

from app.rag.corpus.reader import dir_corpus_reader


def test_dir_reader():
    with tempfile.TemporaryDirectory() as tmp_dir:
        print("Temporary directory created ")
        tmp_dir_path = os.path.join(tmp_dir, "ingest_text_tmp.text")
        with open(tmp_dir_path, "w", encoding="utf-8") as tmp_file:
            tmp_file.write(
                "Black holes are among the most mysterious cosmic objects, much studied but not fully understood. These objects aren’t really holes. They’re huge concentrations of matter packed into very tiny spaces. A black hole is so dense that gravity just beneath its surface, the event horizon, is strong enough that nothing – not even light – can escape. The event horizon isn’t a surface like Earth’s or even the Sun’s. It’s a boundary that contains all the matter that makes up the black hole. \nThere is much we don’t know about black holes, like what matter looks like inside their event horizons. However, there is a lot that scientists do know about black holes."
            )

        load_tmp_directory = dir_corpus_reader(input_dir=tmp_dir)

        assert len(load_tmp_directory) == 1, "Reader is working correctly"
