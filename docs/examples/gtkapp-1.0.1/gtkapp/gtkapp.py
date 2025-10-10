#!/usr/bin/env python3

"""
@file gtkapp.py
@version 1.0.1
@brief PyGTK app.

For more information, see:

    [GitHub](https://github.com/fuzzyklein2/workshop-0.0.1b)
"""

from ignition.program import *
from ignition.server import Server

class GTKApp(Program):
    def __init__(self):
        super().__init__()
        debug(f'Running {PROGRAM_NAME}')
        debug(f'{ARGS=}')
        debug(f'{USER_DATA_DIR=}')

if __name__ == '__main__':
    app = GTKApp()