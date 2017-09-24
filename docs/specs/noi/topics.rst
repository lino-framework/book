.. _noi.specs.topics:

=============================
Topics in Lino Noi
=============================


.. How to test only this document:

    $ doctest docs/specs/noi/topics.rst
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.demo')
    >>> from lino.api.doctest import *


This document specifies the ticket management functions of Lino Noi,
implemented in :mod:`lino_xl.lib.tickets`.


.. contents::
  :local:



Topics
========

The :attr:`topic <lino_xl.lib.tickets.models.Ticket.topic>` of a
ticket is what Trac calls "component". Topics are a "customer-side"
classification of the different components which are being developed
by the team that uses a given Lino Noi site.

There are 4 topics in the demo database.

>>> show_menu_path(topics.AllTopics)
Configure --> Topics --> Topics



>>> rt.show(topics.AllTopics)
=========== ============== ================== ================== =============
 Reference   Designation    Designation (de)   Designation (fr)   Topic group
----------- -------------- ------------------ ------------------ -------------
 linõ        Lino Core
 welfäre     Lino Welfare
 così        Lino Cosi
 faggio      Lino Voga
=========== ============== ================== ================== =============
<BLANKLINE>


Choosing a topic
================

When choosing a topic, the search text looks in both the
:guilabel:`Reference` and the :guilabel:`Designation` field:

>>> base = '/choices/tickets/Tickets/topic'
>>> show_choices("robin", base + '?query=')
<br/>
Lino Core
Lino Welfare
Lino Cosi
Lino Voga

Note that we have a topic whose `ref` is different from `name`, and
that the search works in both fields:

>>> obj = topics.Topic.get_by_ref('faggio')
>>> print(obj.ref)
faggio
>>> print(obj.name)
Lino Voga

>>> show_choices("robin", base + '?query=fag')
Lino Voga

>>> show_choices("robin", base + '?query=voga')
Lino Voga


Interests
=========

Every partner can have its list of "interests". They will get notified
about changes in these topics even when they did not report the
ticket.


>>> obj = contacts.Company.objects.get(name="welket")
>>> rt.show(topics.InterestsByController, obj)
... #doctest: +REPORT_UDIFF
Lino Core, Lino Welfare, Lino Cosi

>>> obj = topics.Topic.objects.get(ref="welfäre")
>>> rt.show(topics.InterestsByTopic, obj)
... #doctest: +REPORT_UDIFF
======================
 Controlled by
----------------------
 *welket*
 *welsch*
 *2015-05-21 by Jean*
======================
<BLANKLINE>


Filtering tickets by topic
==========================

>>> pv = dict(topic=rt.models.topics.Topic.get_by_ref("così"))
>>> rt.show(tickets.Tickets, param_values=pv)
... #doctest: -REPORT_UDIFF
===== =========================================== ========== =========== ======
 ID    Summary                                     Priority   Workflow    Site
----- ------------------------------------------- ---------- ----------- ------
 114   Ticket 114                                  Normal     **Talk**
 110   Ticket 110                                  Normal     **Ready**
 106   Ticket 106                                  Normal     **Talk**
 102   Ticket 102                                  Normal     **Ready**
 98    Ticket 98                                   Normal     **Talk**
 94    Ticket 94                                   Normal     **Ready**
 90    Ticket 90                                   Normal     **Talk**
 86    Ticket 86                                   Normal     **Ready**
 82    Ticket 82                                   Normal     **Talk**
 78    Ticket 78                                   Normal     **Ready**
 74    Ticket 74                                   Normal     **Talk**
 70    Ticket 70                                   Normal     **Ready**
 66    Ticket 66                                   Normal     **Talk**
 62    Ticket 62                                   Normal     **Ready**
 58    Ticket 58                                   Normal     **Talk**
 54    Ticket 54                                   Normal     **Ready**
 50    Ticket 50                                   Normal     **Talk**
 46    Ticket 46                                   Normal     **Ready**
 42    Ticket 42                                   Normal     **Talk**
 38    Ticket 38                                   Normal     **Ready**
 34    Ticket 34                                   Normal     **Talk**
 30    Ticket 30                                   Normal     **Ready**
 26    Ticket 26                                   Normal     **Talk**
 22    Ticket 22                                   Normal     **Ready**
 18    Ticket 18                                   Normal     **Talk**
 14    Bar cannot baz                              Normal     **Ready**
 10    Where can I find a Foo when bazing Bazes?   Normal     **Talk**
 6     Sell bar in baz                             Normal     **Ready**
 2     Bar is not always baz                       Normal     **Talk**
===== =========================================== ========== =========== ======
<BLANKLINE>
 


Topic groups
============

>>> rt.show(topics.TopicGroups)
No data to display

>>> show_menu_path(topics.TopicGroups)
Configure --> Topics --> Topic groups
