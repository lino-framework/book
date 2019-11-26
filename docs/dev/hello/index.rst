.. doctest docs/dev/hello/index.rst
.. _lino.tutorial.hello:

=============================
Your first local Lino project
=============================

.. doctest init::

    >>> from atelier.sheller import Sheller
    >>> shell = Sheller('docs/dev/hello')


In this tutorial we are going to have a deeper look at what happened
when you installed Lino as described in :doc:`/dev/install/index`.

.. contents::
    :depth: 1
    :local:


Project directories
===================

.. xfile::  ~/lino/lino_local

This is your **projects root**, which will hold all the Lino sites on your
computer.  Lino project directories are not very big, and you will hopefully
create many such projects and want to keep a backup of them.

.. xfile::  ~/lino/lino_local/first

The project directory of the first site you created in
:doc:`/dev/install/index`.

A **project directory** is a directory that contains a runnable Django project.
It contains the files necessary for that specific instance of a given Lino
application.



The ``settings.py`` file
========================

Your first :xfile:`settings.py` file should look as follows:

.. literalinclude:: settings.py

Explanations:

#.  :mod:`lino_book.projects.min1` is one of the out-of-the-box
    projects included in the Lino Book. Actually it is the first of a
    series of projects which is documented in
    :doc:`/specs/projects/min`.

    We import these settings directly into our global namespace using
    the wildcard ``*``. This is necessary because that's how Django
    wants settings.

#.  Then comes the important trick which turns your Django project
    into a Lino application::

       SITE = Site(globals(), ...)

    That is, you *instantiate* a :class:`Site <lino.core.site.Site>`
    class and store this object as :setting:`SITE` in your Django
    settings. This line will automatically install default values for
    all required Django settings (e.g. :setting:`DATABASES` and
    :setting:`LOGGING`) into your global namespace.

You might add ``DEBUG = True`` or other settings of your choice
*after* these two lines, but it is not necessary here.

More about this in :doc:`/dev/settings`.


The ``manage.py`` file
=======================

Now add a :xfile:`manage.py` file with the following content:

.. literalinclude:: manage.py

A :xfile:`manage.py` does two things: it sets the
:envvar:`DJANGO_SETTINGS_MODULE` environment variable and then calls
Django's `execute_from_command_line` function.

This is plain traditional Django know-how.  There are many opinions,
tricks, flavors and conventions about Django's :xfile:`manage.py`
files, partly for historical reasons.  Lino does not add any tricks to
the :xfile:`manage.py` file, so you can use your own flavour if you
prefer.


Loading initial data into your database
=======================================

Next we create your database and populate it with some demo
content. With a Lino application this is easier than with a plain
Django project, it is just one command to type::

    $ python manage.py prep

The :manage:`prep` command is a `custom django-admin command
<https://docs.djangoproject.com/en/1.9/howto/custom-management-commands/>`_
provided by Lino.  It is just a thin wrapper which calls :manage:`initdb` with
the application's :ref:`demo_fixtures` as argument. It will ask you::

    INFO Started manage.py prep (using settings) --> PID 28463
    We are going to flush your database (.../default.db).
    Are you sure (y/n) ?

If you answer "y" here, then Lino will delete everything in the given
database and replace it with its "factory default" demo data.  Yes,
that's what we want. So go on and type ``y``.

The output that follows should look like this:

