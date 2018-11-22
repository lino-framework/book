# -*- coding: utf-8 -*-
# Copyright 2013-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Runs some tests about the disable-delete handler and cascading deletes.

Reproduces :ticket:`582`.

You can run only these tests by issuing::

  $ go apc
  $ python manage.py test tests.test_ddh

Or::

  $ python setup.py test -s tests.DemoTests.test_std

"""

from __future__ import unicode_literals
from __future__ import print_function
from builtins import str
import six

from django.core.exceptions import ValidationError
from lino.utils.djangotest import RemoteAuthTestCase
from lino.api import rt
from lino.utils.mti import delete_child
from lino.utils.instantiator import create_row


class DDHTests(RemoteAuthTestCase):
    maxDiff = None

    def test01(self):
        from lino.modlib.users.choicelists import UserTypes
        User = rt.models.users.User
        Partner = rt.models.contacts.Partner
        Person = rt.models.contacts.Person
        Company = rt.models.contacts.Company
        Role = rt.models.contacts.Role
        Account = rt.models.sepa.Account
        Invoice = rt.models.vat.VatAccountInvoice
        Journal = rt.models.ledger.Journal
        VoucherTypes = rt.models.ledger.VoucherTypes
        JournalGroups = rt.models.ledger.JournalGroups

        u = User(username='robin',
                 user_type=UserTypes.admin,
                 language="en")
        u.save()

        def createit():
            obj = Person(first_name="John", last_name="Doe")
            obj.full_clean()
            obj.save()
            pk = obj.pk
            return (obj, Partner.objects.get(pk=pk))

        #
        # If there are no vetos, user can ask to delete from any MTI form
        #
        pe, pa = createit()
        pe.delete()

        pe, pa = createit()
        pa.delete()

        #
        # Cascade-related objects (e.g. addresses) are deleted
        # independently of the polymorphic form which initiated
        # deletion.
        #

        def check_cascade(model):
            pe, pa = createit()
            obj = model.objects.get(pk=pa.pk)
            rel = Account(partner=pa, iban="AL32293653370340154130927280")
            rel.full_clean()
            rel.save()
            obj.delete()
            self.assertEqual(Account.objects.count(), 0)

        check_cascade(Partner)
        check_cascade(Person)

        #
        # Vetos of one form are deteced by all other forms.
        #
        def check_veto(obj, expected):
            try:
                obj.delete()
                self.fail("Failed to raise Warning({0})".format(expected))
            except Warning as e:
                self.assertEqual(str(e), expected)

        VKR = create_row(
            Journal,
            ref="VKR", name="VKR",
            voucher_type=VoucherTypes.get_for_model(Invoice),
            journal_group=JournalGroups.sales)
        
        pe, pa = createit()

        def check_vetos(obj, msg):
            m = obj.__class__
            obj.full_clean()
            obj.save()
            check_veto(pa, msg)
            check_veto(pe, msg)
            self.assertEqual(m.objects.count(), 1)
            obj.delete()
            self.assertEqual(m.objects.count(), 0)

        msg = "Cannot delete Partner Doe John because 1 Invoices refer to it."
        msg = "Kann Partner Doe John nicht löschen weil 1 Rechnungen darauf verweisen."
        check_vetos(Invoice(partner=pa, journal=VKR), msg)

        #
        # Having an invoice does not prevent from removing the Person
        # child of the partner.
        #
        
        invoice = create_row(Invoice, partner=pa, journal=VKR)
        self.assertEqual(Partner.objects.count(), 1)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Invoice.objects.count(), 1)

        delete_child(pa, Person)

        # tidy up:
        self.assertEqual(Partner.objects.count(), 1)
        self.assertEqual(Person.objects.count(), 0)
        invoice.delete()
        pa.delete()
        self.assertEqual(Partner.objects.count(), 0)

        # But Lino refuses to remove the Person child if it has vetos.
        # For example if the person form is being used as a contact person.

        pe, pa = createit()
        co = create_row(Company, name="Test")
        create_row(Role, company=co, person=pe)
        msg = "[u'Cannot delete Partner Doe John because 1 Contact Persons refer to it.']"
        if six.PY2:
            msg = "[u'Kann Partner Doe John nicht l\\xf6schen weil 1 Kontaktpersonen darauf verweisen.']"
        else:
            msg = "['Kann Partner Doe John nicht löschen weil 1 Kontaktpersonen darauf verweisen.']"
        try:
            delete_child(pa, Person)
            self.fail("Expected ValidationError")
        except ValidationError as e:
            self.assertEqual(msg, str(e))

