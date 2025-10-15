#!/usr/bin/env python3

"""
@file driver.py
@version 1.0.1
@brief Subclasses the `Driver` class from cmd.Cmd

This module:

    * Defines the Driver class.

For more information, see:

    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

# if __package__:
#     from .program import *
# else:
#     from program import *

# from cmd import Cmd
# import logging
# from pathlib import Path

# from pygnition.import Program
# from pygnition.tools import get_func_name

from argparse import ArgumentParser as AP
from cmd import Cmd
import logging
from pathlib import Path
import shlex
import shutil

from pygnition.arguments import get_args
from pygnition.configure import configure
from pygnition.constants import EPILOG
from pygnition.lumberjack import debug, error, info, stop, warn
from pygnition.program import Program
from pygnition.settings import Settings

class Driver(Cmd, Program):

    class Command():
        def __init__(self, name, line):
            # self.driver = driver
            self.name = name
            self.options = self.get_opts(self.name, line)
            self.config_file = f"etc/{self.name}.cfg"
            self.app_name = self.__class__.__qualname__.split('.')[0].lower()
            self.prefs_dir = Path.home() / f'.{self.app_name}'
            config = configure([f'{str(self.prefs_dir / self.config_file)}'])
            self.settings = Settings(self, self.options, config)
            self.log = logging.getLogger(name)

        def get_opts(self, name:str, line:str):
            line = shlex.split(line)
            OPTS_FILE = Path(f'data/{name.lstrip('do_')}_opts.csv')
            options = list()
            if OPTS_FILE.exists():
                options = get_args(OPTS_FILE)
            else:
                warn(f'Data file {str(OPTS_FILE)} does not exist!')
            ap = AP(prog=name,
                    description='',
                    epilog=EPILOG)
    
            for opt in options:
                ap.add_argument(*opt[0], **opt[1])
    
            return ap.parse_args(line)

        def run(self):
            self.log.debug(f'Running the {self.name} command ...')
            
    def __init__(self, *args, **kwargs):
        Cmd.__init__(self)
        Program.__init__(self)
        # super().__init__(*args, **kwargs)
        # self.name = self.__class__.__name__
        # self.logger = logging.getLogger(self.name)
        # self.logger.debug(f'Initializing {self.name} object.')
        # self.logger.debug(f'Application directory: {self.appdir}')
        # # self.user_data = Path.home() / f'.{self.__class__.__name__.lower()}'
        # self.logger.debug(f'User data directory: {self.user_data}')
        self.current_cmd = None

        # if not self.user_data.exists():
        #     warn("User data directory does not exist. Creating it now.")
        #     mkdir(self.user_data)
        
        # self.backup = self.user_data / 'backup'
        # mkdir(self.backup)

        # self.temp_dir = self.user_data / 'temp'
        # mkdir(self.temp_dir)


    def command(self, name:str, line:str):
        debug(f'''Doing command.
{name=}
{line=}
{self.__class__.__name__=}
''')
        getattr(self, f'{name.title()}')(name, line).run()


    # @property
    # def appdir(self):
    #     return self._workshop

    # @appdir.setter
    # def appdir(self, p:Path):
    #     self._workshop = p

    # @appdir.deleter
    # def appdir(self):
    #     del self._workshop

    # @property
    # def user_data(self):
    #     return self._user_data

    # @user_data.setter
    # def user_data(self, p:Path):
    #     self._user_data = p

    # @user_data.deleter
    # def user_data(self):
    #     del self._user_data

    @property
    def current_cmd(self):
        return self._current_cmd

    @current_cmd.setter
    def current_cmd(self, s:str | None):
        self._current_cmd = s

    @current_cmd.deleter
    def current_cmd(self):
        del self._current_cmd


    def run(self):
        super().cmdloop()

    def do_quit(self, args):
        """Exit the application."""
        return True

    def preloop(self):
        debug('Running driver ...')

    def default(self, line):
        error(f'Command not found: {line}')

if __name__ == '__main__':
    d = Driver()
    d.run()
