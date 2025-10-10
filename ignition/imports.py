#!/usr/bin/env python3

"""
@file imports.py
@version 0.0.1b
@brief Import modules from the system and any required packages.

For more information, see:

    [GitHub](https://github.com/fuzzyklein2/workshop-0.0.1b)
"""

from argparse import ArgumentParser as AP
import ast
import atexit
from cmd import Cmd
from collections import namedtuple, OrderedDict
from configparser import ConfigParser as CP
from datetime import datetime
from enum import auto, Enum
from functools import partial, singledispatch, singledispatchmethod, wraps
from glob import glob
from inspect import currentframe, getsourcefile
from io import StringIO
import json
import logging
import os
from pathlib import Path, PosixPath
from pprint import pformat, pprint as pp
import re
import shutil
import shlex
from subprocess import run
import sys

run_cmd = partial(run, encoding='utf-8', capture_output=True, check=True, shell=True)

import magic
import pandas as pd
from rich.color import Color
from rich.columns import Columns
from rich.console import Console
from rich.table import Table
from rich import print as rp

# mymodule.py
import inspect
import sys
import os

def import_chain():
    stack = inspect.stack()
    chain = []

    for frame_info in stack:
        filename = frame_info.filename

        # Skip frames from Python internals or this module itself
        if filename.startswith("<") or filename == __file__:
            continue

        # Try to map filename back to a module/package name
        module_name = None
        for name, module in sys.modules.items():
            if hasattr(module, '__file__') and module.__file__:
                if os.path.abspath(module.__file__) == os.path.abspath(filename):
                    module_name = name
                    break
        if module_name is None:
            module_name = os.path.splitext(os.path.basename(filename))[0]

        chain.append(module_name)

    return chain[::-1]  # reverse to show import order from root

# Print import chain at import time
# print(f"{__name__} imported via chain: {import_chain()}")
