========
Glossary
========

.. glossary::

  management command

    See the Django docs about
    `django-admin and manage.py¶
    <https://docs.djangoproject.com/en/3.1/ref/django-admin/>`__
    and
    `Writing custom django-admin commands
    <https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/>`_

.. glossary::
  :sorted:

  customization functions
    See :doc:`/topics/customization`.

  mod_wsgi
   :doc:`/admin/install`

  dummy module
    See :func:`lino.core.dbutils.resolve_app`.

  testing
    The version that is currently being tested.

  DavLink
    See :doc:`/davlink/index`

  WebDAV
    See :doc:`/davlink/index`

  tups
     The machine that served the `saffre-rumma.net`
     domain until 2010
     when it was replaced by :term:`mops`.

  mops
     The machine that is serving the `saffre-rumma.net` domain.

  jana
     An internal virtual Debian server on our LAN used for testing.

  DSBE
     "Dienst für Sozial-Berufliche Eingliederung"
     A public service in Eupen (Belgium),
     the first real user of a Lino application
     :mod:`lino.projects.pcsw`.

  dump
    "To dump" means to write the content of a database into a text file.
    This is used to backup data and for Data Migration.

  data migration

    Data Migration is when your database needs to be converted after
    an upgrade to a newer Lino version. See :doc:`/admin/datamig`.

  CSC
    Context-sensitive ComboBox.
    See :mod:`lino.utils.choices`.

  field lookups
    See https://docs.djangoproject.com/en/3.1/topics/db/queries/#field-lookups

  GC
    Grid Configuration.
    See :blogref:`20100809`,...

  disabled fields
    Fields that the user cannot edit (read-only fields).

  initdb
    See :mod:`lino.management.commands.initdb`

  initdb_tim
    See :mod:`lino.projects.pcsw.management.commands.initdb_tim`

  watch_tim
    A daemon process that synchronizes data from TIM to Lino.
    See :mod:`lino_welfare.modlib.pcsw.management.commands.watch_tim`

  welcome message
     A user-specific message that you get in your main page.  welcome
     messages are being generated dynamically each time your main page
     is being displayed. See :meth:`lino.core.actors.Actor.get_welcome_messages`.


  watch_calendars
    A daemon process that synchronizes remote calendars
    into the Lino database.
    See :mod:`lino.modlib.cal.management.commands.watch_calendars`

  loaddata
    one of Django's standard management commands.
    See `Django docs <http://docs.djangoproject.com/en/2.2/ref/django-admin/#loaddata-fixture-fixture>`_

  makeui
    A Lino-specific Django management command that
    writes local files needed for the front end.
    See :doc:`/topics/qooxdoo`.

  makedocs
    A Lino-specific Django management command that
    writes a Sphinx documentation tree about the models
    installed on this site.
    :mod:`lino.management.commands.makedocs`

  active fields

    See :attr:`dd.Model.active_fields`.

  table

    See :class:`dd.Table` and :class:`dd.AbstractTable`.

  slave table

    A :term:`table` that displays only rows related to a given database object,
    which the slave table calls its :term:`master instance`.

    For example if you have two models `City` and `Person`, with a
    `ForeignKey` `Person.city` pointing to `City`, then you might
    define a slave table `PersonsByCity` which displays only Persons
    who live in a given City.

  master instance

    The database object that acts as master of a :term:`slave table`.

  detail window

    A window that displays data of a single record.  Used for viewing,
    editing or inserting new records.  Besides fields, a Detail Window
    can possibly include :term:`slave tables <slave table>`.

  insert window

    The window used to edit data of a new record before it is being
    saved for the first time.

  GFK

    Generic ForeignKey. This is a ForeignKey that can point to
    different tables.

  minimal application

    See :doc:`/topics/minimal_apps`
