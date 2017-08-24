.. _avanti.specs.avanti:

=================================
Clients in Lino Avanti
=================================

.. How to test just this document:

    $ python setup.py test -s tests.SpecsTests.test_avanti_avanti
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *


.. contents::
  :local:

.. currentmodule:: lino_avanti.lib.avanti


Clients
=======

.. class:: Client(lino.core.model.Model)
           
    A **client** is a person using our services.

    .. attribute:: overview

        A panel with general information about this client.

    .. attribute:: client_state
    
        Pointer to :class:`ClientStates`.

    .. attribute:: unemployed_since

       The date when this client got unemployed and stopped to have a
       regular work.

    .. attribute:: seeking_since

       The date when this client registered as unemployed and started
       to look for a new job.

    .. attribute:: work_permit_suspended_until

    .. attribute:: city

       The place (village or municipality) where this client lives.
       
       This is a pointer to a
       :class:`lino_xl.lib.countries.Place`.

    .. attribute:: municipality

       The *municipality* where this client lives. This is basically
       equal to :attr:`city`, except when :attr:`city` is a *village*
       and has a parent which is a *municipality* (which causes that
       place to be returned).
           
.. class:: ClientDetail

.. class:: Clients
    Base class for most lists of clients.

    .. attribute:: client_state

        If not empty, show only Clients whose `client_state` equals
        the specified value.


.. class:: AllClients(Clients)

   This table is visible for Explorer who can also export it.

   For privacy reasons this table shows only a very limited set of
   fields. For example the names are hidden. OTOH it includes the
   :attr:`municipality <lino_avanti.lib.avanti.Client.municipality>`
   virtual field.


>>> show_columns(avanti.AllClients)
+-------------------+------------------------+-----------------------------------------------+
| Internal name     | Verbose name           | Help text                                     |
+===================+========================+===============================================+
| client_state      | State                  |                                               |
+-------------------+------------------------+-----------------------------------------------+
| starting_reason   | Starting reason        |                                               |
+-------------------+------------------------+-----------------------------------------------+
| ending_reason     | Ending reason          |                                               |
+-------------------+------------------------+-----------------------------------------------+
| city              | City                   | A pointer to the Place which is used as city. |
+-------------------+------------------------+-----------------------------------------------+
| municipality      | Municipality           |                                               |
+-------------------+------------------------+-----------------------------------------------+
| country           | Country                |                                               |
+-------------------+------------------------+-----------------------------------------------+
| zip_code          | Zip code               |                                               |
+-------------------+------------------------+-----------------------------------------------+
| nationality       | Nationality            | The nationality. This is a pointer to         |
|                   |                        | countries.Country which should                |
|                   |                        | contain also entries for refugee statuses.    |
+-------------------+------------------------+-----------------------------------------------+
| gender            | Gender                 | The sex of this person (male or female).      |
+-------------------+------------------------+-----------------------------------------------+
| birth_country     | Birth country          |                                               |
+-------------------+------------------------+-----------------------------------------------+
| in_belgium_since  | Lives in Belgium since | Uncomplete dates are allowed, e.g.            |
|                   |                        | "00.00.1980" means "some day in 1980",        |
|                   |                        | "00.07.1980" means "in July 1980"             |
|                   |                        | or "23.07.0000" means "on a 23th of July".    |
+-------------------+------------------------+-----------------------------------------------+
| needs_work_permit | Needs work permit      |                                               |
+-------------------+------------------------+-----------------------------------------------+
| translator_type   | Translator type        |                                               |
+-------------------+------------------------+-----------------------------------------------+
| mother_tongues    | Mother tongues         |                                               |
+-------------------+------------------------+-----------------------------------------------+
| cef_level_de      | None                   |                                               |
+-------------------+------------------------+-----------------------------------------------+
| cef_level_fr      | None                   |                                               |
+-------------------+------------------------+-----------------------------------------------+
| cef_level_en      | None                   |                                               |
+-------------------+------------------------+-----------------------------------------------+
| user              | Primary coach          |                                               |
+-------------------+------------------------+-----------------------------------------------+
| event_policy      | Recurrency policy      |                                               |
+-------------------+------------------------+-----------------------------------------------+

   
           
.. class:: ClientsByNationality(Clients)


.. class:: Residence(lino.core.model.Model)
           

>>> # rt.show('avanti.Clients')
