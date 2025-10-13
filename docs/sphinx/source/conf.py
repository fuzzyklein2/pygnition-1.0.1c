# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '🔥pygnition.'
copyright = '2025, Russell Klein'
author = 'Russell Klein'
release = '1.0.1'

# -- Add the module to `sys.path` --------------------------------------------
from pathlib import Path
import sys

IGNITION_DATA = Path.home() / '.pygnition.
LOCATION_FILE = IGNITION_DATA / 'location.txt'
LOCATION = LOCATION_FILE.read_text()
sys.path.insert(0, LOCATION)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode',
              'sphinx.ext.autosummary',
             ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_theme = 'furo'
html_static_path = ['_static']

html_theme_options = {
    "light_css_variables": {},
    "dark_css_variables": {
        "color-background-primary": "#000000",
        "color-foreground-primary": "#ffffff", # #0ae5e2
        # "color-link": "#0ae5e2",        # normal link color
        # "color-link--hover": "#99e6ff", # on hover
        # "color-link-visited": "#b3b3ff" # visited links

    },
    "default_color_mode": "light",
}

