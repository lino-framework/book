# -*- coding: UTF-8 -*-
# Copyright 2002-2016 Luc Saffre
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
intersphinx_urls = dict(docs="http://www.lino-framework.org")
srcref_url = 'https://github.com/lsaffre/lino_book/blob/master/%s'

