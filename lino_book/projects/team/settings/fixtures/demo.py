# -*- coding: UTF-8 -*-
# Copyright 2015-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals
from __future__ import print_function

import datetime

from lino.api import rt, dd, _
from lino.utils import Cycler, i2d

from lino.core.roles import SiteAdmin
from lino_xl.lib.cal.choicelists import DurationUnits
from lino_xl.lib.working.roles import Worker
from lino.utils.quantities import Duration
from lino.utils.mldbc import babel_named as named
from lino.modlib.users.utils import create_user

from lino_xl.lib.working.choicelists import ReportingTypes
from lino_xl.lib.tickets.choicelists import SiteStates

from lino_xl.lib.tickets.roles import Reporter, TicketsStaff

UserTypes = rt.models.users.UserTypes

def vote(user, ticket, state, **kw):
    u = rt.models.users.User.objects.get(username=user)
    t = rt.models.tickets.Ticket.objects.get(pk=ticket)
    s = rt.models.votes.VoteStates.get_by_name(state)
    vote = t.get_favourite(u)
    if vote is None:
        vote = rt.models.votes.Vote(user=u, votable=t, state=s, **kw)
    else:
        vote.state = s
    return vote


def tickets_objects():
    # was previously in tickets
    User = rt.models.users.User
    Company = rt.models.contacts.Company
    Person = rt.models.contacts.Person
    # Topic = rt.models.topics.Topic
    TT = rt.models.tickets.TicketType
    Ticket = rt.models.tickets.Ticket
    Group = rt.models.groups.Group
    Membership = rt.models.groups.Membership
    # Competence = rt.models.tickets.Competence
    # Interest = rt.models.topics.Interest
    Milestone = dd.plugins.tickets.milestone_model
    # Milestone = rt.models.deploy.Milestone
    # Project = rt.models.tickets.Project
    # Site = rt.models.tickets.Site
    Site = dd.plugins.tickets.site_model
    Link = rt.models.tickets.Link
    LinkTypes = rt.models.tickets.LinkTypes
    # Subscription = rt.models.tickets.Subscription
    #EntryType = rt.models.blogs.EntryType
    #Entry = rt.models.blogs.Entry
    # Star = rt.models.stars.Star
    # Tagging = rt.models.blogs.Tagging
    # Line = rt.models.courses.Line
    List = rt.models.lists.List


    customer = UserTypes.customer
    contributor = UserTypes.contributor
    dev = UserTypes.developer

    yield create_user("marc", customer)
    yield create_user("mathieu", contributor)
    yield create_user("luc", dev)
    yield create_user("jean", dev)

    # USERS = Cycler(User.objects.all())
    WORKERS = Cycler(User.objects.filter(
        username__in='mathieu luc jean'.split()))
    # END_USERS = Cycler(User.objects.filter(
    #     user_type=rt.models.users.UserTypes.user))
    reporter_types = [t for t in UserTypes.get_list_items()
                      if t.has_required_roles([Reporter])]
    REPORTERS = Cycler(User.objects.filter(user_type__in=reporter_types))

    yield named(Group, _("Developers"))
    yield named(Group, _("Managers"))
    yield named(Group, _("Front-end team"))

    yield named(TT, _("Bugfix"))
    yield named(TT, _("Enhancement"))
    yield named(TT, _("Upgrade"))

    # sprint = named(Line, _("Sprint"))
    # yield sprint

    TYPES = Cycler(TT.objects.all())

    # yield Topic(name="Lino Core", ref="linõ")
    # yield Topic(name="Lino Welfare", ref="welfäre")
    # yield Topic(name="Lino Cosi", ref="così")
    # yield Topic(name="Lino Voga", ref="faggio")
    # ref differs from name

    # TOPICS = Cycler(Topic.objects.all())
    RTYPES = Cycler(ReportingTypes.objects())
    GROUPS = Cycler(Group.objects.all())
    PERSONS = Cycler(Person.objects.order_by("id"))
    COMPANIES = Cycler(Company.objects.order_by("id"))
    end_users = []

    for ref in "welket welsch pypi docs bugs".split():
        kw = dict(ref=ref, reporting_type=RTYPES.pop(), group=GROUPS.pop(), state=SiteStates.active)
        if ref in ("pypi", "docs", "bugs"):
            kw.update(name=ref)
        else:
            obj = COMPANIES.pop()
            eu = PERSONS.pop()
            end_users.append(eu)
            yield rt.models.contacts.Role(person=eu, company=obj)
            kw.update(company=obj)
            kw.update(name=str(obj))
            kw.update(contact_person=eu)
            kw.update(private=True)
        yield Site(**kw)
    END_USERS  = Cycler(end_users)
    yield Company(name="Saffre-Rumma")

    # for u in Company.objects.exclude(name="pypi"):
    #     for i in range(3):
    #         yield Interest(owner=u, topic=TOPICS.pop())

    # prj1 = Project(
    #     name="Framewörk", ref="linö", private=False,
    #     company=COMPANIES.pop(),
    #     reporting_type=RTYPES.pop(),
    #     start_date=i2d(20090101))
    # yield prj1
    # yield Project(
    #     name="Téam", ref="téam", start_date=i2d(20100101),
    #     reporting_type=RTYPES.pop(),
    #     company=COMPANIES.pop(),
    #     parent=prj1, private=True)
    # prj2 = Project(
    #     name="Documentatión", ref="docs", private=False,
    #     reporting_type=RTYPES.pop(),
    #     company=COMPANIES.pop(),
    #     start_date=i2d(20090101), parent=prj1)
    # yield prj2
    # yield Project(
    #     name="Research", ref="research", private=False,
    #     company=COMPANIES.pop(),
    #     start_date=i2d(19980101), parent=prj2)
    # yield Project(
    #     name="Shop", ref="shop", private=False,
    #     reporting_type=RTYPES.pop(),
    #     company=COMPANIES.pop(),
    #     start_date=i2d(20120201), end_date=i2d(20120630))

    # PROJECTS = Cycler(Project.objects.all())

    # for u in User.objects.all():
    #     yield Competence(user=u, project=PROJECTS.pop())
    #     yield Competence(user=u, project=PROJECTS.pop())

    if dd.is_installed('meetings'):
        SITES = Cycler(Site.objects.exclude(name="pypi"))
        # LISTS = Cycler(List.objects.all())
        for i in range(7):
            site = SITES.pop()
            d = dd.today(i*2-20)
            kw = dict(
                user=WORKERS.pop(),
                start_date=d,
                # line=sprint,
                # project=PROJECTS.pop(), # expected=d, reached=d,
                # expected=d, reached=d,
                name="{}@{}".format(d.strftime("%Y%m%d"), site),
                # list=LISTS.pop()
            )
            kw[Milestone.site_field_name] = site
            yield Milestone(**kw)
    # yield Milestone(site=SITES.pop(), expected=dd.today())
    # yield Milestone(project=PROJECTS.pop(), expected=dd.today())

    SITES = Cycler(Site.objects.all())

    TicketStates = rt.models.tickets.TicketStates
    TSTATES = Cycler(TicketStates.objects())

    # Vote = rt.models.votes.Vote
    # VoteStates = rt.models.votes.VoteStates
    # VSTATES = Cycler(VoteStates.objects())

    num = [0]

    def ticket(summary, **kwargs):
        num[0] += 1
        u = REPORTERS.pop()
        kwargs.update(
            ticket_type=TYPES.pop(), summary=summary,
            user=u,
            state=TSTATES.pop())
        if num[0] % 2:
            kwargs.update(site=SITES.pop())
        if num[0] % 4 == 0:
            kwargs.update(private=True)
        # else:
        #     kwargs.update(private=False)
        if u.user_type.has_required_roles([Worker]):
            if num[0] % 5:
                kwargs.update(end_user=END_USERS.pop())
        # if False:
        #     kwargs.update(project=PROJECTS.pop())
        obj = Ticket(**kwargs)
        yield obj
        # if obj.state.active:
        #     yield Vote(
        #         votable=obj, user=WORKERS.pop(), state=VSTATES.pop())

    yield ticket("Föö fails to bar when baz")
    yield ticket("Bar is not always baz")
    yield ticket("Baz sucks")
    yield ticket("Foo and bar don't baz")
    yield ticket("Cannot create Foo", description="""<p>When I try to create
    a <b>Foo</b>, then I get a <b>Bar</b> instead of a Foo.</p>""")

    yield ticket("Sell bar in baz")
    yield ticket("No Foo after deleting Bar")
    yield ticket("Is there any Bar in Foo?")
    yield ticket("Foo never matches Bar")
    yield ticket("Where can I find a Foo when bazing Bazes?")
    yield ticket("Class-based Foos and Bars?")
    yield ticket("Foo cannot bar")

    # Example of memo markup:
    yield ticket("Bar cannot foo",
                 description="""<p>Linking to [ticket 1] and to
                 [url http://luc.lino-framework.org/blog/2015/0923.html blog].</p>
                 """)

    yield ticket("Bar cannot baz")
    yield ticket("Bars have no foo")
    yield ticket("How to get bar from foo")

    TEXTS = Cycler([ln.strip() for ln in """
    Foo never bars
    No more foo when bar is gone
    Cannot delete foo
    Why is foo so bar
    Irritating message when bar
    How can I see where bar?
    Misc optimizations in Baz
    Default account in invoices per partner
    'NoneType' object has no attribute 'isocode'
    """.splitlines() if ln.strip()])

    # n = Ticket.objects.count()

    for i in range(100):
        # yield ticket("Ticket {}".format(i+n+1))
        yield ticket(TEXTS.pop())

    if dd.is_installed('meetings'):
        Deployment = rt.models.deploy.Deployment
        WishTypes = rt.models.deploy.WishTypes
        WTYPES = Cycler(WishTypes.objects())
        MILESTONES = Cycler(Milestone.objects.all())
        for t in Ticket.objects.all():
            # t.set_author_votes()
            if t.id % 4:
                yield Deployment(
                    milestone=MILESTONES.pop(), ticket=t,
                    wish_type=WTYPES.pop())


    yield Link(
        type=LinkTypes.requires,
        parent=Ticket.objects.get(pk=1),
        child=Ticket.objects.get(pk=2))

    # yield EntryType(**dd.str2kw('name', _('Release note')))
    # yield EntryType(**dd.str2kw('name', _('Feature')))
    # yield EntryType(**dd.str2kw('name', _('Upgrade instruction')))

    # ETYPES = Cycler(EntryType.objects.all())
    # TIMES = Cycler('12:34', '8:30', '3:45', '6:02')
    #blogger = USERS.pop()

    # def entry(offset, title, body, **kwargs):
    #     kwargs['user'] = blogger
    #     kwargs['entry_type'] = ETYPES.pop()
    #     kwargs['pub_date'] = dd.today(offset)
    #     kwargs['pub_time'] = TIMES.pop()
    #     return Entry(title=title, body=body, **kwargs)

    # yield entry(-3, "Hello, world!", "This is our first blog entry.")
    # e = entry(-2, "Hello again", "Our second blog entry is about [ticket 1]")
    # yield e
    # yield Interest(owner=e, topic=TOPICS.pop())

    # e = entry(-1, "Our third entry", """\
    # Yet another blog entry about [ticket 1] and [ticket 2].
    # This entry has two taggings""")
    # yield e
    # yield Interest(owner=e, topic=TOPICS.pop())
    # yield Interest(owner=e, topic=TOPICS.pop())

    for u in User.objects.all():
        if u.user_type.has_required_roles([Reporter]):
            yield Membership(group=GROUPS.pop(), user=u)

