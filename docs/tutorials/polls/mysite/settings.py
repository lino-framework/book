from lino.projects.std.settings import *


class Site(Site):

    title = "Cool Polls"

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'polls'

    def setup_menu(self, user_type, main):
        super(Site, self).setup_menu(user_type, main)
        m = main.add_menu("polls", "Polls")
        m.add_action('polls.Questions')
        m.add_action('polls.Choices')

SITE = Site(globals())

# your local settings here

DEBUG = True
