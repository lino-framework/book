#from lino_book.projects.polly.settings import *
from .demo import *
SITE = Site(globals(), remote_user_header='REMOTE_USER')
DEBUG = True
