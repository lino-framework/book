.. doctest docs/specs/avanti/comments.rst
.. _avanti.specs.comments:

=================================
``comments`` (comments in Avanti)
=================================

.. currentmodule:: lino.modlib.comments

The :mod:`lino.modlib.comments` in :ref:`avanti` is configured and used to
satisfy the application requirements.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.avanti1.settings.demo')
>>> from lino.api.doctest import *

Overview
========

Comments in :ref:`avanti` are considered confidential data and can be seen only
by users with appropriate permission.

See also :doc:`roles`.

Private comments are seen only by their respective author.

Public comments are shown to other social workers. Comments are never shown to
the *external supervisor*.

A :term:`system administrator` can see *all* comments (it makes no
sense to hide them because a system admin can easily create or use a user
account with the permissions they want).

Comments are private by default:

>>> dd.plugins.comments.private_default
True

There is only one :class:`Commentable` thing in :ref:`avanti`: the client.

>>> list(rt.models_by_base(comments.Commentable))
[<class 'lino_avanti.lib.avanti.models.Client'>]

Tests
=====

The demo database contains 108 comments, and they are all private.

>>> rt.models.comments.Comment.objects.all().count()
108
>>> rt.models.comments.Comment.objects.filter(private=True).count()
108

Robin can see them all.

>>> rt.login("robin").show(comments.Comments,
...     column_names="id user owner", limit=6)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==== =============== =================================
 ID   Author          Topic
---- --------------- ---------------------------------
 1    audrey          `ABAD Aábdeen (114) <Detail>`__
 2    martina         `ABAD Aábdeen (114) <Detail>`__
 3    nathalie        `ABAD Aábdeen (114) <Detail>`__
 4    nelly           `ABAD Aábdeen (114) <Detail>`__
 5    sandra          `ABAD Aábdeen (114) <Detail>`__
 6    Laura Lieblig   `ABAD Aábdeen (114) <Detail>`__
==== =============== =================================
<BLANKLINE>


Anonymous users don't see any comment:

>>> rt.show(comments.Comments,
...     column_names="id user owner", limit=6)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
No data to display

Nathalie sees only her comments:

>>> rt.login("nathalie").show(comments.Comments,
...     column_names="id user owner", limit=6)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==== ========== ====================================
 ID   Author     Topic
---- ---------- ------------------------------------
 3    nathalie   `ABAD Aábdeen (114) <Detail>`__
 12   nathalie   `ABBAS Aábid (115) <Detail>`__
 21   nathalie   `ABBASI Aáishá (118) <Detail>`__
 30   nathalie   `ABDALLAH Aáish (127) <Detail>`__
 39   nathalie   `ABDELLA Aákif (128) <Detail>`__
 48   nathalie   `ABDELNOUR Aámir (125) <Detail>`__
==== ========== ====================================
<BLANKLINE>


>>> rt.show(comments.RecentComments)
<BLANKLINE>

>>> rt.login("audrey").show(comments.RecentComments)
<BLANKLINE>

>>> rt.login("nathalie").show(comments.RecentComments)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
`... <Detail>`__ by **nathalie** in reply to **martina** about `ABDULLAH Afááf (155) <Detail>`__ :
...
