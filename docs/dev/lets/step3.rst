.. doctest docs/dev/lets/step3.rst
.. include:: /../docs/shared/include/defs.rst
.. _dev.lets.step3:

==========================
Step 3 : Filtering
==========================

In this step we will add end-user filtering using simple parameter fields.

The :term:`grid window` with our products now has a new |gear| button in its
toolbar.  Clicking on this button toggles an additional panel, the parameter
panel, to expand or collapse. 


- We add a new database model "Category"
- We add some database fields (delivery_unit, price)
- We add more demo data so that there is something to filter

To activate the code of this step in your contributor environment::

  $ go lets
  $ git checkout step3

To see what we changed since the previous step::

  $ git diff step2

Not many explanations here yet. Try to understand the code changes and ask
questions.

Some hints:

- Note that the Offers, Demands and Products tables now have a |gear| icon in
  their toolbar. This is the main new feature. Play with it.

- The :attr:`delivery_unit` field is a choicelist field. This is similar to a
  :class:`ForeignKey`, but instead of pointing to a database row, it points to a
  choice in a hard-coded table, which we call a choicelist.
  See :doc:`/dev/choicelists`.

- The :meth:`Model.get_simple_parameters
  <lino.core.fields.TableRow.get_simple_parameters>` method (a class method on a
  database model) yields the name of database fields to be used as "table
  parameters", i.e. the fields that appear in the "parameter panel" (the panel
  that expands and collapses when you hit the |gear| button). See
  :doc:`/dev/parameters`.
