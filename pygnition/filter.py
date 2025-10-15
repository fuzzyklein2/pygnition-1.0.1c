#!/usr/bin/env python3

"""
@file filter.py
@version 1.0.1
@brief Interprets arguments as file names and processes them.

This module:

    * Defines the `Filter` class.

For more information, see:
https://github.com/fuzzyklein2/workshop-0.0.1b
"""

from pathlib import Path
from pprint import pformat

from .picts import DEBUG_PICT
from .program import Program

class Filter(Program):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.paths = [Path(f) for f in self.args]
        if self.testing: print(f"""{DEBUG_PICT} Filter Paths:

{pformat(self.paths)}
""")

    def process_directory(self, d:Path):
        if self.verbose:
            print(f'{FOLDER_PICT}{"Processing" if self.args.recursive else "Skipping"} directory: {str(d)} ...')
        if self.recursive:
            for p in (d / f for f in os.listdir(d)):
                self.process_path(p)

    def is_hidden(self, p:Path) -> bool:
        return p.name.startswith('.')

    def process_file(self, p:Path):
        if self.verbose:
            print(f'Processing {str(p)} ...')

    def process_path(self, p:Path):
        if self.verbose:
            print(f"{GEAR_PICT}Processing {str(p)} ...")
            
        if not p.exists():
            warn(f"File {str(p)} does not exist!")
            return
            
        if p.is_symlink() and not self.follow:
            if self.verbose:
                target = p.readlink()
                output = str()
                exists = target.exists()
                color = 'cyan' if exists else 'red'
                output += f'[{color} bold]'
                output += target.readlink()
                output += f'[/{color} bold]'
                print(f'{LINK_PICT}Skipping symbolic link {output} -> {p.readlink()} ...')
            return
                
        if self.is_hidden(p) and not self.all:
            if self.verbose:
                print(f'Skipping {str(p)} ...')
            return
        
        if p.is_dir():
            return self.process_directory(p)

        self.process_file(p)


    def run(self):
        # super().run()
        if self.verbose: print(f"{GEAR_PICT}Processing files ...")

        for p in self.paths:
            self.process_path(p)
            
        # print(f"{STOP_PICT}Execution complete.")

if __name__ == '__main__':
    f = Filter()
    if f.testing:
        info(f'Running {PROGRAM_NAME} ...')
        debug(f'Command line arguments:\n\n{pformat(ARGS.args)}\n')
    Filter().run()
    # print(RECURSIVE)
