#!/usr/bin/env python3
# -*- coding: utf-8 -*-
templates_path = ["_templates"]

source_suffix = ".rst"
master_doc = "index"

project = "Swiss Federal Elections 2023"
copyright = "David Schurtenberger, 2023"
author = "David Schurtenberger"


language = "en"

exclude_patterns = ["_build"]

pygments_style = "default"

todo_include_todos = False

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "search_bar_text": "Find in doc",
    "show_nav_level": 0,
}

html_static_path = ["_static"]
html_logo = "DVIZ_logo.png"
html_favicon = "DVIZ_logo.png"

html_show_sourcelink = False