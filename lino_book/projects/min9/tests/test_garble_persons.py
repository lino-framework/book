# -*- coding: utf-8 -*-
# Copyright 2016 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Tests the :manage:`garble_persons` command.

.. You can test only this module by issuing either::

  $ go min2
  $ python manage.py test
  $ python manage.py test tests.test_garble_persons

or::

  $ go book
  $ python setup.py test -s tests.ProjectsTests.test_min2

"""

from __future__ import unicode_literals
from __future__ import print_function

from lino.api import rt

# from lino.modlib.gfks.mixins import Controllable

from lino.utils.djangotest import RemoteAuthTestCase

from django.core.management import call_command


class QuickTest(RemoteAuthTestCase):

    fixtures = ['std', 'few_countries', 'few_cities']

    def test_01(self):
        call_command(
            'garble_persons', '--distribution=ee', '--noinput')
