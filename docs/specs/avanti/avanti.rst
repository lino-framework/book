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

           
.. class:: ClientDetail

.. class:: Clients
    Base class for most lists of clients.

    .. attribute:: client_state

        If not empty, show only Clients whose `client_state` equals
        the specified value.


.. class:: AllClients(Clients)

   This table is visible for Explorer who can export it.
           
.. class:: ClientsByNationality(Clients)


.. class:: Residence(lino.core.model.Model)
           
