.. _dev.virtualfields:

====================
About virtual fields
====================

.. glossary::

  database field

    A regular Django model field. CharField, ForeignKey, IntegerField,
    TextField, BooleanField, etc.

  virtual field

    A data element whose value isn't stored in the database but computed on the
    fly each time we want to see it.  For example the :attr:`age
    <lino.mixins.humans.Human.age>` of a person is usually computed from the
    :attr:`birth_data <lino.mixins.humans.Human.birth_data>`. It wouldn't make
    sense to store this number in the database.

Recipes
=======

Define a **virtual field on a model**::

    @dd.virtualfield(models.IntegerField(_("Bus")))
    def bus_needed(self, ar):
        return self.get_places_sum(
            state=EnrolmentStates.requested, needs_bus=True)

(Taken from :class:`lino_avanti.lib.avanti.Client`)

Define a **virtual field on a table**::

    @dd.virtualfield(dd.ForeignKey('polls.Question'))
    def question(self, obj, ar):
        return obj

(Taken from :class:`lino_xl.lib.polls.PollResult`)


Examples of writable virtual fields:
- :class:`lino_xl.lib.ledger.DcAmountField`
- :attr:`lino_xl.lib.polls.AnswersByResponseEditor.remark` is a :class:`lino_xl.lib.polls.AnswerRemarkField`
- :class:`lino_xl.lib.families.CoupleField`
- :class:`lino_xl.lib.cal.ExtAllDayField`
- :attr:`lino_xl.lib.excerpts.Excerpt.body_template_content` is a :class:`lino_xl.lib.excerpts.BodyTemplateContentField`
- :class:`lino.core.mti.EnableChild`


Reference
=========

Some entries to the API:

- :class:`lino.core.fields.VirtualField`
- :class:`lino.utils.mti.EnableChild`
- :attr:`lino.core.model.Model.workflow_buttons`
- `dd.virtualfield`, `dd.displayfield` etc

TODO:

- Write a simple example project in tutorials


Some edge cases
===============

A cool example is in :mod:`lino_welfare.modlib.pcsw.models` where we
have::

    dd.update_field(Client, 'overview', verbose_name=None)

This is special because :class:`Client` is abstract at this place\
[#f1]_.  Abstract models don't have a copy of each inherited virtual
field.  the overview field is

.. [#f1] Note that actually it is abstract only in eupen, not in
         chatelet. But that's another cool thing.
