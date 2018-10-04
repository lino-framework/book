# -*- coding: utf-8 -*-
# Copyright 2013-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Runs some tests about the Sequenced mixin.

You can run only these tests by issuing::

  $ go apc
  $ python manage.py test tests.test_sequenced

"""

from __future__ import unicode_literals
from __future__ import print_function
from builtins import str

from django.core.exceptions import ValidationError
from lino.utils.djangotest import RemoteAuthTestCase
from lino.api import rt
from lino.utils.mti import delete_child
from lino.utils.instantiator import create_row


class Tests(RemoteAuthTestCase):
    maxDiff = None

    def test01(self):
        from lino.modlib.users.choicelists import UserTypes
        User = rt.models.users.User
        Account = rt.models.ledger.Account
        
        Journal = rt.models.ledger.Journal
        Partner = rt.models.contacts.Partner
        Person = rt.models.contacts.Person
        Company = rt.models.contacts.Company
        Role = rt.models.contacts.Role
        # Account = rt.models.sepa.Account
        Invoice = rt.models.vat.VatAccountInvoice
        VoucherTypes = rt.models.ledger.VoucherTypes
        JournalGroups = rt.models.ledger.JournalGroups

        robin = create_row(
            User, username='robin',
            user_type=UserTypes.admin, language="en")
        ar = rt.login('robin')
        
        a = create_row(Account, name="A")
        b = create_row(Account, name="B")
        c = create_row(Account, name="C")
        d = create_row(Account, name="D")

        lst = [i.seqno for i in Account.objects.order_by('name')]
        self.assertEqual(lst, [1, 2, 3, 4])
        
        self.assertEqual(a.seqno, 1)
        self.assertEqual(b.seqno, 2)
        self.assertEqual(c.seqno, 3)
        self.assertEqual(d.seqno, 4)

        response = a.move_down()
        
        self.assertEqual(response, {
            'message': 'Renumbered 1 of 3 siblings.',
            'success': True,
            'refresh_all': True})

        # NOTE that a, b, c and d are invalid now
        a = b = c = d = None

        lst = [i.seqno for i in Account.objects.order_by('name')]
        self.assertEqual(lst, [2, 1, 3, 4])
        
        lst = [i.name for i in Account.objects.order_by('seqno')]
        self.assertEqual(''.join(lst), "BACD")
        
        # fr = create_row(Country, isocode="FR")

