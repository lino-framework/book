.. _dev.lets.step3:

==========================
Step 3 : Filtering
==========================

- We add a new database model "Category"
- We add some database fields (delivery_unit, price)
- We add more demo data so that there is something to filter
- We add end-user filtering using simple parameter fields

To activate the code of this step in your contributor environment::

  $ go lets
  $ git checkout step3

To see what we changed since the previous step::

  $ git diff step2

Not many explanations here yet. Try to understand the code changes and to ask
questions.

Maybe some helpful hints:

- :meth:`lino.core.model.Model.get_simple_parameters`
- :doc:`/dev/choicelists`
