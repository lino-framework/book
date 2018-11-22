# -*- coding: utf-8 -*-
# Copyright 2015-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Test some calendar functionalities-

This module is part of the Lino test suite. You can test only this
module by issuing either::

  $ go min2
  $ python manage.py test
  $ python manage.py test tests.test_cal.QuickTest

or::

  $ go lino
  $ python setup.py test -s tests.ProjectsTests.test_min2



"""

from __future__ import unicode_literals
from __future__ import print_function

from lino.api import dd, rt

from lino.utils.djangotest import RemoteAuthTestCase


class QuickTest(RemoteAuthTestCase):

    fixtures = ['std', 'demo_users']

    def test_create_entry(self):
        """# cal.MyEntries.insert({'requesting_panel': u'ext-comp-3913',
'user': u'luc'})

        """

        ses = rt.login("robin", renderer=dd.plugins.extjs.renderer)
        ba = rt.models.cal.MyEntries.get_action_by_name('submit_insert')
        # a = rt.models.cal.MyEntries.submit_insert
        # ba = rt.models.cal.MyEntries.insert_action
        pv = dict(user=ses.get_user())
        resp = ses.run(ba, param_values=pv)
        # ba.request_from(ses).run_from_ui(ses)
        self.assertEqual(sorted(resp.keys()), [
            'close_window', 'data_record', 'detail_handler_name',
            'info_message', 'message', 'refresh_all', 'rows', 'success'])

        # self.assertEqual(resp['data_record'].keys(), None)

        # The return message is of style 'Event "Event #69 (23.10.2014
        # 15:42)" has been created.'  The start_time is the real time
        # runtime and thus not predictable.  So we retrieve the
        # created object and use it to build that message:

        pk = resp['data_record']['id']
        obj = rt.models.cal.Event.objects.get(pk=pk)
        msg = 'Calendar entry "{0}" has been created.'.format(obj)
        self.assertEqual(resp['message'], msg)
        # self.assertEqual(msg, None)

        
        
