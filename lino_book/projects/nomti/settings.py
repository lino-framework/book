# from lino.projects.std.settings import *
# SITE = Site(globals(), 'nomti')

from lino.projects.std.settings import *


class Site(Site):
    demo_fixtures = ['demo']
    def get_installed_apps(self):
        # yield 'lino.modlib.users'
        yield super(Site, self).get_installed_apps()
        yield 'lino_book.projects.nomti.app'

    def setup_menu(self, profile, main):
        m = main.add_menu("contacts", "Contacts")
        m.add_action('app.Persons')
        m.add_action('app.Places')
        m.add_action('app.Restaurants')

SITE = Site(globals())

DEBUG = True
