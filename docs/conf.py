"""Sphinx configuration."""
project = "Budget"
author = "Leon Deng"
copyright = "2022, Leon Deng"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
