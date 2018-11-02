# -*- coding: UTF-8 -*-
# Copyright 2002-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""The :mod:`lino_book` package contains a set of example projects
used both for testing and explaining Lino framework.

.. autosummary::
   :toctree:

   projects

"""

from os.path import join, dirname
filename = join(dirname(__file__), 'setup_info.py')
exec(compile(open(filename, "rb").read(), filename, 'exec'))

__version__ = SETUP_INFO['version']
# intersphinx_urls = dict(docs="http://www.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/book/blob/master/%s'

# doc_trees = ['docs']
doc_trees = [ 'docs', 'tera_de', 'welfare_de', 'welfare_fr', 'noi']
intersphinx_urls = {
    'docs': "http://www.lino-framework.org",
    'tera_de': "http://tera-handbuch.lino-framework.org",
    'noi': "http://noi.lino-framework.org",
    'welfare_de': "http://de.welfare.lino-framework.org",
    'welfare_fr' : "http://fr.welfare.lino-framework.org",
}
