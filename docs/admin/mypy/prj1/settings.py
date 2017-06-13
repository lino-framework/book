# -*- coding: UTF-8 -*-
from lino.projects.std.settings import *

import logging
logging.getLogger('weasyprint').setLevel("ERROR") # see #1462


class Site(Site):
    title = "Lino@prj1"
    server_url = "https://prj1.mydomain.com"
    
SITE = Site(globals())

# locally override attributes of individual plugins
# SITE.plugins.finan.suggest_future_vouchers = True

# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite', #database name
        'USER': 'django',
        'PASSWORD': 'my cool password',
        'HOST': 'localhost',                  
        'PORT': 3306,
        'OPTIONS': {
           "init_command": "SET storage_engine=MyISAM",
        }
    }
}
