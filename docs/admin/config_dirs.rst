.. doctest docs/admin/config_dirs.rst
.. _config_dirs:

=======================================
Introduction to ``config``  directories
=======================================

Lino has a concept of configuration directories that are a bit like Django's
`templates` directories.

.. contents::
    :depth: 2
    :local:


.. include:: /../docs/shared/include/tested.rst

>>> import os
>>> os.environ['LINO_CACHE_ROOT'] = '' # disable for this doctest
>>> from lino import startup
>>> startup('lino_book.projects.confdirs.settings')
>>> from lino.api.doctest import *

Concepts
========

.. xfile:: config

  A directory named ``config`` that is collected at startup into a list of
  directories to be searched when looking for configuration files.

.. glossary::

  plugin configuration directory

    A :xfile:`config` directory in the source directory of a plugin.

  site configuration directory

    A :xfile:`config` directory in the project directory of a :term:`Lino site`.

  local configuration directory

    A :term:`site configuration directory` that contains locally
    customized template files.


Site config dirs are search before plugin config dirs.

>>> settings.SITE.confdirs  #doctest: +ELLIPSIS
<lino.utils.config.ConfigDirCache object at ...>

>>> for cd in settings.SITE.confdirs.config_dirs:
...     print(cd.name, cd.writeable)  #doctest: +ELLIPSIS
/.../book/lino_book/projects/confdirs/config True
/.../xl/lino_xl/lib/contacts/config False
/.../lino/lino/modlib/users/config False
/.../lino/lino/modlib/printing/config False
/.../lino/lino/modlib/extjs/config False
/.../lino/lino/modlib/bootstrap3/config False
/.../lino/lino/modlib/jinja/config False
/.../lino/lino/config False


The local configuration directory
=================================

All configuration directories are read-only (maintained by the :term:`application
developer`) except one: the :term:`local configuration directory`.

>>> rt.find_config_file('admin_main.html')  #doctest: +ELLIPSIS
'.../lino_book/projects/confdirs/config/admin_main.html'

How to make local print templates editable by end users
=======================================================

Some end users want to be able to configure themselves certain templates.

First step : make a local copy of the relevant templates::

  $ go mysite
  $ cp -a env/lib/python3.6/site-packages/lino_xl/lib/sales/config .

Second step: make the local config directory accessible to the end user via SSH
or WebDAV or any other method.


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

The :mod:`lino_book.projects.apc` demo project has a site config dir.
This is our demo case of a local config dir.
When the
apc tests were run on travis (i.e. :envvar:`LINO_CACHE_ROOT` is set), Lino
forgot to add the apc site's config dir to its list of config dirs.  Another
problem was that these "non-local site config dirs" (for which apc on travis is
the only example) must come before the plugin config dirs. See :xfile:`config`.
