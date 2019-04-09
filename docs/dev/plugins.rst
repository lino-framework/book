.. _dev.plugins:

=======================
Introduction to plugins
=======================

Besides the :class:`Site <lino.core.site.Site>` class (which
encapsules what *Lino* calls an :doc:`application <application>`),
Lino defines the :class:`Plugin <lino.core.plugin.Plugin>` class which
extends what *Django* calls an "application".

The :class:`Plugin <lino.core.plugin.Plugin>` class is comparable to
Django's `AppConfig
<https://docs.djangoproject.com/en/1.11/ref/applications/>`_ class, but
has some advantages over Django's approach which makes that they are
the preferred way.

.. contents::
  :local:

What is a plugin?
=================

A plugin is a Python package which can be yielded by
:meth:`get_installed_apps <lino.core.site.Site.get_installed_apps>`.

A plugin encapsulates a limited set of **functionality** designed to
be potentially used in more than on application.

A plugin can define database models, actors, actions, fixtures,
template files, javascript snippets, and metadata.  None of these
components are mandatory.

The **metadata** about a plugin (configuration values, menu commands,
dependencies, ...) is specified by defining a subclass of
:class:`Plugin <lino.core.plugin.Plugin>` in the :xfile:`__init__.py`
file of your plugin.

Here is a fictive example::

    from lino.api import ad, _
    
    class Plugin(ad.Plugin):
        verbose_name = _("Better calendar")
        extends = 'lino.modlib.cal'
        needs_plugins  = ['lino_xl.lib.contacts']

        def setup_main_menu(self, site, user_type, m):
            m = m.add_menu(self.app_label, self.verbose_name)
            m.add_action('cal.Teams')
            m.add_action('cal.Agendas')


A plugin can **depend on other plugins** by specifying them in the
:attr:`needs_plugins <lino.core.plugin.Plugin.needs_plugins>`
attribute. This means that when you install this plugin, Lino will
automatically install these other plugins as well

A plugin can define a set of **menu commands** using methods like
:meth:`setup_main_menu
<lino.core.plugin.Plugin.setup_main_menu>`. This is explained in
:doc:`menu`.

And last but not least, a plugin can **extend** another plugin by
specifying its name in :attr:`extends_models
<lino.core.plugin.Plugin.extends_models>`.  This is explained in
:doc:`plugin_inheritance`.
      
.. _dev.accessing.plugins:

   
Accessing plugins
=================

Django developers are used to code like this::

    from myapp.models import Foo

    def print_foo(pk=1):
        print(Foo.objects.get(pk=pk))

In Lino we recommend to use the :attr:`rt.models <lino.api.rt.models>`
dict as follows::

    from lino.api import rt

    def print_foo(pk=1):
        Foo = rt.models.myapp.Foo
        print(Foo.objects.get(pk=pk))

At least if you want to use :doc:`plugin_inheritance`. One of the
basic reasons for using plugins is that users of some plugin can
extend it and use their extension instead of the original plugin.
Which means that the plugin developer does not know (and does not
*want* to know) where the model classes are actually defined.

Note that :attr:`rt.models <lino.api.rt.models>` is populated only
*after* having imported the models. So you cannot use it at the
module-level namespace of a :xfile:`models.py` module.  For example
the following variant of above code **would not work**::

    from lino.api import rt
    Foo = rt.models.foos.Foo  # error `AttrDict has no item "foos"`
    def print_foo(pk=1):
        print(Foo.objects.get(pk=pk))


Configuring plugins
===================

.. currentmodule:: lino.core.site

Plugins can have **attributes** for holding configurable options.

Examples of configurable plugin attributes:

- :attr:`lino_xl.lib.countries.Plugin.country_code` 
- :attr:`lino_xl.lib.contacts.Plugin.hide_region`

The values of plugin attributes can be configured at three levels.

As a **plugin developer** you specify a hard-coded default value.

As an **application developer** you can specify default values in your
application* by overriding the
:meth:`Site.get_plugin_configs` or the
:meth:`Site.setup_plugins` method of
your Site class.  For example::

    class Site(Site):

        def get_plugin_configs(self):
            yield super(Site, self).get_plugin_configs()
            yield ('countries', 'country_code', 'BE')
            yield ('contacts', 'hide_region', True)

The old style works also::

    class Site(Site):

        def setup_plugins(self):
            super(Site, self).setup_plugins()
            self.plugins.countries.configure(country_code='BE')
            self.plugins.contacts.configure(hide_region=True)

Note that :meth:`Site.setup_plugins` is called *after*
:meth:`Site.get_plugin_configs`. This can cause unexpected behaviour when you
mix both methods.

As a **system administrator** you can override these configuration
defaults in your project's :xfile:`settings.py` using one of the
following methods:

- by overriding the Site class as described above for application
  developers

- by setting the value directly after instantiation of your
  :setting:`SITE` object.

Another (deprecated) method is by using the :func:`configure_plugin` function.
For example::

    from lino_cosi.lib.cosi.settings import *
    configure_plugin('countries', country_code='BE')
    SITE = Site(globals())

Beware the pitfall: :func:`configure_plugin` must be called *before* the
:setting:`SITE` has been instantiated, otherwise *they will be ignored
silently*.  (It is not easy to prevent accidental calls to it *after*
Site initialization because there are scenarios where you want to
instantiate several `Site` objects.)

Keep in mind that you can indeed never be sure that your :setting:`SITE`
instance is actually being used. A local system admin can always decide to
import your :xfile:`settings.py` module and to re-instantiate your `Site` class
another time. That's part of our game and we don't want it to be forbidden.

