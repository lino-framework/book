.. _dev.actions:

=====================
The actions reference
=====================

This section tries to explain everything you need to know about
actions.

.. contents::
    :depth: 1
    :local:


.. currentmodule:: lino.core.actions


Overview
========

An **action** in Lino is something a user can request to do.

Actions can be **rendered** as a menu item, a toolbar button or a
clickable text or symbol. For example the :guilabel:`Delete` action is
an instance of :class:`DeleteSelected`.  It becomes visible in the
toolbars of the grid and the detail windows and in the context menu on
a grid row.
  
Actions are always linked to their *actor*.  Each actor has its list
of actions.

An **action request** is when a user actually has requested to run a
given action on a given set of database rows.

**Standard actions** are installed automatically on every table when
Lino starts up.  For example 

- :class:`GridEdit`: open a window showing a grid on this table.
- :class:`ShowDetail`: open a detail window on the current record.
- :class:`InsertRow` : open an insert window.
- :class:`SubmitInsert` : create a new database row using the data
  specified in the insert window.
- :class:`DeleteSelected` : delete the selected rows after asking a
  confimation.

Application developers can define new **custom actions**, either by
applying the :func:`action` decorator to a model or table method, or
by subclassing the :class:`Action` class and instantiating them as an
attribute of the model or table.

Application developers can also override standard actions with their
own custom actions. For example (...)
  

The default action of an actor
==============================


Each Actor has a **default action**. The default action for
:class:`Table <lino.core.dbtables.Table>` is :class:`GridEdit`.
That's why you can define a menu item by simply naming an actor.

