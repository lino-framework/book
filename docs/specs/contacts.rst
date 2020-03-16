.. doctest docs/specs/contacts.rst
.. include:: /../docs/shared/include/defs.rst
.. _specs.contacts:

================================
``contacts`` : Managing contacts
================================

.. currentmodule:: lino_xl.lib.contacts

The :mod:`lino_xl.lib.contacts` plugin adds functionality for managing
contacts.  It adss the concept of **partner** with two specializations
**person** and **organization**.  Also adds **roles** of a person in
an organization.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.min1.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q


Glossary
=========

.. glossary::

    Natural person

      A really existing person with a first and last name.

      Represented by :class:`Person`.

    Legal person

      A corporation, company or organization.

      Represented by :class:`Organization`.


Database structure
==================

This plugin defines the following database models.

.. image:: contacts.png

- The main models are :class:`Person` and :class:`Company` and their
  common base :class:`Partner`.  The :class:`Partner` model is *not
  abstract*, i.e. you can see a table where persons organizations are
  together.

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


Partners
========

A **Partner** is any physical or moral person for which you want to
keep contact data (address, phone numbers, ...).

A partner can act as the recipient of a sales invoice, as the sender of an
incoming purchases invoice, ...

A partner has at least a name and usually also an "official" address.

Predefined subclasses of Partners are :class:`Person` for physical
persons and :class:`Company` for companies, organisations and any
kind of non-formal Partners.



.. class:: Partner

    The Django model used to represent a *partner*.

    .. attribute:: name

        The full name of this partner. Used for alphabetic sorting.

        Subclasses may hide this field and fill it automatically,
        e.g. saving a :class:`Person` will automatically set her
        `name` field to "last_name, first_name".

    .. attribute:: prefix

        An optional name prefix. For organisations this is inserted
        before the name, for persons this is inserted between first
        name and last name.

        See :meth:`lino.mixins.human.Human.get_last_name_prefix`.

    .. attribute:: email

        The primary email address.

    .. attribute:: phone

        The primary phone number.

        Note that Lino does not ignore formatting characters in phone numbers
        when searching.  For example, if you enter "087/12.34.56" as a phone
        number, then a search for phone number containing "1234" will *not*
        find it.

    .. attribute:: gsm

        The primary mobile phone number.

    .. attribute:: language

        The language to use when communicating with this partner.

    .. attribute:: purchase_account

        The general account to suggest as default value in purchase
        invoices from this partner.

        This field exists only when :mod:`lino_xl.lib.ledger` is
        installed.  It is defined as the
        :attr:`invoice_account_field_name
        <lino_xl.lib.ledger.TradeType.invoice_account_field_name>`
        for :attr:`TradeTypes.purchases
        <lino_xl.lib.ledger.TradeTypes.purchases>`.

    Two fields exist only when :mod:`lino_xl.lib.vat` is installed:

    .. attribute:: vat_regime

        The default VAT regime to use on invoices for this partner.

    .. attribute:: vat_id

        The national VAT identification number of this partner.


Persons
=======

.. class:: Persons

    Shows all persons.

.. class:: Person

    A physical person and an individual human being.
    See also :ref:`lino.tutorial.human`.

    .. attribute:: name
    .. attribute:: first_name
    .. attribute:: last_name


Organizations
=============

.. class:: Company

    An **organisation**.  The verbose name is "Organization" while the
    internal name is "Company" because the latter easier to type and
    for historical reasons.

    .. attribute:: type

        Pointer to the :class:`CompanyType`.

    The following fields are defined in the base model :class:`Partner`, they
    are what companies and persons have in common:

    .. attribute:: name
    .. attribute:: street
    .. attribute:: gsm
    .. attribute:: phone

.. class:: Companies

  Base table for all tables showing companies.


Quick search
============

When doing a quick search in a list of partners, Lino searches only
the :attr:`name <Partner.name>` field and
not for example the street.

