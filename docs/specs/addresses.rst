.. doctest docs/specs/addresses.rst
.. _specs.addresses:

==============================================
``addresses`` : Multiple addresses per partner
==============================================

.. currentmodule:: lino_xl.lib.addresses

The :mod:`lino_xl.lib.addresses` plugin adds functionality and models to handle
multiple addresses per :term:`partner`.  When this plugin is installed, your
application gets a "Manage addresses" button in the :attr:`overview` field of a
partner.  See also :ref:`team.mt.addresses`.


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q

.. glossary::

  address fields

    The database fields that make up a postal address. Here they are:

    >>> sorted(addresses.Address.ADDRESS_FIELDS)
    ['addr1', 'addr2', 'city', 'country', 'region', 'street', 'street_box', 'street_no', 'street_prefix', 'zip_code']

    Each partner object has these address fields, and each :term:`address
    record` has them.  The address fields of a partner always contain a copy of
    the partner's :term:`primary address`.

  address record

    One of possibly many addresses of a given partner.
    Stored using the :class:`Address` model.
    Implements :class:`lino.utils.addressable.Addressable`.

    Inherits fields from :class:`lino_xl.lib.countries.CountryRegionCity`
    (country, region, city. zip_code) and
    :class:`lino_xl.lib.contacts.AddresssLocation` (street, street_no, ...).

  primary address

    The address that is used as the primary address of a given partner.


Examples
========

>>> rt.show(addresses.Addresses)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=================================== ==================== ======== ===================================================== ========= ==================
 Partner                             Address type         Remark   Address                                               Primary   Data source
----------------------------------- -------------------- -------- ----------------------------------------------------- --------- ------------------
 Bäckerei Ausdemwald                 Official address              Vervierser Straße 45, 4700 Eupen                      Yes       Manually entered
 Bäckerei Ausdemwald                 Official address              Aachener Straße 1                                     No        Manually entered
 Bäckerei Mießen                     Official address              Gospert 103, 4700 Eupen                               Yes       Manually entered
 Bäckerei Mießen                     Unverified address            Akazienweg 2                                          No        Manually entered
 Arens Andreas                       Official address              Akazienweg, 4700 Eupen                                Yes       Manually entered
 Arens Andreas                       Declared address              Alter Malmedyer Weg 4                                 No        Manually entered
 Arens Annette                       Official address              Alter Malmedyer Weg, 4700 Eupen                       Yes       Manually entered
 Arens Annette                       Reference address             Am Bahndamm 5                                         No        Manually entered
 Ausdemwald Alfons                   Official address              Am Bahndamm, 4700 Eupen                               Yes       Manually entered
 Ausdemwald Alfons                   Obsolete                      Am Berg 7                                             No        Manually entered
 ...
 Denon Denis                         Official address              Paris, France                                         Yes       Manually entered
 Jeanémart Jérôme                    Official address              Paris, France                                         Yes       Manually entered
 AS Express Post                     Official address              Peterburi tee 34/5, 11415 Tallinn, Estonia            Yes       Manually entered
 AS Matsalu Veevärk                  Official address              Estonia                                               Yes       Manually entered
 Eesti Energia AS                    Official address              Estonia                                               Yes       Manually entered
 IIZI kindlustusmaakler AS           Official address              Estonia                                               Yes       Manually entered
 Maksu- ja Tolliamet                 Official address              Lõõtsa 8a, 15176 Tallinn, Estonia                     Yes       Manually entered
 Ragn-Sells AS                       Official address              Suur-Sõjamäe 50 a, 11415 Tallinn, Estonia             Yes       Manually entered
 Electrabel Customer Solutions       Official address              Boulevard Simón Bolívar 34, 1000 Brussels             Yes       Manually entered
 Ethias s.a.                         Official address              Rue des Croisiers 24, 4000 Liège                      Yes       Manually entered
 Leffin Electronics                  Official address              Schilsweg 80, 4700 Eupen                              Yes       Manually entered
=================================== ==================== ======== ===================================================== ========= ==================
<BLANKLINE>

