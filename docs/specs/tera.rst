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

>>> dd.is_installed('addresses')
False


Time tracking (Dienstleistungen)
================================

Lino Tera doesn't use *time tracking* like :ref:`noi`.


Partners
========

(The following is maybe obsolete)

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
<class 'lino_tera.lib.tera.models.Client'>

>>> dd.plugins.contacts
lino_tera.lib.contacts (extends_models=['Partner', 'Person', 'Company'])

>>> print([m.__name__ for m in rt.models_by_base(rt.models.contacts.Partner)])
['Company', 'Partner', 'Person', 'Household', 'List', 'Client']


Therapeutical groups
====================

>>> dd.plugins.lists
lino_tera.lib.lists (extends_models=['List'])

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


.. _presto.specs.teams:

Teams
=====

>>> rt.show(teams.Teams)
============= ================== ==================
 Designation   Designation (de)   Designation (fr)
------------- ------------------ ------------------
 Eupen
 St.Vith
============= ================== ==================
<BLANKLINE>


The following just repeats on the first payment order what has been
done for all orders when :mod:`lino_xl.lib.finan.fixtures.demo`
generated them:

>>> from unipath import Path
>>> from lino.utils.xmlgen.sepa.validate import validate_pain001
>>> ses = rt.login()
>>> obj = rt.models.finan.PaymentOrder.objects.all()[0]
>>> rv = obj.write_xml.run_from_session(ses)  #doctest: +ELLIPSIS
xml render <django.template.backends.jinja2.Template object at ...> -> .../media/xml/xml/finan.PaymentOrder-54.xml ('en', {})

>>> rv['success']
True
>>> print(rv['open_url'])
/media/xml/xml/finan.PaymentOrder-54.xml

>>> fn = Path(settings.SITE.cache_dir + rv['open_url'])
>>> fn.exists()
True

>>> validate_pain001(fn)
