from lino.projects.std.settings import *


class Site(Site):

    # demo_fixtures = ['demo']

    catch_layout_exceptions = False

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        yield 'lino_book.projects.gfktest.lib.gfktest'