That's why (in the :meth:`setup_menu
<lino.core.plugin.Site.setup_menu>` method of your :class:`Site`
subclass defined in the :file:`mysite/settings.py` file of the
:ref:`Polls tutorial <lino.tutorial.polls>`) you can say::

    def setup_menu(site, ui, profile, main):
        m = main.add_menu("polls", "Polls")
        m.add_action('polls.Questions')
        m.add_action('polls.Choices')


The :meth:`add_action <lino.core.menus.Menu.add_action>` method of
Lino's :class:`lino.core.menus.Menu` is smart enough to understand
that if you specify a Table, you mean in fact that table's default
action.


Defining custom actions
=======================

Custom actions are the actions defined by the application developer.

The :ref:`Polls tutorial <lino.tutorial.polls>` has one of them:

.. code-block:: python

    @dd.action(help_text="Click here to vote this.")
    def vote(self, ar):
        def yes(ar):
            self.votes += 1
            self.save()
            return ar.success(
                "Thank you for voting %s" % self,
                "Voted!", refresh=True)
        if self.votes > 0:
            msg = "%s has already %d votes!" % (self, self.votes)
            msg += "\nDo you still want to vote for it?"
            return ar.confirm(yes, msg)
        return yes(ar)

The :func:`@dd.action <dd.action>` decorator can have keyword
parameters to specify information about the action. In practice these
may be :attr:`label <Action.label>`, :attr:`help_text
<Action.help_text>` and :attr:`required <Action.required_roles>`.

The action method itself should have the following signature::

    def vote(self, ar, **kw):
        ...
        return ar.success(kw)
        
Where ``ar`` is an :class:`ActionRequest
<lino.core.requests.ActionRequest>` instance that holds information
about the web request which called the action.

- :meth:`callback <lino.core.requests.BaseRequest.callback>` 
  and :meth:`confirm <lino.core.requests.BaseRequest.callback>`
  lets you define a dialog with the user using callbacks.

- :meth:`success <lino.core.requests.BaseRequest.success>` and
  :meth:`error <lino.core.requests.BaseRequest.error>` are possible
  return values where you can ask the client to do certain things.



The :class:`Action` class
=========================

.. class:: Action

    Abstract base class for all actions.

    Lino has a class :class:`Action <lino.core.actions.Action>` which
    represents the methods who have a clickable button or menu item in
    the user interface.

    Each action instance holds a few important pieces of information:

    - label : the text to place on the button or menu item
    - help_text : the text to appear as tooltip when the mouse is over that button
    - permission requirements : specify for whom and under which
      conditions this action is available (a complex subject, we'll talk
      about it in a later tutorial)
    - handler function : the function to execute when the action is invoked
           
           
    .. attribute:: label

        The label of this action. A short descriptive text in user
        language.

    .. attribute:: button_text
                   
        The text to appear on buttons for this action. If this is not
        defined, the :attr:`label` is used.



    .. attribute:: help_text
                   
        A help text that shortly explains what this action does.
        :mod:`lino.modlib.extjs` shows this as tooltip text.

    .. attribute:: disable_primary_key
                   
        Whether primary key fields should be disabled when using this
        action. This is `True` for all actions except :class:`InsertRow`.

    .. attribute:: keep_user_values
                   
        Whether the parameter window should keep its values between
        different calls. If this is True, Lino does not fill any default
        values and leaves those from a previous call.

    .. attribute:: icon_name
                   
        The class name of an icon to be used for this action when
        rendered as toolbar button.  Allowed icon names are defined in
        :data:`lino.core.constants.ICON_NAMES`.

    .. attribute:: combo_group
                   
        The name of another action to which to "attach" this action.
        Both actions will then be rendered as a single combobutton.


    .. attribute:: parameters
                   
        See :attr:`lino.core.utils.Parametrizable.parameters`.

    .. attribute:: use_param_panel
                   
        Used internally. This is True for window actions whose window use
        the parameter panel: grid and emptytable (but not showdetail)


    .. attribute:: no_params_window
                   
    Set this to `True` if your action has :attr:`parameters` but you
    do *not* want it to open a window where the user can edit these
    parameters before calling the action.

    Setting this attribute to `True` means that the calling code must
    explicitly set all parameter values.  Usage example is the
    :attr:`lino_xl.lib.polls.models.AnswersByResponse.answer_buttons`
    virtual field.


    .. attribute:: sort_index = 90
                   
    Determines the sort order in which the actions will be presented
    to the user.

    List actions are negative and come first.

    Predefined `sort_index` values are:

    ===== =================================
    value action
    ===== =================================
    -1    :class:`as_pdf <lino_xl.lib.appypod.PrintTableAction>`
    10    :class:`InsertRow`, :class:`SubmitDetail`
    11    :attr:`duplicate <lino.mixins.duplicable.Duplicable.duplicate>`
    20    :class:`detail <ShowDetailAction>`
    30    :class:`delete <DeleteSelected>`
    31    :class:`merge <lino.core.merge.MergeAction>`
    50    :class:`Print <lino.mixins.printable.BasePrintAction>`
    51    :class:`Clear Cache <lino.mixins.printable.ClearCacheAction>`
    60    :class:`ShowSlaveTable`
    90    default for all custom row actions
    200   default for all workflow actions (:class:`ChangeStateAction <lino.core.workflows.ChangeStateAction>`)
    ===== =================================


    .. attribute:: auto_save

    What to do when this action is being called while the user is on a
    dirty record.
    
    - `False` means: forget any changes in current record and run the
      action.

    - `True` means: save any changes in current record before running
      the action.  `None` means: ask the user.


    .. attribute:: extjs_main_panel
                   
    Used by :mod:`lino_xl.lib.extensible` and
    :mod:`lino.modlib.awesome_uploader`.

    Example::

        class CalendarAction(dd.Action):
            extjs_main_panel = "Lino.CalendarApp().get_main_panel()"
            ...

    
    .. attribute:: js_handler
                   
    This is usually `None`. Otherwise it is the name of a Javascript
    callable to be called without arguments. That callable must have
    been defined in a :attr:`lino.core.plugin.Plugin.site_js_snippets` of the plugin.



    .. attribute:: action_name
                   
    Internally used to store the name of this action within the
    defining Actor's namespace.


    .. attribute:: defining_actor
                   
    Internally used to store the :class:`lino.core.actors.Actor` who
    defined this action.


    .. attribute:: key
                   
    The hotkey to associate to this action in a user interface.


    .. attribute:: default_format = 'html'

    Used internally.

    .. attribute:: editable
                   
    Whether the parameter fields should be editable.
    Setting this to False seems nonsense.

    .. attribute:: readonly
                   
    Whether this action is readonly, i.e. does not change any data.

    Setting this to `False` will make the action unavailable for
    `readonly` user profiles and will cause it to be logged when
    :attr:`log_each_action_request
    <lino.core.site.Site.log_each_action_request>` is set to `True`.
    
    Note that when a readonly action actually *does* modify the
    database, Lino won't "notice" it.

    Discussion
    
    Maybe we should change the name `readonly` to `modifying` or
    `writing` (and set the default value `False`).  Because for the
    application developer that looks more natural.  Or --maybe better
    but probably with even more consequences-- the default value
    should be `False`.  Because being readonly, for actions, is a kind
    of "privilege": they don't get logged, they also exists for
    readonly users...  It would be more "secure" when the developer
    must explicitly "say something" it when granting that privilege.

    Another subtlety is the fact that this attribute is used by
    :class:`lino.modlib.users.mixins.UserAuthored`.  For example the
    :class:`StartTicketSession
    <lino_noi.lib.clocking.actions.StartTicketSession>` action in
    :ref:`noi` is declared "readonly" because we want Workers who are
    not Triagers to see this action even if they are not the author
    (reporter) of a ticket. In this use case the name should rather be
    `requires_authorship`.


    .. attribute:: opens_a_window
                   
    Used internally to say whether this action opens a window.

    .. attribute:: hide_top_toolbar
                   
    Used internally if :attr:`opens_a_window` to say whether the
    window has a top toolbar.


    .. attribute:: hide_navigator
                   
    Used internally if :attr:`opens_a_window` to say whether the
    window has a navigator.


    .. attribute:: show_in_bbar
                   
    Whether this action should be displayed as a button in the toolbar
    and the context menu.

    For example the :class:`CheckinVisitor
    <lino_xl.lib.reception.models.CheckinVisitor>`,
    :class:`ReceiveVisitor
    <lino_xl.lib.reception.models.ReceiveVisitor>` and
    :class:`CheckoutVisitor
    <lino_xl.lib.reception.models.CheckoutVisitor>` actions have this
    attribute explicitly set to `False` because otherwise they would be
    visible in the toolbar.

    .. attribute:: show_in_workflow = False
                   
        Used internally.  Whether this action should be displayed as the
        :attr:`workflow_buttons <lino.core.model.Model.workflow_buttons>`
        column. If this is True, then Lino will automatically set
        :attr:`custom_handler` to True.

         
    .. attribute:: custom_handler = False
                   
        Whether this action is implemented as Javascript function call.
        This is necessary if you want your action to be callable using an
        "action link" (html button).


    .. attribute:: select_rows
                   
        True if this action needs an object to act on.

        Set this to `False` if this action is a list action, not a row
        action.

    .. attribute:: http_method
                   
        HTTP method to use when this action is called using an AJAX call.

    .. attribute:: preprocessor
                   
        Name of a Javascript function to be invoked on the web client when
        this action is called.
    
    

The :func:`action` decorator
============================

.. function:: lino.core.actions.action

    Decorator to define custom actions.
    
    The decorated function will be installed as the actions's
    :meth:`run_from_ui <Action.run_from_ui>` method.

    Same signature as :meth:`Action.__init__`.
    In practice you'll possibly use:
    :attr:`label <Action.label>`,
    :attr:`help_text <Action.help_text>` and
    :attr:`required_roles <lino.core.permissions.Permittable.required_roles>`.

              

The :ref:`Lino Polls tutorial <lino.tutorial.polls>` shows the
simplest form of defining an action by adding the :func:`action
<lino.core.actions.action>` decorator to a method.

This decoratior actually turns the method into an instance of
:class:`lino.core.actions.Action <Action>`



More about actions
==================

- :doc:`/tutorials/actions/index`


Examples of custom actions defined by certain libraries:

- The :class:`MoveUp <lino.mixins.sequenced.MoveUp>` and
  :class:`MoveDown <lino.mixins.sequenced.MoveDown>` actions of a
  :class:`Sequenced <lino.mixins.sequenced.Sequenced>`.

- The :class:`Duplicate <lino.mixins.duplicable.Duplicate>` action for
  creating a copy of the current row.

- In :mod:`lino.mixins.printable`: 
  :class:`DirectPrintAction <lino.mixins.printable.DirectPrintAction>`,
  :class:`CachedPrintAction <lino.mixins.printable.CachedPrintAction>`,
  :class:`ClearCacheAction <lino.mixins.printable.ClearCacheAction>`

- The :class:`ToggleChoice <lino.modlib.polls.ToggleChoice>`
