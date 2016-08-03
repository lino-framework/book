#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This is a Python dump created using dump2py.
# DJANGO_SETTINGS_MODULE was 'lino_book.projects.dumps.settings.a', TIME_ZONE was None.


from __future__ import unicode_literals

import logging
logger = logging.getLogger('lino.modlib.lino_startup.management.commands.dump2py')
import os

SOURCE_VERSION = 'None'

from decimal import Decimal
from datetime import datetime
from datetime import time, date
from django.conf import settings
from django.utils.timezone import make_aware
# from django.contrib.contenttypes.models import ContentType
from lino.utils.dpy import create_mti_child
from lino.utils.dpy import DpyLoader
from lino.core.utils import resolve_model

if settings.USE_TZ:
    def dt(*args):
        return make_aware(datetime(*args))
else:
    def dt(*args):
        return datetime(*args)
        
def new_content_type_id(m):
    if m is None: return m
    ct = settings.SITE.models.contenttypes.ContentType.objects.get_for_model(m)
    if ct is None: return None
    return ct.pk
    

def bv2kw(fieldname, values):
    """
    Needed if `Site.languages` changed between dumpdata and loaddata
    """
    return settings.SITE.babelkw(fieldname, en=values[0],de=values[1],fr=values[2])
    
dumps_Foo = resolve_model("dumps.Foo")


def create_dumps_foo(id, name, last_visit):
    kw = dict()
    kw.update(id=id)
    if name is not None: kw.update(bv2kw('name',name))
    kw.update(last_visit=last_visit)
    return dumps_Foo(**kw)




def main(args):
    loader = DpyLoader(globals())
    from django.core.management import call_command
    call_command('initdb', interactive=args.interactive)
    os.chdir(os.path.dirname(__file__))
    loader.initialize()

    execfile("dumps_foo.py")
    loader.finalize()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Restore the data.')
    parser.add_argument('--noinput', dest='interactive',
        action='store_false', default=True,
        help="Don't ask for confirmation before flushing the database.")

    args = parser.parse_args()
    main(args)
