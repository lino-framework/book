.. _lino.tested.diamond:
.. _lino.tested.diamond2:

===================
Diamond inheritance
===================

This document summarizies some work done in Lino around diamond
inheritance, especially the problem described in Django ticket
:djangoticket:`10808`.

We have two projects for this:
:mod:`lino_book.projects.diamond` and
:mod:`lino_book.projects.diamond2`.

Models 1
========

.. literalinclude:: /../../book/lino_book/projects/diamond/main/models.py



Models 2
========

The difference with variant 1 is that now we have two abstract
parents.

.. literalinclude:: /../../book/lino_book/projects/diamond2/main/models.py

   
The problem
===========

>> from main.models import PizzeriaBar
>> p = PizzeriaBar(name="A", min_age="B", specialty="C",
...     pizza_bar_specific_field="Doodle")

Despite the fact that we specify a non-blank value for `name`, we get
a database object whose `name` is blank, while the
`pizza_bar_specific_field` field is not:

>> print(p.name)
<BLANKLINE>
>> print(p.pizza_bar_specific_field)
Doodle

                    
Lino has a work-around for this problem. But that workaround works
only until Django 1.10.  The corrresponding test case is skipped in
Django 1.11+ where Django raises a `django.core.exceptions.FieldError`
saying that "Local field u'street' in class 'PizzeriaBar' clashes with
field of the same name from base class 'Pizzeria'". This comes because
we additionally to :ref:`simple diamond inheritance
<lino.tested.diamond>` the `street` field is defined in *a parent of*
the common parent. Django then gets messed up when testing for
duplicate fields and incorrectly thinks that `street` is
duplicated. (TODO: verify whether this is a problem)
     


