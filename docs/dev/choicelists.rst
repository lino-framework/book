.. doctest docs/dev/choicelists.rst
.. _dev.choicelists:

===========================
Introduction to choicelists
===========================

.. contents::
    :depth: 1
    :local:

Overview
========


Whenever in *plain Django* you use a `choices` attribute on a database
field, in Lino you probably prefer using a :class:`ChoiceList
<lino.core.choicelists.ChoiceList>` instead.

A :class:`ChoiceList <lino.core.choicelists.ChoiceList>` is a constant
ordered in-memory list of choices.  Each of these choices has a
"value", a "text" and a optionally a "name".  The `text` of a choice
is usually translatable.

You can use a choicelist for much more than filling the
:attr:`choices` attribute of a database field.  You can display a
choicelist as a table using :meth:`show
<lino.core.requests.BaseRequest.show>`.  You can refer to individual
items programmatically using their :attr:`name`.  You can subclass the
choices and add application logic.


Examples
========

For the examples in this document we use the
:mod:`lino_book.projects.min2` project.

>>> from lino import startup
>>> startup('lino_book.projects.min2.settings.demo')
>>> from lino.api.doctest import *
    
For example Lino's calendar plugin (:mod:`lino_xl.lib.cal`) defines a
choicelist :class:`Weekdays <lino_xl.lib.cal.Weekdays>` which has 7
choices, one for each day of the week.

>>> rt.show('cal.Weekdays')
======= =========== ===========
 value   name        text
------- ----------- -----------
 1       monday      Monday
 2       tuesday     Tuesday
 3       wednesday   Wednesday
 4       thursday    Thursday
 5       friday      Friday
 6       saturday    Saturday
 7       sunday      Sunday
======= =========== ===========
<BLANKLINE>


Another example is the :class:`Genders
<lino.modlib.system.choicelists.Genders>` choicelist defined in the
:mod:`lino.modlib.system` plugin.
 
>>> rt.show('system.Genders')
======= ======== ========
 value   name     text
------- -------- --------
 M       male     Male
 F       female   Female
======= ======== ========
<BLANKLINE>



Accessing choicelists
=====================

ChoiceLists are **actors**.
Like every actor, choicelists are **never instantiated**. They are
just the class object itself and as such globally available

You can either import them or use :data:`lino.api.rt.models` to access
them (see :ref:`dev.accessing.plugins` for the difference):

>>> rt.models.cal.Weekdays
lino_xl.lib.cal.choicelists.Weekdays

>>> from lino_xl.lib.cal.choicelists import Weekdays
>>> Weekdays
lino_xl.lib.cal.choicelists.Weekdays

>>> Weekdays is rt.models.cal.Weekdays
True

>>> from lino.modlib.system.choicelists import Genders
>>> Genders is rt.models.system.Genders
True


You can also write code that dynamically resolves a string of type
`app_label.ListName` to resolve them:

>>> rt.models.resolve('cal.Weekdays') is Weekdays
True


Defining choicelists
====================

Here is how the :class:`lino_xl.lib.cal.Weekdays` choicelist has been
defined::

    class Weekdays(dd.ChoiceList):
        verbose_name = _("Weekday")

    add = Weekdays.add_item
    add('1', _('Monday'), 'monday')
    add('2', _('Tuesday'), 'tuesday')
    ...

This is the easiest case.

More complex examples, including choicelists with extended choices:

- :class:`lino.modlib.users.UserTypes`

Accessing individual choices
============================

Each row of a choicelist is a **choice**, more precisely an instance
of :class:`lino.core.choicelists.Choice` or a subclass thereof.

Each Choice has a "value", a "text" and a (optionally) "name".

The **value** is what gets stored when this choice is assigned to a
database field. It must be unique because it is the analog of primary
key.

>>> [rmu(g.value) for g in Genders.objects()]
['M', 'F']


The **text** is what the user sees.  It is a translatable string,
implemented using Django's i18n machine:

>>> Genders.male.text.__class__  #doctest: +ELLIPSIS
<class 'django.utils.functional....__proxy__'>

Calling :func:`str` of a choice is (usually) the same as calling
:func:`str` on its `text` attribute:

>>> [str(g) for g in Genders.objects()]
['Male', 'Female']

The text of a choice depends on the current user language.

>>> from django.utils import translation
>>> with translation.override('fr'):
...     [str(g) for g in Genders.objects()]
['Masculin', 'F\xe9minin']

>>> with translation.override('de'):
...     [str(g) for g in Genders.objects()]
['M\xe4nnlich', 'Weiblich']

>>> with translation.override('et'):
...     [str(g) for g in Genders.objects()]
['Mees', 'Naine']


The text of a choice is a **translatable** string, while *value* and
*name* remain **unchanged**:

>>> with translation.override('fr'):
...     rt.show('cal.Weekdays')
======= =========== ==========
 value   name        text
------- ----------- ----------
 1       monday      Lundi
 2       tuesday     Mardi
 3       wednesday   Mercredi
 4       thursday    Jeudi
 5       friday      Vendredi
 6       saturday    Samedi
 7       sunday      Dimanche
======= =========== ==========
<BLANKLINE>


Named choices
=============

A choice can optionally have a **name**, which makes it accessible as
class attributes on its choicelist so that application code can refer
to this particular choice.

>>> Weekdays.monday
<Weekdays.monday:1>

>>> Genders.male
<Genders.male:M>


>>> rmu([g.name for g in Genders.objects()])
['male', 'female']

>>> rmu(' '.join([d.name for d in Weekdays.objects()]))
'monday tuesday wednesday thursday friday saturday sunday'



Choicelist fields
=================

You use the :class:`Weekdays` choicelist in a model definition as
follows::

    from lino_xl.lib.cal.choicelists import Weekdays

    class WeeklyEvent(dd.Model):
        ...
        day_of_week = Weekdays.field(default=Weekdays.monday)

This adds a database field whose value is an instance of
:class:`lino.core.choicelists.Choice`.

A choicelist field is like a :class:`ForeignKey` field, but instead of
pointing to a database object it points to a :class:`Choice`.  For the
underlying database it is actually a `CharField` which contains the
`value` (not the `name`) of its choice.




The :class:`lino.mixins.human.Human` mixin uses the :class:`Genders
<lino.modlib.system.choicelists.Genders>` choicelist as follows::

    class Human(Model):
        ...
        gender = Genders.field(blank=True)

Because :class:`lino_xl.lib.contacts.Person` inherits from
:class:`Human`, you can use this when you want to select all men:

>>> Person = rt.models.contacts.Person       
>>> list(Person.objects.filter(gender=Genders.male))
... # doctest: +ELLIPSIS
[Person #114 ('Mr Hans Altenberg'), Person #112 ('Mr Andreas Arens'), ...]


A ChoiceList has an `objects` method (not attribute) which returns an
iterator over its choices:

>>> print(Genders.objects())
[<Genders.male:M>, <Genders.female:F>]


Customizing choicelists
=======================

When we say that choicelists are "constant" or "hard-coded", then we
should add "for a given Lino site".  They can be modified either by a
child application or locally by the system administrator.

See :attr:`workflows_module <lino.core.site.Site.workflows_module>`
and :attr:`user_types_module <lino.core.site.Site.user_types_module>`.
      
Miscellaneous
=============

Comparing Choices uses their *value* (not the *name* nor *text*):

>>> UserTypes = rt.models.users.UserTypes

>>> UserTypes.admin > UserTypes.user
True
>>> UserTypes.admin == '900'
True
>>> UserTypes.admin == 'manager'
False
>>> UserTypes.admin == ''
False







