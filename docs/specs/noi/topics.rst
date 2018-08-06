.. doctest docs/specs/noi/topics.rst
.. _noi.specs.topics:

=============================
Topics in Lino Noi
=============================


.. doctest init:

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
===== ============================================== ========== ============ ========
 ID    Summary                                        Priority   Workflow     Site
----- ---------------------------------------------- ---------- ------------ --------
 115   'NoneType' object has no attribute 'isocode'   Normal     **Open**     welket
 111   Irritating message when bar                    Normal     **Closed**   welsch
 107   Foo never bars                                 Normal     **Open**     pypi
 103   How can I see where bar?                       Normal     **Closed**   welket
 99    No more foo when bar is gone                   Normal     **Open**     welsch
 95    Misc optimizations in Baz                      Normal     **Closed**   pypi
 91    Cannot delete foo                              Normal     **Open**     welket
 87    Default account in invoices per partner        Normal     **Closed**   welsch
 83    Why is foo so bar                              Normal     **Open**     pypi
 79    'NoneType' object has no attribute 'isocode'   Normal     **Closed**   welket
 75    Irritating message when bar                    Normal     **Open**     welsch
 71    Foo never bars                                 Normal     **Closed**   pypi
 67    How can I see where bar?                       Normal     **Open**     welket
 63    No more foo when bar is gone                   Normal     **Closed**   welsch
 59    Misc optimizations in Baz                      Normal     **Open**     pypi
 55    Cannot delete foo                              Normal     **Closed**   welket
 51    Default account in invoices per partner        Normal     **Open**     welsch
 47    Why is foo so bar                              Normal     **Closed**   pypi
 43    'NoneType' object has no attribute 'isocode'   Normal     **Open**     welket
 39    Irritating message when bar                    Normal     **Closed**   welsch
 35    Foo never bars                                 Normal     **Open**     pypi
 31    How can I see where bar?                       Normal     **Closed**   welket
 27    No more foo when bar is gone                   Normal     **Open**     welsch
 23    Misc optimizations in Baz                      Normal     **Closed**   pypi
 19    Cannot delete foo                              Normal     **Open**     welket
 15    Bars have no foo                               Normal     **Closed**   welsch
 11    Class-based Foos and Bars?                     Normal     **Open**     pypi
 7     No Foo after deleting Bar                      Normal     **Closed**   welket
 3     Baz sucks                                      Normal     **Open**     welsch
===== ============================================== ========== ============ ========
<BLANKLINE>
 


Topic groups
============

>>> rt.show(topics.TopicGroups)
No data to display

>>> show_menu_path(topics.TopicGroups)
Configure --> Topics --> Topic groups
