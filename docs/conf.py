# -*- coding: utf-8 -*-
#
# python-pptx-ng documentation build configuration file, created by
# sphinx-quickstart on Thu Nov 29 13:59:35 2012.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))

from pptx import __version__  # noqa: E402


# -- Allow nonlocal image URI's to accommodate travis-ci status image -------

import sphinx.environment  # noqa: E402
from docutils.utils import get_source_line  # noqa: E402


def _warn_node(self, msg, node, **kwargs):
    if not msg.startswith("nonlocal image URI found:"):
        self._warnfunc(msg, "%s:%s" % get_source_line(node), **kwargs)


sphinx.environment.BuildEnvironment.warn_node = _warn_node


# -- General configuration --------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "python-pptx-ng"
copyright = "2012, 2013, Steve Canny. 2024, Martin Chrastek"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# A string of reStructuredText that will be included at the end of every source
# file that is read. This is the right place to add substitutions that should
# be available in every file.
rst_epilog = """
.. |ActionSetting| replace:: :class:`.ActionSetting`

.. |Adjustment| replace:: :class:`.Adjustment`

.. |AdjustmentCollection| replace:: :class:`.AdjustmentCollection`

.. |AreaSeries| replace:: :class:`.AreaSeries`

.. |AttributeError| replace:: :exc:`.AttributeError`

.. |Axis| replace:: :class:`.Axis`

.. |AxisTitle| replace:: :class:`.AxisTitle`

.. |_Background| replace:: :class:`._Background`

.. |BarPlot| replace:: :class:`.BarPlot`

.. |BarSeries| replace:: :class:`.BarSeries`

.. |BaseFileSystem| replace:: :class:`BaseFileSystem`

.. |_BaseMaster| replace:: :class:`._BaseMaster`

.. |BasePlaceholder| replace:: :class:`.BasePlaceholder`

.. |_BasePlot| replace:: :class:`._BasePlot`

.. |BaseShape| replace:: :class:`.BaseShape`

.. |BaseSlidePart| replace:: :class:`.BaseSlidePart`

.. |BubbleChartData| replace:: :class:`.BubbleChartData`

.. |BubblePlot| replace:: :class:`.BubblePlot`

.. |BubblePoints| replace:: :class:`.BubblePoints`

.. |BubbleSeries| replace:: :class:`.BubbleSeries`

.. |BubbleSeriesData| replace:: :class:`.BubbleSeriesData`

.. |category.Categories| replace:: :class:`~.category.Categories`

.. |data.Categories| replace:: :class:`~.data.Categories`

.. |category.Category| replace:: :class:`~.category.Category`

.. |data.Category| replace:: :class:`~.data.Category`

.. |CategoryAxis| replace:: :class:`.CategoryAxis`

.. |CategoryChartData| replace:: :class:`.CategoryChartData`

.. |CategoryLevel| replace:: :class:`.CategoryLevel`

.. |CategoryPoints| replace:: :class:`.CategoryPoints`

.. |_Cell| replace:: :class:`_Cell`

.. |Chart| replace:: :class:`.Chart`

.. |ChartData| replace:: :class:`.ChartData`

.. |ChartFormat| replace:: :class:`.ChartFormat`

.. |ChartPart| replace:: :class:`.ChartPart`

.. |ChartTitle| replace:: :class:`.ChartTitle`

.. |ChartXmlWriter| replace:: :class:`.ChartXmlWriter`

.. |_Close| replace:: :class:`_Close`

.. |Collection| replace:: :class:`Collection`

.. |ColorFormat| replace:: :class:`.ColorFormat`

.. |_Column| replace:: :class:`_Column`

.. |_ColumnCollection| replace:: :class:`_ColumnCollection`

.. |Connector| replace:: :class:`.Connector`

.. |CoreProperties| replace:: :class:`.CoreProperties`

.. |DataLabel| replace:: :class:`.DataLabel`

.. |DataLabels| replace:: :class:`.DataLabels`

.. |DateAxis| replace:: :class:`.DateAxis`

.. |datetime| replace:: :class:`datetime.datetime`

.. |DirectoryFileSystem| replace:: :class:`DirectoryFileSystem`

.. |DrawingOperations| replace:: :class:`.DrawingOperations`

.. |Emu| replace:: :class:`.Emu`

.. |False| replace:: :class:`False`

.. |FileSystem| replace:: :class:`FileSystem`

.. |FillFormat| replace:: :class:`.FillFormat`

.. |float| replace:: :class:`float`

.. |Font| replace:: :class:`.Font`

.. |FreeformBuilder| replace:: :class:`.FreeformBuilder`

.. |GradientStops| replace:: :class:`.GradientStops`

.. |GraphicFrame| replace:: :class:`.GraphicFrame`

.. |GroupShape| replace:: :class:`.GroupShape`

.. |GroupShapes| replace:: :class:`.GroupShapes`

.. |_Hyperlink| replace:: :class:`._Hyperlink`

.. |Hyperlink| replace:: :class:`.Hyperlink`

.. |Image| replace:: :class:`.Image`

.. |ImagePart| replace:: :class:`.ImagePart`

.. |Inches| replace:: :class:`.Inches`

.. |int| replace:: :class:`int`

.. |InvalidXmlError| replace:: :exc:`InvalidXmlError`

.. |KeyError| replace:: :exc:`KeyError`

.. |LayoutPlaceholder| replace:: :class:`.LayoutPlaceholder`

.. |LayoutPlaceholders| replace:: :class:`.LayoutPlaceholders`

.. |LayoutShapes| replace:: :class:`.LayoutShapes`

.. |Legend| replace:: :class:`.Legend`

.. |Length| replace:: :class:`.Length`

.. |LineFormat| replace:: :class:`.LineFormat`

.. |_LineSegment| replace:: :class:`._LineSegment`

.. |LineSeries| replace:: :class:`.LineSeries`

.. |list| replace:: :class:`list`

.. |MajorGridlines| replace:: :class:`.MajorGridlines`

.. |Marker| replace:: :class:`.Marker`

.. |MasterPlaceholder| replace:: :class:`.MasterPlaceholder`

.. |MasterPlaceholders| replace:: :class:`.MasterPlaceholders`

.. |MasterShapes| replace:: :class:`.MasterShapes`

.. |_MediaFormat| replace:: :class:`._MediaFormat`

.. |None| replace:: :class:`None`

.. |NotesMaster| replace:: :class:`.NotesMaster`

.. |NotesSlide| replace:: :class:`.NotesSlide`

.. |NotesSlidePlaceholders| replace:: :class:`.NotesSlidePlaceholders`

.. |NotesSlideShapes| replace:: :class:`.NotesSlideShapes`

.. |NotImplementedError| replace:: :exc:`NotImplementedError`

.. |OpcPackage| replace:: :class:`.OpcPackage`

.. |Package| replace:: :class:`Package`

.. |PackURI| replace:: :class:`.PackURI`

.. |_Paragraph| replace:: :class:`_Paragraph`

.. |Part| replace:: :class:`Part`

.. |PartTypeSpec| replace:: :class:`PartTypeSpec`

.. |Picture| replace:: :class:`.Picture`

.. |PieSeries| replace:: :class:`.PieSeries`

.. |_PlaceholderFormat| replace:: :class:`._PlaceholderFormat`

.. |PlaceholderGraphicFrame| replace:: :class:`.PlaceholderGraphicFrame`

.. |PlaceholderPicture| replace:: :class:`.PlaceholderPicture`

.. |Plots| replace:: :class:`.Plots`

.. |Point| replace:: :class:`.Point`

.. |pp| replace:: `python-pptx-ng`

.. |Presentation| replace:: :class:`~pptx.presentation.Presentation`

.. |PresentationPart| replace:: :class:`.PresentationPart`

.. |Pt| replace:: :class:`.Pt`

.. |RadarSeries| replace:: :class:`.RadarSeries`

.. |_Relationship| replace:: :class:`._Relationship`

.. |_Relationships| replace:: :class:`_Relationships`

.. |RGBColor| replace:: :class:`.RGBColor`

.. |_Row| replace:: :class:`_Row`

.. |_RowCollection| replace:: :class:`_RowCollection`

.. |_Run| replace:: :class:`_Run`

.. |Series| replace:: :class:`.Series`

.. |SeriesCollection| replace:: :class:`.SeriesCollection`

.. |ShadowFormat| replace:: :class:`.ShadowFormat`

.. |Shape| replace:: :class:`.Shape`

.. |ShapeCollection| replace:: :class:`.ShapeCollection`

.. |Slide| replace:: :class:`.Slide`

.. |Slides| replace:: :class:`.Slides`

.. |SlideLayout| replace:: :class:`.SlideLayout`

.. |SlideLayouts| replace:: :class:`.SlideLayouts`

.. |SlideLayoutPart| replace:: :class:`.SlideLayoutPart`

.. |SlideMaster| replace:: :class:`.SlideMaster`

.. |SlideMasters| replace:: :class:`.SlideMasters`

.. |SlideMasterPart| replace:: :class:`.SlideMasterPart`

.. |SlidePlaceholders| replace:: :class:`.SlidePlaceholders`

.. |SlideShapes| replace:: :class:`.SlideShapes`

.. |str| replace:: :class:`str`

.. |Table| replace:: :class:`Table`

.. |TextFrame| replace:: :class:`.TextFrame`

.. |TickLabels| replace:: :class:`.TickLabels`

.. |True| replace:: :class:`True`

.. |TypeError| replace:: :exc:`TypeError`

.. |ValueAxis| replace:: :class:`.ValueAxis`

.. |ValueError| replace:: :exc:`ValueError`

.. |WorkbookWriter| replace:: :class:`.WorkbookWriter`

.. |XyChartData| replace:: :class:`.XyChartData`

.. |XyPoints| replace:: :class:`.XyPoints`

.. |XySeries| replace:: :class:`.XySeries`

.. |XySeriesData| replace:: :class:`.XySeriesData`

.. |ZipFileSystem| replace:: :class:`ZipFileSystem`
"""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [".build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "armstrong"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [".themes"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    "**": ["localtoc.html", "relations.html", "sidebarlinks.html", "searchbox.html"]
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "python-pptx-ngdoc"


# -- Options for LaTeX output -----------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
#  documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "python-pptx-ng.tex",
        "python-pptx-ng Documentation",
        "Martin Chrastek",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output -----------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "python-pptx-ng", "python-pptx-ng Documentation", ["Martin Chrastek"], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ---------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "python-pptx-ng",
        "python-pptx-ng Documentation",
        "Martin Chrastek",
        "python-pptx-ng",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://docs.python.org/': None}
