# -*- coding: UTF-8 -*-
# Copyright 2012-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.projects.std.settings import *

import lino_xl


class Site(Site):

    demo_fixtures = 'std few_countries demo demo2'.split()

    verbose_name = "Lino Max"
    version = lino_xl.__version__

    project_name = 'lino_xl_max'

    project_model = 'contacts.Person'
    # use_websockets = True

    # languages = 'en de fr'
    languages = 'en de fr et nl pt-br es'

    user_types_module = 'lino_xl.lib.xl.user_types'

    default_build_method = 'weasy2pdf'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()

        yield 'lino.modlib.system'
        # yield 'lino.modlib.gfks'
        yield 'lino.modlib.users'
        yield 'lino.modlib.changes'
        yield 'lino.modlib.languages'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.properties'
        yield 'lino_xl.lib.contacts'
        yield 'lino.modlib.checkdata'
        yield 'lino_xl.lib.phones'
        yield 'lino_xl.lib.addresses'
        yield 'lino_xl.lib.humanlinks'  # requires Person to be Born
        yield 'lino_xl.lib.polls'
        yield 'lino_xl.lib.lists'

        yield 'lino.modlib.uploads'
        yield 'lino.modlib.notify'
        yield 'lino_xl.lib.notes'
        yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.cal'
        yield 'lino_xl.lib.courses'
        yield 'lino_xl.lib.extensible'
        yield 'lino_xl.lib.reception'
        yield 'lino_xl.lib.excerpts'
        yield 'lino_xl.lib.cv'
        yield 'lino_xl.lib.boards'
        yield 'lino_xl.lib.topics'
        yield 'lino_xl.lib.postings'
        yield 'lino_xl.lib.households'
        yield 'lino_xl.lib.sepa'
        yield 'lino_xl.lib.vat'
        yield 'lino_xl.lib.bevat'
        yield 'lino_xl.lib.sales'
        yield 'lino_xl.lib.invoicing'
        yield 'lino_xl.lib.b2c'
        yield 'lino_xl.lib.deploy'
        yield 'lino_xl.lib.working'
        yield 'lino_xl.lib.skills'
        yield 'lino_xl.lib.tickets'
        yield 'lino_xl.lib.votes'

        yield 'lino_xl.lib.concepts'
        yield 'lino_xl.lib.pages'
        # yield 'lino_xl.lib.beid'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.weasyprint'
        yield 'lino_xl.lib.appypod'

        yield 'lino.modlib.tinymce'
        yield 'lino.modlib.export_excel'
        
        # yield 'lino_welfare.modlib.debts'
        # yield 'lino_welfare.modlib.badges'
        # yield 'lino_welfare.modlib.welfare'
        # yield 'lino_welfare.modlib.pcsw'
        # yield 'lino_xl.lib.b2c'
        # yield 'lino_welfare.modlib.integ'
        # yield 'lino_welfare.modlib.isip'
        # yield 'lino_welfare.modlib.jobs'
        # yield 'lino_welfare.modlib.art61'
        # yield 'lino_welfare.modlib.immersion'
        # yield 'lino_welfare.modlib.active_job_search'
        # yield 'lino_welfare.modlib.xcourses'
        # yield 'lino_welfare.modlib.newcomers'
        # yield 'lino_welfare.modlib.cbss'  # must come after pcsw
        # yield 'lino_welfare.modlib.aids'
        # yield 'lino_welfare.modlib.esf'
        # yield 'lino_welfare.modlib.dupable_clients'


    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('b2c', 'import_statements_path', self.project_dir.child('sepa_in'))
        yield ('countries', 'country_code', 'BE')


    def do_site_startup(self):
        # lino_xl.lib.reception requires some workflow to be imported
        from lino_xl.lib.cal.workflows import feedback
        super(Site, self).do_site_startup()

