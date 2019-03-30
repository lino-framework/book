.. _specs.phones:

=================================================================
``phones`` : Multiple phone numbers per partner (Contact details)
=================================================================

.. currentmodule:: lino_xl.lib.phones

The :mod:`lino_xl.lib.phones` plugin adds functionality to handle multiple
phone numbers, email addresses etc ("contact details") per partner. When this
plugin is installed, your application can show a "Contact Details" panel per
partner instead of the four fields `phone`, `gsm`, `email` and `url`.



.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.liina.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q


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
    
.. class:: ContactDetailType

     .. attribute:: field_name

         The name of field on the :class:`ContactDetailsOwner` where
         the value of the primary item of this type is to be mirrored.
        
.. class:: ContactDetailTypes

     The list of "built-in" types of contact detail items.

.. class:: ContactDetail

    .. attribute:: partner

    .. attribute:: detail_type

    .. attribute:: primary
    
        Whether this item is the primary contact detail for this type
        and this owner.  Setting this field will automatically uncheck
        any previously primary items and update the owner's contact
        detail fields.


           
.. class:: ContactDetailsOwner
           
    Model mixin for the potential owner of contact details.

    This mixin may be used even when its plugin
    (:mod:`lino_xl.lib.phones`) is not installed.  For example
    :mod:`lino_xl.lib.contacts` does this.


.. class:: ContactDetails
           
.. class:: ContactDetailsByPartner
           
.. class:: ContactDetailsOwnerChecker
           
    Checks for mismatches between contact details and owner.
    
    - Field differs from primary item
    - Field is empty but primary item exists
    - Missing primary item

    The last message is fixable: for example when a partner has a
    non-empty phone number but no primary item of type :attr:`phone`,
    then Lino can simply create that item.  This situation is normal
    when a production site which previously had no
    :mod:`lino_xl.lib.phones` plugin installed is migrated to a schema
    with that plugin installed.
