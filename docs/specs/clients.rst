.. doctest docs/specs/clients.rst
.. _specs.clients:

========================
The ``clients`` plugin
========================

..
    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db.models import Q


The :mod:`lino_xl.lib.clients` plugin adds the notions of clients and
client contacts.


.. contents::
  :local:



.. currentmodule:: lino_xl.lib.clients
                   

Database structure
==================


.. class:: ClientContactBase

    Also used by :class:`aids.RefundPartner
    <lino_welfare.modlib.aids.models.RefundPartner>`.


.. class:: ClientBase

    Base class for a client. The model specified as
    :attr:`client_model <Plugin.client_model>` must implement this.

    .. attribute:: client_state

        Pointer to ClientStates

           
.. class:: ClientStates
           
    The list of **client states**.
    
    >>> rt.show(clients.ClientStates)
    ======= ========== ============
     value   name       text
    ------- ---------- ------------
     10      newcomer   Newcomer
     20      coached    Registered
     25      inactive   Inactive
     30      former     Ended
     40      refused    Abandoned
    ======= ========== ============
    <BLANKLINE>
    
    
.. class:: ClientEvents

    The list of **observable client events**.

    >>> rt.show(clients.ClientEvents)
    ========== ========== ==========
     value      name       text
    ---------- ---------- ----------
     created    created    Created
     modified   modified   Modified
     note       note       Note
    ========== ========== ==========
    <BLANKLINE>

    .. attribute:: created
                   
        Select clients whose record has been *created* during the observed
        period.
                   
    .. attribute:: modified
                   
        The choice for :class:`ClientEvents` which selects clients whose
        main record has been *modified* during the observed period.


           
.. class:: ClientContact


    A **client contact** is when a given partner has a given role for
    a given client.

    .. attribute:: client

        The :class:`Client`.

    .. attribute:: type
    
        The type of contact. Pointer to :class:`ClientContactType`.

    .. attribute:: company

        The organization.

    .. attribute:: contact_person
    
        The contact person in the organization.

    .. attribute:: contact_role
    
        The role of the contact person in the organization.

           
.. class:: ClientContactType
           
    A **client contact type** is the type or "role" which must be
    specified for a given :class:`ClientContact`.

    .. attribute:: can_refund

    Whether persons of this type can be used as doctor of a refund
    confirmation. Injected by :mod:`lino_welfare.modlib.aids`.

           
Configuration
=============

.. class:: Plugin

    .. attribute:: client_model = 'contacts.Person'

       The model to which :attr:`ClientContact.client` points to.



Injects
=======

The :mod:`lino_xl.lib.clients` plugin injects the following fields
into models of other plugins.

.. currentmodule:: lino.modlib

    
.. class:: contacts.Partner
    :noindex:

    .. attribute:: client_contact_type
