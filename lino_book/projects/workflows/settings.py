from lino.projects.std.settings import *


class Site(Site):

    demo_fixtures = "std demo demo2"
    languages = 'en'
    # default_user = "robin"
    user_types_module = 'lino_xl.lib.xl.user_types'
    workflows_module = "lino_book.projects.workflows.entries.workflows"

    def get_installed_apps(self):

        yield super(Site, self).get_installed_apps()
        yield 'lino_xl.lib.contacts'
        yield 'lino.modlib.users'

        yield 'lino_book.projects.workflows.entries'


SITE = Site(globals())
# SITE.user_types_module = None

DEBUG = True
