.. doctest docs/dev/choicelists.rst
.. _dev.choicelists:

===========================
Introduction to choicelists
===========================

A **choice list** is an ordered in-memory list of *choices*.
Each choice has a *value*, a *text* and a optionally a *name*.
The **value** of a choice is what is stored in the database.
The **text** is what the user sees.  It is usually translatable.
The **name** can be used to refer to a given choice from program code.

Whenever in *plain Django* you use a `choices` attribute on a database
field, in Lino you probably prefer using a :class:`ChoiceList` instead.

You can use a choicelist for much more than filling the :attr:`choices`
attribute of a database field.  You can display a choicelist as a table (using
:meth:`show <lino.core.requests.BaseRequest.show>` in a doctest or by adding it
to the main menu).  You can refer to individual choices programmatically using
their :attr:`name`.  You can subclass the choices and add application logic.


.. currentmodule:: lino.core.choicelists

.. contents::
    :depth: 1
    :local:

.. include:: /../docs/shared/include/tested.rst

The examples in this document use the :mod:`lino_book.projects.min2` project.

>>> from lino import startup
>>> startup('lino_book.projects.min2.settings.demo')
>>> from lino.api.doctest import *
>>> from django.utils import translation

Examples
========

For example Lino's calendar plugin (:mod:`lino_xl.lib.cal`) defines a
choicelist :class:`Weekdays <lino_xl.lib.cal.Weekdays>`, which has 7
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
Like every actor, choicelists are **never instantiated**.
They are just the class object itself and as such globally available

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
```app_label.ListName`` to resolve them:

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

Each choice has a "value", a "text" and (optionally) a "name".

The **value** is what gets stored when this choice is assigned to a
database field. It must be unique because it is the analog of primary
key.

>>> [g.value for g in Genders.objects()]
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


>>> [g.name for g in Genders.objects()]
['male', 'female']

>>> [d.name for d in Weekdays.objects()]
['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


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

A choicelist field is similar to a :class:`ForeignKey` field in that it uses a
:doc:`combo box </dev/combo/index>` as widget, but instead of pointing to a
database object it points to a :class:`Choice`.  For the underlying database it
is actually a `CharField` which contains the `value` (not the `name`) of its
choice.


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


A ChoiceList has an :meth:`get_list_items` method which returns an iterator
over its choices:

>>> print(Genders.get_list_items())
[<Genders.male:M>, <Genders.female:F>]

Note that :meth:`objects` is a deprecated alias for :meth:`get_list_items`.


Customizing choicelists
=======================

When we say that choicelists are "constant" or "hard-coded", then we
should add "for a given Lino site".  They can be modified either by a
child application or locally by the system administrator.

See :attr:`workflows_module <lino.core.site.Site.workflows_module>`
and :attr:`user_types_module <lino.core.site.Site.user_types_module>`.

Sorting choicelists
===================

Lino displays the choices of a choicelist in a combobox in their natural order
of how they have been added to the list.

You can explicitly call :meth:`Choicelist.sort` to sort them. This makes sense
e.g. in :mod:`lino_presto.lib.ledger` where we add a new journal group "Orders"
which we want to come before any other journal groups.

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




Seeing all choicelists in your application
==========================================

>>> from lino.core.kernel import choicelist_choices
>>> pprint(choicelist_choices())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
[('about.TimeZones', 'about.TimeZones (Time zones)'),
 ('cal.AccessClasses', 'cal.AccessClasses (Access classes)'),
 ('cal.DisplayColors', 'cal.DisplayColors (Display colors)'),
 ('cal.DurationUnits', 'cal.DurationUnits'),
 ('cal.EntryStates', 'cal.EntryStates (Entry states)'),
 ('cal.EventEvents', 'cal.EventEvents (Observed events)'),
 ('cal.GuestStates', 'cal.GuestStates (Presence states)'),
 ('cal.PlannerColumns', 'cal.PlannerColumns (Planner columns)'),
 ('cal.Recurrencies', 'cal.Recurrencies'),
 ('cal.ReservationStates', 'cal.ReservationStates (States)'),
 ('cal.TaskStates', 'cal.TaskStates (Task states)'),
 ('cal.Weekdays', 'cal.Weekdays'),
 ('cal.YearMonths', 'cal.YearMonths'),
 ('checkdata.Checkers', 'checkdata.Checkers (Data checkers)'),
 ('contacts.CivilStates', 'contacts.CivilStates (Civil states)'),
 ('contacts.PartnerEvents', 'contacts.PartnerEvents (Observed events)'),
 ('countries.PlaceTypes', 'countries.PlaceTypes'),
 ('printing.BuildMethods', 'printing.BuildMethods'),
 ('system.Genders', 'system.Genders'),
 ('system.PeriodEvents', 'system.PeriodEvents (Observed events)'),
 ('system.YesNo', 'system.YesNo (Yes or no)'),
 ('users.UserTypes', 'users.UserTypes (User types)'),
 ('xl.Priorities', 'xl.Priorities (Priorities)')]

The :attr:`lino_xl.lib.properties.PropType.choicelist` field uses this function
for its choices.
