from lino.projects.std.settings import *


class Site(Site):

    title = "Cool Polls"

    anonymous_user_type = '900'
    demo_fixtures = ['demo']

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'polls'

    def setup_menu(self, utype, main):
        m = main.add_menu("polls", "Polls")
        m.add_action('polls.Questions')
        m.add_action('polls.Choices')
        super(Site, self).setup_menu(utype, main)

SITE = Site(globals())

# your local settings here

DEBUG = True
