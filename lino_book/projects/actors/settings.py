from lino.projects.std.settings import *
SITE = Site(
    globals(),
    'lino_book.projects.actors',
    # user_model=None,
    demo_fixtures=['demo'])
#print(SITE.is_local_project_dir)
#SITE.is_local_project_dir = False
#from lino.core.utils import is_devserver
#print(is_devserver())
# print(SITE.installed_plugins)
# print(MEDIA_URL, MEDIA_ROOT)
