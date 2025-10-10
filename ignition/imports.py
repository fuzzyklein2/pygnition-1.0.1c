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

