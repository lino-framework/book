.. doctest docs/specs/addresses.rst
.. _specs.addresses:

==============================================
``addresses`` : Multiple addresses per partner
==============================================

.. currentmodule:: lino_xl.lib.addresses

The :mod:`lino_xl.lib.addresses` plugin adds  functionality and models to handle
multiple addresses per :class:`lino_xl.lib.contacts.Partner`. When this plugin
is installed, your application gets a "Manage addresses" button per partner.


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q

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
=================================== ==================== ======== ===================================================== ========= ==================
<BLANKLINE>

The primary address is show in the partner's :attr:`overview
<lino_xl.lib.contacts.Partner.overview>` field:

>>> obj = contacts.Partner.objects.get(name="Arens Andreas")
>>> print(to_rst(contacts.Partners.request().get_data_value(obj, 'overview')))
See as Organisation, **Partner**, Household
**Arens Andreas**
Akazienweg
4700 Eupen[Manage addresses]
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

    Inherits fields from
    :class:`lino_xl.lib.countries.CountryRegionCity` (country, region,
    city. zip_code) and :class:`lino_xl.lib.contacts.AddresssLocation`
    (street, street_no, ...)

    .. attribute:: partner

    .. attribute:: address_type

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

.. class:: AddressOwnerChecker

    Checks for the following data problems:

    - :message:`Unique address is not marked primary.` --
      if there is exactly one :class:`Address` object which just fails to
      be marked as primary, mark it as primary and return it.

    - :message:`Non-empty address fields, but no address record.`
      -- if there is no :class:`Address` object, and if the
      :class:`Partner` has some non-empty address field, create an
      address record from these, using `AddressTypes.official` as
      type.
