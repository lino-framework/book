.. doctest docs/specs/migrate.rst
.. _book.specs.migrate:

================================
Django migrations on a Lino site
================================

Lino applications cannot deliver out-of-the-box Django migrations because the
database schema of a Lino site also depends on local settings. For example the
:class:`languages <lino.core.site.Site.languages>` setting affects your database
structure.  Or you may locally disable a plugin.  Or some plugin options can
cause the structure to change.

Which just means that you must always run :manage:`makemigrations` before
running :manage:`migrate`.

The :xfile:`migrations` directory
=================================

.. xfile:: migrations

Django migrations are automatically enabled on a site when its
:attr:`project_dir <lino.core.site.Site.project_dir>` has a subdirectory named
:xfile:`migrations`. Lino then automatically sets the :class:`migrations_package
<lino.core.site.Site.migrations_package>` to the corresponding Python package
name derived from the :setting:`DJANGO_SETTINGS_MODULE`.

Running :manage:`prep` without Django migrations
================================================

Let's use the :mod:`lino_book.projects.migs` project to play with migrations.

>>> from atelier.sheller import Sheller
>>> shell = Sheller("lino_book/projects/migs")

We begin with Django migrations disabled:

>>> shell("./clean.sh")
Removed migrations and database.

The :manage:`prep` command works also when Django migrations are disabled.' In
this context Django considers all Lino plugins as "unmigrated".  Only some
native Django plugins (contenttypes, sessions, staticfiles) are managed by
Django:

>>> shell("python manage.py prep --noinput")
... #doctest: +ELLIPSIS
`initdb std demo demo2 checksummaries` started on database .../default.db.
Operations to perform:
  Synchronize unmigrated apps: about, appypod, bootstrap3, cal, changes, checkdata, comments, contacts, countries, dashboard, django_mailbox, excerpts, export_excel, extensible, extjs, gfks, github, jinja, lino, lists, mailbox, memo, noi, notify, office, printing, rest_framework, restful, smtpd, staticfiles, summaries, system, tickets, tinymce, uploads, users, userstats, weasyprint, working, xl
  Apply all migrations: contenttypes, sessions
Synchronizing apps without migrations:
...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying sessions.0001_initial... OK
...
Installed 488 object(s) from 17 fixture(s)

Tidy up:

>>> shell("./clean.sh")
Removed migrations and database.

Running :manage:`prep` with Django migrations
=============================================

We enable Django migrations by creating an empty :xfile:`migrations` directory.

>>> shell("mkdir settings/migrations")
<BLANKLINE>

When Django migrations are enabled, the :manage:`prep` command does the same,
but in a different way.  Django now considers all Lino plugins as "migrated":

>>> shell("python manage.py prep --noinput")
... #doctest: +ELLIPSIS
`initdb std demo demo2 checksummaries` started on database .../default.db.
Operations to perform:
  Synchronize unmigrated apps: staticfiles
  Apply all migrations: cal, changes, checkdata, comments, contacts, contenttypes, countries, dashboard, django_mailbox, excerpts, gfks, github, lists, notify, sessions, system, tickets, tinymce, uploads, users, userstats, working
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  ...
Installed 488 object(s) from 17 fixture(s)


>>> from lino import startup
>>> startup("lino_book.projects.migs.settings.demo")
>>> from lino.api.doctest import *

The :term:`application programmer` can see whether Django migrations are enabled
or not by looking at the
:class:`migrations_package <lino.core.site.Site.migrations_package>` site attribute.

>>> print(settings.SITE.migrations_package)
lino_book.projects.migs.settings.migrations

When Django migrations are enabled, Lino automatically fills the
:xfile:`migrations` directory with many subdirectories (one for each installed
plugin) and sets the :setting:`MIGRATION_MODULES` setting.

>>> pprint(settings.MIGRATION_MODULES)
{'about': 'lino_book.projects.migs.settings.migrations.about',
 'appypod': 'lino_book.projects.migs.settings.migrations.appypod',
 'bootstrap3': 'lino_book.projects.migs.settings.migrations.bootstrap3',
 'cal': 'lino_book.projects.migs.settings.migrations.cal',
 'changes': 'lino_book.projects.migs.settings.migrations.changes',
 'checkdata': 'lino_book.projects.migs.settings.migrations.checkdata',
 'comments': 'lino_book.projects.migs.settings.migrations.comments',
 'contacts': 'lino_book.projects.migs.settings.migrations.contacts',
 'countries': 'lino_book.projects.migs.settings.migrations.countries',
 'dashboard': 'lino_book.projects.migs.settings.migrations.dashboard',
 'django_mailbox': 'lino_book.projects.migs.settings.migrations.django_mailbox',
 'excerpts': 'lino_book.projects.migs.settings.migrations.excerpts',
 'export_excel': 'lino_book.projects.migs.settings.migrations.export_excel',
 'extensible': 'lino_book.projects.migs.settings.migrations.extensible',
 'extjs': 'lino_book.projects.migs.settings.migrations.extjs',
 'gfks': 'lino_book.projects.migs.settings.migrations.gfks',
 'github': 'lino_book.projects.migs.settings.migrations.github',
 'jinja': 'lino_book.projects.migs.settings.migrations.jinja',
 'lino': 'lino_book.projects.migs.settings.migrations.lino',
 'lists': 'lino_book.projects.migs.settings.migrations.lists',
 'mailbox': 'lino_book.projects.migs.settings.migrations.mailbox',
 'memo': 'lino_book.projects.migs.settings.migrations.memo',
 'noi': 'lino_book.projects.migs.settings.migrations.noi',
 'notify': 'lino_book.projects.migs.settings.migrations.notify',
 'office': 'lino_book.projects.migs.settings.migrations.office',
 'printing': 'lino_book.projects.migs.settings.migrations.printing',
 'rest_framework': 'lino_book.projects.migs.settings.migrations.rest_framework',
 'restful': 'lino_book.projects.migs.settings.migrations.restful',
 'smtpd': 'lino_book.projects.migs.settings.migrations.smtpd',
 'summaries': 'lino_book.projects.migs.settings.migrations.summaries',
 'system': 'lino_book.projects.migs.settings.migrations.system',
 'tickets': 'lino_book.projects.migs.settings.migrations.tickets',
 'tinymce': 'lino_book.projects.migs.settings.migrations.tinymce',
 'uploads': 'lino_book.projects.migs.settings.migrations.uploads',
 'users': 'lino_book.projects.migs.settings.migrations.users',
 'userstats': 'lino_book.projects.migs.settings.migrations.userstats',
 'weasyprint': 'lino_book.projects.migs.settings.migrations.weasyprint',
 'working': 'lino_book.projects.migs.settings.migrations.working',
 'xl': 'lino_book.projects.migs.settings.migrations.xl'}


Note that the :mod:`lino_book.projects.migs` uses a *settings package* (not a
settings file), so the :xfile:`migrations` directory is under the
:file:`settings` directory, not under the project's root directory.

>>> print(settings.SITE.project_dir)
... #doctest: +ELLIPSIS
/.../lino_book/projects/migs/settings

TODO: write tests to show a :term:`site upgrade` using Django migrations.

.. tidy up before leaving:

  >>> shell("./clean.sh")
  Removed migrations and database.
