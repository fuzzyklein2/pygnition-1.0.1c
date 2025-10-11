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

import logging
import os
from pathlib import Path
from pprint import pformat
from types import SimpleNamespace

# try:
#     from .arguments import *
#     from .environment import Environment
#     from .configure import *
#     from .lumberjack import *
# except ImportError:

from ignition.arguments import parse_arguments
from ignition.configure import configure
from ignition.constants import DESCRIPTION, EPILOG, VERSION
from ignition.environment import Environment
from ignition.lumberjack import debug, error, info, setuplog, stop, warn
from ignition.stdinput import get_piped_input
from ignition.tools import mkdir
from ignition.where import PROGRAM_NAME, PROJECT_DIR, RUNNING_CLI, \
                           USER_DATA_DIR, USER_PREFS_DIR

# breakpoint()
INPUT = get_piped_input()

# PROJECT_DIR = Path(__file__).resolve().parent.parent if RUNNING_CLI else Path(os.curdir).resolve()
ARGS_FILE = PROJECT_DIR / 'data/std_opts.csv'
# CONFIG_FILE = USER_DATA_DIR / f'etc/{PROGRAM_NAME}.cfg'
# if not CONFIG_FILE.exists():

# CONFIG_FILE = PROJECT_DIR / 'etc/config.ini'
# LOG_FILE = PROJECT_DIR / f'logs/{PROGRAM_NAME}.log'
if not USER_PREFS_DIR.exists():
    mkdir(USER_PREFS_DIR)
CONFIG_FILES = [USER_PREFS_DIR / s for s in os.listdir(USER_PREFS_DIR) if Path(s).suffix in {'.ini', '.cfg'}]
LOG_FILE = USER_DATA_DIR / f'logs/{PROGRAM_NAME}.log'

# assert(PROJECT_DIR.exists())
# assert(ARGS_FILE.exists())
# assert(CONFIG_FILE.exists())

ARGS = None
if RUNNING_CLI:
    if ARGS_FILE.exists():
        ARGS = parse_arguments(ARGS_FILE, PROGRAM_NAME, VERSION, DESCRIPTION, EPILOG)

# assert(ARGS)

if ARGS:
    if hasattr(ARGS, 'config'):
        if ARGS.config:
            CONFIG_FILES = [ARGS.config]

ENV = Environment()

# print('Configuration file: ' + str(CONFIG_FILE))
CONFIG = None
if CONFIG_FILES:
    CONFIG = configure(CONFIG_FILES).config
else:
    mkdir(USER_DATA_DIR / 'etc')
    shutil.copy2(IGNITION_DIR / 'etc/server.cfg', USER_DATA_DIR / 'etc/server.cfg')

if ARGS:
    if hasattr(ARGS, 'log'):
        if ARGS.log:
            LOG_FILE = ARGS.log
elif CONFIG and ('LOG_FILE' in CONFIG['DEFAULT'].keys()):
    LOG_FILE = CONFIG['DEFAULT']['LOG_FILE']
# LOG_FILE = ARGS.LOG_FILE if ARGS.LOG_FILE else CONFIG['DEFAULT']['LOG_FILE']

# print(f'{ARGS=}')

LOG_LEVEL = logging.WARNING

if ARGS:
    if ARGS.debug or ARGS.testing:
        LOG_LEVEL = logging.DEBUG
    elif ARGS.verbose:
        LOG_LEVEL = logging.INFO

# print(f'{LOG_FILE=}\n{LOG_LEVEL=}')

if LOG_FILE.parent.exists():
    setuplog(LOG_FILE, LOG_LEVEL)

SETTINGS = dict()
if CONFIG: SETTINGS.update(dict(CONFIG['DEFAULT']))
if ENV: SETTINGS.update(ENV)
if ARGS: SETTINGS.update(vars(ARGS))
if INPUT: SETTINGS.update({'input', INPUT})

class Settings(SimpleNamespace):
    def __init__(self, *args, **kwargs):
        super().__init__(**SETTINGS)
        self.user_data = USER_DATA_DIR

    def dumps(self):
        return pformat(self)

    def dump(self):
        debug(f"""{self.__class__.__name__} attributes:
{self.dumps()}
""")
    
if __name__ == '__main__':
    debug(f'Running {PROGRAM_NAME}')
    debug(f'{type(ARGS)=}')
    debug(f'{dict(CONFIG['DEFAULT'])=}')
    debug(f'''Settings:
{pformat(Settings())}
''')
    # s = Settings()
    # debug(f'{s.debug=}')
    # debug(f'{s.input=}')
    # debug(f'{s.args=}')
    # debug(f'{dict(s.config[s.section]=}')
    # debug(f'{s.logfile=}')
    