=======================
The ``getlino`` package
=======================

The :mod:`getlino` package greatly helps with installing Lino to your computer.
But it is still work in progress, so use it only for testing purposes. If you
just want to quickly try a Lino, read :doc:`/dev/quick/install`.

Content moved to :ref:`getlino`.



.. _ss:

The ``startsite`` template
==========================

The `cookiecutter-startsite
<https://github.com/lino-framework/cookiecutter-startsite>`__ project contains
a cookiecutter template used by :cmd:`getlino startsite`.


Notes
=====

When you maintain a Lino server, then you don't want to decide for each new
site which database engine to use. You decide this once for all during
:cmd:`getlino configure`. In general, `apt-get install` is called only during
:cmd:`getlino configure`, never during :cmd:`getlino startsite`. If you have a
server with some mysql sites and exceptionally want to install a site with
postgres, you simply call :cmd:`getlino configure` before calling
:cmd:`getlino startsite`.
