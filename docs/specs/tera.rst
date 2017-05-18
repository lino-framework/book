.. _tera.specs:
.. _presto.specs.psico:

=============================
Lino Tera : a first overview
=============================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_tera
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *

**Lino Tera** (from Italian *terapia*, therapy) is a Lino application
designed to be used in a center for `sociopsychological
<https://en.wikipedia.org/wiki/Social_psychology>`_ consultations.

The demo project :mod:`lino_book.projects.lydia` is used for testing
the following document.

>>> settings.SETTINGS_MODULE
'lino_book.projects.lydia.settings.doctests'


All :ref:`tera` application have a :xfile:`settings.py` module which
inherits from :mod:`lino_tera.lib.tera.settings`.

>>> from lino_tera.lib.tera.settings import Site
>>> isinstance(settings.SITE, Site)
True


Time tracking (Dienstleistungen)
================================

Lino Psico uses *time tracking* like :ref:`noi`, but unlike :ref:`noi`
it does not have the notion of *tickets*.  When a psychologist starts
a session, they don't specify a *ticket* but a *person*.


>>> dd.is_installed('clocking')
True

>>> dd.is_installed('tickets')
False

The clocking
plugin has its own implementation specific to :ref:`tera`:

>>> dd.plugins.clocking
lino_tera.lib.clocking (extends_models=['Session'])

>>> print(dd.plugins.clocking.ticket_model)
<class 'lino_tera.lib.contacts.models.Person'>

Partners
========

In Lino Tera, the partner is the central database object.  Many
statistical reports are based on attributes of partners.

A partner is either a single person, a family, a household, or a group
of otherwise non-related partners having a same problem (called a
*therapeutic group*).

There might be (it is not yet decided) a differetiation between
"partner" and "dossier": a same partner can have more than one dossier
within the years. Currently they simply create the same partner a
second time (and add a field which connects them).

>>> print(settings.SITE.project_model)
<class 'lino_tera.lib.contacts.models.Partner'>

>>> dd.plugins.contacts
lino_presto.projects.psico.lib.contacts (extends_models=['Partner', 'Person', 'Company'])

>>> print([m.__name__ for m in rt.models_by_base(rt.models.contacts.Partner)])
['Company', 'Partner', 'Person', 'Household']


Therapeutical groups
====================

>>> dd.plugins.lists
lino_presto.projects.psico.lib.lists (extends_models=['List'])

>>> rt.show(lists.Lists)
=========== ========================= ===========
 Reference   Description               List Type
----------- ------------------------- -----------
             *Women's group 2014*
             *Men's group 2014*
             *Children's group 2014*
             *Women's group 2015*
             *Men's group 2015*
             *Children's group 2015*
             *Women's group 2016*
             *Men's group 2016*
             *Children's group 2016*
=========== ========================= ===========
<BLANKLINE>



>>> rt.show(teams.Teams)
============= ================== ==================
 Designation   Designation (de)   Designation (fr)
------------- ------------------ ------------------
 Eupen
 St.Vith
============= ================== ==================
<BLANKLINE>
