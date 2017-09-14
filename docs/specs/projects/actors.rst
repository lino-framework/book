.. _specs.projects.actors:

======================
The label of the actor
======================


..  To test only this document, run::

       $ doctest docs/specs/projects/actors.rst

    doctest init:
    >>> from lino import startup
    >>> startup('lino_book.projects.actors.settings')
    >>> from lino.api.doctest import *
    >>> globals().update(rt.models.actors.__dict__)


This document describes the :mod:`lino_book.projets.actors` demo
project which shows different ways of specifying the label of an
actor.

It was started as a doctest for :blogref:`20130907`.


.. contents::
   :local:
   :depth: 2   

  
Here is the :xfile:`models.py` file we will use for this tutorial:

.. literalinclude:: ../../../lino_book/projects/actors/models.py
                    
.. literalinclude:: ../../../lino_book/projects/actors/desktop.py
  

The `label` of an Actor
-----------------------

If a Table has no explicit `label` attribute, then it 
takes the verbose_name_plural meta option of the model:

>>> print(Partners.label)
Partners
>>> print(Persons.label)
Persons

You may specify an explicit constant `label` attribute:

>>> print(FunnyPersons.label)
Funny persons

In versions after :blogref:`20130907` this explicit label attribute 
is also inherited to subclasses:

>>> print(MyFunnyPersons.label)
Funny persons


Dynamic actor labels
--------------------


>>> rt.show(PartnerType)
==== ===============
 ID   Name
---- ---------------
 1    Our customers
 2    Our providers
==== ===============
<BLANKLINE>


>>> print(Customers.label)
Our customers

>>> print(Providers.label)
Our providers


>>> rt.show(Partners)
==== =============== ==========
 ID   partner type    Name
---- --------------- ----------
 1    Our customers   Adams
 2    Our customers   Bowman
 3    Our providers   Carlsson
 4    Our customers   Dickens
==== =============== ==========
<BLANKLINE>

>>> rt.show(Customers)
==== =============== =========
 ID   partner type    Name
---- --------------- ---------
 1    Our customers   Adams
 2    Our customers   Bowman
 4    Our customers   Dickens
==== =============== =========
<BLANKLINE>

>>> rt.show(Providers)
==== =============== ==========
 ID   partner type    Name
---- --------------- ----------
 3    Our providers   Carlsson
==== =============== ==========
<BLANKLINE>
