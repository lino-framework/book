# -*- coding: utf-8 -*-
# Copyright 2016-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Runs some tests about the notification framework.

You can run only these tests by issuing::

  $ go team
  $ python manage.py test tests.test_notify

Or::

  $ go book
  $ python setup.py test -s tests.test_demo.TestCase.test_team

"""

from __future__ import unicode_literals

# import six
import datetime

from mock import patch

from django.conf import settings
from django.utils.timezone import make_aware

from lino.api import dd, rt
from lino.utils.djangotest import TestCase
from lino.core import constants

from lino.modlib.users.choicelists import UserTypes

from lino.utils.instantiator import create

from lino.modlib.notify.models import send_pending_emails_often
from lino.modlib.notify.choicelists import MailModes
from lino.core.diff import ChangeWatcher

import sys
# from cStringIO import StringIO
from io import StringIO
import contextlib

@contextlib.contextmanager
def capture_stdout():
    oldout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        yield out
    finally:
        sys.stdout = oldout
        # out = out.getvalue()


class TestCase(TestCase):
    """Miscellaneous tests."""
    maxDiff = None

    def test_01(self):
        self.assertEqual(settings.SETTINGS_MODULE, None)
        self.assertEqual(settings.LOGGING, {})
        self.assertEqual(settings.SERVER_EMAIL, 'root@localhost')

    @patch('lino.api.dd.logger')
    def test_comment(self, logger):
        """Test what happens when a comment is posted on a ticket with
        watchers.

        """
        ContentType = rt.models.contenttypes.ContentType
        Ticket = rt.models.tickets.Ticket
        # Project = rt.models.tickets.Project
        Site = rt.models.tickets.Site
        Subscription = rt.models.tickets.Subscription
        # Vote = rt.models.votes.Vote
        # Star = rt.models.stars.Star
        Message = rt.models.notify.Message
        User = settings.SITE.user_model
        # create(Project, name="Project")
        robin = create(
            User, username='robin',
            first_name="Robin",
            user_type=UserTypes.admin)
        aline = create(
            User, username='aline',
            first_name="Aline",
            email="aline@example.com", language='fr',
            user_type=UserTypes.admin)

        foo = create(Site, name="Foo")
        create(Subscription, site=foo, user=aline)

        obj = create(
            Ticket, summary="Save the world, après moi le déluge",
            user=robin, site=foo)

        self.assertEqual(Message.objects.count(), 0)

        ar = rt.login('robin')
        self.client.force_login(ar.user)
        url = "/api/comments/CommentsByRFC"
        post_data = dict()
        post_data[constants.URL_PARAM_ACTION_NAME] = 'submit_insert'
        post_data.update(body="I don't agree (#foobar).")
        post_data[constants.URL_PARAM_MASTER_PK] = obj.pk
        ct = ContentType.objects.get_for_model(Ticket)
        post_data[constants.URL_PARAM_MASTER_TYPE] = ct.id
        # post_data[constants.URL_PARAM_REQUESTING_PANEL] = '123'
        self.client.force_login(robin)
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')
        result = self.check_json_result(
            response, 'rows success message close_window navinfo')
        self.assertEqual(result['success'], True)
        self.assertEqual(
            result['message'],
            """Comment "Comment #1" has been created.""")

        self.assertEqual(Message.objects.count(), 1)
        msg = Message.objects.all()[0]
        # self.assertEqual(msg.message_type)
        self.assertEqual(msg.seen, None)
        self.assertEqual(msg.user, aline)
        expected = """Robin a commenté [ticket 1] (Save the world, """\
                   """après moi le déluge):<br>I don't agree (#foobar)."""
        self.assertEqual(expected, msg.body)

        # manually set created timestamp so we can test on it later.
        now = datetime.datetime(2016, 12, 22, 19, 45, 55)
        if settings.USE_TZ:
            now = make_aware(now)
        msg.created = now
        msg.save()

        settings.SERVER_EMAIL = 'root@example.com'

        with capture_stdout() as out:
            send_pending_emails_often()

        out = out.getvalue().strip()

        # if six.PY3:
        #     if isinstance(out, bytes):
        #         out = out.decode()

        # # if isinstance(out, bytes):
        # raise Exception(out)
        # print(out)

        expected = """send email
Sender: root@example.com
To: aline@example.com
Subject: [Django] Robin a comment? #1 (? Save the world, apr?s moi le d?luge)
<html><head><base href="http://127.0.0.1:8000/" target="_blank"></head><body>
(22/12/2016 19:45)
Robin a comment? <a href="/api/tickets/Tickets/1" title="Save the world, apr&#232;s moi le d&#233;luge">#1</a> (Save the world, apr?s moi le d?luge):<br>I don't agree (#foobar).
</body></html>
"""
        self.assertEquivalent(expected, out)

        self.assertEqual(logger.debug.call_count, 1)
        logger.debug.assert_called_with(
            'Send out %s summaries for %d users.',
            MailModes.often, 1)
        # logger.info.assert_called_with(
        #     'Notify %s users about %s', 1, 'Change by robin')

        Message.objects.all().delete()
        self.assertEqual(Message.objects.count(), 0)

        cw = ChangeWatcher(obj)
        from lino_xl.lib.tickets.choicelists import Priorities
        obj.priority = Priorities.low
        obj.save_watched_instance(ar, cw)


        with capture_stdout() as out:
            send_pending_emails_often()

        out = out.getvalue().strip()
        # print(out)
        expected = ""
        # self.assertEquivalent(expected, out)

        # we do not test the output because the datetime changes. But
        # we actually just wanted to see if there is no
        # UnicodeException. We capture it in order to hide it from
        # test runner output.

        self.assertEqual(logger.debug.call_count, 2)
        logger.debug.assert_called_with(
            'Send out %s summaries for %d users.',
            MailModes.often, 1)
