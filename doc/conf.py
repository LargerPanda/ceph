import sys
import os

project = u'Ceph'
copyright = u'2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA'
version = 'dev'
release = 'dev'

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['**/.#*', '**/*~', 'start/quick-common.rst']
if tags.has('man'):
    exclude_patterns += ['architecture.rst', 'glossary.rst', 'release*.rst',
                         'api/*',
                         'cephfs/*',
                         'dev/*',
                         'install/*',
                         'mon/*',
                         'rados/*',
                         'radosgw/*',
                         'rbd/*',
                         'start/*']

pygments_style = 'sphinx'

html_theme = 'ceph'
html_theme_path = ['_themes']
html_title = "Ceph Documentation"
html_logo = 'logo.png'
html_favicon = 'favicon.ico'
html_use_smartypants = True
html_show_sphinx = False
html_sidebars = {
    '**': ['smarttoc.html', 'searchbox.html'],
    }

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
    'sphinx.ext.todo',
    'sphinxcontrib.ditaa',
    'breathe',
    ]
ditaa = 'ditaa'
todo_include_todos = True

top_level = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

breathe_default_project = "Ceph"
# see $(top_srcdir)/Doxyfile

breathe_build_directory = os.path.join(top_level, "build-doc")
breathe_projects = {"Ceph": os.path.join(top_level, breathe_build_directory)}
breathe_projects_source = {
    "Ceph": (os.path.join(top_level, "src/include/rados"),
             ["rados_types.h", "librados.h"])
}
pybind = os.path.join(top_level, 'src/pybind')
if pybind not in sys.path:
    sys.path.insert(0, pybind)
