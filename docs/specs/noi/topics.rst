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
Lino Core, Lino Welfare, Lino Voga

>>> obj = topics.Topic.objects.get(ref="welfäre")
>>> rt.show(topics.InterestsByTopic, obj)
... #doctest: +REPORT_UDIFF
=================
 Controlled by
-----------------
 *Rumma & Ko OÜ*
 *welket*
 *Saffre-Rumma*
=================
<BLANKLINE>


Filtering tickets by topic
==========================

>>> pv = dict(topic=rt.models.topics.Topic.get_by_ref("così"))
>>> rt.show(tickets.Tickets, param_values=pv)
... #doctest: -REPORT_UDIFF
===== ============================ ========== ============ ========
 ID    Summary                      Priority   Workflow     Site
----- ---------------------------- ---------- ------------ --------
 115   Ticket 115                   Normal     **Open**     welket
 111   Ticket 111                   Normal     **Closed**   welsch
 107   Ticket 107                   Normal     **Open**     pypi
 103   Ticket 103                   Normal     **Closed**   welket
 99    Ticket 99                    Normal     **Open**     welsch
 95    Ticket 95                    Normal     **Closed**   pypi
 91    Ticket 91                    Normal     **Open**     welket
 87    Ticket 87                    Normal     **Closed**   welsch
 83    Ticket 83                    Normal     **Open**     pypi
 79    Ticket 79                    Normal     **Closed**   welket
 75    Ticket 75                    Normal     **Open**     welsch
 71    Ticket 71                    Normal     **Closed**   pypi
 67    Ticket 67                    Normal     **Open**     welket
 63    Ticket 63                    Normal     **Closed**   welsch
 59    Ticket 59                    Normal     **Open**     pypi
 55    Ticket 55                    Normal     **Closed**   welket
 51    Ticket 51                    Normal     **Open**     welsch
 47    Ticket 47                    Normal     **Closed**   pypi
 43    Ticket 43                    Normal     **Open**     welket
 39    Ticket 39                    Normal     **Closed**   welsch
 35    Ticket 35                    Normal     **Open**     pypi
 31    Ticket 31                    Normal     **Closed**   welket
 27    Ticket 27                    Normal     **Open**     welsch
 23    Ticket 23                    Normal     **Closed**   pypi
 19    Ticket 19                    Normal     **Open**     welket
 15    Bars have no foo             Normal     **Closed**   welsch
 11    Class-based Foos and Bars?   Normal     **Open**     pypi
 7     No Foo after deleting Bar    Normal     **Closed**   welket
 3     Baz sucks                    Normal     **Open**     welsch
===== ============================ ========== ============ ========
<BLANKLINE>
 


Topic groups
============

>>> rt.show(topics.TopicGroups)
No data to display

>>> show_menu_path(topics.TopicGroups)
Configure --> Topics --> Topic groups
