# -*- coding: utf-8 -*-
# Copyright 2016-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Runs some tests about the disable-delete handler and cascading deletes.

You can run only these tests by issuing::

  $ go team
  $ python manage.py test tests.test_ddh

Or::

  $ go book
  $ python setup.py test tests.test_ddh

"""

from __future__ import unicode_literals
from __future__ import print_function

from django.core.exceptions import ValidationError
from lino.utils.djangotest import RemoteAuthTestCase
from lino.api import rt

from lino.utils.instantiator import create_row as create
    

class DDHTests(RemoteAuthTestCase):
    maxDiff = None

    def test01(self):
        from lino.modlib.users.choicelists import UserTypes
        Ticket = rt.models.tickets.Ticket
        User = rt.models.users.User
        Subscription = rt.models.tickets.Subscription
        Site = rt.models.tickets.Site
        # ContentType = rt.models.contenttypes.ContentType
        # ct_Ticket = ContentType.objects.get_for_model(Ticket)

        site = create(Site, name='project')
        robin = create(User, username='robin',
                       first_name="Robin",
                       user_type=UserTypes.admin,
                       language="en")
        create(Subscription, site=site, user=robin)

        def createit():
            return create(Ticket, summary="Test", user=robin, site=site)

        #
        # If there are no vetos, user can ask to delete it
        #
        ticket = createit()
        ticket.delete()

        ticket = createit()

        # we cannot delete the user because a ticket refers to it:

        try:
            robin.delete()
            self.fail("Expected veto")
        except Warning as e:
            self.assertEqual(
                str(e), "Cannot delete User Robin "
                "because 1 Tickets refer to it.")

        
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(Ticket.objects.count(), 1)

        # when we have deleted the ticket, deleting the user works
        # because the subscription is deleted in cascade:
        
        ticket.delete()
        robin.delete()
        self.assertEqual(Subscription.objects.count(), 0)
        self.assertEqual(Ticket.objects.count(), 0)
        self.assertEqual(User.objects.count(), 0)
