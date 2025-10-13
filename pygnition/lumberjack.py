#!/usr/bin/env python3

"""
@file lumberjack.py
@version 1.2.3
@brief Set up logging for whatever script calls it.

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

# if VERBOSE:
#     print(f"{WARNING_PICT}{color_str('yellow', "WARNING!")} {color_str('green', PROGRAM)} is under construction!{CONSTRUCTION_PICT}")

LOG_PICTS = { logging.DEBUG: DEBUG_PICT,
              logging.INFO: INFO_PICT,
              logging.WARNING: WARNING_PICT,
              logging.ERROR: ERROR_PICT,
              logging.CRITICAL: CRITICAL_PICT
            }

def setuplog(LOGFILE:Path|str, level):
    if type(LOGFILE) is str:
        LOGFILE = Path(LOGFILE)
    
    # if not LOGFILE.exists():
    #     LOGFILE.parent.mkdir(parents=True, exist_ok=True)
    #     LOGFILE.touch()
    
    
    # if DEBUG:
    #     level = logging.DEBUG
    # elif VERBOSE:
    #     level = logging.INFO
    # elif WARNINGS or TESTING:
    #     level = logging.WARNING
    # else:
    #     level = logging.ERROR
    
    if LOGFILE.exists():
        LOGFILE.write_text('')
    else:
        LOGFILE.parent.mkdir(parents=True, exist_ok=True)
    
    # # Determine logging level
    # level = logging.DEBUG  # or INFO/WARNING depending on your flags
    
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(level)
    
    # Formatter
    formatter = logging.Formatter('%(message)s')
    # formatter = logging.Formatter(f'{LOG_PICTS
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler
    file_handler = logging.FileHandler(LOGFILE)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.debug(f"{GEAR_PICT}Logging configuration complete.")
    logger.debug(f'{LOG_PICT}Log file: {LOGFILE.resolve()}')
    now = datetime.now()
    logger.debug(f'{current_clock_pict(now)}Current time: {now}')

    return logger

def log(level, message):
    if NEWLINE in message:
        logging.log(level, '')
    logging.log(level, f"{LOG_PICTS[level]}{message}")
    # if NEWLINE in message:
    #     logging.log(level, '')

def debug(message):
    log(logging.DEBUG, message)

def info(message):
    log(logging.INFO, message)

def warn(message):
    log(logging.WARNING, message)

def error(message):
    log(logging.ERROR, message)

def stop(message):
    log(logging.CRITICAL, message)
    if RUNNING_CLI:
        exit(1)

if __name__ == '__main__':
    setuplog(Path(__file__).parent.parent / f'logs/{PROGRAM_NAME}.log',
             level=logging.DEBUG)
    debug(f'Testing {PROGRAM_NAME}')