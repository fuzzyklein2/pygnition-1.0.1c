#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file constants.py
@version 0.0.1b
@brief Defines constant values.

This module:

    * Determines whether the script is running in Jupyter, CLI, or CGI.
    * Defines a file system for new projects.
    * Imports config files.
    * Defines constants for doxygen tags in docstrings.
    * Looks for ~/.workshop/ and creates it if necessary.

For more information, see:
https://github.com/fuzzyklein2/workshop-0.0.1b
"""

# ---------------------------
# System imports
# ---------------------------
try:
    from .imports import *
except ImportError:
    from imports import *

# ---------------------------
# Program environment
# ---------------------------
RUNNING_CLI = False
RUNNING_CONSOLE = False
RUNNING_IN_JUPYTER = False
RUNNING_GATEWAY = False

DEBUG = False
VERBOSE = False
WARNINGS = False
TESTING = False

PROGRAM_NAME = "UNKNOWN"
PROGRAM_PATH = None

class Interpreters(Enum):
    IPYTHON = auto()
    CONSOLE = auto()
    JUPYTER = auto()
    CLI = auto()
    GATEWAY = auto()
    TKINTER = auto()
    UNKNOWN = auto()

# ---------------------------
# Determine interpreter
# ---------------------------
try:
    PROGRAM_PATH = Path(sys.modules["__main__"].__file__).resolve()
except (KeyError, AttributeError):
    # Running in interactive console or notebook
    PROGRAM_PATH = Path.cwd()

if not sys.argv[0]:
    RUNNING_CONSOLE = True
    INTERPRETER = Interpreters.CONSOLE

if "GATEWAY_INTERFACE" in os.environ:
    RUNNING_GATEWAY = True
    INTERPRETER = Interpreters.GATEWAY

elif "ipykernel" in sys.modules:
    RUNNING_IN_JUPYTER = True
    INTERPRETER = Interpreters.JUPYTER

elif "IPython" in sys.modules:
    RUNNING_CONSOLE = True
    INTERPRETER = Interpreters.IPYTHON

elif sys.stdin.isatty:
    if not RUNNING_CONSOLE:
        RUNNING_CLI = True
        # RUNNING_CONSOLE = True
        INTERPRETER = Interpreters.CLI

else:
    # fallback
    RUNNING_CLI = True
    INTERPRETER = Interpreters.UNKNOWN

PROJECT_DIR = PROGRAM_PATH.parent
PROGRAM_NAME = PROJECT_DIR.stem.split('-')[0]

if RUNNING_CLI or RUNNING_GATEWAY:
    PROJECT_DIR = PROJECT_DIR.parent

# ---------------------------
# Project and user directories
# ---------------------------
PROJECT_NAME = PROJECT_DIR.stem.split("-")[0]

try:
    IGNITION_DIR = Path(getsourcefile(Interpreters)).parent.parent
except Exception:
    IGNITION_DIR = PROJECT_DIR

USER_DATA_DIR = Path.home() / f".{PROJECT_NAME}"
USER_PREFS_DIR = USER_DATA_DIR / "etc"

# ---------------------------
# Command line flags
# ---------------------------
DEBUG = bool({'-d', '--debug'}.intersection(sys.argv))
VERBOSE = bool({'-v', '--verbose'}.intersection(sys.argv))
WARNINGS = bool({'-w', '--warnings'}.intersection(sys.argv))
TESTING = bool({'-t', '--test'}.intersection(sys.argv))

def display_where_info():
    """Test this module from any program that imports it."""
    print(f"Running: {PROGRAM_NAME}")
    print(f"Program path: {PROGRAM_PATH}")
    print(f"Ignition directory: {IGNITION_DIR}")
    print(f"Project directory: {PROJECT_DIR}")
    print(f"User data directory: {USER_DATA_DIR}")
    print(f"Interpreter: {INTERPRETER.name}")
    print(f"RUNNING_CLI={RUNNING_CLI}, RUNNING_IN_JUPYTER={RUNNING_IN_JUPYTER}, "
          f"RUNNING_CONSOLE={RUNNING_CONSOLE}, RUNNING_GATEWAY={RUNNING_GATEWAY}")

if not RUNNING_CLI and not RUNNING_GATEWAY:
    display_where_info()
    
# ---------------------------
# Optional: display info if testing
# ---------------------------
if __name__ == "__main__" and TESTING:
    display_where_info()