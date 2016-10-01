.. _dev.plugins:

=======================
Introduction to plugins
=======================

Besides the :class:`Site <lino.core.site.Site>` class (which
encapsules what *Lino* calls an :doc:`application <application>`),
Lino defines a :class:`Plugin <lino.core.plugin.Plugin>` class which
extends what *Django* calls an "application".

The :class:`Plugin <lino.core.plugin.Plugin>` class is comparable to
Django's `AppConfig
<https://docs.djangoproject.com/en/1.8/ref/applications/>`_ class, but
has some advantages over Django's approach which makes that they are
the preferred way.  It was developed and used before Django 1.7.  We
are still working (:ticket:`38`) on the question on whether it makes
sense to reconcile both approaches.

.. contents::
  :local:


Defining plugins
================

Application developers usually define a subclass of :class:`Plugin
<lino.core.plugin.Plugin>` in the :xfile:`__init__.py` file of every
plugin.  Here is a fictive example::

    from lino.api import ad, _
    
    class Plugin(ad.Plugin):
        verbose_name = _("Better calendar")
        extends = 'lino.modlib.cal'
        needs_plugins  = ['lino_xl.lib.contacts']

        def setup_main_menu(self, site, profile, m):
            m = m.add_menu(self.app_label, self.verbose_name)
            m.add_action('cal.Teams')
            m.add_action('cal.Agendas')


Some interesting plugin attributes are

- :attr:`needs_plugins <lino.core.plugin.Plugin.needs_plugins>`
- :attr:`extends_models <lino.core.plugin.Plugin.extends_models>`
- :attr:`site_js_snippets <lino.core.plugin.Plugin.site_js_snippets>`
- :meth:`setup_main_menu <lino.core.plugin.Plugin.setup_main_menu>`




Accessing plugins
=================

Django developers are used to code like this::

    from myapp.models import Foo

    def print_foo(pk=1):
        print(Foo.objects.get(pk=pk))


In Lino we recommend to use the :attr:`lino.api.rt.models` dict as
follows::

    from lino.api import rt

    def print_foo(pk=1):
        Foo = rt.modules.myapp.Foo
        print(Foo.objects.get(pk=pk))

At least if you want to use :doc:`plugin_inheritance`. One of the
basic assumptions of this feature is that users of some plugin can
extend it and use their extension instead of the original plugin.
Which means that the plugin developer does not know (and does not
*want* to know) where the model classes are actually defined.

Note that :attr:`rt.models <lino.api.rt.models>` is populated only
*after* having imported the models. So you cannot use it at the
module-level namespace of a :xfile:`models.py` module.  For example
the following variant of above code **would not work**::

    from lino.api import rt
    Foo = rt.modules.foos.Foo  # error `AttrDict has no item "foos"`
    def print_foo(pk=1):
        print(Foo.objects.get(pk=pk))

Neither would work (after :ticket:`576`) something like::

    def print_foo(pk=1):
        from lino.api.rt.models.myapp import Foo
        print(Foo.objects.get(pk=pk))



Configuring plugins
===================

As an application developer you can specify *in your application* that
you want to configure certain plugins by overriding the
:meth:`lino.core.site.Site.setup_plugins` method.

You should do this by overriding the :meth:`setup_plugins
<lino.core.site.Site.setup_plugins>` method of your Site class.  For
example::

    from lino_book.projects.std.settings import Site

    class Site(Site):

        def setup_plugins(self):
            super(Site, self).setup_plugins()
            self.plugins.countries.configure(country_code='BE')


As a system administrator you can override these configuration
defaults in your project's :xfile:`settings.py` using one of the
following methods:

- by overriding the Site class as described above for application developers

- using the :func:`configure_plugin <lino.core.site.configure_plugin>` function.

  For example, if you want to set the :attr:`country_code
  <lino_xl.lib.countries.Plugin.country_code>` of
  :mod:`lino_xl.lib.countries` to `'DE'`::

    from lino_cosi.projects.apc.settings import *
    configure_plugin('countries', country_code='DE')
    SITE = Site(globals())

  Beware the pitfall: :func:`configure_plugin
  <lino.core.site.configure_plugin>` must be called *before* the
  :setting:`SITE` has been instantiated, otherwise *they will be
  ignored silently*.  (It is not easy to prevent accidental calls to
  *after* Site initialization because there are scenarios where you
  want to instantiate several `Site` objects.)

- by setting the value directly after instantiation of your
  :setting:`SITE` object.

Keep in mind that you can indeed never be sure that your
:setting:`SITE` instance is actually being used. A local system admin
can always decide to import your :xfile:`settings.py` module and the
reinstantiate your `Site` class another time. That's part of our game
and we don't want it to be forbidden.

Uncomplete list of configurable plugin attributes:

- :attr:`lino_xl.lib.countries.Plugin.country_code` 
- :attr:`lino_xl.lib.contacts.Plugin.hide_region`

See also :doc:`/admin/settings`.


