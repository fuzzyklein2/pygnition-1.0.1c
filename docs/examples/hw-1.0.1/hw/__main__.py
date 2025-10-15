#!/usr/bin/env python3

import subprocess
from pathlib import Path
from datetime import datetime

from .startmeup import *

MODULE_NAME = Path(__file__).stem

def last_saved_datetime(path: str | Path, repo_wide: bool = False) -> datetime | None:
    """
    Return the datetime of the last Git commit for a file or repo.
    Falls back to filesystem modification time if not committed yet.

    :param path: Path to file or directory.
    :param repo_wide: If True, use the latest commit in the repo.
    :return: datetime object or None if unavailable.
    """
    path = Path(path).resolve()

    # --- 1. Try git commit timestamp ---
    try:
        args = ["git", "log", "-1", "--format=%ct"]
        if not repo_wide:
            args.append(str(path))
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        ts = result.stdout.strip()
        if ts:
            return datetime.fromtimestamp(int(ts))
    except subprocess.CalledProcessError:
        pass  # not in git or not committed

    # --- 2. Fall back to file modification time ---
    try:
        return datetime.fromtimestamp(path.stat().st_mtime)
    except FileNotFoundError:
        return None


__doc__ = f"""A concise summary of what this module does.

:module: hw.{MODULE_NAME}
:version: {VERSION}
:author: {AUTHOR}
:date: {last_saved_datetime(__file__)}

Description
-----------
A more detailed description of this module’s purpose and behavior.
You can describe its main classes, functions, and relationships to other
modules here. Keep it short, 5–10 lines max.

Typical Use
-----------
>>> from pygnition.module_name import SomeClass
>>> obj = SomeClass()
>>> obj.do_something()

Main Components
---------------
- :class:`SomeClass` – brief one-line summary.
- :func:`some_function` – what it does in a few words.

Notes
-----
You can include implementation notes, dependencies, or version-specific
details here.

"""

# """
# @file __main__.py
# @version 0.0.1b
# @brief Defines the code that runs the module as a program.


# For more information, see:

#     https://github.com/fuzzyklein2/workshop-0.0.1b
# """

from .hw import HW

if __name__ == '__main__':
    HW().run()
