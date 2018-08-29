.. doctest docs/specs/cosi/tim2lino.rst
.. _cosi.specs.tim2lino:

==================
Importing from TIM
==================

>>> import lino
>>> lino.startup('lino_book.projects.pierre.settings.demo')
>>> from lino.api.doctest import *
>>> from django.db.models import Q


>>> from lino_xl.lib.tim2lino.utils import TimLoader
>>> tim = TimLoader('', 'en')
>>> tim.dc2lino("D")
False
>>> tim.dc2lino("C")
True

>>> tim.dc2lino("A")
False
>>> tim.dc2lino("E")
True
