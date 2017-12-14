"""The demo fixture for this tutorial.
"""
from django.conf import settings
from django.utils.timezone import make_aware
from datetime import datetime
from lino_book.projects.dumps.models import Foo

if settings.USE_TZ:
    def dt(*args):
        return make_aware(datetime(*args))
    # , timezone=pytz.timezone('Europe/Brussels')
else:
    def dt(*args):
        return datetime(*args)


def objects():
    yield Foo(
        name="First",
        last_visit=dt(2016, 7, 2, 23, 55, 12))
    yield Foo(
        name="Second",
        last_visit=dt(2016, 7, 3, 0, 10, 23))
    yield Foo(
        name="Third",
        last_visit=dt(2016, 10, 30, 2, 34, 0))
    # on the last sunday of october, at 3am all clocks are turned back
    # by one hour to 2am again. So on that day when you say 2:34 in a
    # naive timestamp


