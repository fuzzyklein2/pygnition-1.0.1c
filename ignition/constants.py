#!/usr/bin/env python3

"""
@file constants.py
@version 0.0.1b
@brief Defines constant values.

This module:

    * Determines whether the script is running in Jupyter or CLI. [Deprecated.].
    * Defines a file system for new projects.
    * Imports config files.
    * Defines constants for doxygen tags in docstrings.
    * Looks for ~/.workshop/ and creates it if necessary.

    For more information, see:
    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

if __package__:
    from .utils import *
else:
    from utils import *

NEWLINE = '\n'
HYPHEN = '-'

# RUNNING_IN_JUPYTER = Path(sys.argv[0]).stem.startswith('ipykernel')
# RUNNING_CLI = not RUNNING_IN_JUPYTER
# NOTEBOOK = 'notebook'

FILE_TAG = '@file'
BRIEF_TAG = '@brief'
VERSION_TAG = '@version'

PROGRAM = PROGRAM_NAME
VERSION = None
MAIN_FILE = PROGRAM_PATH

try:
    DOCSTR = get_docstring_from_file(MAIN_FILE)
    DOCSTR_MISSING = not bool(DOCSTR)
except FileNotFoundError as e:
    print(f'{WARNING_PICT} File not found: {MAIN_FILE}')
    DOCSTR_MISSING = True
    
if DOCSTR_MISSING:
    VERSION = '1.0.0'
    DESCRIPTION = f'Python script: {MAIN_FILE}'
    EPILOG = 'https://github.com/fuzzyklein2/workshop-0.0.1b'
else:
    VERSION = remove_tag(grep(VERSION_TAG, DOCSTR)[0])
    DESCRIPTION = remove_tag(grep(BRIEF_TAG, DOCSTR)[0])
    EPILOG = DOCSTR[-1]

CWD = Path.cwd()
