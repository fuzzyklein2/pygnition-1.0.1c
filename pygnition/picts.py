#!/usr/bin/env python3

"""
@file picts.py
@version 1.0.1
@brief Defines constants for (mostly) Unicode emojis and such.

This module:


For more information, see:

    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

from datetime import datetime

# if __package__:
#     from .where import *
# else:
#     from where import *

from pygnition.where import *

LEADING_SPACE = ''
if RUNNING_CLI:
    LEADING_SPACE = '  '

CRITICAL_PICT = f"🛑{LEADING_SPACE}"
INFO_PICT = f"💬{LEADING_SPACE}"
ERROR_PICT = f"❗{LEADING_SPACE}"
WARNING_PICT = f"⚠️{LEADING_SPACE}"
DEBUG_PICT = f"🐞{LEADING_SPACE}"
CONSTRUCTION_PICT = f"🚧{LEADING_SPACE}"
NEWLINE = '\n'
STOP_PICT = f"✋{LEADING_SPACE}"
WAVE_PICT = f"🖐️{LEADING_SPACE}"
# RGB for CMYK process blue: approximately (0, 183, 235)
ASK_PICT = f"\033[38;2;0;183;235m\u2754\033[0m{LEADING_SPACE}"  # ❔ in blue
CHECK_PICT = f"✅{LEADING_SPACE}"
FAILURE_PICT = f"❌{LEADING_SPACE}"
HOURGLASS_PICT = f"⏳{LEADING_SPACE}"
INFO_PICT_2 = f"ℹ️{LEADING_SPACE}"
GEAR_PICT = f"⚙️{LEADING_SPACE}"
TEXT_PICT = f"✍️{LEADING_SPACE}"
PYTHON_PICT = f"🐍{LEADING_SPACE}"
C_PICT = f"💻{LEADING_SPACE}"
SCRIPT_PICT = f"📜{LEADING_SPACE}"
FRAMED_PICT = f"🖼️{LEADING_SPACE}"
MUSIC_PICT = f"🎵{LEADING_SPACE}"
VIDEO_PICT = f"🎬{LEADING_SPACE}"
BOOK_PICT = f"📖{LEADING_SPACE}"
PKG_PICT = f"📦{LEADING_SPACE}"
FOLDER_PICT = f"📁{LEADING_SPACE}"
LOG_PICT = f"🗃️{LEADING_SPACE}"
POLICE_LIGHT_PICT = f"🚨{LEADING_SPACE}"
LINK_PICT = f"🔗{LEADING_SPACE}"

WORRIED_PICT = f"😦{LEADING_SPACE}"
FROWN_PICT = f"😞{LEADING_SPACE}"
TEAR_PICT = f"😢{LEADING_SPACE}"
FROWN_MAD_PICT = f"😣{LEADING_SPACE}"

CLOCK_PICTS = {
    "1:00": f"🕐{LEADING_SPACE}",
    "2:00": f"🕑{LEADING_SPACE}",
    "3:00": f"🕒{LEADING_SPACE}",
    "4:00": f"🕓{LEADING_SPACE}",
    "5:00": f"🕔{LEADING_SPACE}",
    "6:00": f"🕕{LEADING_SPACE}",
    "7:00": f"🕖{LEADING_SPACE}",
    "8:00": f"🕗{LEADING_SPACE}",
    "9:00": f"🕘{LEADING_SPACE}",
    "10:00": f"🕙{LEADING_SPACE}",
    "11:00": f"🕚{LEADING_SPACE}",
    "12:00": f"🕛{LEADING_SPACE}",

    "1:30": f"🕜{LEADING_SPACE}",
    "2:30": f"🕝{LEADING_SPACE}",
    "3:30": f"🕞{LEADING_SPACE}",
    "4:30": f"🕟{LEADING_SPACE}",
    "5:30": f"🕠{LEADING_SPACE}",
    "6:30": f"🕡{LEADING_SPACE}",
    "7:30": f"🕢{LEADING_SPACE}",
    "8:30": f"🕣{LEADING_SPACE}",
    "9:30": f"🕤{LEADING_SPACE}",
    "10:30": f"🕥{LEADING_SPACE}",
    "11:30": f"🕦{LEADING_SPACE}",
    "12:30": f"🕧{LEADING_SPACE}",
}

GLOBE_AMERICA_PICT = f"🌎{LEADING_SPACE}"
GLOBE_AFRICA_PICT = f"🌍{LEADING_SPACE}"
GLOBE_ASIA_PICT = f"🌏{LEADING_SPACE}"
GLOBE_MERIDIANS = f"🌐{LEADING_SPACE}"
SATURN_PICT = f"🪐{LEADING_SPACE}"
WORLD_MAP_PICT = f"🗺️{LEADING_SPACE}"

def current_clock_pict(dt: datetime) -> str:
    """
    Return the clock emoji from CLOCK_PICTS most closely representing the given datetime.
    """
    hour = dt.hour % 12
    if hour == 0:
        hour = 12
    minute = dt.minute

    # Round to nearest half hour
    if minute < 15:
        rounded_hour, rounded_minute = hour, 0
    elif minute < 45:
        rounded_hour, rounded_minute = hour, 30
    else:
        rounded_hour = (hour % 12) + 1
        if rounded_hour == 13:
            rounded_hour = 1
        rounded_minute = 0

    key = f"{rounded_hour}:{rounded_minute:02d}"

    # Fallback if not in CLOCK_PICTS
    if key not in CLOCK_PICTS:
        def minutes_from_key(k: str) -> int:
            h, m = map(int, k.split(":"))
            return (h % 12) * 60 + m
        target_minutes = (rounded_hour % 12) * 60 + rounded_minute
        key = min(CLOCK_PICTS.keys(), key=lambda k: abs(minutes_from_key(k) - target_minutes))

    return CLOCK_PICTS[key]

FILE_ICONS = {
  # Text & markup
  ".txt": "✍️",
  ".md": "📝",
  ".rst": "📄",
  ".csv": "📄",
  ".json": "📰",
  ".yaml": "📂",
  ".yml": "📂",
  ".xml": "📃",
  ".ini": "🔧",
  ".conf": "🔧",
  ".toml": "📂",
  ".cfg": "🔧",
  ".log": "📃",
  ".tex": "📜",

    # Programming languages
  ".py": "🐍",
  ".c": "💻",
  ".cpp": "💻",
  ".cxx": "💻",
  ".h": "💻",
  ".hpp": "💻",
  ".java": "☕",
  ".js": "🐝",
  ".ts": "🐝",
  ".sh": "📜",
  ".bat": "📜",
  ".ps1": "📜",
  ".rb": "💎",
  ".go": "🐹",
  ".rs": "🦀",
  ".php": "🐘",
  ".swift": "🦅",
  ".kt": "🤖",
  ".kts": "🤖",
  ".scala": "🛠️",
  ".lua": "🌙",
  ".dart": "🎯",
  ".groovy": "🎵",
  ".elm": "🌿",
  ".clj": "☘️",
  ".cljs": "☘️",
  ".fs": "🎸",
  ".fsi": "🎸",
  ".fsi": "🎸",

    # Documents
  ".pdf": "📖",
  ".doc": "📖",
  ".docx": "📖",
  ".xls": "📈",
  ".xlsx": "📈",
  ".ppt": "📉",
  ".pptx": "📉",
  ".epub": "📚",
  ".rtf": "📄",
  ".odt": "📄",
  ".ods": "📊",
  ".odp": "📉",

    # Images
  ".png": "🖼️",
  ".jpg": "🖼️",
  ".jpeg": "🖼️",
  ".gif": "🖼️",
  ".bmp": "🖼️",
  ".svg": "🖼️",
  ".ico": "🖼️",
  ".tif": "🖼️",
  ".tiff": "🖼️",
  ".webp": "🖼️",
  ".heic": "🖼️",

    # Audio / Video
  ".mp3": "🎵",
  ".wav": "🎵",
  ".ogg": "🎵",
  ".flac": "🎵",
  ".aac": "🎵",
  ".m4a": "🎵",
  ".mp4": "🎬",
  ".mkv": "🎬",
  ".avi": "🎬",
  ".mov": "🎬",
  ".wmv": "🎬",
  ".flv": "🎬",
  ".webm": "🎬",
  ".mpeg": "🎬",

    # Archives
  ".zip": "📦",
  ".tar": "📦",
  ".gz": "📦",
  ".bz2": "📦",
  ".7z": "📦",
  ".rar": "📦",
  ".xz": "📦",
  ".cab": "📦",
  ".iso": "💿",
  ".img": "💿",
  ".dmg": "💿",
  ".apk": "🤖",
  ".deb": "📦",
  ".rpm": "📦",
  ".tar.gz": "📦",
  ".tgz": "📦",

    # Folders & links
  "folder": "📁",
  ".lnk": "🔗",
  ".url": "🔗",

    # Databases
  ".db": "🗄️",
  ".sqlite": "🗄️",
  ".sql": "🗃️",
  ".mdb": "🗄️",
  ".accdb": "🗄️",

    # Fonts
  ".ttf": "🔤",
  ".otf": "🔤",
  ".woff": "🔤",
  ".woff2": "🔤",
  ".eot": "🔤",

    # Executables / scripts
  ".exe": "⚙️",
  ".dll": "⚙️",
  ".so": "⚙️",
  ".bin": "⚙️",
  ".run": "⚙️",
  ".app": "⚙️",
  ".jar": "☕",

    # System / config
  ".sys": "🛠️",
  ".drv": "🛠️",
  ".service": "⚙️",
  ".log": "📃",
  ".pid": "📝",

    # Git / VCS
  ".gitignore": "🗃️",
  ".gitattributes": "🗃️",
  ".gitmodules": "🗃️",
  ".patch": "🩹",
  ".diff": "🩹",

    # Web / markup
  ".html": "🌐",
  ".htm": "🌐",
  ".css": "🎨",
  ".scss": "🎨",
  ".less": "🎨",
  ".xml": "📃",
  ".xsl": "📃",
  ".xhtml": "🌐",

    # Misc
  ".torrent": "🧲",
  ".iso": "💿",
  ".img": "💿",
  ".dmg": "💿",
  ".log": "📃",
  ".bak": "📦",
  ".tmp": "🗑️",
  ".lock": "🔒",
}

if __name__ == '__main__':
    now = datetime.now()
    print(f'{current_clock_pict(now)} Current time: {now}')
