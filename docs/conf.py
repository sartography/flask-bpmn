"""Sphinx configuration."""
from datetime import datetime


project = "Flask Bpmn"
author = "Sartography"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    'sphinx.ext.autosummary',  # Create neat summary tables
    "sphinx.ext.napoleon",
    "sphinx_click",
]

autosummary_generate = True  # Turn on sphinx.ext.autosummary

autodoc_typehints = "description"
html_theme = "furo"
