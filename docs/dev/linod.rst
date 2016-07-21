.. _dev.linod:

=======================
Running :manage:`linod`
=======================

.. _schedule: https://github.com/dbader/schedule

In a development environment you might want to run :manage:`linod`
when you are developing or testing one of your applications.

Usage for developers
====================

Before running :manage:`linod` for the first time, you need to install
the Python package schedule_ written by Daniel Bader::

    $ . env/bin/activate
    $ pip install schedule
    
Now you simply go to your project directory and invoke the admin
command::

    $ cd ~/projects/mysite
    $ python manage.py linod

This process will run as long as you don't kill it, e.g. until you
hit :kbd:`Ctrl-C`.

What it does
============

The :manage:`linod` command is responsible for running the scheduled
background jobs defined by your application. This includes for
example:

- Send out emails for notifications

- Run nightly maintenance tasks such as :manage:`checkdata` or
  :manage:`checksummaries`.


You can see a list of these jobs by running::

    $ cd ~/projects/mysite
    $ python manage.py linod --list

Applications can register these jobs either using the schedule_ API
directly, but Lino itself differentiates two types of background
tasks: "often" and "daily".  
:func:`dd.api.schedule_often`
:func:`dd.api.schedule_daily`

