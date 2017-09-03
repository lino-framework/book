.. _cosi.specs.contacts:

========
Contacts
========

..
    >>> import lino
    >>> lino.startup('lino_book.projects.min1.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db.models import Q

About partners, persons, companies and others
=============================================

Note that I also have to define a :meth:`full_clean` method which
automatically fills the :name` field from the value of the
:attr:`designation` field (similarily to Person and Household)
    


Quick search
============

When doing a quick search in a list of partners, Lino searches only
the :attr:`name <lino_xl.lib.contacts.models.Partner.name>` field and
not for example the street.

>>> rt.show(contacts.Partners, quick_search="berg")
==================== ================ =====
 Name                 e-mail address   ID
-------------------- ---------------- -----
 Altenberg Hans                        114
 Garage Mergelsberg                    104
==================== ================ =====
<BLANKLINE>

Without that restriction, a user who enters "berg" in the quick search
field would also get e.g. the following partners (because their
address contains the query string):

>>> rt.show(contacts.Partners, column_names="name street",
...     filter=Q(street__icontains="berg"))
===================== ===================
 Name                  Street
--------------------- -------------------
 Bastiaensen Laurent   Am Berg
 Collard Charlotte     Auf dem Spitzberg
 Ernst Berta           Bergkapellstraße
 Evers Eberhart        Bergstraße
 Kaivers Karl          Haasberg
 Lazarus Line          Heidberg
===================== ===================
<BLANKLINE>

This behaviour is implemented using the :attr:`quick_search_fields
<lino.core.model.Model.quick_search_fields>` attribute on the model.

>>> contacts.Partner.quick_search_fields
frozenset(['phone', 'prefix', 'gsm', 'name'])


Numeric quick search
====================

You can search for phone numbers

>>> rt.show(contacts.Partners, quick_search="123", column_names="name phone id")
=============== ============== =====
 Name            Phone          ID
--------------- -------------- -----
 Arens Andreas   +32 87123456   112
 Arens Annette   +32 87123457   113
=============== ============== =====
<BLANKLINE>


Quickly finding a partner using its primary key
===============================================

A special type of quick search is when the search string starts with
"#".  In that case you get the partner with that primary key.

>>> rt.show(contacts.Partners, quick_search="#123")
====================== ================ =====
 Name                   e-mail address   ID
---------------------- ---------------- -----
 Dobbelstein Dorothée                    123
====================== ================ =====
<BLANKLINE>



This behaviour is the same for all subclasses of Partner, e.g. for
persons and for organizations.


>>> rt.show(contacts.Persons, quick_search="berg")
=================== ============================= ================ ======= ===== ===== ==========
 Name                Address                       e-mail address   Phone   GSM   ID    Language
------------------- ----------------------------- ---------------- ------- ----- ----- ----------
 Mr Hans Altenberg   Aachener Straße, 4700 Eupen                                  114
=================== ============================= ================ ======= ===== ===== ==========
<BLANKLINE>

>>> rt.show(contacts.Companies, quick_search="berg")
==================== ============================== ================ ======= ===== ===== ==========
 Name                 Address                        e-mail address   Phone   GSM   ID    Language
-------------------- ------------------------------ ---------------- ------- ----- ----- ----------
 Garage Mergelsberg   Kasinostraße 13, 4720 Kelmis                                  104
==================== ============================== ================ ======= ===== ===== ==========
<BLANKLINE>

