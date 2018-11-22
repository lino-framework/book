# -*- coding: UTF-8 -*-
# Copyright 2013-2015 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
Default settings module for a :ref:`polly` project.
"""

from __future__ import unicode_literals

from lino.projects.std.settings import *

from django.utils.translation import ugettext_lazy as _


class Site(Site):

    """
    Base class for a :ref:`polly` application,
    designed to be instantiated into the :setting:`SITE` setting.
    """

    verbose_name = "Lino Polly"
    description = _("a Lino application to make surveys and polls.")
    version = "0.1"
    url = "http://www.lino-framework.org/examples/polly"
    author = 'Luc Saffre'
    author_email = 'luc.saffre@gmail.com'

    demo_fixtures = 'std demo feedback compass demo2'.split()
    # user_types_module = 'lino_book.projects.polly.user_types'
    user_types_module = 'lino_xl.lib.xl.user_types'

    languages = 'en de et'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        yield 'lino.modlib.users'
        yield 'lino_xl.lib.polls'
