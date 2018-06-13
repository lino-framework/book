.. _dev.delete:

=========================
Deleting database objects
=========================

This section is a topic guide about how to customize behaviour around
deleting records.

Unlike Django, Lino has PROTECT as the default on_delete strategy in
ForeignKey fields.  If you want CASCADE, then you specify it
explicitly using the :attr:`allow_cascaded_delete
<lino.core.model.Model.allow_cascaded_delete>` attribute on the model
whose instances will be deleted.

The :meth:`disable_delete <lino.core.model.Model.disable_delete>`
method of a model decides whether a given database object may be
deleted or not.
Also the :meth:`disable_delete <lino.core.dbtables.Table.disable_delete>`
method of an actor.

The :attr:`disable_delete` item in :attr:`data_record
<lino.core.requests.ValidActionResponses.data_record>` is a "preview"
of whether that row can be deleted or not.  The user interface may use
this information to disable or enable its delete button.

But the :class:`DeleteSelected <lino.core.actions.DeleteSelected>`
action will verify again before actually deleting a row.

When Lino analyzes the application's models at startup, it adds a
"disable_delete handler" (:mod:`lino.core.ddh`) to every model.

The :meth:`lino.utils.diag.Analyzer.show_foreign_keys` can help to
find examples for writing tests. It is used in specs like
:ref:`noi.specs.ddh` or :ref:`voga.specs.db_roger`.




