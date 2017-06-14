from lino.projects.std.settings import *


class Site(Site):

    demo_fixtures = "std demo demo2"
    languages = 'en'
    # default_user = "robin"
    user_types_module = 'lino_xl.lib.xl.user_types'

    def get_installed_apps(self):

        yield super(Site, self).get_installed_apps()
        yield 'lino_xl.lib.contacts'
        #~ yield 'lino_xl.lib.notes'
        # yield 'lino.modlib.changes'
        yield 'lino.modlib.users'

        yield 'lino_book.projects.watch.entries'


SITE = Site(globals())
# SITE.user_types_module = None

DEBUG = True
