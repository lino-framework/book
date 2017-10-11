# -*- coding: UTF-8 -*-
# Copyright 2015-2017 Luc Saffre
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals
from __future__ import print_function

import datetime

from django.conf import settings
from lino.api import rt, dd, _
from lino.utils import Cycler, i2d

from lino.core.roles import SiteAdmin
from lino_xl.lib.cal.choicelists import DurationUnits
#from lino_xl.lib.clocking.roles import Worker
from lino.utils.quantities import Duration
from lino.utils.mldbc import babel_named as named
from lino.modlib.users.utils import create_user

#from lino_xl.lib.clocking.choicelists import ReportingTypes


def objects():
    UserTypes = rt.models.users.UserTypes
    Company = rt.models.contacts.Company
    Product = rt.models.products.Product
    Account = rt.models.accounts.Account
    AccountTypes = rt.models.accounts.AccountTypes

    yield create_user("daniel", UserTypes.therapist)
    yield create_user("elmar", UserTypes.therapist)
    yield create_user("lydia", UserTypes.secretary)

    # yield faculties_objects()

    obj = Company(
        name="Tough Thorough Thought Therapies",
        country_id="BE", vat_id="BE12 3456 7890")
    yield obj
    settings.SITE.site_config.update(site_company=obj)

    yield named(Product, _("Group therapy"), sales_price=30)
    indacc = named(
        Account, _("Sales on individual therapies"),
        type=AccountTypes.incomes, ref="7010")
    yield indacc
    yield named(
        Product, _("Individual therapy"),
        sales_price=60, sales_account=indacc)
    yield named(Product, _("Other"), sales_price=35)

    


def faculties_objects():
    "was previously in faculties.fixtures.demo2"

    Faculty = rt.models.faculties.Faculty
    Competence = rt.models.faculties.Competence
    Demand = rt.models.faculties.Demand
    # Ticket = rt.models.tickets.Ticket
    User = rt.models.users.User

    yield named(Faculty, _('Psychotherapy'))
    yield named(Faculty, _('Psychiatry'))

    SKILLS = Cycler(Faculty.objects.all())
    END_USERS = Cycler(dd.plugins.faculties.end_user_model.objects.all())

    i = 0
    for j in range(2):
        for u in User.objects.all():
            i += 1
            yield Competence(user=u, faculty=SKILLS.pop())
            if i % 2:
                yield Competence(user=u, faculty=SKILLS.pop())
            if i % 3:
                yield Competence(
                    user=u, faculty=SKILLS.pop(),
                    end_user=END_USERS.pop())
            
    for i, t in enumerate(
            dd.plugins.faculties.demander_model.objects.all()):
        yield Demand(demander=t, skill=SKILLS.pop())
        if i % 3:
            yield Demand(demander=t, skill=SKILLS.pop())
