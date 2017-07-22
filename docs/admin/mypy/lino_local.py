# -*- coding: UTF-8 -*-
# replace 'mydomain.com' by your domain name
# change the value of SECRET_KEY

import site
import os, sys
from os.path import split, dirname, join, realpath, exists

def manage(filename, *args, **kw):
    # Called from manage.py files
    setup(dirname(filename), *args, **kw)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

def wsgi(globals_dict, *args, **kw):
    # Called from wsgi.py files
    homedir = dirname(globals_dict['__file__'])
    sp = realpath(join(homedir, 'env/lib/python2.7/site-packages'))
    assert exists(sp)
    site.addsitedir(sp)
    setup(homedir, *args, **kw)
    from django.core.wsgi import get_wsgi_application
    globals_dict.update(application=get_wsgi_application())

def setup(homedir, settings_module=None):
    if settings_module is None:
        # If homedir is '/path/to/mysites/prj1/', set settings_module
        # to 'mysites.prj1.settings':
        parts = split(homedir)
        prj = parts[-1]
        prefix = split(parts[-2])[-1] + '.'
        settings_module = prefix + prj + '.settings'
    
    os.environ['DJANGO_SETTINGS_MODULE'] = settings_module
    os.environ['LINO_SITE_MODULE'] = 'lino_local'
    

def setup_site(self):
    # Site-wide default Django settings.
    # Called when the Site object has been initialized. The Django
    # settings module cannot yet be imported but we can write to its
    # global namespace.
    self.csv_params = dict(delimiter=',', encoding='utf-16')
    self.build_js_cache_on_startup = False
    self.default_build_method='appypdf'
    self.appy_params.update(ooPort=8100)

    self.django_settings.update(
        EMAIL_HOST='mail.mydomain.com',
        ALLOWED_HOSTS=['.mydomain.com'],
        EMAIL_SUBJECT_PREFIX='['+self.project_name+'] ',
        SERVER_EMAIL='noreply@mydomain.com',
        DEFAULT_FROM_EMAIL='noreply@mydomain.com',
        ADMINS=[["John Doe", "john@mydomain.com"]],
        DEBUG=False,
        SECRET_KEY='?~hdakl123ASD%#¤/&¤')

