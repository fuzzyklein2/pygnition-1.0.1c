#!/usr/bin/env python3

"""
pygnition.py
============

A short description of what this module does. This is analogous to Doxygen's @brief.

:version: 1.0.1c         # analogous to @version
:author: Russell Klein   # optional
# :email: you@example.com  # optional
:date: 2025-10-12        # optional, like @date

Detailed Description
--------------------
Here you can add a longer explanation if needed. Analogous to Doxygen's detailed description section.

Usage Example
-------------
You can include short examples for clarity:

>>> import mymodule
>>> mymodule.foo()
'bar'

Functions
---------
List and describe the main functions/classes in this module. Sphinx will also pick up docstrings from each function automatically.
"""

# from enum import auto, Enum
# from glob import glob
# import logging
# import os
# from pathlib import Path
# from pprint import pformat
# from subprocess import run
# import sys


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

