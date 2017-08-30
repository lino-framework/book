from lino.projects.std.settings import *

class Site(Site):

    title = "MLDBC Tutorial"

    demo_fixtures = ['demo']

    languages = 'en fr'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        # yield 'lino.modlib.system'
        yield 'lino_book.projects.mldbc'

    def setup_menu(self, user_type, main):
        m = main.add_menu("products", "Products")
        m.add_action('mldbc.Products')
        super(Site, self).setup_menu(user_type, main)
        
SITE = Site(globals())

DEBUG = True
