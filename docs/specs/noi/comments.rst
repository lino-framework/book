.. doctest docs/specs/noi/comments.rst
.. _noi.specs.comments:

==============================
``comments`` (comments in Noi)
==============================

.. currentmodule:: lino.modlib.comments

Noi does not extend :mod:`lino.modlib.comments`


.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.team.settings.demo')
>>> from lino.api.doctest import *

Comments
========

Comments in :ref:`noi` are visible even to anonymous users. At least non-private
comments.  Whether a comment is private or not depends on its :attr:`owner` (a
:class:`lino.modlib.comments.Commentable`).

There are two :class:`Commentable` things in :ref:`noi` tickets and teams.

Comments are private by default:

>>> dd.plugins.comments.private_default
True

>>> list(rt.models_by_base(comments.Commentable))
[<class 'lino_noi.lib.groups.models.Group'>, <class 'lino_noi.lib.tickets.models.Ticket'>]

Comments on a ticket are public when neither the ticket nor its site are marked
private.

Comments on a team are public when the team is not private.

>>> rt.models.comments.Comment.objects.all().count()
168
>>> rt.models.comments.Comment.objects.filter(private=True).count()
134

>>> rt.login("robin").show(comments.Comments,
...     column_names="id ticket__site user owner short_preview",
...     offset=82, limit=6)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
+----+--------+-------------+-----------------------------------------------+--------------------------------------------------------------------------------+
| ID | Site   | Author      | Topic                                         | Preview                                                                        |
+====+========+=============+===============================================+================================================================================+
| 83 |        | Rolf Rompen | `Developers <Detail>`__                       | Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc cursus felis     |
|    |        |             |                                               | nisi, eu pellentesque lorem lobortis non. Aenean non sodales neque, vitae      |
|    |        |             |                                               | venenatis lectus. In eros dui, gravida et dolor at, pellentesque hendrerit     |
|    |        |             |                                               | magna. Quisque vel lectus dictum, rhoncus massa feugiat, condimentum sem.      |
|    |        |             |                                               | Donec elit nisl, placerat vitae imperdiet eget, hendrerit nec quam. Ut         |
|    |        |             |                                               | elementum ligula vitae odio efficitur rhoncus. Duis in blandit neque. Sed      |
|    |        |             |                                               | dictum mollis volutpat. Morbi at est et nisi euismod viverra. Nulla quis lacus |
|    |        |             |                                               | vitae ante sollicitudin tincidunt. Donec nec enim in leo vulputate ultrices.   |
|    |        |             |                                               | Suspendisse potenti. Ut elit nibh, porta ut enim ac, convallis molestie risus. |
|    |        |             |                                               | Praesent consectetur lacus lacus, in faucibus justo fringilla vel. (...)       |
+----+--------+-------------+-----------------------------------------------+--------------------------------------------------------------------------------+
| 84 |        | Robin Rood  | `Managers <Detail>`__                         | Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec interdum dictum |
|    |        |             |                                               | erat. Fusce condimentum erat a pulvinar ultricies. (...)                       |
+----+--------+-------------+-----------------------------------------------+--------------------------------------------------------------------------------+
| 85 | welket | Jean        | `#1 (⛶ Föö fails to bar when baz) <Detail>`__ | breaking (...)                                                                 |
+----+--------+-------------+-----------------------------------------------+--------------------------------------------------------------------------------+
| 86 | welket | Luc         | `#1 (⛶ Föö fails to bar when baz) <Detail>`__ | (...)                                                                          |
+----+--------+-------------+-----------------------------------------------+--------------------------------------------------------------------------------+
| 87 | welket | Marc        | `#1 (⛶ Föö fails to bar when baz) <Detail>`__ | Some plain text.                                                               |
+----+--------+-------------+-----------------------------------------------+--------------------------------------------------------------------------------+
| 88 | welket | Mathieu     | `#1 (⛶ Föö fails to bar when baz) <Detail>`__ | Two paragraphs of plain text. (...)                                            |
+----+--------+-------------+-----------------------------------------------+--------------------------------------------------------------------------------+
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
34


>>> rt.show(comments.RecentComments,
...     column_names="id ticket__site user owner short_preview",
...     limit=6)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF


>>> obj = tickets.Ticket.objects.get(pk=2)
>>> rt.login('luc').show(comments.CommentsByRFC, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
<p><b>Write comment</b></p><ul><li><a ...>...</a> by <a href="Detail">Luc</a> [<b> Reply </b>] <a ...>⁜</a><div id="comment-86"><p>Very confidential comment</p></div></li></ul>