The primary address is shown in the partner's :attr:`overview
<lino_xl.lib.contacts.Partner.overview>` field:

>>> obj = contacts.Partner.objects.get(name="Arens Andreas")
>>> print(to_rst(contacts.Partners.request().get_data_value(obj, 'overview')))
See as Organisation, **Partner**, Household
**Arens Andreas**
Akazienweg
4700 Eupen[Manage addresses]
`andreas@arens.com <mailto:andreas@arens.com>`__, +32 87123456 [Contact details]
<BLANKLINE>

When you click on [Manage addresses] you see:

>>> rt.show(addresses.AddressesByPartner, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
================== ======== ======================== =========
 Address type       Remark   Address                  Primary
------------------ -------- ------------------------ ---------
 Official address            Akazienweg, 4700 Eupen   Yes
 Declared address            Alter Malmedyer Weg 4    No
================== ======== ======================== =========
<BLANKLINE>

>>> rt.show(addresses.AddressTypes)
======= ============ ====================
 value   name         text
------- ------------ --------------------
 01      official     Official address
 02      unverified   Unverified address
 03      declared     Declared address
 04      reference    Reference address
 98      obsolete     Obsolete
 99      other        Other
======= ============ ====================
<BLANKLINE>

>>> rt.show(addresses.DataSources)
======= ========== ==================
 value   name       text
------- ---------- ------------------
 01      manually   Manually entered
 02      eid        Read from eID
======= ========== ==================
<BLANKLINE>



Reference
=========

.. class:: Address

    Django model to represent and address record.

    .. attribute:: partner

    .. attribute:: address_type

      The type of this address record.
      A pointer to :class:`AddressTypes`.
      The default value is :attr:`AddressTypes.official`.

    .. attribute:: data_source

        Pointer to :class:`DataSources`.

        Specifies how this information entered into our database.

    .. attribute:: primary

        Whether this address is the primary address of its owner.
        Setting this field will automatically uncheck any previousl
        primary addresses and update the owner's address fields.

.. class:: Addresses

  Shows all addresses in the database.

  Filter parameters:

  .. attribute:: partner

    Show only addresses of the given partner in :attr:`Address.partner`.

  .. attribute:: place

    Show only addresses having the given place in :attr:`Address.city`.

  .. attribute:: address_type

    Show only addresses having the given type.


.. class:: AddressesByPartner

  Shows all addresses of this partner.

.. class:: AddressOwner

    Base class for the "addressee" of any address.

    .. method:: get_primary_address()

      Return the primary address of this address owner.  If the owner has no
      direct address, look up the "address parent" and return its primary
      address.

    .. method:: get_address_by_type(address_type)

.. class:: AddressTypes

    A choicelist with all available address types.

    >>> rt.show(addresses.AddressTypes)
    ======= ============ ====================
     value   name         text
    ------- ------------ --------------------
     01      official     Official address
     02      unverified   Unverified address
     03      declared     Declared address
     04      reference    Reference address
     98      obsolete     Obsolete
     99      other        Other
    ======= ============ ====================
    <BLANKLINE>

.. class:: DataSources

    A choicelist with all available data sources.

    >>> rt.show(addresses.DataSources)
    ======= ========== ==================
     value   name       text
    ------- ---------- ------------------
     01      manually   Manually entered
     02      eid        Read from eID
    ======= ========== ==================
    <BLANKLINE>

.. _specs.addresses.AddressOwnerChecker:

Data check on addresses
=======================

The :class:`AddressOwnerChecker` detects inconsistencies between the address on
the owner (partner) and its collection of addresses.  Theoretically things are
easy: the partner's address fields contain a copy of the partner's primary
address.  But bugs and other circumstances can lead to inconsistencies. And when
you have thousands of addresses, you don't want to get bothered by problems that
might get fixed automatically. Quite sophisticated task though, because Lino
must not loose any data and must not "fix" problems for which actually a human
is needed.

.. class:: AddressOwnerChecker

    Checks for the data problems described below.

Here is a utility function used to describe and test the possible data problems
and how Lino handles them.  The remaining part of this section will call this
function over and over again.  For each test it creates a partner and a list of
addresses, then runs the data checker to detect problems, then prints the
problem message and a summary of the database content after fixing them before
cleaning up the database.  Most addresses have just a street name to simplify
things.

>>> from lino_xl.lib.contacts.utils import street2kw
>>> checker = rt.models.addresses.AddressOwnerChecker.self
>>> PK = 1234
>>> Partner = dd.plugins.addresses.partner_model
>>> Address = rt.models.addresses.Address
>>> def p(street="", **kwargs):
...     return Partner(pk=PK, name="x", **street2kw(street, **kwargs))
>>> def a(street="", primary=False, **kwargs):
...     return Address(primary=primary, **street2kw(street, **kwargs))
>>> def test(partner, *addresses):
...     # delete all db objects:
...     Address.objects.filter(partner_id=PK).delete()
...     Partner.objects.filter(id=PK).delete()
...     # store partner and addresses:
...     partner.save()
...     for a in addresses:
...         a.partner = partner
...         a.save()
...     for (fixable, msg) in checker.get_checkdata_problems(partner, fix=True):
...         print(("(*) " if fixable else "") + str(msg))
...     print(', '.join(Partner.objects.get(pk=PK).address_location_lines()))
...     for addr in Address.objects.filter(partner_id=PK):
...         print("- " + ("primary " if addr.primary else "") + ', '.join(addr.address_location_lines()))
...     Address.objects.filter(partner_id=PK).delete()
...     Partner.objects.filter(id=PK).delete()


>>> test(p("foo"))  #doctest: +NORMALIZE_WHITESPACE
(*) Primary address is missing.
foo
- primary foo

When the partner has some non-empty address field and there is no
:class:`Address` object that matches this address, Lino fixes this by creating
an address record from these.

>>> test(p("foo"), a("bar"))  #doctest: +NORMALIZE_WHITESPACE
(*) Primary address is missing.
foo
- bar
- primary foo

The :message:`Unique address is not marked primary.` means that  there is
exactly one :class:`Address` object which matches the partner and just fails to
be marked as primary, mark it as primary and return it.

>>> test(p("foo"), a("foo"))  #doctest: +NORMALIZE_WHITESPACE
(*) Unique address is not marked primary.
foo
- primary foo

Multiple primary addresses are not allowed.  If one of them matches the partner,
Lino can fix it by removing primary from the others:

>>> test(p("foo"), a("foo", True), a("bar", True))  #doctest: +NORMALIZE_WHITESPACE
(*) Multiple primary addresses.
foo
- primary foo
- bar

But if none of them matches the partner, Lino cannot fix the issue:

>>> test(p("foo"), a("bar", True), a("baz", True))  #doctest: +NORMALIZE_WHITESPACE
Multiple primary addresses.
foo
- primary bar
- primary baz


>>> test(p("foo"), a("bar", True))  #doctest: +NORMALIZE_WHITESPACE
Primary address differs from owner address (street:foo->bar).
foo
- primary bar

>>> test(p("foo"), a("", True))  #doctest: +NORMALIZE_WHITESPACE
(*) Must sync owner to address.
foo
- primary foo

When the only address is overwritable but not marked primary, Lino will set it
to primary.

>>> test(p("foo"), a(""))  #doctest: +NORMALIZE_WHITESPACE
(*) Must sync owner to address.
foo
- primary foo

Two addresses, but the wrong one is marked primary:

>>> test(p("foo"), a("bar", True), a("foo"))
(*) Matching address is not marked primary.
foo
- bar
- primary foo

When exactly one addresses matches the partner, it becomes primary and
potentially gets synchronized if it is incomplete.

>>> test(p("foo"), a("bar"), a("foo"))
(*) Matching address is not marked primary.
foo
- bar
- primary foo

>>> test(p("foo"), a("foo"), a("bar"))
(*) Matching address is not marked primary.
foo
- primary foo
- bar

When the address record just lacks some field, Lino can update it.

>>> test(p("foo", addr2="foo2"), a("foo"), a("bar"))
(*) Primary address is not complete
(*) Matching address is not marked primary.
foo, foo2
- primary foo, foo2
- bar

When no address record matches:

>>> test(p("foo"), a("bar"), a("baz"))
(*) Primary address is missing.
foo
- bar
- baz
- primary foo

When more than one address record matches:

>>> test(p("foo"), a("foo"), a("foo"))
No primary address, but matching addresses exist.
foo
- foo
- foo


The wrong address is marked as primary:

>>> test(p("foo"), a("foo"), a("bar"), a("baz", True))
(*) Matching address is not marked primary.
foo
- primary foo
- bar
- baz


When the partner's address is empty, we can have as many addresses as we want as
long as none of them is marked primary.

>>> test(p())
<BLANKLINE>
>>> test(p(""), a("bar"))  #doctest: +NORMALIZE_WHITESPACE
<BLANKLINE>
- bar
>>> test(p(""), a("foo"), a("bar"))  #doctest: +NORMALIZE_WHITESPACE
<BLANKLINE>
- foo
- bar
