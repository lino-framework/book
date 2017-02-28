.. _cosi.specs.contacts:

========
Contacts
========

..  to test only this document:

    $ python setup.py test -s tests.DocsTests.test_contacts

    >>> import lino
    >>> lino.startup('lino_cosi.projects.std.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db.models import Q


Quick search
============

When doing a quick search in a list of partners, Lino searches only
the :attr:`name<lino.modlib.contacts.models.Partner.name>` field.

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

Implementation note: this is because we use the
:attr:`quick_search_fields
<lino.core.model.Model.quick_search_fields>` attribute on the model.

>>> contacts.Partner.quick_search_fields
frozenset(['name'])


Quickly finding a partner using its primary key
===============================================

A special type of quick search is when the user enters a number and
not a sequence of letters.  In that case you get the partner with that
primary key.

>>> rt.show(contacts.Partners, quick_search="123")
====================== ================ =====
 Name                   e-mail address   ID
---------------------- ---------------- -----
 Dobbelstein Dorothée                    123
====================== ================ =====
<BLANKLINE>

Without our rule, the above list would also contain *Reinhards
Baumschule* because their house number is 123:

>>> obj = contacts.Partner.objects.get(street_no__contains="123")
>>> print(obj.address)
Reinhards Baumschule
Segelfliegerdamm 123
12487 Berlin
Germany

Also note that numeric searches are exact matches, not partial: *12*
will find a most one partner, and not find all partners whose primary
key *contains* the sequence *12*.

>>> rt.show(contacts.Partners, quick_search="12")
No data to display


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

