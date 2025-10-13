#!/usr/bin/env python3

"""
@file environment.py
@version 1.0.1
@brief Retrieves relevant environment variables from the system.

This module:

    * Defines the `Environment` class.

For more information, see:

    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

import os

# if __package__:
#     from .arguments import *
#     from .configure import *
#     from .lumberjack import *
# else:
#     from arguments import *
#     from configure import *
#     from lumberjack import *

# if __package__:
#     from .utils import *
# else:
#     from utils import *

from pygnition.utils import *

class Environment(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        
        ENV_PREFIX = PROGRAM_NAME.upper() + '_'
        KEYS = grep(ENV_PREFIX, os.environ.keys())

        # ENV = dict()

        for k in KEYS:
            # print(f'$ENVIRONMENT_LOGFILE: {os.environ["ENVIRONMENT_LOGFILE"]}')
            self[k.lstrip(ENV_PREFIX).lower()] = os.environ[k]

    def dumps(self):
        return pformat(self)

if __name__ == '__main__':
    print(f'{PROGRAM_NAME=}')
    print(f"""Environtment variables:

{pformat(Environment())}
""")
    # print(f'{type(os.environ)=}')