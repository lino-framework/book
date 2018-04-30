.. doctest docs/tested/gfks.rst
.. _lino.tested.gfks:

====================
Generic Foreign Keys
====================

This document tests some functionalities implemented by
:mod:`lino.modlib.gfks`.


.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.docs.settings.doctests')
    >>> from lino.api.doctest import *



The detail view of :class:`lino.modlib.gfks.ContentTypes` has the
following fields:

>>> ct = contenttypes.ContentType.objects.get_for_model(countries.Country).id
>>> d = get_json_dict('robin', 'gfks/ContentTypes/{}'.format(ct))
>>> rmu(sorted(d.keys()))
['data', 'disable_delete', 'id', 'navinfo', 'title']
>>> rmu(sorted(d['data'].keys()))
['app_label', 'base_classes', 'disable_editing', 'disabled_fields', 'id', 'model']
>>> for k in sorted(d['data'].keys()):
...    print("{} : {}".format(k, rmu(d['data'][k])))  #doctest: +ELLIPSIS
app_label : countries
base_classes : <p />
disable_editing : False
disabled_fields : {'id': True}
id : ...
model : country
