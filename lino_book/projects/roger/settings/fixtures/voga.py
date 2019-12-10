# -*- coding: UTF-8 -*-
# Copyright 2013-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
Demo data specific for :ref:`voga`.
See also :doc:`/specs/courses`.
"""

from __future__ import unicode_literals

from builtins import range
from builtins import str

from lino.utils.instantiator import Instantiator, i2d
from lino.utils import Cycler
from django.conf import settings
from atelier.utils import date_offset
from lino.api import dd, rt, _
from lino.utils.mldbc import babeld

ENROLMENT_STORIES = Cycler([
    [(-20, None, None)],  # early enrolment
    [(-5, None, None)],  # normal enrolment
    [(-5, None, 5*7)],  # stops after 5 weeks
    [(None, None, None)],  # last minute enrolment (same day)
    [(15, 15, None)],  # starts after second week
    [(None, None, 3*7), (None, 7*7, None)]  # interrupts for 4 weeks
])


cal = dd.resolve_app('cal')
courses = dd.resolve_app('courses')
rooms = dd.resolve_app('rooms')

Booking = dd.resolve_model('rooms.Booking')
Room = dd.resolve_model('cal.Room')
Event = dd.resolve_model('cal.Event')
Partner = dd.resolve_model('contacts.Partner')
Company = dd.resolve_model('contacts.Company')
Teacher = dd.resolve_model('courses.Teacher')
TeacherType = dd.resolve_model('courses.TeacherType')
Pupil = dd.resolve_model('courses.Pupil')
Enrolment = dd.resolve_model('courses.Enrolment')
Course = dd.resolve_model('courses.Course')
Product = dd.resolve_model('products.Product')
CourseStates = courses.CourseStates
EnrolmentStates = courses.EnrolmentStates
BookingStates = rooms.BookingStates
Calendar = dd.resolve_model('cal.Calendar')
Tariff = rt.models.invoicing.Tariff

demo_date = dd.demo_date

# DEMO_REF_DATE = i2d(20140101)

# def demo_date(*args, **kw):
#     return date_offset(DEMO_REF_DATE, *args, **kw)


class Loader1(object):

    def objects(self):
        VatClasses = rt.models.vat.VatClasses
        # yield PupilType(ref="M", name="Mitglied")
        # yield PupilType(ref="H", name="Helfer")
        # yield PupilType(ref="L", name="LFV")
        # yield PupilType(ref="C", name="COK")
        #~ yield PupilType(ref="E",name="Extern")

        yield TeacherType(ref="S", **dd.str2kw('name', _("Independant")))
        yield TeacherType(ref="EP", **dd.babelkw('name', de="Ehrenamtlich pauschal", fr="Volontaire (forfait)", en="Voluntary (flat)"))
        yield TeacherType(ref="ER", **dd.babelkw('name', de="Ehrenamtlich real", fr="Volontaire (réel)", en="Voluntary (real)"))
        yield TeacherType(ref="LBA", **dd.babelkw('name', de="LBA", fr="ALE", en="LEA"))
        #~ yield TeacherType(ref="A",**dd.babelkw('name',de="Andere",fr="Autre",en="Other"))

        company = Instantiator('contacts.Company', 'name city:name').build

        we = company("Die Buche V.o.G.", "Eupen",
                     street="Birkenweg", street_no=5,
                     vat_id="BE0123456789")
        yield we
        settings.SITE.site_config.site_company = we
        yield settings.SITE.site_config

        ProductCat = rt.models.products.ProductCat
        # productcat = Instantiator('products.ProductCat').build

        self.course_fees = ProductCat(**dd.str2kw(
            'name', _("Participation fees")))
        yield self.course_fees

        self.trips = ProductCat(**dd.str2kw('name', _("Trips")))
        # et="Väljasõidud", de="Ausflüge", fr="Excursions"))
        yield self.trips

        kw = dd.str2kw('name', _("Journeys"))
        self.journeys_cat = ProductCat(**kw)
        yield self.journeys_cat

        kw.update(sales_price="295.00")
        self.journey_fee = Product(cat=self.journeys_cat, **kw)
        yield self.journey_fee

        rent = ProductCat(**dd.str2kw('name', _("Room renting")))
        # et="Ruumiüür", de="Raummiete", fr="Loyer"))
        yield rent
        # other = ProductCat(**dd.str2kw('name', _("Other")))
        # et="Muud", de="Sonstige", fr="Autres"))
        # yield other

        t5 = babeld(Tariff, _("5 times"), number_of_events=5, min_asset=1)
        yield t5
        t8 = babeld(Tariff, _("8 times"), number_of_events=8, min_asset=2)
        yield t8
        t12 = babeld(
            Tariff, _("12 times"), number_of_events=12, min_asset=4)
        yield t12

        product = Instantiator(
            'products.Product', "sales_price cat name",
            vat_class=VatClasses.services).build
        yield product("20", self.course_fees, "20€")
        yield product("48", self.course_fees, "48€/8 hours", tariff=t8)
        # yield p
        # yield Tariff(product=p, number_of_events=8, min_asset=2)

        yield product("64", self.course_fees, "64€/12 hours", tariff=t12)
        # yield p
        # yield Tariff(product=p, number_of_events=12, min_asset=4)

        yield product("50", self.course_fees, "50€/5 hours", tariff=t5)
        # yield p
        # yield Tariff(product=p, number_of_events=5, min_asset=1)

        yield product("80", self.course_fees, "80€")

        rent20 = product("20", rent, "Spiegelraum Eupen")
        yield rent20
        rent10 = product("10", rent, **dd.babelkw(
            'name',
            en="Rent per meeting", et="Ruumi üürimine",
            de="Raummiete pro Versammlung",
            fr="Loyer par réunion"))
        yield rent10

        self.PRICES = Cycler(Product.objects.filter(cat=self.course_fees))

        event_type = Instantiator('cal.EventType').build
        kw = dd.str2kw('name', _("Courses"))
        kw.update(dd.str2kw('event_label', _("Hour")))
        self.kurse = event_type(**kw)
        yield self.kurse
        settings.SITE.site_config.default_event_type = self.kurse
        yield settings.SITE.site_config

        self.seminare = event_type(**dd.str2kw('name', _("Seminars")))
        yield self.seminare

        self.excursions = event_type(
            max_days=10, **dd.str2kw('name', _("Excursions")))
        # de="Ausflüge",
        #  fr="Excursions",
        #  en="Excursions",
        yield self.excursions

        self.hikes = event_type(
            max_days=60, **dd.str2kw('name', _("Hikes")))
        # de="Wanderungen",
        # fr="Randonnées",
        # en="Hikes",
        yield self.hikes

        yield event_type(**dd.str2kw('name', _("Meetings")))
                                      # de="Versammlungen",
                                      # fr="Réunions",
                                      # en="Meetings",

        yield event_type(
            email_template='Team.eml.html',
            **dd.str2kw('name', _("Team Meetings")))
                         # de="Team-Besprechungen",
                         # fr="Coordinations en équipe",
                         # en="Team Meetings",

        #~ yield event_type(**dd.babelkw('name',
              #~ de="Feiertage",
              #~ fr="Jours fériés",
              #~ en="Holidays",
              #~ ))
        #~

        company = Instantiator('contacts.Company', 'name city:name').build
        eupen = company("Lern- und Begegnungszentrum", "Eupen",
                        street="Kirchstraße", street_no=39, street_box="/B2")
        yield eupen
        bbach = company("Lern- und Begegnungszentrum", "Butgenbach")
        yield bbach
        kelmis = company("Zur Klüüs", "Kelmis")
        yield kelmis
        stvith = company("Sport- und Freizeitzentrum", "Sankt Vith")
        yield stvith

        self.ext1 = company("AA Neudorf", "Raeren")
        yield self.ext1
        self.ext2 = company("Nisperter Schützenverein", "Eupen")
        yield self.ext2

        room = Instantiator('cal.Room').build
        kw = dict(company=eupen)
        kw.update(dd.str2kw('name', _("Mirrored room")))
        kw.update(fee=rent20)
        self.spiegel = room(**kw)
        yield self.spiegel

        kw.update(dd.str2kw('name', _("Computer room")))
        kw.update(fee=rent10)
        self.pc_eupen = room(**kw)
        yield self.pc_eupen

        kw = dict(company=bbach)
        kw.update(dd.str2kw('name', _("Conferences room")))
        self.konf = room(**kw)
        yield self.konf

        kw.update(dd.str2kw('name', _("Computer room")))
        self.pc_bbach = room(**kw)
        yield self.pc_bbach

        kw = dict(company=kelmis)
        kw.update(dd.str2kw('name', _("Computer room")))
        self.pc_kelmis = room(**kw)
        yield self.pc_kelmis

        kw = dict(company=stvith)
        kw.update(dd.str2kw('name', _("Computer room")))
        self.pc_stvith = room(**kw)
        yield self.pc_stvith

        # a room without company
        kw = dict()
        kw.update(dd.str2kw('name', _("Outside")))
        self.outside = room(**kw)
        yield self.outside

        COLORS = Cycler(Calendar.COLOR_CHOICES)

        for u in Room.objects.all():
            obj = Calendar(name=str(u), color=COLORS.pop())
            yield obj
            #~ dd.logger.info("20131018 %s", obj)
            u.calendar = obj
            u.save()


class Loader2(Loader1):

    def objects(self):

        yield super(Loader2, self).objects()

        Enrolment = rt.models.courses.Enrolment

        topic = Instantiator('courses.Topic').build
        line = Instantiator('courses.Line', 'topic event_type fee').build
        course = Instantiator(
            'courses.Course', 'line room start_time end_time').build
        booking = Instantiator(
            'rooms.Booking', 'room start_time end_time').build

        TEACHERS = Cycler(Teacher.objects.all())
        COMPANIES = Cycler(Company.objects.all())
        USERS = Cycler(settings.SITE.user_model.objects.all())

        def add_course(*args, **kw):
            kw.update(user=USERS.pop())
            kw.update(teacher=TEACHERS.pop())
            #~ kw.update(price=PRICES.pop())
            obj = course(*args, **kw)
            if obj.line.fee.tariff and obj.line.fee.tariff.number_of_events:
                obj.max_events = None
            return obj

        Product = rt.models.products.Product
        ProductCat = rt.models.products.ProductCat
        CourseAreas = rt.models.courses.CourseAreas
        PaymentTerm = rt.models.ledger.PaymentTerm

        journey_options = ProductCat(**dd.str2kw(
            'name', _("Hotel options")))
        yield journey_options
        option = Instantiator(Product, cat=journey_options).build
        yield option(**dd.str2kw('name', _("Single room")))
        yield option(**dd.str2kw('name', _("Double room")))
        yield option(**dd.str2kw('name', _("Triple room")))
        # yield option(**dd.str2kw('name', _("Shower")))
        # yield option(**dd.str2kw('name', _("Night club")))

        # trip_options = ProductCat(**dd.str2kw('name', _("Trip options")))
        # yield trip_options
        # option = Instantiator(Product, cat=trip_options).build
        # yield option(name="Eupen Oberstadt")
        # yield option(name="Eupen Unterstadt")
        # yield option(name="Raeren")
        # yield option(name="Kelmis")
        # yield option(name="Büllingen")

        journey = Instantiator(
            'courses.Course', 'line name start_date end_date').build

        def add_journey(*args, **kw):
            kw.update(user=USERS.pop())
            kw.update(teacher=TEACHERS.pop())
            kw.update(every_unit=cal.Recurrencies.once)
            kw.update(payment_term=PaymentTerm.get_by_ref('P30'))
            return journey(*args, **kw)

        self.journeys_topic = topic(**dd.str2kw('name', _("Journeys")))
        yield self.journeys_topic
        europe = line(self.journeys_topic,
                      self.excursions,
                      self.journey_fee,
                      options_cat=journey_options,
                      course_area=CourseAreas.journeys,
                      fees_cat=self.journeys_cat,
                      **dd.str2kw('name', _("Europe")))

        yield europe
        yield add_journey(europe, "Greece 2014",
                          i2d(20140814), i2d(20140820),
                          state=courses.CourseStates.active)
        yield add_journey(europe, "London 2014",
                          i2d(20140714), i2d(20140720))

        comp = topic(name="Computer")
        yield comp
        sport = topic(name="Sport")
        yield sport
        medit = topic(name="Meditation")
        yield medit
        externe = topic(name="Externe")
        yield externe

        obj = line(comp, self.kurse, self.PRICES.pop(),
                   fees_cat=self.course_fees,
                   ref="comp",
                   **dd.babelkw('name', de="Erste Schritte", en="First Steps"))
        yield obj
        kw = dict(max_events=8)
        kw.update(max_places=3)
        kw.update(start_date=demo_date(-430))
        kw.update(state=courses.CourseStates.active)
        kw.update(every=1)
        kw.update(every_unit=cal.Recurrencies.weekly)

        yield add_course(obj, self.pc_bbach, "13:30", "15:00",
                         monday=True, **kw)
        yield add_course(obj, self.pc_eupen, "17:30", "19:00",
                         wednesday=True, **kw)
        yield add_course(obj, self.pc_kelmis, "13:30", "15:00",
                         friday=True, **kw)

        desc = """
    Behandelte Themengebiete:

    - Grundlagen, Voraussetzungen
    - Arbeiten im WWW unter Verwendung eines Browsers
    - Navigieren im WWW
    - Links in die Linkleiste legen
    - aus Webseiten heraus drucken
    - Favoriten bzw. Lesezeichen verwenden
    - Aufgabe und Funktionsweise von Suchmaschinen
    - Elektronische Post: E-Mails verfassen, senden, empfangen, beantworten
    - E-Mails mit Anlagen
    - E-mail Sicherheit
    - Tipps und Tricks
    """
        obj = line(
            comp, self.kurse, self.PRICES.pop(),
            ref="WWW",
            fees_cat=self.course_fees,
            description=desc, **dd.babelkw(
                'name',
                de="Internet: World Wide Web für Anfänger",
                en="Internet for beginners"))
        yield obj
        kw = dict(max_events=8)
        kw.update(max_places=4)
        kw.update(start_date=demo_date(-210))
        kw.update(state=courses.CourseStates.active)
        yield add_course(obj, self.pc_bbach, "13:30", "15:00",
                         monday=True, **kw)
        yield add_course(obj, self.pc_eupen, "17:30", "19:00",
                         wednesday=True, **kw)
        yield add_course(obj, self.pc_kelmis, "13:30", "15:00",
                         friday=True, **kw)

        obj = line(sport, self.kurse, self.PRICES.pop(),
                   ref="BT",
                   fees_cat=self.course_fees,
                   **dd.babelkw('name', de="Bauchtanz", en="Belly dancing"))
        yield obj
        kw = dict(max_events=8)
        kw.update(max_places=10)
        kw.update(start_date=demo_date(-420))
        kw.update(state=CourseStates.active)
        yield add_course(obj, self.spiegel, "19:00", "20:00",
                         wednesday=True, **kw)

        obj = line(sport, self.kurse, self.PRICES.pop(),
                   ref="FG",
                   fees_cat=self.course_fees,
                   **dd.babelkw('name',
                                de="Funktionsgymnastik",
                                en="Functional gymnastics"))
        yield obj
        kw = dict(max_events=10, state=CourseStates.active)
        kw.update(max_places=5)
        kw.update(start_date=demo_date(-230))
        yield add_course(obj, self.spiegel, "11:00", "12:00", monday=True, **kw)
        yield add_course(obj, self.spiegel, "13:30", "14:30", monday=True, **kw)

        obj = line(sport, self.kurse, self.PRICES.pop(),
                   ref="Rücken",
                   fees_cat=self.course_fees,
                   **dd.babelkw('name', de="Rücken fit durch Schwimmen", en="Swimming"))
        yield obj
        kw = dict(max_events=10, state=CourseStates.active)
        kw.update(max_places=20)
        kw.update(start_date=demo_date(50))
        yield add_course(obj, self.spiegel, "11:00", "12:00", monday=True, **kw)
        yield add_course(obj, self.spiegel, "13:30", "14:30", monday=True, **kw)
        yield add_course(obj, self.pc_stvith, "11:00", "12:00", tuesday=True, **kw)
        yield add_course(obj, self.pc_stvith, "13:30", "14:30", tuesday=True, **kw)
        yield add_course(obj, self.pc_kelmis, "11:00", "12:00", thursday=True, **kw)
        yield add_course(obj, self.pc_kelmis, "13:30", "14:30", thursday=True, **kw)

        obj = line(sport, self.kurse, self.PRICES.pop(),
                   ref="SV",
                   fees_cat=self.course_fees,
                   **dd.babelkw('name', de="Selbstverteidigung im Alltag", en="Self-defence"))
        yield obj
        kw = dict(max_events=6)
        kw.update(max_places=12)
        kw.update(start_date=demo_date(-80))
        kw.update(state=CourseStates.active)
        yield add_course(obj, self.spiegel, "18:00", "19:00", friday=True, **kw)
        yield add_course(obj, self.spiegel, "19:00", "20:00", friday=True, **kw)

        obj = line(medit, self.kurse, self.PRICES.pop(),
                   ref="GLQ",
                   fees_cat=self.course_fees,
                   name="GuoLin-Qigong")
        yield obj
        kw = dict(max_events=10)
        kw.update(start_date=demo_date(-310))
        kw.update(state=CourseStates.active)
        yield add_course(obj, self.spiegel, "18:00", "19:30",
                         monday=True, **kw)
        yield add_course(obj, self.spiegel, "19:00", "20:30",
                         friday=True, **kw)

        obj = line(medit, self.kurse, self.PRICES.pop(),
                   ref="MED",
                   fees_cat=self.course_fees,
                   **dd.babelkw(
                       'name',
                       de="Den Kopf frei machen - zur inneren Ruhe finden",
                       en="Finding your inner peace"))
        yield obj
        kw = dict(max_events=10)
        kw.update(max_places=30)
        kw.update(start_date=demo_date(-610))
        kw.update(state=CourseStates.active)
        yield add_course(obj, self.konf, "18:00", "19:30", monday=True, **kw)
        kw.update(start_date=demo_date(-110))
        yield add_course(obj, self.konf, "19:00", "20:30", friday=True, **kw)

        obj = line(medit, self.kurse, self.PRICES.pop(), name="Yoga")
        yield obj
        kw = dict(max_events=10)
        kw.update(start_date=demo_date(-560))
        kw.update(max_places=20)
        kw.update(state=CourseStates.active)
        yield add_course(obj, self.konf, "18:00", "19:30", monday=True, **kw)
        yield add_course(obj, self.konf, "19:00", "20:30", friday=True, **kw)

        for obj in Course.objects.filter(ref__isnull=True):
            if obj.line.fee.tariff and obj.line.fee.tariff.number_of_events:
                obj.ref = "%03dC" % obj.id
            else:
                obj.ref = "%03d" % obj.id
            yield obj

        EXTS = Cycler(self.ext1, self.ext2)

        def add_booking(*args, **kw):
            kw.update(user=USERS.pop())
            kw.update(event_type=self.seminare)
            #~ kw.update(price=PRICES.pop())
            #~ kw.update(fee=PRICES.pop())
            #~ kw.update(calendar=self.kurse)
            kw.update(every=1)
            kw.update(company=EXTS.pop())
            return booking(*args, **kw)

        #~ obj = line(externe,self.kurse,PRICES.pop(),**dd.babelkw('name',
            #~ de="Raumbuchung",en="Room booking"))
        #~ yield obj
        kw = dict(max_events=10)
        kw.update(every_unit=cal.Recurrencies.weekly)
        kw.update(start_date=demo_date(160))
        kw.update(state=BookingStates.registered)
        kw.update(company=COMPANIES.pop())
        yield add_booking(self.konf, "20:00", "22:00", tuesday=True, **kw)
        kw.update(company=COMPANIES.pop())
        yield add_booking(self.konf, "20:00", "22:00", thursday=True, **kw)

        kw = dict(max_events=1)
        kw.update(every_unit=cal.Recurrencies.once)
        kw.update(company=COMPANIES.pop())
        kw.update(every_unit=cal.Recurrencies.once)
        yield add_booking(self.konf, "10:00", "14:00", **kw)

        # a series of five week-ends:
        kw = dict()
        kw.update(user=USERS.pop())
        kw.update(teacher=TEACHERS.pop())
        kw.update(every_unit=cal.Recurrencies.monthly)
        kw.update(max_events=5)
        kw.update(friday=True)
        kw.update(payment_term=PaymentTerm.get_by_ref('P30'))
        yield journey(europe, "Five Weekends 2015",
                      i2d(20150619), i2d(20150621), **kw)

        # PUPILS = Cycler()
        #~ print 20130712, Pupil.objects.all()
        COURSES = Cycler(Course.objects.filter(
            line__fee__isnull=False).order_by('room__company__city'))
        # STATES = Cycler(EnrolmentStates.objects())
        FREE_EVENTS = Cycler([3, 2, 5, -2])

        # assert len(USERS) > 1
        pupils = Pupil.objects.order_by('id')
        # print("20171028 {} courses, {} pupils".format(
        #     len(COURSES), pupils.count()))
        # assert pupils.count() == 50

        n = 0
        for pupil in pupils:
            for i in range(pupil.id % 6):
                n += 1
                # every pupil can be in up to 5 courses. That's a bit
                # unrealistic, but we have 25 courses and 35
                # pupils and want to have
                course = COURSES.pop()

                def coursedate(*args, **kwargs):
                    return date_offset(course.start_date, *args, **kwargs)

                kw = dict(user=USERS.pop(), course=course, pupil=pupil)
                #~ print 20130712, kw
                story = ENROLMENT_STORIES.pop()
                assert isinstance(story, list)
                for rd, sd, ed in story:
                    # kw.update(state=STATES.pop())
                    # enrolments are requested from 3 weeks before until 1
                    # week after start date of course:
                    # kw.update(request_date=coursedate(i % 28 - 7))
                    kw.update(request_date=coursedate(rd))
                    if course.line == europe:
                        if n % 3 == 0:
                            kw.update(places=2)
                    obj = Enrolment(**kw)
                    # print("20171027b {}".format(obj))
                    obj.full_clean()
                    if sd is not None:
                        obj.start_date = coursedate(sd)
                        # obj.request_date = obj.start_date
                    if ed is not None:
                        obj.end_date = coursedate(ed)
                    if n % 10 == 0:
                        obj.state = EnrolmentStates.requested
                    elif n % 13 == 0:
                        obj.state = EnrolmentStates.cancelled
                    else:
                        obj.state = EnrolmentStates.confirmed
                    if n % 9 == 0:
                        if course.line.fee.tariff:
                            if course.line.fee.tariff.number_of_events:
                                obj.free_events = FREE_EVENTS.pop()
                    yield obj

        ses = settings.SITE.login()

        for model in (Course, Booking):
            for obj in model.objects.all():
                rc = ses.run(obj.do_update_events)
                if not rc.get('success', False):
                    raise Exception("update_reminders on %s returned %s" %
                                    (obj, rc))

        Event = rt.models.cal.Event
        EntryStates = rt.models.cal.EntryStates
        qs = Event.objects.filter(
            start_date__lt=dd.demo_date()).order_by('id')
        for i, e in enumerate(qs):
            if i % 8:
                e.state = EntryStates.took_place
                yield e

        # n = 0
        # for p in Partner.objects.all():
        #     if n > 10:
        #         break
        #     try:
        #         rc = ses.run(p.create_invoice)
        #         if rc.get('success', True):
        #             n += 1
        #     except Warning:
        #         pass


objects = Loader2().objects
