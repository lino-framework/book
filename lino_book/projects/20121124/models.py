# -*- coding: UTF-8 -*-
# Copyright 2017-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
Is it allowed to annotate the Sum of a TimeField?
==================================================

Answer: Not under sqlite. See :djangoticket:`19360`.

>>> from lino import startup
>>> startup("lino_book.projects.20121124.settings")
>>> from lino.api.doctest import *

Let's create two tickets:

>>> t1 = Ticket(name="Ticket #1")
>>> t1.save()
>>> t2 = Ticket(name="Ticket #2")
>>> t2.save()
>>> print(Ticket.objects.all())
[<Ticket: Ticket #1>, <Ticket: Ticket #2>]

and some sessions:

>>> Session(ticket=t1,time="0:45",price="0.75").save()
>>> Session(ticket=t1,time="1:30",price="1.50").save()
>>> print(Session.objects.all())
[<Session: at 00:45:00>, <Session: at 01:30:00>]

Get the sum of the prices of all sessions for each ticket:

>>> qs = Ticket.objects.annotate(pricesum=models.Sum('sessions__price'))
>>> print([t.pricesum for t in qs])
[Decimal('2.25'), None]


Now the same with a timefield:

>>> qs = Ticket.objects.annotate(timesum=models.Sum('sessions__time'))
>>> print([str(t.timesum) for t in qs])
['02:15:00','']

The above example raises the following Exception::

  Traceback (most recent call last):
  ...
  TypeError: expected string or buffer

The same exception comes when I use Django development trunk revision 17942.

- `Value conversions of aggregate return values -- is float conversion really required?
  <https://groups.google.com/forum/?fromgroups=#!topic/django-developers/6HQlh2t1j4M>`_

"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from lino.api import dd


class Ticket(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Session(models.Model):
    ticket = dd.ForeignKey(Ticket, related_name="sessions")
    time = models.TimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "at %s" % self.time
