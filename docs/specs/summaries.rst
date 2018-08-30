==============
Summary tables
==============

The :mod:`lino.modlib.summaries` plugin installs a framework for
defining summary tables.  A summary table is a table with data that
has been computed (aggregated) as a summary of other tables.

Usage examples: :doc:`userstats` :mod:`lino_xl.lib.tickets` and
:mod:`lino_welfare.modlib.esf`.

The plugin has no models on its own but provides the :class:`Summary`
model mixin and the :manage:`checksummaries` command.  It also
schedules a daily task which runs the :manage:`checksummaries`
command.

.. currentmodule:: lino.modlib.summaries

The ``Summary`` model mixin
===========================
           
.. class:: TimelessSummary
           
    Model mixin for all "summary data" models.
           
    .. attribute:: master

        Any implementing subclass of :class:`TimelessSummary` must
        define a field named :attr:`master` which must be a ForeignKey
        field.  The target model of the :attr:`master` will
        automatically receive an action `check_summaries`.
        The mixin also sets
        :attr:`allow_cascaded_delete
        <lino.core.model.Model.allow_cascaded_delete>` to ``'master'``.

       
    .. method:: compute_results

        Update this summary.

        An instance of :class:`ComputeResults`.
                   
    .. method:: reset_summary_data

        Set all counters and sums to 0.
        
    .. method:: compute_summary_values

        Reset summary data fields (:meth:`reset_summary_data`), for
        every collector (:meth:`get_summary_collectors`) loop over its
        database objects and collect data, then save this record.
        
    .. method:: get_summary_collectors
                
        To be implemented by subclasses. This should yield a sequence
        of ``(collector, qs)`` tuples, where `collector` is a callable
        and `qs` a queryset. Lino will call `collector` for each `obj`
        in `qs`. The collector is responsible for updating that
        object.

.. class:: Summary

    .. attribute:: summary_period
                   
       Can be ``'yearly'``, ``'monthly'`` or ``'timeless'``.
       
    .. attribute:: year
    .. attribute:: month
                   
                

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

             
.. class:: ComputeResults

    See :meth:`Summary.compute_results`
           
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
