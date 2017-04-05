# -*- coding: UTF-8 -*-
# Copyright 2012-2016 Luc Saffre
# License: BSD (see file COPYING for details)
"""
Default settings for a :mod:`lino_book.projects.min2` application.
"""

from lino.projects.std.settings import *


class Site(Site):
    """The parent of all :mod:`lino_book.projects.min2` applications.
    """
    title = "Lino Mini 2"
    project_model = 'contacts.Person'
    # project_model = 'projects.Project'
    languages = 'en et fr'
    user_types_module = 'lino_xl.lib.xl.user_types'

    demo_fixtures = """std demo demo2 checkdata""".split()

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        self.plugins.comments.configure(
            commentable_model='contacts.Partner')
        
    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        # yield 'lino.modlib.users'
        yield 'lino_xl.lib.excerpts'
        yield 'lino_book.projects.min2.modlib.contacts'
        yield 'lino_xl.lib.addresses'
        yield 'lino_xl.lib.reception'
        # yield 'lino.modlib.sepa'
        yield 'lino_xl.lib.notes'
        # yield 'lino_xl.lib.projects'
        yield 'lino_xl.lib.humanlinks'
        yield 'lino_xl.lib.households'
        yield 'lino_xl.lib.extensible'
        yield 'lino_xl.lib.pages'
        yield 'lino.modlib.export_excel'
        yield 'lino_xl.lib.dupable_partners'
        yield 'lino.modlib.plausibility'
        yield 'lino.modlib.tinymce'
        yield 'lino.modlib.wkhtmltopdf'
        yield 'lino_xl.lib.appypod'
        yield 'lino.modlib.notify'
        yield 'lino.modlib.changes'
        yield 'lino.modlib.comments'

    def setup_actions(self):
        super(Site, self).setup_actions()
        partners = self.modules.contacts
        from lino.core.merge import MergeAction
        for m in (partners.Person, partners.Organisation):
            m.define_action(merge_row=MergeAction(m))

