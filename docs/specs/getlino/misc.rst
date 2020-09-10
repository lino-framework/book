.. _getlino.usage:

=============
Miscellaneous
=============

Configuration files
===================

.. xfile:: ~/.getlino.conf
.. xfile:: /etc/getlino/getlino.conf



Multiple database engines on a same server
==========================================

Note that :cmd:`getlino startsite` does not install any db engine because this
is done by :cmd:`getlino configure`.

When you maintain a Lino server, you don't want to decide for each new site
which database engine to use. You decide this once during :cmd:`getlino
configure`. In general, `apt-get install` is called only during :cmd:`getlino
configure`, never during :cmd:`getlino startsite`. If you have a server with
some mysql sites and exceptionally want to install a site with postgres, you
simply call :cmd:`getlino configure` before calling :cmd:`getlino startsite`.

You may use multiple database engines on a same server by running configure
between startsite invocations.

.. _ss:

The ``startsite`` template
==========================

No longer used: the `cookiecutter-startsite
<https://github.com/lino-framework/cookiecutter-startsite>`__ project contains a
cookiecutter template used by :cmd:`getlino startsite`.


Shared virtual environments
===========================

You can run multiple sites on a same :term:`virtualenv`.  That virtualenv is
then called a shared environment.

If you update a shared virtualenv (by activating it and running :xfile:`pull.sh`
of some pip command), the change will affect all sites and you must take special
care for migrating their data if needed.

In a :term:`developer environment` and a :term:`contributor environment` you
usually have a single shared env used by all your sites.  On a :term:`production
server` you usually have no shared-env at all (each production site has its own
env). On a :term:`demo server` you usually hav several shared envs:

- /usr/local/lino/sharedenvs/master
- /usr/local/lino/sharedenvs/stable

You can specify a *default* shared environment with
:option:`getlino configure --shared-env`
:option:`getlino startsite --shared-env`.

Note that :option:`getlino configure --clone`) will install all known framework
repositories into the default shared env.

:cmd:`getlino startsite` does not install any Python packages when a shared env
is used.
