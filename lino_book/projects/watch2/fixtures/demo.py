## Copyright 2013-2018 Rumma & Ko Ltd
## This file is part of the Lino project.

from lino.api import rt
from django.conf import settings

from lino.utils import Cycler

Entry = rt.models.watch2.Entry
EntryType = rt.models.watch2.EntryType
Company = rt.models.watch2.Company
User = rt.models.users.User

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def objects():

    kwargs = dict(user_type=rt.models.users.UserTypes.user)
    # kwargs = dict()
    
    yield User(username="Albert", **kwargs)
    yield User(username="Boris", **kwargs)
    yield User(username="Claire", **kwargs)
    
    yield Company(name="AllTech inc.")
    yield Company(name="BestTech inc.")
    yield Company(name="CoolTech inc.")
    
    yield EntryType(designation="Consultation")
    yield EntryType(designation="Evaluation")
    yield EntryType(designation="Test")
    yield EntryType(designation="Analysis")
    yield EntryType(designation="Observation")
    
    TYPES = Cycler(EntryType.objects.all())
    COMPANIES = Cycler(Company.objects.all())
    USERS = Cycler(User.objects.all())
    SUBJECTS = Cycler(LOREM_IPSUM.split())
    
    for i in range(200):
        d = settings.SITE.demo_date(-i)
        e = Entry(date=d,
            company=COMPANIES.pop(),
            user=USERS.pop(),
            subject=SUBJECTS.pop(),
            entry_type=TYPES.pop())
        if i % 7:
            yield e
    
