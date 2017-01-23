.. _book.specs.gfks:

=========================================
Some internals about Generic Foreign Keys
=========================================

.. to test just this doc:

    $ python setup.py test -s tests.SpecsTests.test_gfks

    >>> from lino import startup
    >>> startup('lino_book.projects.min2.settings.doctests')
    >>> from lino.api.doctest import *


The :func:`gfk2lookup` function
===============================

The :func:`gfk2lookup <lino.core.utils.gfk2lookup>` function is mostly
internal use, but occasionally you might want to use it.

>>> from lino.core.utils import full_model_name as fmn
>>> from lino.core.gfks import gfk2lookup
>>> from lino.modlib.gfks.mixins import Controllable

List of models which inherit from :class:`Controllable
<lino.modlib.gfks.mixins.Controllable>`:

>>> print(' '.join([fmn(m) for m in rt.models_by_base(Controllable)]))
cal.Event cal.Task excerpts.Excerpt notes.Note notify.Message plausibility.Problem

>>> obj = contacts.Person.objects.all()[0]
>>> gfk2lookup(notes.Note.owner, obj)
{'owner_type': <ContentType: Person>, 'owner_id': 201}

If the object has a non-integer primary key, then it cannot be target
of a GFK. In this case it is enough to filter on the content
type. Anyway the list will be empty.  `countries.Country` is actually
the only model with a non-integer primary key.

>>> obj = countries.Country.objects.all()[0]
>>> gfk2lookup(notes.Note.owner, obj)
{'owner_type': <ContentType: Country>}
