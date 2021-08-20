project = "his-geo-backend"
copyright = "Akuna Capital LLC"
author = "Akuna Capital LLC"

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"
html_theme_options = {"display_version": True, "collapse_navigation": False}
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.inheritance_diagram",
    "m2r2",
    "sphinxcontrib.plantuml",
]
autodoc_default_options = {"members": True, "undoc-members": True, "inherited-members": True, "show-inheritance": True}
source_suffix = [".rst", ".md"]
inheritance_graph_attrs = {"bgcolor": "transparent"}
graphviz_output_format = "svg"
autoclass_content = "both"
plantuml_output_format = "svg_img"
