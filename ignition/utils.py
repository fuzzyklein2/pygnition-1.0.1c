#!/usr/bin/env python3

"""
@file utils.py
@version 0.0.1b
@brief Defines constant values.

This module:

    * Defines functions that are required by `constants.py`:

        - `get_docstring_from_file`
        - `remove_tag`
        - `grep`

    For more information, see:
    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

if __package__:
    from .picts import *
    # from .responses import *
else:
    from picts import *
    # from responses import *

def parse_file_for_docstr(s:str) -> str | None:
    return ast.get_docstring(ast.parse(s))

@singledispatch
def get_docstring_from_file(arg) -> str | None:
    raise TypeError(f"Unsupported type: {type(arg)}")

@get_docstring_from_file.register
def _(p: Path) -> str | None:
    source = p.read_text(encoding='utf-8')
    return parse_file_for_docstr(source)

@get_docstring_from_file.register
def _(s: str) -> str | None:
    source = Path('__init__.py').read_text(encoding='utf-8')
    return parse_file_for_docstr(source)

def remove_tag(s:str) -> str:
    return ' '.join(s.strip().split()[1:])

def grep(pattern, s):
    if isinstance(s, str):
        lines = s.splitlines()
    else:
        lines = s
    return [line for line in lines if line.startswith(pattern)]

def is_rich_color(name: str) -> bool:
    try:
        Color.parse(name)
        return True
    except Exception:
        return False
        
def color_str(color, s:str) -> str:
    if is_rich_color(color):
        buffer = StringIO()
        console = Console(file=buffer, color_system='truecolor', force_terminal=True)
        console.print(f"[{color}]{s}")
        return buffer.getvalue().strip()
    else:
        return f'[red]ERROR![end] Invalid color!'
