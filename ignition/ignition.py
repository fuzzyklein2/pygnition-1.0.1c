#!/usr/bin/env python3

"""
@file ignition.py
@version 1.2.3
@brief Startup module for simple Python scripts.

This module:

    * Parses arguments.
    * Sets up logging.
    * Imports config files.

    For more information, see:
    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

# from enum import auto, Enum
# from glob import glob
# import logging
# import os
# from pathlib import Path
# from pprint import pformat
# from subprocess import run
# import sys

if __package__:
    from .tools import *
else:
    from tools import *

# ap = AP(prog=PROGRAM, description=DESCRIPTION, epilog=EPILOG)
# for option in STD_OPTS:
#     ap.add_argument(*option[0], **option[1])

# ARGS = ap.parse_args(sys.argv[1:])
                     
# if __debug__:
#     print(f'{ARGS.debug=}')
#     print(f'{ARGS.verbose=}')

# DEBUG = bool({'-d', '--debug'}.intersection(sys.argv))
# VERBOSE = bool({'-v', '--verbose'}.intersection(sys.argv))
# WARNINGS = bool({'-w', '--warnings'}.intersection(sys.argv))
# TESTING = bool({'-t', '--test'}.intersection(sys.argv))

if __name__ == '__main__':
    if VERBOSE:
        print(f"{WARNING_PICT}{color_str('yellow', "WARNING!")} {color_str('green', PROGRAM)} is under construction!{CONSTRUCTION_PICT}")

