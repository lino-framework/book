.. _dev.parameters:

================================
Introduction to table parameters
================================

Any table in Lino can have optional panel with so-called **table
parameters**.

For example, here is a `My Appointments` table, first with the
**parameter panel** collapsed and then expanded:

.. image:: parameters1.png
   :width: 300
           
.. image:: parameters2.png
   :width: 300

You can toggle between these two states by clicking the `Show or hide
the table parameters` button in the toolbar.  This button is available
only on tables which do have parameters.

- :meth:`lino.core.model.Model.get_simple_parameters`
- :meth:`lino.core.model.Model.get_parameter_fields`


TODO: continue to write documentation.

:attr:`lino.core.utils.Parametrizable.parameters`

