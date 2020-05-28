.. doctest docs/admin/config_dirs.rst
.. _config_dirs:

=======================================
Introduction to ``config``  directories
=======================================


.. contents::
    :depth: 2
    :local:


.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.confdirs.settings')
>>> from lino.api.doctest import *


The local configuration directory
=================================

.. glossary::

  local configuration directory

    A :xfile:`config` directory on a :term:`Lino site` that contains locally
    customized template files.


How to make local print templates editable by end users
=======================================================

Some end users want to be able to configure themselves certain templates.

First step : make a local copy of the relevant templates::

  $ go mysite
  $ cp -a env/lib/python3.6/site-packages/lino_xl/lib/sales/config .

Second step: make the local config directory accessible to the end user via SSH
or WebDAV or any other method.


.. xfile:: config

Lino has a concept of configuration directories that are a bit like Django's
`templates` directories.


Creating a desktop link to the local configuration directory
============================================================

A :term:`site operator` may designate a **template manager** who is responsible
for managing the files in the local configuration directory.

The template manager should have a **link on their desktop** so that
they can easily access the configuration directory using their GUI
file manager.

The directory to be shared is the :xfile:`config` subdirectory of the
:attr:`cache_dir <lino.core.site.Site.cache_dir>`,
which usually is the same as the *project directory* for production sites.

Lino does not create this directory automatically. If you want to use local
templates, the :term:`site maintainer` must create that directory and make sure
that the Lino web server process has write permission to it.


If the template manager has an **Ubuntu desktop** with the default
files manager, then it is easy:

- Open *Files* manager
- Select :menuselection:`File --> Connect to server`
- As the Server Address type something like::

    sftp://admin@123.456.78.90/path/to/mysite/config

Otherwise consult the documentation of your file manager.  If appropriate you
might write instructions and contribute them so that we can add them here.


Typical workflow
================

Here is a typical workflow for a local template optimization.

- Some user wants some change in a printed output.

- The template manager needs to know a database object that serves as
  example.

- Figure out how to clear the cache and rebuild the printable document
  without creating useless database content such as new excerpts.

- Find out which file is being used as template. Look at the
  :xfile:`lino.log` if you have no idea where to start.

- Create a backup copy of the template file.

- Make some change, save the template file, rebuild the printable.

- When you are satisfied, remove the backup file.


Implementation details
======================

- :attr:`lino.core.site.Site.cache_dir`
- :mod:`lino.utils.config`