>>> shell("python manage.py prep --noinput")
... #doctest: +ELLIPSIS +REPORT_UDIFF
`initdb std demo demo2` started on database .../hello/default.db.
Operations to perform:
  Synchronize unmigrated apps: about, bootstrap3, cal, checkdata, contacts, countries, export_excel, extjs, gfks, jinja, lino, office, printing, staticfiles, system, users, xl
  Apply all migrations: contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Creating table system_siteconfig
    Creating table users_user
    Creating table users_authority
    Creating table countries_country
    Creating table countries_place
    Creating table contacts_partner
    Creating table contacts_person
    Creating table contacts_companytype
    Creating table contacts_company
    Creating table contacts_roletype
    Creating table contacts_role
    Creating table gfks_helptext
    Creating table checkdata_problem
    Creating table cal_dailyplannerrow
    Creating table cal_remotecalendar
    Creating table cal_room
    Creating table cal_eventtype
    Creating table cal_guestrole
    Creating table cal_calendar
    Creating table cal_subscription
    Creating table cal_task
    Creating table cal_eventpolicy
    Creating table cal_recurrentevent
    Creating table cal_event
    Creating table cal_guest
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying sessions.0001_initial... OK
Loading data from .../lino_xl/lib/contacts/fixtures/std.py
Loading data from .../lino/modlib/gfks/fixtures/std.py
Loading data from .../lino_xl/lib/cal/fixtures/std.py
Loading data from .../lino/modlib/users/fixtures/demo.py
Loading data from .../lino_xl/lib/countries/fixtures/demo.py
Loading data from .../lino_xl/lib/contacts/fixtures/demo.py
Loading data from .../lino_xl/lib/cal/fixtures/demo.py
Loading data from .../lino/modlib/users/fixtures/demo2.py
Loading data from .../lino_xl/lib/cal/fixtures/demo2.py
Installed ... object(s) from ... fixture(s)


Lino applications make abundant use of what we call *Python fixtures*
in order to have a rich set of "demo data".  We will come back to this
in :doc:`/dev/initdb`.



Start the web server
====================

Now you can invoke :manage:`runserver` to start the development
server::

  $ python manage.py runserver

which should output something like::

  Validating models...
  0 errors found
  Django version 1.4.5, using settings 'hello.settings'
  Development server is running at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.

And then point your web browser to http://127.0.0.1:8000 and you
should see something like this:

.. image:: hello1.png

Congratulations! Enjoy the first Lino application that exists only on
your machine!


Visualizing database content from the command-line
==================================================

The :manage:`runserver` command starts a web server and lets you
interact with the database through the web interface. But Django also
offers a :manage:`shell` interface.
We will come back to this later, for the moment just try the following.

You can visualize the content of your database from the command-line
without starting a web server using Lino's :manage:`show` command.
For example to see the list of users, you can write::

    $ python manage.py show users.Users

The output should be as follows:

>>> shell("python manage.py show users.AllUsers")
... #doctest: +ELLIPSIS
========== ===================== ============ ===========
 Username   User type             First name   Last name
---------- --------------------- ------------ -----------
 robin      900 (Administrator)   Robin        Rood
========== ===================== ============ ===========

Or you can see the list of countries:

>>> shell("python manage.py show countries.Countries")
... #doctest: +ELLIPSIS
============================= ==========
 Designation                   ISO code
----------------------------- ----------
 Belgium                       BE
 Congo (Democratic Republic)   CD
 Estonia                       EE
 France                        FR
 Germany                       DE
 Maroc                         MA
 Netherlands                   NL
 Russia                        RU
============================= ==========


Exercises
=========

You can now play around by changing things in your project.

#.  In your :file:`settings.py` file, replace
    :mod:`lino_book.projects.min2` by :mod:`lino_book.projects.liina`.
    Run :command:`python manage.py prep` followed by :command:`python
    manage.py runserver`. Log in and play around.

#.  Same as previous, but with :mod:`lino_book.projects.chatter`

#.  Write three descriptions in LibreOffice `.odt` format, one for
    each of the applications you just saw: what it can do, what are
    the features, what functionalities are missing. Use screenshots.
    Use a language which can be understood by non-programmers.  Send
    these documents to your mentor.

#.  Read the documentation about the following Site attributes and
    try to change them:

    - :attr:`is_demo_site <lino.core.site.Site.is_demo_site>`
    - :attr:`languages <lino.core.site.Site.languages>`
