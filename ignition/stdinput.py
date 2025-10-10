#!/usr/bin/env python3

"""
@file input.py
@version 1.0.1
@brief Retrieves standard input if there is any.

This module:

    * Imports config files.

For more information, see:
https://github.com/fuzzyklein2/workshop-0.0.1b
"""

# from rich import print as rp

if __package__:
    from .constants import *
else:
    from constants import *
    
def get_piped_input() -> str|None:
    if not sys.stdin.isatty():
        INPUT = sys.stdin.read()
        return INPUT
    return None

if __name__ == '__main__':
    print(f"{INFO_PICT}Testing {MAIN_FILE.name}\n")
    rp(f"{DEBUG_PICT}[bold][cyan]Input[/cyan][/bold]:\n")

    # rp(f"[bold]{DEBUG_PICT}{color_str('cyan', 'Input')}[/bold]:\n")
    print(get_piped_input())
