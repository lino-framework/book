from lino.projects.std.settings import *

# configure_plugin('countries', country_code='BE')

class Site(Site):

    verbose_name = "20121124"

    # demo_fixtures = ["few_countries", "few_cities", "demo"]

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino_book.projects.20121124'


SITE = Site(globals())
DEBUG = True


# INSTALLED_APPS = ['lino_book.projects.20121124']
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': ':memory:'
#     }
# }


#SECRET_KEY = "123"
