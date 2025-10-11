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

from ignition.lumberjack import debug, error, info, warn, stop
from ignition.picts import *
from ignition.settings import Settings

class Program(Settings):
    def __init__(self):
        super().__init__()
        atexit.register(self.shutdown)
        # self.user_data = Path.home() / f'.{self.__class__.__name__.lower()}'

        # if not self.user_data.exists():
        #     warn("User data directory does not exist. Creating it now.")
        #     mkdir(self.user_data)
        
        # self.backup = self.user_data / 'backup'
        # mkdir(self.backup)

        # self.temp_dir = self.user_data / 'temp'
        # mkdir(self.temp_dir)


    
    def run(self):
        info(f'Hello, {GLOBE_AMERICA_PICT.strip()} !')

    def shutdown(self):
        if self.verbose:
            print(f"{CHECK_PICT}Execution complete.")
            print(f'{WAVE_PICT}Goodbye!')

if __name__ == '__main__':
    Program().run()