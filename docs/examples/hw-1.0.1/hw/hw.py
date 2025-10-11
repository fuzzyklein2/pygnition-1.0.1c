#!/usr/bin/env python3

"""
@file hw.py
@version 0.0.1b
@brief Defines the class that runs the module as a program.


For more information, see:

    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

from pathlib import Path
import sys

#from rich import print as rp
#
DEBUG = not __debug__

from ignition.lumberjack import *
from ignition.program import Program

class HW(Program):
    def __init__(self):
        super().__init__()
        # self.debug(f'Initializing program {PROGRAM_NAME} ...')
        # self.debug(f'{self.testing=}')

    def test(self):
        self.warn(f'{self.name} is under construction!')

if __name__ == '__main__':
    p = HW()
    if p.testing:
        p.test()
    else:
        p.run()
