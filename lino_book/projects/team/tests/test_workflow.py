# -*- coding: utf-8 -*-
# Copyright 2016-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Runs some tests about ticket and vote workflow.

You can run only these tests by issuing::

  $ go team
  $ python manage.py test tests.test_workflow

"""

from __future__ import unicode_literals
from __future__ import print_function

from django.conf import settings
from django.core.exceptions import ValidationError
from lino.utils.djangotest import RemoteAuthTestCase
from lino.api import dd, rt

from lino.utils.instantiator import create_row as create
    

class WorkflowTests(RemoteAuthTestCase):
    maxDiff = None

    def test01(self):
        from lino.modlib.users.choicelists import UserTypes
        Ticket = rt.models.tickets.Ticket
        # Project = rt.models.tickets.Project
        # Line = rt.models.courses.Line
        # Activity = rt.models.courses.Course
        # Enrolment = rt.models.courses.Enrolment
        # Meeting = rt.models.meetings.Meeting
        Change = rt.models.changes.Change
        User = rt.models.users.User
        # Vote = rt.models.votes.Vote
        # VoteStates = rt.models.votes.VoteStates
        # VotesByVotable = rt.models.votes.VotesByVotable
        # ContentType = rt.models.contenttypes.ContentType
        # ct_Ticket = ContentType.objects.get_for_model(Ticket)

        # create(Project, name='project')

        robin = create(User, username='robin',
                       first_name="Robin",
                       user_type=UserTypes.admin,
                       language="en")
        anna = create(User, username='anna',
                      first_name="Anna",
                      user_type=UserTypes.customer,
                      language="en")
        berta = create(User, username='berta',
                       first_name="Berta",
                       user_type=UserTypes.customer,
                       language="en")
        # meeting = create(Meeting, name="Test")
        # sprints = create(Line, name="Sprints")
        # sprint = create(Activity, line=sprints)
        #
        # Enrolment(course=sprint, pupil=robin)
        
        ses = rt.login('robin')
        
        ticket = create(Ticket, summary="First", user=robin)
        ticket.after_ui_save(ses, None)
        # vote = Vote.objects.get(votable=ticket)
        # self.assertEqual(vote.user, robin)
        # self.assertEqual(vote.state, VoteStates.author)
        
        def check_success(ia, **kwargs):
            rv = ia.run_from_session(ses, **kwargs)
            self.assertEqual(rv, {'success': True, 'refresh': True})

        check_success(ticket.mark_talk)
        check_success(ticket.mark_working)
        check_success(ticket.mark_refused)
        check_success(ticket.mark_closed)
        check_success(ticket.mark_refused)
        
        # Vote.objects.all().delete()
        Ticket.objects.all().delete()
        
        # self.assertEqual(Vote.objects.count(), 0)

        ticket = create(
            Ticket, summary="Second", user=robin, end_user=anna)
        ticket.after_ui_save(ses, None)
        # self.assertEqual(Vote.objects.count(), 2)
        #
        # vote = Vote.objects.get(votable=ticket, user=anna)
        # self.assertEqual(vote.state, VoteStates.author)
        #
        #
        # # manually creating a vote will make the vote invited:
        # vote = create(
        #     Vote, votable=ticket, user=berta)
        # # vote.after_ui_save(ses, None)
        # self.assertEqual(vote.state, VoteStates.invited)

        # raise Exception("{!r}".format(
        #     VotesByVotable.submit_insert.defining_actor))
        # rv = VotesByVotable.submit_insert.run_from_session(
        #     ses, user=berta)


        # try:
        #     robin.delete()
        #     self.fail("Expected veto")
        # except Warning as e:
        #     self.assertEqual(
        #         str(e), "Cannot delete User Robin "
        #         "because 1 Changes refer to it.")

        
