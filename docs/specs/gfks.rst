.. doctest docs/specs/gfks.rst
.. _book.specs.gfks:

=========================================
Some internals about Generic Foreign Keys
=========================================

..
    >>> from lino import startup
    >>> startup('lino_book.projects.min9.settings.doctests')
    >>> from lino.api.doctest import *


The :func:`gfk2lookup` function
===============================

The :func:`gfk2lookup <lino.core.gfks.gfk2lookup>` function is mostly
internal use, but occasionally you might want to use it.

>>> from lino.core.utils import full_model_name as fmn
>>> from lino.core.gfks import gfk2lookup
>>> from lino.modlib.gfks.mixins import Controllable

List of models which inherit from :class:`Controllable
<lino.modlib.gfks.mixins.Controllable>`:

>>> print(' '.join([fmn(m) for m in rt.models_by_base(Controllable)]))
cal.Event cal.Task checkdata.Problem comments.Comment excerpts.Excerpt notes.Note notify.Message uploads.Upload

>>> obj = contacts.Person.objects.all()[0]
>>> d = gfk2lookup(notes.Note.owner, obj)
>>> d['owner_type']
<ContentType: Person>
>>> d['owner_id']
201

{'owner_type': <ContentType: Person>, 'owner_id': 201}

If the object has a non-integer primary key, then it cannot be target
of a GFK.  In this case we filter only on the content type because
anyway the list will be empty.  `countries.Country` is actually the
only model with a non-integer primary key.

>>> obj = countries.Country.objects.all()[0]
>>> gfk2lookup(notes.Note.owner, obj)
{'owner_type': <ContentType: Country>}