def working_objects():
    # was previously in working
    Company = rt.models.contacts.Company
    # Vote = rt.models.votes.Vote
    SessionType = rt.models.working.SessionType
    Session = rt.models.working.Session
    Ticket = rt.models.tickets.Ticket
    User = rt.models.users.User
    UserTypes = rt.models.users.UserTypes
    # devs = (UserTypes.developer, UserTypes.senior)
    devs = [p for p in UserTypes.items()
            if p.has_required_roles([Worker])
            and not p.has_required_roles([SiteAdmin])]
    workers = User.objects.filter(user_type__in=devs)
    WORKERS = Cycler(workers)
    TYPES = Cycler(SessionType.objects.all())
    # TICKETS = Cycler(Ticket.objects.all())
    DURATIONS = Cycler([12, 138, 90, 10, 122, 209, 37, 62, 179, 233, 5])

    # every fourth ticket is unassigned and thus listed in
    # PublicTickets
    # for i, t in enumerate(Ticket.objects.exclude(private=True)):
    for i, t in enumerate(Ticket.objects.all()):
        if i % 4:
            t.assigned_to = WORKERS.pop()
            yield t

    for u in workers:

        # VOTES = Cycler(Vote.objects.filter(user=u))
        # TICKETS = Cycler(Ticket.objects.filter(assigned_to=u))
        TICKETS = Cycler(Ticket.objects.filter())
        # if len(VOTES) == 0:
        #     continue

        for offset in (0, -1, -3, -4):

            date = dd.demo_date(offset)
            worked = Duration()
            ts = datetime.datetime.combine(date, datetime.time(9, 0, 0))
            for i in range(7):
                obj = Session(
                    ticket=TICKETS.pop(),
                    session_type=TYPES.pop(), user=u)
                obj.set_datetime('start', ts)
                d = DURATIONS.pop()
                worked += d
                if offset < 0:
                    ts = DurationUnits.minutes.add_duration(ts, d)
                    obj.set_datetime('end', ts)
                yield obj
                if offset == 0 or worked > 8:
                    break

    ServiceReport = rt.models.working.ServiceReport
    # welket = Company.objects.get(name="welket")
    welket = rt.models.tickets.Site.objects.get(ref="welket").company
    yield ServiceReport(
        start_date=dd.today(-90), interesting_for=welket)


def skills_objects():
    "was previously in skills.fixtures.demo2"

    Skill = rt.models.skills.Skill
    Competence = rt.models.skills.Competence
    Demand = rt.models.skills.Demand
    # Ticket = rt.models.tickets.Ticket
    User = rt.models.users.User

    yield named(Skill, _('Analysis'))
    yield named(Skill, _('Code changes'))
    yield named(Skill, _('Documentation'))
    yield named(Skill, _('Testing'))
    yield named(Skill, _('Configuration'))
    yield named(Skill, _('Enhancement'))
    yield named(Skill, _('Optimization'))
    yield named(Skill, _('Offer'))

    SKILLS = Cycler(Skill.objects.all())
    END_USERS = Cycler(dd.plugins.skills.end_user_model.objects.all())

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
            dd.plugins.skills.demander_model.objects.all()):
        yield Demand(demander=t, skill=SKILLS.pop())
        if i % 3:
            yield Demand(demander=t, skill=SKILLS.pop())

def votes_objects():

    yield vote('mathieu', 1, 'candidate')
    yield vote('luc', 1, 'candidate')
    yield vote('jean', 2, 'assigned')


def objects():
    yield tickets_objects()
    yield working_objects()
    # yield skills_objects()
    # yield votes_objects()
