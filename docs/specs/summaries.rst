==============
Summary tables
==============

Installs a framework for defining summary tables.  using the
:class:`Summary` model mixin and the :manage:`checksummaries` command.

Usage examples:
:mod:`lino_xl.lib.tickets` and
:mod:`lino_welfare.modlib.esf`.



Checking summaries
==================

The plugin schedules a daily task which runs the
:manage:`checksummaries` command.


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
           

The ``Summary`` model mixin
===========================
           
.. class:: Summary

    Abstract base class for all "summary data" models.

    .. attribute:: summary_period
                   
       Can be 'yearly', 'monthly' or 'timeless'
       
    .. attribute:: year
    .. attribute:: month
                   
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

                
