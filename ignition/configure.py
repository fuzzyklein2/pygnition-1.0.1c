#!/usr/bin/env python3

"""
@file configure.py
@version 1.0.1
@brief Gathers options from configuration files.

This module:

    * Imports config files.

For more information, see:
https://github.com/fuzzyklein2/workshop-0.0.1b
"""

# from configparser import ConfigParser as CP

# from rich import print as rp

if __package__:
    from .arguments import parse_arguments
    from .stdinput import *
else:
    from arguments import parse_arguments
    from stdinput import *

class Configuration():
    def __init__(self, files:list):
        # Normalize files into a list of strings
        if files is None:
            files_list = []
        elif isinstance(files, (str, Path)):
            files_list = [str(files)]
        elif isinstance(files, list):
            files_list = [str(f) for f in files]
        else:
            raise TypeError(f"files must be str, Path, or list of str/Path, got {type(files)}")

        self.config = CP()
        if files_list:
            for f in files_list:
                try:
                    lines = Path(f).read_text().splitlines()
                except FileNotFoundError:
                    print(f'{WARNING_PICT}Configuration file not found: {f}')
                    break
                if not lines[0].startswith('DEFAULT'):
                    lines.insert(0, '[DEFAULT]')
                self.config.read_string(NEWLINE.join(lines))
            # self.config.read(files)

    def as_dict(self) -> dict:
        result = {'DEFAULT': dict(self.config.defaults())}
        result.update({section: dict(self.config[section]) for section in self.config.sections()})
        return result

def configure(files:list|None=None):
    # rp(f"{DEBUG_PICT}[hot_pink2][bold]`configure`[/bold][/hot_pink2]")
    # breakpoint()
    if not files:
        files = list()
    # else: print(f'{type(files)=}')
    config = Configuration(files)
#     print(f'''Configuration:

# {pformat(config.as_dict())}
# ''')
    return Configuration(files)
    
if __name__ == '__main__':
    print(f'Running {PROGRAM_NAME}')
    print(f'Program path: {PROGRAM_PATH}')
    # print("Running `configure.py` ...")
    config = configure('etc/project.ini')
    pp(config.as_dict())
