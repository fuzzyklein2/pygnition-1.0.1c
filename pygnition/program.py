#!/usr/bin/env python3

"""
@file program.py
@version 1.0.1
@brief Consolidates input into a single object and runs.

This module:

    * Defines the `Program` class.

For more information, see:
https://github.com/fuzzyklein2/workshop-0.0.1b
"""

import atexit

# if __package__:
#     from .settings import *
# else:
#     from settings import *

from pygnition.lumberjack import debug, error, info, warn, stop
from pygnition.picts import *
from pygnition.settings import Settings

class Program(Settings):
    def __init__(self):
        super().__init__()
        atexit.register(self.shutdown)
    
    def run(self):
        debug(f'Running {self.name}')
        if self.testing: self.test()

    def shutdown(self):
        if self.verbose:
            print(f"{CHECK_PICT}Execution complete.")
            print(f'{WAVE_PICT}Goodbye!')

if __name__ == '__main__':
    Program().run()