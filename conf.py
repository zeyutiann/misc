#!/usr/bin/env python

import os
import sys
import ablog
import alabaster

from pathlib import Path
from typing import Any, Dict

import pydata_sphinx_theme
from sphinx.application import Sphinx

sys.path.append(str(Path(".").resolve()))

# -- Project information ------------------------------------------------------
project = "zeyutiann.misc"
copyright = "2022, TIAN Zeyu"
author = "TIAN Zeyu"

# -- General configurations ---------------------------------------------------
extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'myst_parser',
    'alabaster',
    'ablog',
    'bokeh.sphinxext.bokeh_plot',
    'jupyter_sphinx',
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", ablog.get_html_templates_path()]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [".venv/*","_website/_static/vendor/*","_website/_static/scripts/bootstrap.js.LICENSE.txt","blog/**/*interview*"]

# -- Internationalization ----------------------------------------------------

# specifying the natural language populates some key tags
language = "en"


# -- MyST options ------------------------------------------------------------
# markdown links: https://myst-parser.readthedocs.io/en/v0.13.5/using/intro.html
myst_update_mathjax = False

# -- bokeh options ------------------------------------------------------------
bokeh_plot_pyfile_include_dirs = ["_static/python"]

# -- Font-Awesome Options -----------------------------------------------------
fontawesome_included = True

# -- Ablog options -----------------------------------------------------------
blog_title = "misc"
blog_path = "zeyutiann.github.io/misc"
blog_baseurl = "https://zeyutiann.github.io/misc"

blog_authors = {
    "TIAN Zeyu": ("TIAN Zeyu", None),
}



# -- Options for HTML output ----------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_logo = '_static/logo/logo.jpeg'
html_favicon = '_static/logo/logo.jpeg'
html_sourcelink_suffix = ""

html_theme_options = {

    "external_links": [
        {"name": "tech" , "url": "https://zeyutiann.github.io"} ,
        {"name": "quant" , "url": "https://zeyutiann.github.io/quantmashup"}
    ],
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/zeyutiann",  # required
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },],

    'logo': {
        "text": "misc" ,
        "image_light": '_static/logo/logo.jpeg' ,
        "image_dark": '_static/logo/logo.jpeg' ,
    } ,
    "show_toc_level": 1,
}


html_sidebars = {
    '**': [
            #'recentposts.html',
            'categories.html',
            'tagcloud.html',
            'archives.html',
            'searchbox.html',
            # 'search-field.html'
            ],
    }

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [alabaster.get_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
todo_include_todos = True


rst_prolog = """
.. role:: python(code)
    :language: python
    :class: highlight
"""

# Output file base name for HTML help builder.
htmlhelp_basename = "zeyutiann_blog"

# -- favicon options ---------------------------------------------------------

# see https://sphinx-favicon.readthedocs.io for more information about the
# sphinx-favicon extension
favicons = [
    # generic icons compatible with most browsers
    "favicon-32x32.png",
    "favicon-16x16.png",
    {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
    # chrome specific
    "android-chrome-192x192.png",
    # apple icons
    {"rel": "mask-icon", "color": "#459db9", "href": "safari-pinned-tab.svg"},
    {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
    # msapplications
    {"name": "msapplication-TileColor", "content": "#459db9"},
    {"name": "theme-color", "content": "#ffffff"},
    {"name": "msapplication-TileImage", "content": "mstile-150x150.png"},
]

# -- Sphinx Options -----------------------------------------------------------

# If your project needs a minimal Sphinx version, state it here.
needs_sphinx = '1.2'

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = "index"
pygments_style = 'sphinx'



# -- application setup -------------------------------------------------------
def setup(app:Sphinx):
    app.add_css_file('css/custom.css',  900)