>>> rt.show(contacts.Partners, quick_search="berg")
==================== ===== =========================== ================
 Name                 ID    See as                      e-mail address
-------------------- ----- --------------------------- ----------------
 Altenberg Hans       114   Organization, **Partner**
 Garage Mergelsberg   104   **Partner**, Person
==================== ===== =========================== ================
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
(<django.db.models.fields.CharField: prefix>, <django.db.models.fields.CharField: name>, <django.db.models.fields.CharField: phone>, <django.db.models.fields.CharField: gsm>)


Numeric quick search
====================

You can search for phone numbers

>>> rt.show(contacts.Partners, quick_search="123", column_names="name phone id")
====================== ============== =====
 Name                   Phone          ID
---------------------- -------------- -----
 Arens Andreas          +32 87123456   112
 Arens Annette          +32 87123457   113
 Dobbelstein Dorothée                  123
====================== ============== =====
<BLANKLINE>


Quickly finding a partner using its primary key
===============================================

A special type of quick search is when the search string starts with
"#".  In that case you get the partner with that primary key.

>>> rt.show(contacts.Partners, quick_search="#123", column_names="name phone id")
====================== ======= =====
 Name                   Phone   ID
---------------------- ------- -----
 Dobbelstein Dorothée           123
====================== ======= =====
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
==================== ============================= ================ ======= ===== ===== ==========
 Name                 Address                       e-mail address   Phone   GSM   ID    Language
-------------------- ----------------------------- ---------------- ------- ----- ----- ----------
 Garage Mergelsberg   Hauptstraße 13, 4730 Raeren                                  104
==================== ============================= ================ ======= ===== ===== ==========
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

    .. attribute:: with_roles_history

        Whether to define two additional fields
        :attr:`Role.start_date` and :attr:`Role.end_date`.

    .. attribute:: use_vcard_export

        Whether Lino should provide a button for exporting contact
        data as a vcf file.

        If you set this to `True`, then you must install `vobject
        <http://eventable.github.io/vobject/>`__ into your Python
        environment::

              pip install vobject



User roles
==========

.. class:: SimpleContactsUser

   A user who has access to basic contacts functionality.

.. class:: ContactsUser

   A user who has access to full contacts functionality.

.. class:: ContactsStaff

   A user who can configure contacts functionality.

Filtering partners
==================

.. class:: PartnerEvents

    A choicelist of observable partner events.

    .. attribute:: has_open_movements

      See :ref:`has_open_movements` in :ref:`xl.specs.ledger`.
      This choice exists only when :mod:`lino_xl.lib.ledger` is installed.

Other models
============

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

    A **role** is when a given **person** exercises a given
    **function** (:class:`ContactType`) in a given **organization**.

    .. attribute:: company

        The organization where this person has this role.

    .. attribute:: type

        The function of this person in this organization.

    .. attribute:: person

        The person having this role in this organization.

        This is a learning foreign key. See `Automatically creating contact persons`_

    .. attribute:: start_date

        When this person started to exercise this function in this
        organization.

        This is a dummy field when :attr:`Plugin.with_roles_history`
        is `False`.

    .. attribute:: end_date

        When this person stopped to exercise this function in this
        organization.

        This is a dummy field when :attr:`Plugin.with_roles_history`
        is `False`.


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


Civil state
===========

>>> from lino_xl.lib.contacts.choicelists import CivilStates
>>> show_choicelist(CivilStates)
======= ==================== ==================== ============================= =============================
 value   name                 en                   de                            fr
------- -------------------- -------------------- ----------------------------- -----------------------------
 10      single               Single               Ledig                         célibataire
 20      married              Married              Verheiratet                   marié
 30      widowed              Widowed              Verwitwet                     veuf/veuve
 40      divorced             Divorced             Geschieden                    divorcé
 50      separated            Separated            Getrennt von Tisch und Bett   Séparé de corps et de biens
 51      separated_de_facto   De facto separated   Faktisch getrennt             Séparé de fait
 60      cohabitating         Cohabitating         Zusammenwohnend               Cohabitant
