from ..settings import *

SITE = Site(globals(), is_demo_site=True)
DEBUG = True

# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'
