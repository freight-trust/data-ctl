import os

import sys

sys.path.insert(0, os.path.abspath('..'))

import drewry_container_index

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'Container Freight Contract Index'

copyright = "2020, FreightTrust and Clearing Corporation"

author = "FreightTrust and Clearing Corporation"

version = drewry_container_index.__version__

release = drewry_container_index.__version__

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = 'alabaster'

html_static_path = ['_static']

htmlhelp_basename = 'drewry_container_indexdoc'

latex_elements = {}

latex_documents = [(master_doc, 'drewry_container_index.tex', 'Container Freight Contract Index Documentation', 'FreightTrust and Clearing Corporation', 'manual')]

man_pages = [(master_doc, 'drewry_container_index', 'Container Freight Contract Index Documentation', [author], 1)]

texinfo_documents = [(master_doc, 'drewry_container_index', 'Container Freight Contract Index Documentation', author, 'drewry_container_index', 'One line description of project.', 'Miscellaneous')]
