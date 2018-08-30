# -*- coding: utf-8 -*-
# Copyright 2013-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


"""This module contains tests that are run on a demo database without
any fixture. 

You can run only these tests by issuing::

  $ cd lino_book/projects/apc
  $ python manage.py test tests.test_ledger

"""

from __future__ import unicode_literals
from __future__ import print_function

from lino.api.shell import dd, ledger, settings

from lino.utils.djangotest import RemoteAuthTestCase


class QuickTest(RemoteAuthTestCase):

    def test01(self):
        self.assertEqual(dd.plugins.ledger.fix_y2k, False)
        self.assertEqual(settings.SITE.today().year, 2015)
        obj = ledger.FiscalYear.create_from_year(
            settings.SITE.today().year)
        obj.full_clean()
        obj.save()
        self.assertEqual(obj.ref, '2015')
        
        obj = ledger.AccountingPeriod()
        obj.full_clean()
        self.assertEqual(
            str(obj),
            'AccountingPeriod(start_date=2015-03-01,'
            'state=<PeriodStates.open:10>,year=1)')

