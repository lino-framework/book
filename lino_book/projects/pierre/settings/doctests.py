from .demo import *
SITE = Site(globals(), remote_user_header='REMOTE_USER')
# just to make the menu item visible:
SITE.plugins.b2c.configure(import_statements_path=SITE.project_dir)
DEBUG = True
