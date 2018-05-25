# -*- coding: utf-8 -*-
# Copyright 2017 Luc Saffre
# This file is part of Lino Voga.
#
# Lino Voga is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Voga is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Voga.  If not, see
# <http://www.gnu.org/licenses/>.

"""Tests about how Lino computes whether there are still available
places in a course. That computation can be complex in long-running
courses where participants come and go.

To run just this test::

  $ go roger
  $ python manage.py test tests.test_max_places

"""

from __future__ import unicode_literals

from builtins import str
from lino.api import rt
from lino.api.shell import courses
from lino.api.shell import users
from django.conf import settings

from lino.utils.djangotest import RemoteAuthTestCase
from lino.utils import i2d
from lino.modlib.users.choicelists import UserTypes

from lino.utils.instantiator import create_row as create

# def create(model, **kwargs):
#     obj = model(**kwargs)
#     obj.full_clean()
#     obj.save()
#     return obj
    

class QuickTest(RemoteAuthTestCase):
    maxDiff = None

    def test01(self):
        Enrolment = rt.models.courses.Enrolment
        Pupil = rt.models.courses.Pupil
        Line = rt.models.courses.Line
        Course = rt.models.courses.Course
        CourseStates = rt.models.courses.CourseStates
        EnrolmentStates = rt.models.courses.EnrolmentStates
        EventType = rt.models.cal.EventType

        
        # room = create(cal.Room, name="First Room")
        lesson = create(EventType, name="Lesson", event_label="Lesson")
        line = create(Line, name="First Line", event_type=lesson)
        obj = create(
            Course,
            line=line,
            # room=room,
            max_places=3,
            #monday=True,
            #start_date=i2d(20140110),
            state=courses.CourseStates.active)
        self.assertEqual(str(obj), "Activity #1")

        # self.assertEqual(settings.SITE.kernel.site, settings.SITE)
        # self.assertEqual(settings.SITE, dd.site)
        # self.assertEqual(settings.SITE.plugins, dd.plugins)
        # self.assertEqual(settings.SITE.plugins.extjs, dd.plugins.extjs)

        settings.SITE.verbose_client_info_message = True
        users.User(username="robin",
                   user_type=UserTypes.admin,
                   language="en").save()
        ses = settings.SITE.login('robin')

        anna = create(Pupil, first_name="Anna")
        bert = create(Pupil, first_name="Bert")
        claire = create(Pupil, first_name="Claire")
        ernie = create(Pupil, first_name="Ernie")

        def ENR(p, start_date, **kwargs):
            return create(
                Enrolment, course=obj, pupil=p,
                state=EnrolmentStates.confirmed,
                start_date=start_date, **kwargs)

        # anna and ernie participated from the beginning.
        # bert stopped in may, and claire started in june.
        # so there were never more than 3 participants.

        # 2015-12-31 : 0 participants, 3 free places
        # 2016-01-01 : 3 participants
        # 2016-05-01 : bert leaves. 2 participants
        # 2016-06-01 : claire starts. 3 participants
        
        ENR(anna, i2d(20160101))
        ENR(bert, i2d(20160101), end_date=i2d(20160501))
        ENR(claire, i2d(20160601))
        ENR(ernie, i2d(20160101))

        self.assertEqual(obj.get_free_places(i2d(20151231)), 3)
        self.assertEqual(obj.get_free_places(i2d(20160101)), 0)
        self.assertEqual(obj.get_free_places(i2d(20160301)), 0)
        self.assertEqual(obj.get_free_places(i2d(20160531)), 1)
        self.assertEqual(obj.get_free_places(i2d(20161231)), 0)
        
        #self.assertEqual(enr.get_confirm_veto(None), '')
        
