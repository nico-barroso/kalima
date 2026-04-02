import os


def styles_file_opener(caller_file: str, file_name="styles.css") -> str:
    """Opens the styles document to be used on streamlit.
    - caller_file: the path of the style file. Is recommended to pass __file__ as an argument if the styles file
    is in the same folder
    - file_name: the name of the file. By default styles.css
    """

    BASE_DIR = os.path.dirname(caller_file)
    with open(os.path.join(BASE_DIR, file_name)) as f:
        return f.read()

