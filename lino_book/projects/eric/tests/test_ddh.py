# -*- coding: utf-8 -*-
# Copyright 2016-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Runs some tests about the disable-delete handler and cascading deletes.

You can run only these tests by issuing::

  $ go team
  $ python manage.py test tests.test_ddh

Or::

  $ go book
  $ python setup.py test -s tests.ProjectsTests.test_ddh

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
        Project = rt.models.tickets.Project
        User = rt.models.users.User
        Star = rt.models.votes.Vote
        # ContentType = rt.models.contenttypes.ContentType
        # ct_Ticket = ContentType.objects.get_for_model(Ticket)

        create(Project, name='project')
        robin = create(User, username='robin',
                       first_name="Robin",
                       user_type=UserTypes.admin,
                       language="en")

        def createit():
            return create(Ticket, summary="Test", user=robin)

        #
        # If there are no vetos, user can ask to delete it
        #
        obj = createit()
        obj.delete()

        obj = createit()

        if False:
            try:
                robin.delete()
                self.fail("Expected veto")
            except Warning as e:
                self.assertEqual(
                    str(e), "Cannot delete User Robin "
                    "because 1 Tickets refer to it.")

        
        create(Star, votable=obj, user=robin)
        
        try:
            robin.delete()
            self.fail("Expected veto")
        except Warning as e:
            self.assertEqual(
                str(e), "Cannot delete User Robin "
                "because 1 Tickets refer to it.")

        self.assertEqual(Star.objects.count(), 1)
        self.assertEqual(Ticket.objects.count(), 1)

        obj.delete()
        self.assertEqual(Star.objects.count(), 0)
        self.assertEqual(Ticket.objects.count(), 0)
