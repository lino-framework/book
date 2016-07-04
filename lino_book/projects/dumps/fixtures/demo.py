"""The demo fixture for this tutorial.
"""
from django.conf import settings
from django.utils.timezone import make_aware
from datetime import datetime
from lino_book.projects.dumps.models import Foo

if settings.USE_TZ:
    def dt(*args):
        return make_aware(datetime(*args))
else:
    def dt(*args):
        return datetime(*args)


def objects():
    yield Foo(
        name="First",
        last_visit=dt(2016, 07, 02, 23, 55, 12))
    yield Foo(
        name="Last",
        last_visit=dt(2016, 07, 03, 0, 10, 23))
