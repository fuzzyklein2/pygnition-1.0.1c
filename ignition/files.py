#!/usr/bin/env python3

"""
@file files.py
@version 1.0.1
@brief Defines the `File` class.

For more information, see:

    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

from .where import *

# import magic
# from pathlib import Path

def file_info(path: str, mime: bool = False, encoding: bool = False) -> str:
    """
    Return type information for a file, similar to the `file` command.

    :param path: Path to the file
    :param mime: If True, return MIME type (e.g., 'image/png')
    :param encoding: If True, return encoding info (e.g., 'utf-8')
    """
    if mime:
        ms = magic.Magic(mime=True)
    elif encoding:
        ms = magic.Magic(mime_encoding=True)
    else:
        ms = magic.Magic()

    return ms.from_file(str(Path(path)))


class File():
    def __init__(self, p:Path):
        self.p = p

    def output(self):
        result = self.p.name
        if self.p.is_dir():
            result = '[blue bold]' + result + '[/blue bold]'
        return result

    def info(self):
        return file_info(str(p.resolve()))

    def mime(self):
        return file_info(str(p.resolve()))

if __name__ == '__main__':
    print(F"Running {PROGRAM_NAME}")