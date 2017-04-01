================
The votes module
================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_votes
    
    doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.demo')
    >>> from lino.api.doctest import *


The :mod:`lino_xl.lib.votes` module adds the concept of "votes" to
:ref:`noi`.

A **vote** is when a user has an opinion or interest about a given
ticket (or any other votable).

A **votable**, in :ref:`noi`, is a ticket. But the module is designed
to be reusable in other contexts.


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



My tasks ("To-Do list")
=======================

Shows your votes having states `assigned` and `done`.

>>> rt.login('luc').user.profile
users.UserTypes.developer:400

>>> rt.login('jean').show(votes.MyTasks)
... #doctest: +REPORT_UDIFF
====================================================== ========================================================================= ==========
 Description                                            Actions                                                                   Priority
------------------------------------------------------ ------------------------------------------------------------------------- ----------
 `#2 (Bar is not always baz) <Detail>`__                [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done] [Rate]   0
 `#90 (Ticket 90) <Detail>`__ by `Mathieu <Detail>`__   [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done] [Rate]   0
 `#75 (Ticket 75) <Detail>`__ by `Mathieu <Detail>`__   [▶] [★] **Done** → [Rate]                                                 0
 `#42 (Ticket 42) <Detail>`__ by `Mathieu <Detail>`__   [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done] [Rate]   0
 `#27 (Ticket 27) <Detail>`__ by `Mathieu <Detail>`__   [▶] [★] **Done** → [Rate]                                                 0
====================================================== ========================================================================= ==========
<BLANKLINE>



>>> rt.login('mathieu').show(votes.MyTasks)
... #doctest: +REPORT_UDIFF
================================================================================== ================================================================== ==========
 Description                                                                        Actions                                                            Priority
---------------------------------------------------------------------------------- ------------------------------------------------------------------ ----------
 `#106 (Ticket 106) <Detail>`__ by `Luc <Detail>`__                                 [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done]   0
 `#91 (Ticket 91) <Detail>`__ by `Luc <Detail>`__                                   [▶] [★] **Done**                                                   0
 `#58 (Ticket 58) <Detail>`__ by `Luc <Detail>`__                                   [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done]   0
 `#43 (Ticket 43) <Detail>`__ by `Luc <Detail>`__                                   [▶] [★] **Done**                                                   0
 `#10 (Where can I find a Foo when bazing Bazes?) <Detail>`__ by `Luc <Detail>`__   [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done]   0
================================================================================== ================================================================== ==========
<BLANKLINE>


>>> rt.login('luc').show(votes.MyTasks)
... #doctest: -REPORT_UDIFF
==================================================================== ================================================================== ==========
 Description                                                          Actions                                                            Priority
-------------------------------------------------------------------- ------------------------------------------------------------------ ----------
 `#107 (Ticket 107) <Detail>`__ by `Jean <Detail>`__                  [▶] [★] **Done**                                                   0
 `#74 (Ticket 74) <Detail>`__ by `Jean <Detail>`__                    [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done]   0
 `#59 (Ticket 59) <Detail>`__ by `Jean <Detail>`__                    [▶] [★] **Done**                                                   0
 `#26 (Ticket 26) <Detail>`__ by `Jean <Detail>`__                    [▶] [★] **Assigned** → [Cancelled] [Watching] [Pro] [Con] [Done]   0
 `#11 (Class-based Foos and Bars?) <Detail>`__ by `Jean <Detail>`__   [▶] [★] **Done**                                                   0
==================================================================== ================================================================== ==========
<BLANKLINE>



>>> rt.login('luc').show(votes.MyOffers)
... #doctest: -REPORT_UDIFF
=================================================== =======================================================================
 Description                                         Actions
--------------------------------------------------- -----------------------------------------------------------------------
 `#1 (Föö fails to bar when baz) <Detail>`__         [▶] [★] **Candidate** → [Cancelled] [Watching] [Pro] [Con] [Assigned]
 `#89 (Ticket 89) <Detail>`__ by `Jean <Detail>`__   [▶] [★] **Candidate** → [Cancelled] [Watching] [Pro] [Con]
 `#41 (Ticket 41) <Detail>`__ by `Jean <Detail>`__   [▶] [★] **Candidate** → [Cancelled] [Watching] [Pro] [Con]
=================================================== =======================================================================
<BLANKLINE>

Note that Luc is not a triager, that's why he does not have an
[Assigned] action of other people's tickets.

>>> from lino_xl.lib.tickets.roles import Triager
>>> rt.login('luc').user.profile.has_required_roles([Triager])
False

