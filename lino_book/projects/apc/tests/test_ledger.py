# -*- coding: utf-8 -*-
# Copyright 2013-2017 Luc Saffre
# License: BSD (see file COPYING for details)


"""This module contains tests that are run on a demo database without
any fixture. 

You can run only these tests by issuing::

  $ cd lino_book/projects/apc
  $ python manage.py test

"""

from __future__ import unicode_literals
from __future__ import print_function

import logging
logger = logging.getLogger(__name__)

from atelier.utils import AttrDict
import json

from lino.api.shell import *

from lino.utils.djangotest import RemoteAuthTestCase


class QuickTest(RemoteAuthTestCase):

    def test01(self):
        obj = ledger.AccountingPeriod()
        obj.full_clean()
        self.assertEqual(
            str(obj),
            'AccountingPeriod(start_date=2015-03-01,'
            'state=<PeriodStates.open:10>,year=<FiscalYears:15>)')

