# -*- coding: UTF-8 -*-
# Copyright 2012-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.projects.std.settings import *


class Site(Site):
    title = "Lino Mini 9"
    project_model = 'contacts.Person'
    # project_model = 'projects.Project'
    languages = 'en et fr'
    user_types_module = 'lino_xl.lib.xl.user_types'

    demo_fixtures = """std demo demo2 checkdata""".split()

    default_build_method = 'weasy2pdf'

    # def setup_plugins(self):
    #     super(Site, self).setup_plugins()
    #     self.plugins.comments.configure(
    #         commentable_model='contacts.Partner')
        
    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        # yield 'lino.modlib.users'
        yield 'lino_xl.lib.excerpts'
        yield 'lino_book.projects.min9.modlib.contacts'
        yield 'lino_xl.lib.addresses'
        yield 'lino_xl.lib.reception'
        yield 'lino_xl.lib.courses'
        # yield 'lino.modlib.sepa'
        yield 'lino_xl.lib.notes'
        # yield 'lino_xl.lib.projects'
        yield 'lino_xl.lib.humanlinks'
        yield 'lino_xl.lib.households'
        yield 'lino_xl.lib.extensible'
        yield 'lino_xl.lib.pages'
        yield 'lino.modlib.export_excel'
        yield 'lino_xl.lib.dupable_partners'
        yield 'lino.modlib.checkdata'
        yield 'lino.modlib.tinymce'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.weasyprint'
        yield 'lino_xl.lib.appypod'
        yield 'lino.modlib.notify'
        yield 'lino.modlib.changes'
        yield 'lino.modlib.comments'
        yield 'lino.modlib.uploads'

    # def setup_actions(self):
    #     super(Site, self).setup_actions()
    #     partners = self.modules.contacts
    #     from lino.core.merge import MergeAction
    #     for m in (partners.Person, partners.Organisation):
    #         m.define_action(merge_row=MergeAction(m))

    # migration_module = 'lino_book.projects.min9.db_migrations'
