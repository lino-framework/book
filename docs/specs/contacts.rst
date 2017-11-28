.. _specs.contacts:

=======================
The ``contacts`` plugin
=======================

..  To run only this test:

    $ doctest docs/specs/contacts.rst
    
    
    >>> import lino
    >>> lino.startup('lino_book.projects.min1.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db.models import Q


The :mod:`lino_xl.lib.contacts` plugin adds functionality for managing
contacts.  It features a common MTI model **partner** with two
specializations **person** and **organization**.  Stores the **roles**
of a person in an organization.

.. contents::
  :local:



.. currentmodule:: lino_xl.lib.contacts
                   

Database structure
==================

This plugin defines the following database models.

.. image:: contacts.png
           
- The main models are :class:`Person` and :class:`Company` and their
  common base :class:`Partner`.
  :class:`Partner` model is *not abstract*, i.e. you can see a table
  where persons organizations are together.
  
- A :class:`Role` is when a given person has a given function in a
  given company.

- A :class:`RoleType` ("Function") where you can configure the
  available functions.
  
- A :class:`CompanyType` model can be used to classify companies.


Menu entries
============

This plugin adds the following menu entries:

- :menuselection:`Contacts --> Persons`
- :menuselection:`Contacts --> Organizations`
  
- :menuselection:`Configuration --> Contacts --> Functions`
- :menuselection:`Configuration --> Contacts --> Organization types`
  
- :menuselection:`Explorer --> Contacts --> Partners`
- :menuselection:`Explorer --> Contacts --> Roles`


Dependencies
============

This plugin needs :mod:`lino_xl.lib.countries` and
:mod:`lino.modlib.system`.
           
This plugin is being extended by :ref:`welfare` in
:mod:`lino_welfare.modlib.contacts` or by :ref:`voga` in
:mod:`lino_voga.modlib.contacts`.


Functions
=========

>>> rt.show(contacts.RoleTypes)
==== ============= ================== =====================
 ID   Designation   Designation (de)   Designation (fr)
---- ------------- ------------------ ---------------------
 1    Manager       Geschäftsführer    Gérant
 2    Director      Direktor           Directeur
 3    Secretary     Sekretär           Secrétaire
 4    IT Manager    EDV-Manager        Gérant informatique
 5    President     Präsident          Président
==== ============= ================== =====================
<BLANKLINE>
     




Quick search
============

When doing a quick search in a list of partners, Lino searches only
the :attr:`name <Partner.name>` field and
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



Exporting contacts as vcard files
=================================

.. class:: ExportVCardFile

    Download all records as a .vcf file which you can import to another
    contacts application.

    This action exists on every list of partners when your
    application has :attr:`use_vcard_export
    <lino_xl.lib.contacts.Plugin.use_vcard_export>` set to `True`.





Reference
=========

.. class:: Plugin

    .. attribute:: region_label

        The `verbose_name` of the `region` field.
           
    .. attribute:: use_vcard_export

        Whether Lino should provide a button for exporting contact
        data as a vcf file.

        If you set this to True, then you must install `vobject
        <http://eventable.github.io/vobject/>`__ into your Python
        environment::

              pip install vobject

        

.. class:: SimpleContactsUser

   A user who has access to basic contacts functionality.

.. class:: ContactsUser

   A user who has access to full contacts functionality.
   
.. class:: ContactsStaff

   A user who can configure contacts functionality.
   
.. class:: PartnerEvents

    A choicelist of observable partner events.

           
.. class:: Partner
           
    A Partner is any physical or moral person for which you want to
    keep contact data (address, phone numbers, ...).

    A :class:`Partner` can act as the recipient of a sales invoice, as
    the sender of an incoming purchases invoice, ...

    A Partner has at least a name and usually also an "official" address.

    Predefined subclasses of Partners are :class:`Person` for physical
    persons and :class:`Company` for companies, organisations and any
    kind of non-formal Partners.

    .. attribute:: name

        The full name of this partner. Used for alphabetic sorting.
        Subclasses may hide this field and fill it automatically,
        e.g. saving a :class:`Person` will automatically set her
        `name` field to "last_name, first_name".

    .. attribute:: prefix

        An optional name prefix. For organisations this is inserted
        before the name, for persons this is inserted between first
        name and last name (see
        :meth:`lino.mixins.human.Human.get_last_name_prefix`).

    .. attribute:: email

        The primary email address.

    .. attribute:: phone

        The primary phone number.  Note that Lino does not ignore
        formatting characters in phone numbers when searching.  For
        example, if you enter "087/12.34.56" as a phone number, then a
        search for phone number containing "1234" will *not* find it.

    .. attribute:: gsm

        The primary mobile phone number.

    .. attribute:: language

        The language to use when communicating with this partner.

           
.. class:: Persons

    Shows all persons.
           
.. class:: Person

    A physical person and an individual human being.
    See also :ref:`lino.tutorial.human`.


.. class:: Company
.. class:: Companies

    An **organisation**.  The verbose name is "Organization" while the
    internal name is "Company" because the latter easier to type and
    for historical reasons.

    .. attribute:: type
    
        Pointer to the :class:`CompanyType`.

    .. attribute:: name
    .. attribute:: street
    .. attribute:: gsm
    .. attribute:: phone

        These fields (and some others) are defined in the base model
        :class:`Partner`, they are what companies and persons have in
        common.
        
.. class:: CompanyTypes
.. class:: CompanyType

    A type of organization. Used by :attr:`Company.type` field.
           
.. class:: RoleType

    A **function** (:class:`RoleType`) is what a given :class:`Person`
    can be in a given :class:`Company`.

    TODO: rename "RoleType" to "Function" or "ContactType".

    .. attribute:: name
    
        A translatable designation. Used e.g. in document templates
        for contracts.

           
.. class:: Role
           
    A **role** is when a given **person** has a given **function**
    (:class:`ContactType`) in a given **organization**.

    .. attribute:: company

        The organization where this person has this role.

    .. attribute:: type

        The function of this person in this company.
    
    .. attribute:: person

        The person having this role in this company.
    

.. class:: ContactRelated

    Model mixin for things that relate to **either** a private person
    **or** a company, the latter potentially represented by a contact
    person having a given role in that company.  Typical usages are
    **invoices** or **contracts**.

    Adds 3 database fields and two virtual fields.

    .. attribute:: company

        Pointer to :class:`Company`.

    .. attribute:: contact_person

        Pointer to :class:`Person`.

    .. attribute:: contact_role

        The optional :class:`Role`
        of the :attr:`contact_person` within :attr:`company`.

    .. attribute:: partner

        (Virtual field) The "legal partner", i.e. usually the
        :attr:`company`, except when that field is empty, in which
        case `partner` contains the :attr:`contact_person`.  If both
        fields are empty, then `partner` contains `None`.

    .. attribute:: recipient

        (Virtual field) The :class:`Addressable
        <lino.utils.addressable.Addressable>` object to use when
        printing a postal address for this.
        This is typically either the :attr:`company` or
        :attr:`contact_person` (if one of these fields is
        non-empty). It may also be a
        :class:`lino_xl.lib.contacts.models.Role` object.


    Difference between :attr:`partner` and `recipient`: an invoice can
    be issued and addressed to a given person in a company (i.e. a
    :class:`Role <lino_xl.lib.contacts.models.Role>` object), but
    accountants want to know the juristic person, which is either the
    :attr:`company` or a private :attr:`person` (if no :attr:`company`
    specified), but not a combination of both.

           
.. class:: PartnerDocument

    Deprecated.
    Adds two fields 'partner' and 'person' to this model, making it
    something that refers to a "partner".  `person` means a "contact
    person" for the partner.



Print templates
===============

           
.. xfile:: contacts/Person/TermsConditions.odt

    Prints a "Terms & Conditions" document to be used by organisations
    who need a signed permission from their clients for storing their
    contact data.  The default content may be localized.

