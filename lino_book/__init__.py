# -*- coding: UTF-8 -*-
# Copyright 2002-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""The :mod:`lino_book` package contains a set of example projects
used both for testing and explaining Lino framework.

It is not published on PyPI because that would make no sense.  You use it by
cloning the repository from GitHub (which is done automatically by
:ref:`getlino`).

.. autosummary::
   :toctree:

   projects

"""

from os.path import join, dirname
from .setup_info import SETUP_INFO
# filename = join(dirname(__file__), 'setup_info.py')
# with open(filename, "rb") as fd: exec(compile(fd.read(), filename, 'exec'))

__version__ = SETUP_INFO['version']
# intersphinx_urls = dict(docs="http://www.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/book/blob/master/%s'

# doc_trees = ['docs']
doc_trees = [ 'docs']
intersphinx_urls = {
    'docs': "http://www.lino-framework.org",
}
