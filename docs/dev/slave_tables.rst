.. _slave_tables:

============
Slave tables
============

A table is called a **slave table** when it "depends" on a master.

For example the `BooksByAuthor` table
in :ref:`lino.tutorial.tables`
shows the *books* written by a
given *author*.  Or the `ChoicesByQuestion` table in
:ref:`lino.tutorial.polls`
shows the *choices* for a given *question*
(its master).  Other examples of slave tables are used in
:ref:`dev.lets` and :doc:`/dev/table_summaries`.
     
A slave table cannot render if we don't define the master.  You cannot
ask Lino to render the :class:`BooksByAuthor` table if you don't
specify for *which* author you want it.

Slave tables are most often used as elements of a detail layout.  In this case
Lino renders them in a *slave panel* widget, and the current record is the
master.


.. _remote_master:

Slave tables with remote master
===============================

The :attr:`master_key` of a :ref:`slave table <slave_tables>` can be a remote
field.

.. graphviz::

   digraph foo  {
       A -> B
       B -> C
  }

When you have three models A, B and C with A.b being a pointer to B
and B.c being a pointer to C, then you can design a table `CsByA`
which shows the C instances of a given A instance by saying::

    class CsByA(Cs):
        master_key = "c__b"

For example :class:`lino_xl.lib.courses.ActivitiesByTopic` shows all
courses about a given topic. But a course has no FK `topic`, so you
cannot say ``master_key = 'topic'``. But a course does know its topic
indirectll because it knows it's course series, and the course series
knows its topic. So you can specify a remote field::

    class ActivitiesByTopic(Courses):
        master_key = 'line__topic'

        allow_create = False

A slave table with a remote master should have :attr:`allow_create
<lino.core.actors.Actor.allow_create>` set to `False` because we cannot set a
line for a new course.

Other examples

- :class:`lino_avanti.lib.courses.RemindersByPupil`
  
.. :class:`lino_xl.lib.courses.EntriesByTeacher`


.. _related_master:

Slave tables with related master
================================

Another special case is when you have the following structure where you have
orders and invoices both related to a partner, but the invoices don't know
their order.

.. graphviz::

   digraph foo  {
       Order -> Partner
       Invoice -> Partner
  }

The :class:`lino_xl.lib.orders.InvoicesByOrder` table can be used in the detail
of an order to show the invoices of the partner of that order.  Here is how to
define this case::

    class InvoicesByOrder(InvoicesByPartner):

        label = _("Sales invoices (of client)")

        @classmethod
        def get_master_instance(cls, ar, model, pk):
            # the master instance of InvoicesByPartner must be a Partner, but since
            # we use this on an order, we get the pk of an order
            assert model is rt.models.contacts.Partner
            order = rt.models.orders.Order.objects.get(pk=pk)
            return order.project

