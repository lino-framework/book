.. _dev.actions:

=======================
Introduction to actions
=======================

This section tries to explain everything you need to know about
actions.

.. contents::
    :depth: 1
    :local:


.. currentmodule:: lino.core.actions


Overview
========

An **action** in Lino is something a user can request to do.  Actions
are visible to the end-users as menu items, toolbar buttons or
clickable chunks of text at arbitrary places.

An **action request** is when a user "actually clicked on that
button", i.e. requested to run a given action on a given set of
database rows.

For example the :class:`ShowTable` action opens a window showing a
grid on a given table.  Most items of the main menu are
:class:`ShowTable` actions.

Or the :class:`DeleteSelected` action is visible in the toolbars of
the grid and the detail windows and in the context menu on a grid row.

**Standard actions** are installed automatically on every table when
Lino starts up.

For example 

- :class:`DeleteSelected`, :class:`SubmitDetail` and
  :class:`SubmitInsert` send an AJAX request which causes something to
  happen on the server.
  
- :class:`ShowTable`, :class:`ShowDetail`, :class:`ShowInsert` open a
  window


Actions are always linked to their *actor*.  Each actor has its list
of actions.

Application developers can define new :doc:`custom_actions`, or also
override standard actions with their own custom actions.


Some action attributes include:

- label : the text to place on the button or menu item
- handler function : the function to call when the action is invoked
- help_text : the text to appear as tooltip when the mouse is over
  that button
- permission requirements : for whom and under which conditions this
  action is available


  

  

The default action of an actor
==============================


Each Actor has a **default action**. The default action for
:class:`Table <lino.core.dbtables.Table>` is :class:`ShowTable`.
That's why you can define a menu item by simply naming an actor.

That's why (in the :meth:`setup_menu
<lino.core.plugin.Site.setup_menu>` method of your :class:`Site`
subclass defined in the :file:`mysite/settings.py` file of the
:ref:`Polls tutorial <lino.tutorial.polls>`) you can say::

    def setup_menu(site, ui, user_type, main):
        m = main.add_menu("polls", "Polls")
        m.add_action('polls.Questions')
        m.add_action('polls.Choices')


The :meth:`add_action <lino.core.menus.Menu.add_action>` method of
Lino's :class:`lino.core.menus.Menu` is smart enough to understand
that if you specify a Table, you mean in fact that table's default
action.


The :class:`Action` class
=========================

.. class:: Action

    Abstract base class for all actions.

    The first argument is the optional `label`, other arguments should
    be specified as keywords and can be any of the existing class
    attributes.

           
    .. attribute:: label

        The label of this action. A short descriptive text in user
        language. Used e.g. on menu items. Also on toolbar buttons if
        they have neither :attr:`icon_name` nor :attr:`button_text`

    .. method:: get_label(self)
                
        Return the `label` of this action, or the `action_name` if the
        action has no explicit label.
                
    .. attribute:: button_text
                   
        The text to appear on buttons for this action. If this is not
        defined, the :attr:`label` is used.

    .. attribute:: button_color

        The color to be used on icon-less buttons for this action
        (i.e. which have no :attr:`icon_name`).
        See also :attr:`lino.core.site.Site.use_silk_icons`.
        
        Not yet implemented. This is currently being ignored.

    .. attribute:: help_text
                   
        A help text that shortly explains what this action does.  In a
        graphical user interface this will be rendered as a **tooltip**
        text.

        If this is not given by the code, Lino will potentially set it at
        startup when loading the :xfile:`help_texts.py` files.

    .. attribute:: disable_primary_key
                   
        Whether primary key fields should be disabled when using this
        action. This is `True` for all actions except :class:`ShowInsert`.

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
        10    :class:`ShowInsert`, :class:`SubmitDetail`
        11    :attr:`duplicate <lino.mixins.duplicable.Duplicable.duplicate>`
        20    :class:`detail <ShowDetail>`
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
                   
        Not used. The keybaord hotkey to associate to this action in a
        user interface.


    .. attribute:: default_format = 'html'

        Used internally.

    .. attribute:: editable
                   
        Whether the parameter fields should be editable.
        Setting this to False seems nonsense.

    .. attribute:: readonly
                   
        Whether this action is readonly, i.e. does not change any data.

        Setting this to `False` will make the action unavailable for
        `readonly` user types and will cause it to be logged when
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
    
    .. method:: attach_to_actor(self, owner, name):

        Called once per Actor per Action on startup before a
        BoundAction instance is being created.  If this returns False,
        then the action won't be attached to the given actor.

        The owner is the object which "defines" the action, i.e. uses
        that instance for the first time. Subclasses of the owner may
        re-use the same instance without becoming the owner.

   

