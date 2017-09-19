.. _dev.choicelists:

===========================
Introduction to choicelists
===========================

.. To run only this test:

   $ doctest docs/dev/choicelists.rst

Whenever in *plain Django* you use a `choices` attribute on a database
field, in Lino you probably prefer using a :class:`ChoiceList
<lino.core.choicelists.ChoiceList>` instead.

A :class:`ChoiceList <lino.core.choicelists.ChoiceList>` is a constant
ordered list of translatable values.  You can use it for much more
than filling the `choices` attribute of a database field. You can
refer to individual items programmatically using a name. You can
subclass them and add application logic.  You can display a choicelist
as a table using :meth:`show <lino.core.requests.BaseRequest.show>`.

..
    >>> from lino import startup
    >>> startup('lino_book.projects.min2.settings.demo')
    >>> from lino.api.doctest import *
    
For example Lino's calendar plugin (:mod:`lino_xl.lib.cal`) defines a
choicelist :class:` <lino_xl.lib.cal.Weekdays>` which has 7 choices,
one for each day of the week.

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

Here is how the :class:`lino_xl.lib.cal.Weekdays` choicelist has been
defined::

    class Weekdays(dd.ChoiceList):
        verbose_name = _("Weekday")

    add = Weekdays.add_item
    add('1', _('Monday'), 'monday')
    add('2', _('Tuesday'), 'tuesday')
    ...
        
You use the Weekdays choicelists in a model definition as follows::

    from lino_xl.lib.cal.choicelists import Weekdays

    class WeeklyEvent(dd.Model):
        ...
        day_of_week = Weekdays.field(default=Weekdays.monday)


ChoiceLists are **actors**.  They are globally accessible in
:data:`rt.models`.

      
>>> rt.models.cal.Weekdays
lino_xl.lib.cal.choicelists.Weekdays

Like every Actor, ChoiceLists are **never instantiated**. They are
just the class object itself:

>>> from lino_xl.lib.cal.choicelists import Weekdays
>>> Weekdays is rt.models.cal.Weekdays
True




Accessing individual choices
============================

Each row of a choicelist is a choice. Individual choices can have a
*name*, which makes them accessible as **class attributes** on the
*choicelist* which own them:

>>> Weekdays.monday
<Weekdays.monday:1>


As another example, let's look at
the :class:`Genders <lino.modlib.system.choicelists.Genders>`
choicelist which is part of the :mod:`lino.modlib.system` plugin.
 
>>> from lino.modlib.system.choicelists import Genders

>>> rt.show(Genders)
======= ======== ========
 value   name     text
------- -------- --------
 M       male     Male
 F       female   Female
======= ======== ========
<BLANKLINE>

The :class:`lino.mixins.human.Human` mixin uses this as follows::

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

Each Choice has a "value", a "name" and a "text". 

The **value** is what gets stored when this choice is assigned to a
database field.

>>> [g.value for g in Genders.objects()]
[u'M', u'F']

The **name** is how Python code can refer to this choice.

>>> [g.name for g in Genders.objects()]
[u'male', u'female']

>>> print(repr(Genders.male))
<Genders.male:M>

The **text** is what the user sees.  It is a translatable string,
implemented using Django's i18n machine:

>>> Genders.male.text.__class__
<class 'django.utils.functional.__proxy__'>

Calling :func:`str` of a choice is (usually) the same as calling
unicode on its `text` attribute:

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


Comparing Choices uses their *value* (not the *name* nor *text*):

>>> UserTypes = rt.modules.users.UserTypes

>>> UserTypes.admin > UserTypes.user
True
>>> UserTypes.admin == '900'
True
>>> UserTypes.admin == 'manager'
False
>>> UserTypes.admin == ''
False







