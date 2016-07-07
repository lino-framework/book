# -*- coding: UTF-8 -*-
# Copyright 2012-2014 Luc Saffre
# License: BSD (see file COPYING for details)


import os
import lino

from lino.projects.std.settings import *


class Site(Site):
    #~ title = __name__
    version = "0.0.1"
    verbose_name = "Lino-HWS"
    url = "http://www.lino-framework.org/autodoc/lino.projects.homeworkschool"
    #~ author = "Luc Saffre"
    #~ author_email = "luc.saffre@gmx.net"

    #~ help_url = "http://lino.saffre-rumma.net/az/index.html"

    demo_fixtures = 'std few_languages demo demo2'.split(
    )

    #~ project_model = 'contacts.Person'
    #~ project_model = 'courses.Pupil'
    project_model = 'courses.Course'
    #~ project_model = None

    languages = ('en', 'de', 'fr')

    use_eid_jslib = False

    #~ index_view_action = "dsbe.Home"

    override_modlib_models = {
        'contacts.Person': None,
        'sales.Invoice': None,
        'sales.InvoiceItem': None,
    }

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.contacts'
        yield 'lino_xl.lib.households'
        yield 'lino_xl.lib.notes'
        yield 'lino.modlib.uploads'
        yield 'lino_xl.lib.extensible'
        yield 'lino_xl.lib.cal'
        yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.pages'

        # yield 'lino.modlib.accounts'
        # yield 'lino.modlib.ledger'
        # yield 'lino.modlib.vat'
        yield 'lino_xl.lib.products'
        # yield 'lino.modlib.auto.sales'

        yield 'lino.modlib.courses'
        yield 'lino_book.projects.homeworkschool'

