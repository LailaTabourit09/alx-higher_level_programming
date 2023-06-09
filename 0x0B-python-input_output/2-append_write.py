#!/usr/bin/python3
"""Module contains a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a text file(UTF8)

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
