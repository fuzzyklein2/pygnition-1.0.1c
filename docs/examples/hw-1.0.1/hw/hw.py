#!/usr/bin/env python3

"""
@file hw.py
@version 0.0.1b
@brief Defines the class that runs the module as a program.


For more information, see:

    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

from pygnition.picts import *
from pygnition.program import Program
from pygnition.lumberjack import info, warn

class HW(Program):
    def __init__(self):
        super().__init__()

    def test(self):
        warn(f'{self.name} is under construction!')
        self.dump()

    def run(self):
        super().run()
        print(f'Hello, {GLOBE_AMERICA_PICT.strip()} !')

if __name__ == '__main__':
    p = HW()
    if p.testing:
        p.test()
    p.run()