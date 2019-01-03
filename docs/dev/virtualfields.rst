.. _dev.virtualfields:

====================
About virtual fields
====================

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


             
   
