## Copyright 2013-2018 Rumma & Ko Ltd

from lino.projects.std.settings import *

from lino.api import _

class Site(Site):
    
    demo_fixtures = "std demo demo2"
    languages = 'en'
    # user_types_module = 'lino_xl.lib.xl.user_types'
    
    def get_installed_apps(self):
        
        yield super(Site, self).get_installed_apps()
            
        #~ yield 'lino.modlib.gfks'
        # yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        #~ yield 'lino.modlib.changes'
        
        # yield 'lino_xl.lib.countries'
        # yield 'lino_xl.lib.contacts'
        #~ yield 'lino_xl.lib.notes'
        
        yield 'lino_book.projects.watch2'
        
    def setup_menu(self, user_type, main):
        m = main.add_menu("entries", _("Entries"))
        m.add_action(self.models.watch2.Companies)
        m.add_action(self.models.watch2.Entries)
        m.add_action(self.models.watch2.EntryTypes)
        m.add_action(self.models.watch2.CompaniesWithEntryTypes)


SITE = Site(globals())

DEBUG = True
