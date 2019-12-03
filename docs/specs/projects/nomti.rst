===================
Is MTI a bad thing?
===================

If you believe that multi-table inheritance "is a bad thing", then this example
shows how you would solve the same real-world problem as
:mod:`lino_book.projects.mti` by using OneToOneFields instead of MTI.


.. how to test just this document:
    $ python setup.py test -s tests.SpecsTests.test_projects_nomti

    doctest init:
    >>> from lino import startup
    >>> startup('lino_book.projects.nomti.settings')
    >>> from lino.api.doctest import *
    >>> Person = app.Person
    >>> Restaurant = app.Restaurant
    >>> Bar = app.Bar
    >>> Place = app.Place


The database models
-------------------

Here is the :file:`models.py` file used for this example.

We have a table of Places, some of them are Restaurants,
some are Pubs, and some are neither Pub nor Restaurant.


.. literalinclude:: /../../book/lino_book/projects/nomti/app/models.py


The demo data
-------------

Here are the **Persons** who act in our story:

>>> rt.show('app.Persons')
========
 name
--------
 Anne
 Bert
 Claude
 Dirk
 Ernie
 Fred
========
<BLANKLINE>

>>> rt.show('app.Places')
==== ===================== ======== ======================================
 ID   name                  person   owners
---- --------------------- -------- --------------------------------------
 1    Bert's pub            Anne     `Anne <Detail>`__, `Bert <Detail>`__
 2    The Chopping Shack    Bert     `Claude <Detail>`__
 3    The Abacus Well       Ernie    `Fred <Detail>`__
 4    The Olive Lounge      Bert     `Claude <Detail>`__
 5    The Autumn Bite       Ernie    `Fred <Detail>`__
 6    The Private Mission   Bert     `Claude <Detail>`__
 7    Nova                  Ernie    `Fred <Detail>`__
 8    Babylon               Bert     `Claude <Detail>`__
 9    Blossoms              Ernie    `Fred <Detail>`__
 10   Whisperwind           Bert     `Claude <Detail>`__
 11   Catch                 Ernie    `Fred <Detail>`__
==== ===================== ======== ======================================
<BLANKLINE>

>>> rt.show('app.Restaurants')
==== ========================================================= ================= ===================
 ID   place                                                     serves hot dogs   cooks
---- --------------------------------------------------------- ----------------- -------------------
 1    The Chopping Shack Restaurant (ceo=Bert,owners=Claude)    No                `Dirk <Detail>`__
 2    The Abacus Well Restaurant (ceo=Ernie,owners=Fred)        No                `Anne <Detail>`__
 3    The Olive Lounge Restaurant (ceo=Bert,owners=Claude)      No                `Dirk <Detail>`__
 4    The Autumn Bite Restaurant (ceo=Ernie,owners=Fred)        No                `Anne <Detail>`__
 5    The Private Mission Restaurant (ceo=Bert,owners=Claude)   No                `Dirk <Detail>`__
 6    Nova Restaurant (ceo=Ernie,owners=Fred)                   No                `Anne <Detail>`__
 7    Babylon Restaurant (ceo=Bert,owners=Claude)               No                `Dirk <Detail>`__
 8    Blossoms Restaurant (ceo=Ernie,owners=Fred)               No                `Anne <Detail>`__
 9    Whisperwind Restaurant (ceo=Bert,owners=Claude)           No                `Dirk <Detail>`__
 10   Catch Restaurant (ceo=Ernie,owners=Fred)                  No                `Anne <Detail>`__
==== ========================================================= ================= ===================
<BLANKLINE>
