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

DEBUG = not __debug__

LOCATION_PATH = Path.home() / '.ignition/location.txt'
IGNITION_PATH = LOCATION_PATH.read_text().strip()

sys.path.insert(0, str(IGNITION_PATH))
from ignition.program import *

class HW(Program):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    if DEBUG:
        rp(f"{WARNING_PICT}[yellow bold]WARNING[/yellow bold]: {PROGRAM_NAME} is under construction! {CONSTRUCTION_PICT}")
        Program().run()