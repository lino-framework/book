.. _admin.linod:

===========================
The :manage:`linod` service
===========================

..
    $ python setup.py test -s tests.DocsAdminTests.test_linod

This document explains how to install :manage:`linod` as a service on
a production server.

What's it and do I need it?
===========================

It depends on the application whether is necessary to have
:manage:`linod` running besides the web server.  Applications can
declare background tasks using :func:`dd.schedule_often
<lino.api.dd.schedule_often>` and :func:`dd.schedule_daily
<lino.api.dd.schedule_daily>`.  These tasks will be executed only when
:manage:`linod` is running.

As a system administrator you can check whether an application has
background tasks by issuing::

    $ python manage.py linod --list

For example in the `team` demo project there are 4 tasks:

>>> from atelier.sheller import Sheller
>>> shell = Sheller("lino_book/projects/team")
>>> shell("python manage.py linod --list")
... #doctest: +ELLIPSIS
4 scheduled jobs:
[1] Every 10 seconds do send_pending_emails_often() (last run: [never], next run: ...)
[2] Every 1 day at 20:00:00 do send_pending_emails_daily() (last run: [never], next run: ...)
[3] Every 1 day at 20:00:00 do clear_seen_messages() (last run: [never], next run: ...)
[4] Every 10 seconds do get_new_mail() (last run: [never], next run: ...)

  
  

The :manage:`linod` admin command
=================================

.. management_command:: linod

Starts a long-running process that runs scheduled background tasks.

On a development machine you simply run this in a separate
terminal. On a production server we recommend to run this as a daemon
via Supervisor as described below.

Independently of whether it is being run as a daemon or not, this
command requires the `schedule <https://github.com/dbader/schedule>`__
package which you must install manually::

  $ pip install schedule

Note the nice story of the `schedule` package by its author Dan Bader:
`In Love, War, and Open-Source: Never Give Up
<https://dbader.org/blog/in-love-war-and-open-source-never-give-up>`__



Installation instructions
=========================

- Install the `Supervisor <http://www.supervisord.org/index.html>`_
  package::

      $ sudo apt-get install supervisor

  The supervisor package is being installed system-wide, it is not
  related to any specific project.

- Create a shell script in your project directory::

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
    command=/path/to/myprj/linod.sh
    username = www-data

- Restart :program:`supervisord`::

    $ sudo service supervisor restart

- Have a look at the log files in :file:`/var/log/supervisor`.

