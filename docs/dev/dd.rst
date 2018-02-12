============================================
The ``lino.api.dd`` module (database design)
============================================

See also :mod:`lino.api`


.. module:: lino.api.dd

Global application attributes
=============================

.. data:: plugins

    Shortcut to :attr:`lino.core.site.Site.plugins`.

.. data:: logger

    Shortcut to the main Lino logger.
          

Utilities
=========
          
.. function:: schedule_often(every=10):
          
    Decorator which schedules the given function to be run "often"
    (default every 10 seconds).

    Does nothing if `schedule
    <https://pypi.python.org/pypi/schedule>`__ is not installed.
    See :ref:`dev.linod`.
          
.. function:: schedule_daily(at="20:00"):
              
    Decorator which schedules the given function to be run "daily" (by
    default at 20:00).

    Does nothing if `schedule
    <https://pypi.python.org/pypi/schedule>`__ is not installed.
    See :ref:`dev.linod`.

Date related
============
    
.. function:: today(*args, **kwargs)

    Shortcut to :func:`lino.core.site.Site.today`.
              
.. function:: demo_date(*args, **kwargs)

    Shortcut to :func:`lino.core.site.Site.demo_date`.
    Deprecated; it is recommented to call :func:`today` instead

.. function:: fds(d)
.. function:: fdf(d)
.. function:: fdl(d)
.. function:: fdm(d)

   Shortcuts to functions of same name in :mod:`lino.utils.format_date`.
   
   :func:`fds` adds support for class:`IncompleteDate
   :<lino.fields.IncompleteDate>`.
    
   
Actors
======
              
.. class:: Table
              
    Shortcut to :class:`lino.core.dbtables.Table`
  
.. class:: Choicelist
              
    Shortcut to :class:`lino.core.choicelists.ChoiceList`
  
.. class:: VirtualTable
              
    Shortcut to :class:`lino.core.tables.VirtualTable`
  
.. class:: VentilatingTable
              
    Shortcut to :class:`lino.core.choicelists.ChoiceList`
  
.. class:: Frame
              
    Shortcut to :class:`lino.core.frames.Frame`
  

Application:

- :attr:`decfmt <lino.core.site.Site.decfmt>`
- :attr:`str2kw <lino.core.site.Site.str2kw>`
- :attr:`today <lino.core.site.Site.today>`
- :attr:`strftime <lino.core.site.Site.strftime>`
- :attr:`is_abstract_model <lino.core.site.Site.is_abstract_model>`
- :attr:`is_installed <lino.core.site.Site.is_installed>`
- :attr:`add_welcome_handler <lino.core.site.Site.add_welcome_handler>`
- :attr:`build_media_url <lino.core.site.Site.build_media_url>`
- :attr:`get_default_language <lino.core.site.Site.get_default_language>`


Extended Fields:

- :class:`CharField <fields.CharField>`
- :class:`IncompleteDateField <lino.core.fields.IncompleteDateField>`
- :class:`PasswordField <lino.core.fields.PasswordField>`
- :class:`MonthField <lino.core.fields.MonthField>`
- :class:`PercentageField <lino.core.fields.PercentageField>`
- :class:`QuantityField <lino.core.fields.QuantityField>`
- :class:`PriceField<lino.core.fields.PriceField>`
- :class:`CustomField <lino.core.fields.CustomField>`
- :class:`RecurrenceField <lino.core.fields.RecurrenceField>`
- :class:`DummyField <lino.core.fields.DummyField>`
- :func:`ForeignKey <lino.core.fields.ForeignKey>`

Virtual Fields:

- :class:`Constant <lino.core.fields.Constant>` and
  :class:`@constant <lino.core.fields.constant>`
- :class:`DisplayField <lino.core.fields.DisplayField>` and
  :class:`@displayfield <lino.core.fields.displayfield>`
- :class:`VirtualField <lino.core.fields.VirtualField>` and
  :class:`@virtualfield <lino.core.fields.virtualfield>`
- :class:`HtmlBox <lino.core.fields.HtmlBox>`

Layouts:

- :class:`DetailLayout <lino.core.layouts.DetailLayout>`
- :class:`Panel <lino.core.layouts.Panel>`
- :class:`FormLayout <lino.core.layouts.FormLayout>` no longer supported.
  Application code should use either InsertLayout or DetailLayout instead.

Utilities:

- :func:`obj2str <lino.core.utils.obj2str>`
- :func:`obj2unicode <lino.core.utils.obj2unicode>`
- :func:`range_filter <lino.core.utils.range_filter>`,
  :func:`inrange_filter <lino.core.utils.inrange_filter>`
- :func:`full_model_name <lino.core.utils.full_model_name>`
- :func:`fields_list <lino.core.fields.fields_list>`
- :func:`chooser <lino.utils.choosers.chooser>`
- :class: `ParameterPanel <lino.core.utils.ParameterPanel>`


Inter-app relations:

- :func:`resolve_field <lino.core.utils.resolve_field>`
- :func:`resolve_model <lino.core.utils.resolve_model>`
- :func:`resolve_app <lino.core.utils.resolve_app>`
- :func:`update_field <lino.core.inject.update_field>`
- :func:`inject_field <lino.core.inject.inject_field>`
- :func:`inject_action <lino.core.inject.inject_action>`
- :func:`update_model <lino.core.inject.update_model>`

- :func:`inject_quick_add_buttons <lino.core.inject.inject_quick_add_buttons>`

Signals:

- See :ref:`lino.signals`

Actions:

- :class:`Action <lino.core.actions.Action>`
- :class:`ChangeStateAction <lino.core.workflows.ChangeStateAction>`
- :class:`MergeAction <lino.core.merge.MergeAction>`
- :class:`ShowSlaveTable <lino.core.actions.ShowSlaveTable>`

Permissions:

- :class:`UserGroups <lino.modlib.users.mixins.UserGroups>`
- :class:`UserLevels <lino.modlib.users.mixins.UserLevels>`


Workflows:

- :class:`Workflow <lino.core.workflows.Workflow>`
- :class:`State <lino.core.workflows.State>`

