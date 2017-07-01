from lino.projects.std.settings import *


class Site(Site):

    verbose_name = "Lino LETS Tutorial (v2)"

    demo_fixtures = ['demo']

    def setup_menu(self, profile, main):
        m = main.add_menu("master", "Master")
        m.add_action(self.models.lets.Members)
        m.add_action(self.models.lets.Customers)
        m.add_action(self.models.lets.Suppliers)
        m.add_action(self.models.lets.Products)

        m = main.add_menu("market", "Market")
        m.add_action(self.models.lets.Offers)
        m.add_action(self.models.lets.Demands)

        m = main.add_menu("config", "Configure")
        m.add_action(self.models.lets.Places)

    def get_dashboard_items(self, user):

        yield self.models.lets.ActiveProducts

SITE = Site(globals(), 'lino_book.projects.lets2.lets')

DEBUG = True

