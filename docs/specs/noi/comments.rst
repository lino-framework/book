.. doctest docs/specs/noi/comments.rst
.. _noi.specs.comments:

==============================
``comments`` (comments in Noi)
==============================

.. currentmodule:: lino.modlib.comments


The :mod:`lino.modlib.comments` plugin in :ref:`noi` is configured and used to
satisfy the application requirements.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.team.settings.demo')
>>> from lino.api.doctest import *


Overview
========

Public comments in :ref:`noi` are visible even to anonymous users.

There are two :class:`Commentable` things in :ref:`noi` tickets and teams.

>>> list(rt.models_by_base(comments.Commentable))
[<class 'lino_noi.lib.groups.models.Group'>, <class 'lino_noi.lib.tickets.models.Ticket'>]

Whether a comment is private or not depends on its :term:`discussion topic`:
Comments on a ticket are public when neither the ticket nor its site are marked
private.

Comments are private by default:

>>> dd.plugins.comments.private_default
True

Comments on a team are public when the team is not private.

Tests
=====

>>> rt.models.comments.Comment.objects.all().count()
168
>>> rt.models.comments.Comment.objects.filter(private=True).count()
140

>>> rt.login("robin").show(comments.Comments,
...     column_names="id ticket__site user owner",
...     offset=82, limit=6)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==== ======== ============= ===============================================
 ID   Site     Author        Topic
---- -------- ------------- -----------------------------------------------
 83            Rolf Rompen   `Front-end team <Detail>`__
 84            Robin Rood    `Front-end team <Detail>`__
 85   welket   Jean          `#1 (⚹ Föö fails to bar when baz) <Detail>`__
 86   welket   Luc           `#1 (⚹ Föö fails to bar when baz) <Detail>`__
 87   welket   Marc          `#1 (⚹ Föö fails to bar when baz) <Detail>`__
 88   welket   Mathieu       `#1 (⚹ Föö fails to bar when baz) <Detail>`__
==== ======== ============= ===============================================
<BLANKLINE>


The demo database contains 168 comments, 84 about a team and 84 about a ticket.
34 comments are public.

>>> comments.Comment.objects.all().count()
168
>>> comments.Comment.objects.filter(ticket__isnull=False).count()
84
>>> comments.Comment.objects.filter(ticket=None).count()
84
>>> comments.Comment.objects.filter(group=None).count()
84
>>> comments.Comment.objects.filter(private=False).count()
28


>>> rt.login("marc").show(comments.RecentComments)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
`... <Detail>`__ by **marc** in reply to **jean** about `#12 <Detail>`__@welket : Lorem ipsum ... (...)
...
`... <Detail>`__ by **robin** in reply to **romain** about `#9 <Detail>`__@bugs : Lorem ipsum dolor ... (...)
...
**Okay** | **✅** | **❎**


>>> rt.show(comments.RecentComments)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
`... <Detail>`__ by **robin** in reply to **marc** about `#10 <Detail>`__ : 
Who What Done?
<BLANKLINE>
...
<BLANKLINE>
`... <Detail>`__ by **romain** about `#9 <Detail>`__@bugs (2 replies) : Styled comment pasted from word!
...
