import os, sys
from os.path import split, dirname, abspath, join, exists, realpath

DEBUG=False

def manage(filename,*args,**kw):
    setup(dirname(abspath(filename)), *args, **kw)
    # print(20170216, sys.path)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


def setup_wsgi(globals_dict,*args,**kw):
    filename = globals_dict['__file__']
    home_dir,tail = split(dirname(abspath(filename)))
    assert tail == 'apache', "%r is not apache" % tail
    setup(home_dir, *args, **kw)
    import django.core.handlers.wsgi
    globals_dict.update(application=django.core.handlers.wsgi.WSGIHandler())

def setup(homedir,settings_module=None):
    if False:
      sp = realpath(join(homedir, 'env/lib/python2.7/site-packages'))
      if not exists(sp):
        raise Exception("Oops: {} does not exist!".format(sp))
      import site
      #print("20170216 adding site", sp)
      site.addsitedir(sp)
    if settings_module is None:
        # prj = split(dirname(abspath(filename)))[-1]
        parts = split(homedir)
        prj = parts[-1]
        prefix = split(parts[-2])[-1] + '.'
        settings_module = prefix + prj + '.settings'
    os.environ['DJANGO_SETTINGS_MODULE'] = settings_module
    os.environ['LINO_SITE_MODULE'] = 'lino_local'


def setup_site(self):
    # some example content
    self.is_demo_site = False
    self.build_js_cache_on_startup = False
    self.django_settings.update(EMAIL_HOST=...)
    
    
