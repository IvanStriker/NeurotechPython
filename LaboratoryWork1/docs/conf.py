# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

project = 'LaboratoryWork1'
copyright = '2025, Ivan Vinogradov'
author = 'Ivan Vinogradov'
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
      'sphinx.ext.autodoc',
      'sphinx.ext.napoleon',
      'autodocsumm',
      'sphinx.ext.coverage'
]

auto_doc_default_options = {'autosummary': True}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'haiku'

html_static_path = ['_static']

sys.path.insert(0,  os.path.abspath('..\\src'))
