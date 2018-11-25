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
Lino renders them in a *slave panel* widget.


.. _remote_master:

Tables with remote master
=========================

The :attr:`master_key` of a :ref:`slave table <slave_tables>` can be a remote field. 

When you have three models A, B and C with A.b being a pointer to B
and B.c being a pointer to C, then you can design a table `CsByA`
which shows the C instances of a given A instance by saying::

    class CsByA(Cs):
        master_key = "c__b"

For example :class:`lino_xl.lib.courses.CoursesByTopic` shows all
courses about a given topic. But a course has no FK `topic`, so you
cannot say ``master_key = 'topic'``. But a course does know its topic
indirectyl because it knows it's course series, and the course series
knows its topic. So you can specify a remote field::

  master_key = 'line__topic'

Other examples

- :class:`lino_avanti.lib.courses.RemindersByPupil`
  
.. :class:`lino_xl.lib.courses.EntriesByTeacher`



