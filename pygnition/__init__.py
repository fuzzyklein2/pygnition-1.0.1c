#!/usr/bin/env python3

from datetime import datetime as dt
from pathlib import Path
import subprocess

PKG_PATH = Path(__file__).parent.parent
PKG_NAME = '-'.join(PKG_PATH.name.split('-')[:-1])

PROJ_DATA = PKG_PATH / 'data'
VERSION = PKG_PATH.name.split('-')[-1]
AUTHOR = (PROJ_DATA / 'author.txt').read_text()

def is_valid_data_line(s:str)->bool:
    if s.startswith('#') or s.isspace() or not s: return False
    return True

def read_lines(p:Path):
    return p.read_text().splitlines()
    
REQ_FILE = Path('requirements.txt')
if not REQ_FILE.exists():
    REQ_FILE = Path('requirements.in')
REQUIREMENTS = '\n'.join([f'* {s}' for s in read_lines(REQ_FILE) if is_valid_data_line(s)])

def git_repo_last_commit_datetime() -> dt | None:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ct"],
            capture_output=True, text=True, check=True
        )
        timestamp = int(result.stdout.strip())
        return dt.fromtimestamp(timestamp)
    except subprocess.CalledProcessError:
        return None

def last_saved_datetime(path: str | Path, repo_wide: bool = False) -> dt | None:
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

__doc__ = f"""The **{PKG_NAME}** package initializes the runtime environment and exposes
the primary interfaces for project components such as configuration,
logging, and execution control.

This module is executed automatically when the package is imported. It
may perform setup tasks, import key submodules, or define high-level
symbols for convenient access.

:package: {PKG_NAME}
:version: {VERSION}
:author: {AUTHOR}
:date: {git_repo_last_commit_datetime()}

Overview
--------
{PKG_NAME.title()} provides a unified framework for developing modular Python
applications. Importing the package typically prepares the environment
and registers essential utilities such as:

- :mod:`pygnition.program`
- :mod:`pygnition.settings`
- :mod:`pygnition.driver`
- :mod:`pygnition.filter`

Usage Example
-------------
>>> import pygnition
>>> app = pygnition.Program()
>>> app.run()

System Requirements
-------------------
{REQUIREMENTS}

Notes
-----
This file may re-export selected symbols from submodules for convenience.
Check the package reference documentation for details.
"""
