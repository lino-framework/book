.. _lino.tested.gfks:

====================
Generic Foreign Keys
====================

This document tests some functionalities implemented by
:mod:`lino.modlib.gfks`.


.. to run only this test:

    $ doctest docs/tested/gfks.rst
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.docs.settings.doctests')
    >>> from lino.api.doctest import *



The detail view of :class:`lino.modlib.gfks.ContentTypes` has the
following fields:

>>> d = get_json_dict('robin', 'gfks/ContentTypes/9')
>>> sorted(d.keys())
[u'data', u'disable_delete', u'id', u'navinfo', u'title']
>>> rmu(sorted(d['data'].keys()))
['app_label', 'base_classes', 'disable_editing', 'disabled_fields', 'id', 'model']
>>> for k in sorted(d['data'].keys()):
...    print k, ":", rmu(d['data'][k])
app_label : countries
base_classes : <p />
disable_editing : False
disabled_fields : {'id': True}
id : 9
model : country
