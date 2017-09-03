from lino.projects.std.settings import *

class Site(Site):

    languages = 'en de de-be'

    demo_fixtures = ['demo']

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino_book.projects.de_BE'

    def setup_menu(self, user_type, main):
        m = main.add_menu("master", "Master")
        m.add_action('de_BE.Expressions')
        super(Site, self).setup_menu(user_type, main)
    

SITE = Site(globals())
