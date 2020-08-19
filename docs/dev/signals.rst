.. _lino.signals:

================
Signals overview
================

Lino defines a few additional Django signals.

Each signal is an instance of :class:`django.dispatch.Signal` stored in
:mod:`lino.core.signals`.

.. currentmodule:: lino.core.signals


Startup signals
===============

.. data:: pre_startup
.. data:: post_startup

    Sent exactly once per process at site startup,
    just before any application-specific startup actions.

    - `sender`:  the :class:`lino.core.site.Site` instance

.. data:: pre_analyze

    Sent exactly once per process at site startup, just before Lino
    analyzes the models.

    - `sender`:  the :class:`lino.core.site.Site` instance
    - `models_list` list of models


.. data:: post_analyze

    Sent exactly once per process at site startup, just after Site has
    finished to analyze the models.

.. data:: pre_ui_build

.. data:: post_ui_build




Database signals
================

.. data:: database_connected

    No longer used.

.. data:: testcase_setup

    Emitted each time `lino.core.utils.TestCase.setUp` is called.
    Lino uses this signal to reset its SiteConfig cache.

    It is necessary because (afaics) the Django test runner doesn't
    send a 'connected' signal when it restores the database to a
    virgin state before running a new test case.


Row-level signals
=================

.. data:: on_ui_created

    Sent when a new model instance has been created and saved.

.. data:: pre_ui_delete

    Sent just before a model instance is being deleted using the user
    interface.

    - `request`: The HttpRequest object



.. data:: pre_ui_save

    Sent before a database object gets saved using the web user
    interface.

    - `sender`   the database model
    - `instance` the database object which is going to be saved.
    - `ar` the action request

.. data:: on_ui_updated

    Sent when a database model instance has been modified and saved
    using the web interface.

    A receiver of this signal gets the following keyword parameters:

    :sender: the database model of the instance which has been updated

    :watcher: the :class:`ChangeWatcher
              <lino.core.utils.ChangeWatcher>` object (which contains
              the model instance and information about the changes)

    :request: the BaseRequest object

.. data:: pre_merge

    Sent when a model instance is being merged into another instance.

.. data:: auto_create

    The :attr:`auto_create` signal is sent when :func:`lookup_or_create
    <lino.core.models.Model.lookup_or_create>` silently created a model
    instance.

    Arguments sent with this signal:

    - ``sender`` : The model instance that has been created.
    - ``field`` : The database field
    - ``known_values`` : The specified known values

.. data:: pre_remove_child
.. data:: pre_add_child

    Sent when an MTI child has been added. Arguments to the handler are:

    - `sender` : the parent (a database object instance)
    - `request` : the HttpRequest which asks to create an MTI child
    - `child` : the child model (a class object)



Test-specific signals
=====================

- :attr:`testcase_setup <lino.core.signals.testcase_setup>`
  Fired in :meth:`lino.utils.djangotest.TestCase.setUp`,
  i.e. at the beginning of each test case.

Runtime signals:

- :attr:`auto_create <lino.core.signals.auto_create>`
- :attr:`pre_add_child <lino.core.signals.pre_add_child>`
- :attr:`pre_remove_child <lino.core.signals.pre_remove_child>`
- :attr:`pre_merge <lino.core.signals.pre_merge>`
- :attr:`pre_ui_create <lino.core.signals.pre_ui_create>`
- :attr:`pre_ui_update <lino.core.signals.pre_ui_update>`
- :attr:`pre_ui_delete <lino.core.signals.pre_ui_delete>`


Utilities:

- :attr:`ChangeWatcher <lino.core.signals.ChangeWatcher>`
- :attr:`receiver <django.dispatch.receiver>` : the standard Django receiver decorator





:mod:`lino.ui.models` also defines a handler which will fire
the `database_connected` signal
and call the :func:`lino.ui.site.clear_site_config`
method on each of the following signals:

- testcase_setup
- connection_created
- post_syncdb
