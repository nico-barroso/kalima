import sys
import tempfile

import pytest

text_placeholder = "Black holes are among the most mysterious cosmic objects, much studied but not fully understood. These objects aren’t really holes. They’re huge concentrations of matter packed into very tiny spaces. A black hole is so dense that gravity just beneath its surface, the event horizon, is strong enough that nothing – not even light – can escape. The event horizon isn’t a surface like Earth’s or even the Sun’s. It’s a boundary that contains all the matter that makes up the black hole. \nThere is much we don’t know about black holes, like what matter looks like inside their event horizons. However, there is a lot that scientists do know about black holes."

sys.path.insert(0, "app")


@pytest.fixture
def tmp_doc_dir():
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield tmp_dir


@pytest.fixture
def tmp_file():
    def _create(
        path_to_dir,
        content=text_placeholder,
    ):
        with open(path_to_dir, "w", encoding="utf-8") as tmp_file:
            tmp_file.write(content)

    return _create
