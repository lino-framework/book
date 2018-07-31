# -*- coding: utf-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

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

        # 20180731 the default value for the enrolment state was a
        # string which became an EnrolmentStates choice only during
        # full_clean().  Now this case is being resolved in
        # ChoiceListField.__init__().
        
        enr = Enrolment(course=obj, pupil=anna)
        self.assertEqual(enr.state, EnrolmentStates.requested)
