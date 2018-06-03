from .demo import *
team_db = DATABASES

SITE = Site(
    globals(),
    remote_user_header='REMOTE_USER')
DEBUG = True
DATABASES = team_db

# SITE.appy_params.update(raiseOnError=True)
# SITE.appy_params.update(pythonWithUnoPath='/usr/bin/python3')
SITE.default_build_method = "appyodt"
SITE.webdav_url = '/'