======= ==================== ==================== ============================= =============================
<BLANKLINE>



.. class:: CivilStates

    The global list of **civil states** that a person can have.  The
    field pointing to this list is usually named :attr:`civil_state`.

    Usage examples are
    :class:`lino_welfare.modlib.pcsw.models.Client>` and
    :class:`lino_tera.lib.tera.Client>` and
    :class:`lino_avanti.lib.avanti.Client>` .

    **The four official civil states** according to Belgian law are:

    .. attribute:: single

        célibataire : vous n’avez pas de partenaire auquel vous êtes
        officiellement lié

    .. attribute:: married

        marié(e) : vous êtes légalement marié

    .. attribute:: widowed

        veuf (veuve) / Verwitwet : vous êtes légalement marié mais
        votre partenaire est décédé

    .. attribute:: divorced

        divorcé(e) (Geschieden) : votre mariage a été juridiquement dissolu

    **Some institutions define additional civil states** for people
    who are officially still married but at different degrees of
    separation:

    .. attribute:: de_facto_separated

        De facto separated (Séparé de fait, faktisch getrennt)

        Des conjoints sont séparés de fait lorsqu'ils ne respectent
        plus le devoir de cohabitation. Leur mariage n'est cependant
        pas dissous.

        La notion de séparation de fait n'est pas définie par la
        loi. Toutefois, le droit en tient compte dans différents
        domaines, par exemple en matière fiscale ou en matière de
        sécurité sociale (assurance maladie invalidité, allocations
        familiales, chômage, pension, accidents du travail, maladies
        professionnelles).

    .. attribute:: separated

        Legally separated, aka "Separated as to property" (Séparé de
        corps et de biens, Getrennt von Tisch und Bett)

        La séparation de corps et de biens est une procédure
        judiciaire qui, sans dissoudre le mariage, réduit les droits
        et devoirs réciproques des conjoints.  Le devoir de
        cohabitation est supprimé.  Les biens sont séparés.  Les
        impôts sont perçus de la même manière que dans le cas d'un
        divorce. Cette procédure est devenue très rare.

    **Another unofficial civil state** (but relevant in certain
    situations) is:

    .. attribute:: cohabitating

        Cohabitating (cohabitant, zusammenlebend)

        Vous habitez avec votre partenaire et c’est
        reconnu légalement.

    Sources for above: `belgium.be
    <http://www.belgium.be/fr/famille/couple/divorce_et_separation/separation_de_fait/>`__,
    `gouv.qc.ca
    <http://www4.gouv.qc.ca/EN/Portail/Citoyens/Evenements/separation-divorce/Pages/separation-fait.aspx>`__,
    `wikipedia.org <https://en.wikipedia.org/wiki/Cohabitation>`__

.. _specs.contacts.learningfk:

Automatically creating contact persons
======================================

The :attr:`Role.person` field
in the :class:`RolesByCompany` table
is a :term:`Learning foreign key` field:
if you type the name of a person that
does not yet exist in the database, Lino creates it silently.

Some examples of how the name is parsed when creating a person:

>>> pprint(rt.models.contacts.Person.parse_to_dict("joe smith"))
{'first_name': 'Joe', 'last_name': 'Smith'}

>>> pprint(rt.models.contacts.Person.parse_to_dict("Joe W. Smith"))
{'first_name': 'Joe W.', 'last_name': 'Smith'}

>>> pprint(rt.models.contacts.Person.parse_to_dict("Joe"))
Traceback (most recent call last):
...
django.core.exceptions.ValidationError: ['Cannot find first and last name in "Joe"']

>>> pprint(rt.models.contacts.Person.parse_to_dict("Guido van Rossum"))
{'first_name': 'Guido', 'last_name': 'van Rossum'}

The algorithm has already some basic intelligence but plenty of growing potential...
