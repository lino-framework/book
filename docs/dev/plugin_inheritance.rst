.. _plugin_inheritance:

==================
Plugin inheritance
==================

**Plugin inheritance** is when you extend some existing Lino plugin by
inheriting everything of it (its models, views, methods, fixtures and
admin commands) and then overriding some of it.

Plugins aren't *classes*, they are *packages*, so plugin inheritance
is not "real" inheritance but rather a series of guidelines and
programming patterns.

Plugin inheritance is intensively used by Lino's plugin libraries.

A **plugin library** is a collection of reusable plugins which are
designed to work together. For example :mod:`lino.modlib`,
:mod:`lino_xl.lib`, :mod:`lino_noi.lib`, :mod:`lino_voga.lib`,
:mod:`lino_welfare.modlib`.


A simple example
================

A simple example of plugin inheritance is the
:mod:`lino_book.projects.min2` project: it defines a
:mod:`lino_book.projects.min2.modlib.contacts` plugin which inherts
from :mod:`lino_xl.lib.contacts` by adding a series of mixins to some
of its models. Look at the code and at the resulting application!


Overriding models
=================

As a more complex example let's look at :ref:`voga`.  It uses Lino's
standard calendar module :mod:`lino_xl.lib.cal`, but extends the
:class:`Room` model defined there:

- it adds two fields :attr:`tariff` and :attr:`calendar`
- it adds another base class (the :class:`ContactRelated
  <lino_xl.lib.contacts.models.ContactRelated>` mixin)
- it overrides the :meth:`save` method to add some specific behaviour

Here is the relevant application code which defines the *Voga* version
of :class:`cal.Room <lino_voga.lib.cal.models.Room>`::

    from lino_xl.lib.cal.models import Room
    from lino_xl.lib.contacts.models import ContactRelated

    class Room(Room, ContactRelated):

        tariff = dd.ForeignKey('products.Product', ...)
        calendar = dd.ForeignKey('cal.Calendar', ...)

    def save(self, *args, **kwargs):
        super(Room, self). save(*args, **kwargs)

        # add specific behaviour

For this to work, the *library version* of :class:`cal.Room`
(i.e. :class:`lino_xl.lib.cal.models.Room`) must have `abstract=True`.

But only in this special case. The general case is that when an
application installs :mod:`lino_xl.lib.cal` , it gets (among others) a
new model :class:`cal.Room <lino_xl.lib.cal.models.Room>`.  We
wouldn't want to force every application which uses
:mod:`lino_xl.lib.cal` to override the `Room` model just to make it
concrete.

There is no way in Django to make a model abstract "afterwards". When
it is declared as abstact, then you *must* override it in order to get
a concrete model. When it is not abstract, then you *cannot* override
it by a model of same name (Django complains if you try).

In other words: The *abstractness of certain models* in a plugin
depends on whether the plugin is going to be extended.

So how can the library version know whether the :class:`Room` model
should be abstract or not?

This is why we need a central place where models modules can ask
whether it wants a given model to be abstract or not.

To solve this problem, Lino offers the :meth:`is_abstract_model
<lino.core.site.Site.is_abstract_model>` method.  Usage example::

    class Room(dd.BabelNamed):
        class Meta:
            abstract = dd.is_abstract_model(__name__, 'Room')
            verbose_name = _("Room")
            verbose_name_plural = _("Rooms")

The trick here is that the :file:`lino_voga/lib/cal/__init__.py` file
now contains this information in the `extends_models` attribute::


    from lino_xl.lib.cal import Plugin

    class Plugin(Plugin):

        extends_models = ['Room']

The implementation of :meth:`is_abstract_model
<lino.core.site.Site.is_abstract_model>` has evolved in time.  The
first implementation used a simple set of strings in a class attribute
of :class:`lino.core.site.Site`.  That might have been a standard
Django setting.  But as things got more and more complex, it became
difficult to define this manually. And it was redundant because every
plugin *does* know which library models it is *going* to override.
But how to load that information from a plugin before actually
importing it?  We then discovered that Django doesn't use the
:file:`__init__.py` files of installed plugins.  And of course we were
lucky to have a :class:`lino.core.site.Site` class which is being
*instantiated* before `settings` have finished to load...

.. _plugin_namespaces:

Plugin namespaces
=================

Some packages in a plugin library exist only because the library wants to
provide different variants of a same plugin.  We want them to be
interchangeable, so they must have the same Django app_name. That's why we
introduce and additional module level in order to differentiate them.

Examples of plugin namespaces are :mod:`lino_xl.lib.statbel`,
:mod:`lino_xl.lib.online` and :mod:`lino_voga.lib.roger`.

- :mod:`lino_xl.lib.countries` and :mod:`lino_xl.lib.statbel.countries`
- :mod:`lino.modlib.users` and :mod:`lino_xl.lib.online.users`
- :mod:`lino_voga.lib.courses` and :mod:`lino_voga.lib.roger.courses`

Application developers can easily switch from the default version of the
countries plugin to the "statbel" version of the same plugin.  Since we don't
add an additional plugin but replace the default version, we can use the
:meth:`get_apps_modifiers <lino.core.site.Site.get_apps_modifiers>` method::

    def get_apps_modifiers(self, **kw):
        kw = super(Site, self).get_apps_modifiers(**kw)
        kw.update(courses='lino_voga.lib.roger.courses')
        return kw





Overriding other things
=======================

Overriding other Python objects (ChoiceList, Action, Plugin) is
straightforward.

But the `fixtures`, `config` and `management` subdirs need special
attention when doing plugin inheritance.


The `config` directory
======================

The :xfile:`config` subdirectories are handled automatically as expected: Lino
scans first the `config` subdirectory of the child, then those of the parents.


Inheriting fixtures and django-admin commands
=============================================

When you extend a plugin that has a :xfile:`fixtures` package, then you must
decide whether you want to inherit these fixtures.

There are good chances that you actually just want to inherit them without
changing anything. In that case you must define a **wrapper fixture** for each
fixture you want to inherit, which imports at least `objects` from its "parent"
fixture.

For example the :xfile:`fixtures` package  of :mod:`lino_voga.lib.cal` contains
a suite of one-line modules, one for each fixture defined by its parent, the
:mod:`lino_xl.lib.cal` plugin.  Each of these wrapper fixtures has just one
`import` statement like this::

  from lino_xl.lib.cal.fixtures.demo import objects

There is currently no easier way to inherit the default behaviour.  Keep in mind
that your fixtures may do something else, or you may decide to not inherit some
fixture from your parent.

There is a possible pitfall: when you create a new fixture in a plugin, then the
users of your plugin will not automatically get notified that you added a new
fixture and that they must create a wrapper if they want it as well.


.. xfile:: management

A similar approach is necessary for django-admin commands.  Django
discovers them by checking whether the plugin has a subpackage
:xfile:`management` and then calling :meth:`os.listdir` on that module's
"commands" subdirectory.  (See Django's
:file:`core/management/__init__.py` file.)  So when you extent a
plugin which has admin commands, you must create a pseudo command
