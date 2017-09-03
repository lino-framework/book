.. _specs.phones:

====================================================
Contact details (Multiple phone numbers per partner)
====================================================

..  to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_phones

    >>> import lino
    >>> lino.startup('lino_book.projects.liina.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db.models import Q

Overview
========

The :mod:`lino_xl.lib.phones` plugin adds models and methods to handle
multiple phone numbers, email addresses etc ("contact details") per
partner.

When this plugin is installed, your application usually has a "Contact
Details" panel per :class:`Partner <lino_xl.lib.contacts.Partner>`
instead of the four fields `phone`, `gsm`, `email` and `url`.

Demo data
=========

>>> rt.show(phones.ContactDetailTypes)
======= ======= =========
 value   name    text
------- ------- ---------
 010     email   E-Mail
 020     gsm     Mobile
 030     phone   Phone
 040     url     Website
 050     fax     Fax
 090     other   Other
======= ======= =========
<BLANKLINE>

>>> rt.show(phones.ContactDetails)
============================== ===================== ======== =============== ==== =========
 Value                          Contact detail type   Remark   Partner         ID   Primary
------------------------------ --------------------- -------- --------------- ---- ---------
 http://www.saffre-rumma.net/   Website                        Rumma & Ko OÜ   1    Yes
 andreas@arens.com              E-Mail                         Arens Andreas   2    Yes
 +32 87123456                   Phone                          Arens Andreas   3    Yes
 annette@arens.com              E-Mail                         Arens Annette   4    Yes
 +32 87123457                   Phone                          Arens Annette   5    Yes
============================== ===================== ======== =============== ==== =========
<BLANKLINE>


Reference
=========
    
.. currentmodule:: lino_xl.lib.phones

.. class:: ContactDetail

    .. attribute:: partner

    .. attribute:: detail_type

    .. attribute:: primary
    
        Whether this item is the primary contact detail for this type
        and this owner.  Setting this field will automatically uncheck
        any previously primary items and update the owner's contact
        detail fields.


           
.. class:: ContactDetailsOwner
           
    Base class for the potential owner of contact details.

    This mixin may be used even when its plugin
    (:mod:`lino_xl.lib.phones`) is not installed.  For example
    :mod:`lino_xl.lib.contacts` does this.


.. class:: ContactDetails
           
.. class:: ContactDetailsByPartner
           
