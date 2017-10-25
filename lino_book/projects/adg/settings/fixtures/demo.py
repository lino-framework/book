# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""General demo data for Lino Avanti.

- Course providers and courses

"""

from __future__ import unicode_literals

# from django.conf import settings
# from lino.utils import mti
from lino.utils import Cycler  # join_words
from lino.utils.mldbc import babel_named as named
from lino.api import rt, dd, _

from lino.modlib.users.choicelists import UserTypes
from lino_xl.lib.cal.choicelists import Recurrencies
from lino_xl.lib.courses.choicelists import EnrolmentStates

course_stages = [
    _("Dispens"),
    _("Eingeschrieben"),
    _("Abgeschlossen"),
    _("Abgebrochen"),
    _("Ausgeschlossen")]

trends_config = []
trends_config.append((
    _("Info Integration"),
    [ "Erstgespräch",
      "Sprachtest",
      "Einschreibung in Sprachkurs",
      "Einschreibung in Integrationskurs",
      "Bilanzgespräch"]))
trends_config.append((_("Alphabetisation"), course_stages))
trends_config.append((_("A1"), course_stages))
trends_config.append((_("A2"), course_stages))
trends_config.append((_("Citizen course"), course_stages))
trends_config.append((_("Professional integration"), [
    "Begleitet vom DSBE",
    "Begleitet vom ADG",
    "Erwerbstätigkeit",
]))


def objects():

    Line = rt.models.courses.Line
    Teacher = dd.plugins.courses.teacher_model
    Course = rt.models.courses.Course
    Topic = rt.models.courses.Topic
    Enrolment = rt.models.courses.Enrolment
    User = rt.models.users.User
    EventType = rt.models.cal.EventType
    Guest = rt.models.cal.Guest
    GuestRole = rt.models.cal.GuestRole
    GuestStates = rt.models.cal.GuestStates
    EntryStates = rt.models.cal.EntryStates
    Event = rt.models.cal.Event
    Person = rt.models.contacts.Person
    CommentType = rt.models.comments.CommentType
    TrendStage = rt.models.trends.TrendStage
    TrendArea = rt.models.trends.TrendArea

    for area, stages in trends_config:
        ta = named(TrendArea, area)
        yield ta
        for stage in stages:
            yield named(TrendStage, stage, trend_area=ta)
    
    kw = dd.str2kw('name', _("Lesson"))
    kw.update(dd.str2kw('event_label', _("Lesson")))
    event_type = EventType(**kw)
    yield event_type

    pupil = named(GuestRole, _("Pupil"))
    yield pupil
    yield named(GuestRole, _("Assistant"))

    topic_citizen = named(Topic, _("Citizen course"))
    yield topic_citizen
    
    topic_lang = named(Topic, _("Language courses"))
    yield topic_lang
    
    kw.update(topic=topic_citizen)
    kw = dict(event_type=event_type, guest_role=pupil)
    yield named(Line, _("Citizen course"), **kw)
    
    kw.update(topic=topic_lang)
    alpha = named(Line, _("Alphabetisation"), **kw)
    yield alpha
    yield named(Line, _("German for beginners"), **kw)
    yield named(Line, _("German A1+"), **kw)
    yield named(Line, _("German A2"), **kw)
    yield named(Line, _("German A2 (women)"), **kw)
        
    yield named(CommentType, _("Phone call"))
    yield named(CommentType, _("Visit"))
    yield named(CommentType, _("Individual consultation"))
    yield named(CommentType, _("Internal meeting"))
    yield named(CommentType, _("Meeting with partners"))
    
    laura = Teacher(first_name="Laura", last_name="Lieblig")
    yield laura
    yield User(username="laura", user_type=UserTypes.teacher,
               partner=laura)
    
    yield User(username="nathalie", user_type=UserTypes.user)
    yield User(username="audrey", user_type=UserTypes.auditor)
    yield User(username="martina", user_type=UserTypes.coordinator)

    USERS = Cycler(User.objects.exclude(
        user_type__in=(UserTypes.auditor, UserTypes.admin)))
    
    kw = dict(monday=True, tuesday=True, thursday=True, friday=True)
    kw.update(
        line=alpha,
        start_date=dd.demo_date(-30),
        start_time="9:00", end_time="12:00",
        max_date=dd.demo_date(10),
        every_unit=Recurrencies.daily,
        user=USERS.pop(),
        teacher=laura,
        max_places=5)
    
    yield Course(**kw)

    kw.update(start_time="14:00", end_time="17:00", user=USERS.pop())
    yield Course(**kw)

    
    PUPILS = Cycler(dd.plugins.courses.pupil_model.objects.all())
    # print(20170302, dd.plugins.courses.pupil_model.objects.all())
    COURSES = Cycler(Course.objects.all())
    STATES = Cycler(EnrolmentStates.objects())

    def fits(course, pupil):
        if course.max_places and course.get_free_places() == 0:
            return False
        if Enrolment.objects.filter(course=course, pupil=pupil).count():
            return False
        return True
    for i in range(10):
        course = COURSES.pop()
        pupil = PUPILS.pop()
        while not fits(course, pupil):
            course = COURSES.pop()
        kw = dict(user=USERS.pop(), course=course, pupil=pupil)
        kw.update(request_date=dd.demo_date(-i))
        kw.update(state=STATES.pop())
        yield Enrolment(**kw)


    ar = rt.login('robin')
    for obj in Course.objects.all():
        obj.update_auto_events(ar)
        
    # Suggested calendar entries older than 7 days should be marked as
    # either took_place or cancelled. 
    qs = Event.objects.filter(
        start_date__lte=dd.demo_date(-7),
        state=EntryStates.suggested)
    for i, obj in enumerate(qs):
        if i % 9:
            obj.state = EntryStates.took_place
        else:
            obj.state = EntryStates.cancelled
        obj.full_clean()
        obj.save()

    # participants of events which took place should be marked as
    # either absent or present or excused:
    qs = Guest.objects.filter(
        event__start_date__lte=dd.demo_date(-7),
        event__state=EntryStates.took_place)
    for i, obj in enumerate(qs):
        if i % 9:
            obj.state = GuestStates.present
        elif i % 3:
            obj.state = GuestStates.absent
        else:
            obj.state = GuestStates.excused
        obj.full_clean()
        obj.save()
        
