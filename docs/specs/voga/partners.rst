.. doctest docs/specs/voga/partners.rst
.. _voga.specs.partners:

=====================
Partners in Lino Voga
=====================

..  doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *


Partners in Lino Voga are :class:`polymorphic
<lino.mixins.polymorphic.Polymorphic>`, i.e. the database has a series
of models which are more or less specialized subclasses of a partner.

In Lino Voga we differentiate the following subclasses of Partner:

.. django2rst:: contacts.Partner.print_subclasses_graph()


..
    >>> from lino.mixins.polymorphic import Polymorphic
    >>> issubclass(contacts.Person, Polymorphic)
    True
    >>> issubclass(contacts.Person, contacts.Partner)
    True
    >>> issubclass(courses.Pupil, contacts.Person)
    True
    >>> issubclass(courses.Teacher, contacts.Person)
    True
    >>> issubclass(courses.Teacher, contacts.Partner)
    True

    >>> print(noblanklines(contacts.Partner.get_subclasses_graph()))
    .. graphviz::
       digraph foo {
        "Partner" -> "Organization"
        "Partner" -> "Person"
        "Person" -> "Participant"
        "Person" -> "Instructor"
      }



Partner lists
=============

The demo database currently contains no data about partner lists.

>>> rt.show(lists.Members)
No data to display

>>> from django.utils.http import urlquote
>>> url = '/api/lists/Members?'
>>> url += 'limit=10&start=0&fmt=json&'
>>> url += "filter=" + urlquote('[{"type":"string","value":"3","field":"list"}]')
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200

>>> d = json.loads(res.content.decode())
>>> d['count']
1
>>> d['rows'][0]
[None, None, None, None, None, None, None, None, None, None, None, None, None]

