.. doctest docs/specs/search.rst
.. _specs.search:

=============================
``about`` : Site-wide search
=============================

.. currentmodule:: lino.modlib.about

The :mod:`lino.modlib.about` plugin also adds functionality for doing site-wide
searches across all tables of the application.


.. contents::
   :depth: 1
   :local:


.. include:: /../docs/shared/include/tested.rst


>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *

Code snippets in this document use the :mod:`lino_book.projects.lydia` demo
project.


The ``SiteSearch`` table
========================

.. class:: SiteSearch

    The virtual table used to implement site-wide searches


>>> rt.show('about.SiteSearch', quick_search="foo")
No data to display

If you search contains more than one word, it shows all rows containing both
words.

>>> rt.show('about.SiteSearch', quick_search="est land")
============================== ===================================================================================================
 Description                    Matches
------------------------------ ---------------------------------------------------------------------------------------------------
 *Estonia* (Country)            name:**Est**onia, name_de:**Est****land**, name_fr:**Est**onie
 *Flandre de l'Est* (Place)     name:F**land**re de l'**Est**, name_de:Ostf**land**ern, name_fr:F**land**re de l'**Est**
 *Flandre de l'Ouest* (Place)   name:F**land**re de l'Ou**est**, name_de:W**est**f**land**ern, name_fr:F**land**re de l'Ou**est**
============================== ===================================================================================================
<BLANKLINE>


>>> rt.show('about.SiteSearch', quick_search="123")  #doctest: +SKIP
===================================================== ========================
 Description                                           Matches
----------------------------------------------------- ------------------------
 *Arens Andreas* (Partner)                             phone:+32 87**123**456
 *Arens Annette* (Partner)                             phone:+32 87**123**457
 *Dobbelstein-Demeulenaere Dorothée* (Partner)         id:123
 *Mr Andreas Arens* (Person)                           phone:+32 87**123**456
 *Mrs Annette Arens* (Person)                          phone:+32 87**123**457
 *Mrs Dorothée Dobbelstein-Demeulenaere* (Person)      id:123
 *+32 87123456* (Contact detail)                       value:+32 87**123**456
 *+32 87123457* (Contact detail)                       value:+32 87**123**457
 *Diner (09.05.2015 13:30)* (Calendar entry)           id:123
 *SLS 9.2* (Movement)                                  id:123
 *DOBBELSTEIN-DEMEULENAERE Dorothée (123)* (Patient)   id:123
===================================================== ========================
<BLANKLINE>

Dobbelstein-Demeulenaere Dorothée (id 123) is Partner, Person and
Patient.  All three instances are listed in the SiteSearch.


Don't read on
=============

The remaining part of this page is just technical stuff.


>>> from lino.core.utils import get_models
>>> rt.models.tera.Client in set(get_models())
True

>>> ar = rt.login()
>>> user_type = ar.get_user().user_type
>>> count = 0
>>> for model in get_models():
...     t = model.get_default_table()
...     if not t.get_view_permission(user_type):
...         print("Not visible: {}".format(t))
...     count += 1
>>> print("Verified {} models".format(count))
Verified 98 models

>>> rt.models.contacts.Person.quick_search_fields_digit
(<django.db.models.fields.AutoField: id>,)


The following request caused problems before 20180920 (:ticket:`2544`
SiteSearch fails when it finds a name containing "&")

>>> rt.show('about.SiteSearch', quick_search="rumma")
================================== =================================
 Description                        Matches
---------------------------------- ---------------------------------
 *Rumma & Ko OÜ* (Partner)          name:**Rumma** & Ko OÜ
 *Rumma & Ko OÜ* (Organization)     name:**Rumma** & Ko OÜ
 *SLS 1/2015* (Sales invoice)       partner__name:**Rumma** & Ko OÜ
 *Row # 70* (Bank Statement item)   partner__name:**Rumma** & Ko OÜ
 *Row # 21* (Bank Statement item)   partner__name:**Rumma** & Ko OÜ
 *Row # 2* (Bank Statement item)    partner__name:**Rumma** & Ko OÜ
 *Row # 1* (Payment Order item)     partner__name:**Rumma** & Ko OÜ
 *Row # 1* (Payment Order item)     partner__name:**Rumma** & Ko OÜ
 *Row # 1* (Payment Order item)     partner__name:**Rumma** & Ko OÜ
 *Row # 1* (Payment Order item)     partner__name:**Rumma** & Ko OÜ
================================== =================================
<BLANKLINE>
