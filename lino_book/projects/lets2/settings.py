from lino.projects.std.settings import *


class Site(Site):

    verbose_name = "Lino LETS Tutorial (v2)"

    demo_fixtures = ['demo']

    def setup_menu(self, profile, main):
        m = main.add_menu("master", "Master")
        m.add_action(self.actors.lets.Members)
        m.add_action(self.actors.lets.Customers)
        m.add_action(self.actors.lets.Suppliers)
        m.add_action(self.actors.lets.Products)

        m = main.add_menu("market", "Market")
        m.add_action(self.actors.lets.Offers)
        m.add_action(self.actors.lets.Demands)

        m = main.add_menu("config", "Configure")
        m.add_action(self.actors.lets.Places)

    def get_dashboard_items(self, user):

        yield self.actors.lets.ActiveProducts

SITE = Site(globals(), 'lino_book.projects.lets2.lets')

DEBUG = True

