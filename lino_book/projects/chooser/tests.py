# -*- coding: utf-8 -*-
# Copyright 2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
To run only this test::

  $ go combo
  $ python manage.py test

"""

from __future__ import unicode_literals

from django.conf import settings
from django.utils import translation
from django.core.exceptions import ValidationError

from lino.utils.djangotest import RemoteAuthTestCase

from lino.api import dd, rt



class QuickTest(RemoteAuthTestCase):

    def test01(self):
        """
        Tests some basic funtionality.
        """
        self.assertEqual(1+1,3)
        
