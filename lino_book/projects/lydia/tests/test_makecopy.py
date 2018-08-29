# -*- coding: utf-8 -*-
# Copyright 2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""This module contains some quick tests:

You can run only these tests by issuing::

  $ go lydia
  $ python manage.py test tests.test_makecopy

"""

from __future__ import unicode_literals
from __future__ import print_function


from lino.api import rt
from lino.utils.djangotest import RemoteAuthTestCase
from lino.utils.instantiator import create_row
from lino.core.renderer import TestRenderer


#class QuickTest(RemoteAuthTestCase):
class QuickTest(object):  # skipping since MakeCopy is no longer needed.
    maxDiff = None
    # fixtures = ["std", 'demo']
    fixtures = 'std minimal_ledger'.split()
    
    def test_makecopy(self):
        UserTypes = rt.models.users.UserTypes
        Partner = rt.models.contacts.Partner
        Account = rt.models.ledger.Account
        AnaAccountInvoice = rt.models.ana.AnaAccountInvoice
        jnl = rt.models.ledger.Journal.objects.get(ref="PRC")
        # acc = rt.models.ledger.Account.objects.get(ref="PRC")
        user = create_row(rt.models.users.User,
            username="robin", user_type=UserTypes.admin)
        ses = rt.login('robin', renderer=TestRenderer())
        partner = create_row(Partner, name="Foo")
        self.assertEqual(AnaAccountInvoice.objects.count(), 0)
        invoice = jnl.create_voucher(partner=partner, user=user)
        self.assertEqual(
            invoice.__class__, AnaAccountInvoice)
        invoice.full_clean()
        invoice.save()
        ga = Account.objects.filter(
            needs_ana=True, ana_account__isnull=False).order_by('ref')[0]
        for n in range(3):
            i = invoice.add_voucher_item(
                account=ga,
                seqno=3-n,  # enter them in reverse order to reproduce
                            # #2470
                total_incl=123+n)
            i.full_clean()
            i.save()
        
        s = ses.show('ana.ItemsByInvoice', invoice,
                     column_names="seqno account total_incl")
        # print(s)
        expected = """\
==================== ============================= =================
 No.                  Account                       Total incl. VAT
-------------------- ----------------------------- -----------------
 1                    (6010) Purchase of services   125,00
 2                    (6010) Purchase of services   124,00
 3                    (6010) Purchase of services   123,00
 **Total (3 rows)**                                 **372,00**
==================== ============================= =================
"""
        self.assertEqual(s, expected)
        self.assertEqual(AnaAccountInvoice.objects.count(), 1)
        self.assertEqual(invoice.number, 1)

        invoice.make_copy.run_from_session(ses)
        self.assertEqual(AnaAccountInvoice.objects.count(), 2)

        invoice = AnaAccountInvoice.objects.get(number=2)

        s = ses.show('ana.ItemsByInvoice', invoice,
                     column_names="seqno account total_incl")
        # print(s)
        self.assertEqual(s, expected)
        
