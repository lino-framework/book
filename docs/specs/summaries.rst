==============================
``summaries`` : Summary tables
==============================

.. currentmodule:: lino.modlib.summaries

The :mod:`lino.modlib.summaries` plugin installs a framework for defining
summary fields and summary tables.  A summary table is a table with summary
fields.

A summary field is a readonly and otherwise regular database field whose value
is computed at certain moments as a summary of other tables.  This can be used
as an alternative for virtual fields whose value is computed on the fly for each
request.

The plugin has no models on its own but provides several model mixins and a
:manage:`checksummaries` command which updates all summaries. It also schedules
a daily :manage:`linod` task which does the same.

Users also get a button :guilabel:`∑` on each model for which there are slave
summaries.

Usage examples: :doc:`userstats` :mod:`lino_xl.lib.tickets` and
:mod:`lino_welfare.modlib.esf`.


The ``Summarized`` model mixin
================================
           
.. class:: Summarized

    Model mixin for database objects that have summary fields.

    .. attribute:: delete_them_all

        Set this to True if all instances of this model should be considered
        temporary data to be deleted by :manage:`checksummaries`.

    .. method:: compute_results

        Update all the summary fields on this database object.

    .. method:: reset_summary_data

        Set all counters and sums to 0.

    .. method:: compute_summary_values

        Reset summary data fields (:meth:`reset_summary_data`), for
        every collector (:meth:`get_summary_collectors`) loop over its
        database objects and collect data, then save this record.

    .. method:: get_summary_collectors

        To be implemented by subclasses. This must yield a sequence
        of ``(collector, qs)`` tuples, where `collector` is a callable
        and `qs` a queryset. Lino will call `collector` for each `obj`
        in `qs`. The collector is responsible for updating that
        object.

.. class:: SlaveSummarized

    Mixin for :class:`Summarized` models that are related to a master.

    The master is another database object for which this summary data applies.
    Implementing subclasses must define a
    field named :attr:`master` which must be a foreignkey to the master model.

    .. attribute:: master

        The target model of the :attr:`master` will automatically receive an
        action `check_summaries`.

        The mixin also sets :attr:`allow_cascaded_delete
        <lino.core.model.Model.allow_cascaded_delete>` to ``'master'``.

       
.. class:: MonthlySummarized

    A :class:`Summarized` that will have more than one entries per master,
    one for each month.

    .. attribute:: summary_period

       Can be ``'yearly'`` or ``'monthly'``.

    .. attribute:: year
    .. attribute:: month

.. class:: MonthlySlaveSummary

    A combination of :class:`SlaveSummary` and :class:`MonthlySummarized`.



The ``checksummaries`` admin command
====================================

.. management_command:: checksummaries


.. py2rst::

  from lino.modlib.summaries.management.commands.checksummaries \
      import Command
  print(Command.help)

        


Actions
=======


.. data:: check_summaries
          
    This plugin installs a :data:`check_summaries` action

    - (instance of :class:`UpdateSummariesByMaster`)
      on every model for which there is at least one :class:`Summary`

    - (instance of :class:`CheckSummaries`)
      on the :class:`lino.modlib.system.SiteConfig` object.


.. function:: get_summary_models
              
    Return a `dict` mapping each model which has at least one summary
    to a list of these summaries.

             
.. class:: CheckSummaries
           
    Web UI version of :manage:`checksummaries`.
          
.. class:: UpdateSummariesByMaster
           
    Update summary data for this object.
           

Plugin configuration
====================

The plugin has two configurable attributes :attr:`start_year
<Plugin.start_year>` and :attr:`end_year <Plugin.end_year>` which can
be set to specify the years to be covered in summary tables. The
default is the current year and two precedent ones.
