.. _specs.noi.votes:

================
The votes module
================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_votes
    
    doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.demo')
    >>> from lino.api.doctest import *


The :mod:`lino_xl.lib.votes` module adds the concept of "votes" to an
application. This document describes how this looks in :ref:`noi`.

.. contents::
  :local:

Introduction
============

A **vote** is when a given user has an opinion or interest about a
given ticket.  A special case are **vote invitations** (votes having
state "invited") where the user did not yet express any opinion or
interest but is *asked* to do so.

Votes are visible in the `VotesByVotable` panel of a ticket. Your
votes become visible as invitations, candidatures or tasks in your
Office menu or your dashboard.


Vote invitations
================

Lino automatically creates vote invitations when a user *comments* on
a ticket, *works* on a ticket or *participates* in an activity with
that ticket.


When you have pending vote invitations, Lino displays them in the "My
vote invitations" table on your dashboard.

This table basically is a list of tickets asking you to choose, for
each of them, one of four options:

- Cancelled : not interested. You declare that you don't want to be
  bothered with this ticket.
- Watching : You are interested, you are neutral and did not
  yet declare your opinion. You want to be notified when
  something happens in this ticket.
- Pro : optimistically watching. You declare that you want this ticket
  to get *done*. You support this ticket.
- Con : skeptically watching. You declare that you want this ticket to
  get *refused*.

The pro and con states will be visible in the WishesByMilestone
view and may be used for quick voting polls.


Voting polls
============

A **voting poll** is when one user asks other users to vote "yes",
"no" or "undecided" on a series of questions.

You can run a voting poll in Noi as follows:

- formulate your questions as tickets
- create an activity and add your tickets as wishes
- add enrolments to your activity. The participants will automatically
  get a vote invitation. Note that you must click the Save button of
  the activity for Lino to create vote invitations.


Candidatures
============

When a ticket has been declared "Open" by its author, then any
watching user may decide move from unengaged *watching* to engaged
*acting*.  This is done in two steps: first you declare yourself as a
*candidate*. The author of the ticket can then see your candidature
and possibly *assign* you to that ticket.


My tasks
========

This table thows your votes having states `assigned` and `done`.
It is your general "To-Do list".

Here are some examples for different users.

>>> rt.login('jean').show(votes.MyTasks)
... #doctest: +REPORT_UDIFF
========================================================================================================= =========================================================================
 Description                                                                                               Actions
--------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------
 `#2 (☎ Bar is not always baz) <Detail>`__, assigned to `Jean <Detail>`__                                  [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done] [Rate]
 `#91 (☉ Ticket 91) <Detail>`__  by `Mathieu <Detail>`__, assigned to `Jean <Detail>`__                    [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done] [Rate]
 `#51 (☉ Ticket 51) <Detail>`__  by `Mathieu <Detail>`__, assigned to `Jean <Detail>`__                    [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done] [Rate]
 `#11 (☉ Class-based Foos and Bars?) <Detail>`__  by `Mathieu <Detail>`__, assigned to `Jean <Detail>`__   [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done] [Rate]
========================================================================================================= =========================================================================
<BLANKLINE>




>>> rt.login('mathieu').show(votes.MyTasks)
... #doctest: +REPORT_UDIFF
========================================================== ==================
 Description                                                Actions
---------------------------------------------------------- ------------------
 `#92 (⚒ Ticket 92) <Detail>`__  by `Luc <Detail>`__        [▶] [★] **Done**
 `#52 (⚒ Ticket 52) <Detail>`__  by `Luc <Detail>`__        [▶] [★] **Done**
 `#12 (⚒ Foo cannot bar) <Detail>`__  by `Luc <Detail>`__   [▶] [★] **Done**
========================================================== ==================
<BLANKLINE>


>>> rt.login('luc').show(votes.MyTasks)
... #doctest: -REPORT_UDIFF
======================================================== ==================
 Description                                              Actions
-------------------------------------------------------- ------------------
 `#114 (☎ Ticket 114) <Detail>`__  by `Jean <Detail>`__   [▶] [★] **Done**
 `#74 (☎ Ticket 74) <Detail>`__  by `Jean <Detail>`__     [▶] [★] **Done**
 `#34 (☎ Ticket 34) <Detail>`__  by `Jean <Detail>`__     [▶] [★] **Done**
======================================================== ==================
<BLANKLINE>



>>> rt.login('luc').show(votes.MyOffers)
... #doctest: -REPORT_UDIFF
====================================================================================== =======================================================================
 Description                                                                            Actions
-------------------------------------------------------------------------------------- -----------------------------------------------------------------------
 `#1 (⛶ Föö fails to bar when baz) <Detail>`__                                          [▶] [★] **Candidate** → [Cancelled] [Watching] [Pro] [Con] [Assigned]
 `#90 (☎ Ticket 90) <Detail>`__  by `Jean <Detail>`__                                   [▶] [★] **Candidate** → [Cancelled] [Watching] [Pro] [Con]
 `#50 (☎ Ticket 50) <Detail>`__  by `Jean <Detail>`__                                   [▶] [★] **Candidate** → [Cancelled] [Watching] [Pro] [Con]
 `#10 (☎ Where can I find a Foo when bazing Bazes?) <Detail>`__  by `Jean <Detail>`__   [▶] [★] **Candidate** → [Cancelled] [Watching] [Pro] [Con]
====================================================================================== =======================================================================
<BLANKLINE>

Note that Luc is not a triager, that's why he does not have an
[Assigned] action of other people's tickets.

>>> from lino_xl.lib.tickets.roles import Triager
>>> rt.login('luc').user.profile.has_required_roles([Triager])
False


The state of a vote
===================

See :class:`lino_xl.lib.votes.choicelists.VoteStates`

>>> rt.login().show(votes.VoteStates)
... #doctest: +REPORT_UDIFF
======= =========== ===========
 value   name        text
------- ----------- -----------
 00      author      Author
 05      invited     Invited
 10      watching    Watching
 15      pro         Pro
 16      con         Con
 20      candidate   Candidate
 30      assigned    Assigned
 40      done        Done
 50      rated       Rated
 60      cancelled   Cancelled
======= =========== ===========
<BLANKLINE>



The :class:`Votable` mixin
==========================

A **votable**, in :ref:`noi`, is a ticket. But the module is designed
to be reusable in other contexts.

