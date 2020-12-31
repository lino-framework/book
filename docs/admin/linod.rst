.. doctest docs/admin/linod.rst
.. _admin.linod:

===============
The Lino Daemon
===============

This document explains why and how to use :manage:`linod`.

A :term:`Lino application` can declare background tasks. Such tasks run in the
background, i.e. as a service in another process than the web server. That other
process runs a Lino specific admin command called :manage:`linod`.

.. management_command:: linod

Starts a long-running process that runs scheduled background tasks.

On a development machine you simply run this in a separate terminal. On a
production server we recommend to run this as a daemon via Supervisor as
described below.

This feature requires `Dan Bader <https://dbader.org/about/>`__'s `schedule
<https://github.com/dbader/schedule>`__  package, which will get installed
automatically if you run :manage:`install`.

As an :term:`application developer` you define background tasks using
:func:`dd.schedule_often <lino.api.dd.schedule_often>` and
:func:`dd.schedule_daily <lino.api.dd.schedule_daily>`.  For example the
:func:`send_pending_emails_often <lino.modlib.notify.send_pending_emails_often>`
and :func:`clear_seen_messages <lino.modlib.notify.clear_seen_messages>` of the
:mod:`lino.modlib.notify` plugin.



:attr:`use_linod <lino.core.site.Site.use_linod>`

To enable this feature, you must set :attr:`use_linod
<lino.core.site.Site.use_linod>` to `True`.   This is usually done by the
application developer, but this decision can be overridden by a system admin in
a local :xfile:`settings.py` file. The :manage:`linod` command will simply do
nothing when this setting is `False`.

Additionally to having :attr:`use_linod <lino.core.site.Site.use_linod>` set to
`True`, you must also start the :manage:`linod` service in order to actually
execute the scheduled tasks.  The :cmd:`getlino configure --linod` option
specifies that every new Lino site will automatically have a :xfile:`linod.sh`
file in its project directory and a supervisor job that runs the
:xfile:`linod.sh` script as a service.


Activating the feature
======================

>>> from atelier.sheller import Sheller
>>> shell = Sheller("lino_book/projects/roger")
>>> shell("python manage.py linod --list")
This site does not use linod.

As a :term:`site maintainer` you can check whether your application has
scheduled background jobs by issuing the following command in your project
directory::

    $ python manage.py linod --list

For example in the :mod:`noi1e <lino_book.projects.noi1e>` demo project
there are 7 jobs:

>>> shell = Sheller("lino_book/projects/noi1e")
>>> shell("python manage.py linod --list")
... #doctest: +ELLIPSIS
7 scheduled jobs:
[1] Every 1 day at 20:00:00 do checksummaries() (last run: [never], next run: ...)
[2] Every 1 day at 20:00:00 do checkdata() (last run: [never], next run: ...)
[3] Every 10 seconds do send_pending_emails_often() (last run: [never], next run: ...)
[4] Every 1 day at 20:00:00 do send_pending_emails_daily() (last run: [never], next run: ...)
[5] Every 1 day at 20:00:00 do clear_seen_messages() (last run: [never], next run: ...)
[6] Every 3600 seconds do update_all_repos() (last run: [never], next run: ...)
[7] Every 10 seconds do get_new_mail() (last run: [never], next run: ...)



Installation instructions
=========================

This section has become useless because these things are now done automatically
by :ref:`getlino`.

- Install the `Supervisor <http://www.supervisord.org/index.html>`_
  package::

      $ sudo apt install supervisor

  The supervisor package is being installed system-wide, it is not
  related to any specific project.

- Create a shell script :xfile:`linod.sh` in your project directory::

    #!/bin/bash
    set -e  # exit on error
    cd /path/to/myprj
    . env/bin/activate
    exec python manage.py linod

  Note: the `exec
  <http://wiki.bash-hackers.org/commands/builtin/exec>`_ command is
  needed here in order to avoid :ticket:`1086`. Thanks to `Paul
  Lockaby
  <https://lists.supervisord.org/pipermail/supervisor-users/2016-July/001636.html>`_

- Create a file :file:`linod_myprj.conf` in
  :file:`/etc/supervisor/conf.d/` with this content::

    [program:linod_myprj]
    command = /path/to/myprj/linod.sh
    username = www-data
    umask = 002

- Restart :program:`supervisord`::

    $ sudo service supervisor restart

- Have a look at the log files in :file:`/var/log/supervisor`.
