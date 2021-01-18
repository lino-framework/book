.. doctest docs/dev/sessions.rst
.. _dev.sessions:

=============
User sessions
=============

.. currentmodule:: lino.modlib.users

The :mod:`lino.modlib.users` plugin also provides functionality for monitoring
user sessions.

.. contents::
    :depth: 1
    :local:


See who is working on my site
=============================

A :term:`site administrator` can select :menuselection:`Site --> User sessions`
to open the :class:`Sessions` table, which shows who is currently working on
this site.

This feature is popular on production sites with relatively few users (less than
100), It requires the database back-end for managing sessions,  which is the
default behaviour for a Lino site (Lino site maintainers usually don't need to
care about `How to use sessions
<https://docs.djangoproject.com/en/3.1/topics/http/sessions/>`__).

Limit the number of simultaneous user sessions
==============================================

A :term:`hosting provider` can base the pricing of their hosting service on a
:term:`sessions limit`, i.e. a maximum number of allowed :term:`user sessions
<user session>`.

The :term:`site maintainer` can configure this value by setting the
:attr:`active_sessions_limit <lino.modlib.users.Plugin.active_sessions_limit>`
setting of the :mod:`lino.modlib.users` plugin.

An :term:`end user` might potentially get a message "There are more than X
active user sessions. Please try again later" when trying to to log in on a site
with a :term:`sessions limit`.


Dangling user sessions
======================

User sessions can remain in the database even when the user doesn't actually
need them any more.  We call them :term:`dangling sessions <dangling session>`.

Don't mix up :term:`dangling sessions <dangling session>` with **expired**
sessions.  Sessions have a given time to live, and they *expire* after that
time. Expired sessions are never shown in the :class:`Sessions` table and aren't
taken into account for the :term:`sessions limit`. Besides using up database
space they don't disturb. Django has an admin command to clean up these
periodically (`Clearing the session store
<https://docs.djangoproject.com/en/3.1/topics/http/sessions/#clearing-the-session-store>`__).
The site maintainer can configure how long Lino should remember user sessions
with the :setting:`SESSION_COOKIE_AGE` setting. The default value for this
setting is two weeks.

Dangling sessions can cause "false alerts" on a site with a :term:`sessions
limit`, i.e. Lino would say "There are more than X active user sessions. Please
try again later" although "in reality" these users aren't actively working on
the site.

Dangling sessions can come because :term:`user sessions <user session>` are
deleted only when the user logs out explicitly. When a user just closes their
browser on one device and logs in from another device, they get a second
session, and their first session will remain in the database. Don't expect Lino
to remove this session automatically because after all the user might open their
first browser again after some time and expect Lino to remember them. Other
possible reasons for dangling sessions are browsers having the option "Delete
cookies and site data when browser is closed", or private browser sessions.  We
have seen situations where one user had more than 1000 dangling sessions.

To help with detecting dangling sessions, Lino adds the *Last activity* column
in the :class:`Sessions` table.  When you see a session with last activity 4
days ago, you may probably assume that it is a :term:`dangling session`.

There are several ways to handle false :term:`sessions limit` alerts:

- Reduce the value of :setting:`SESSION_COOKIE_AGE`, e.g. two days instead
  of two weeks.
- Set :setting:`SESSION_EXPIRE_AT_BROWSER_CLOSE` to `True` so that sessions expire
  when the browser closes.
- Instruct users to explicitly log out when they don't use Lino.
- Increase the :term:`sessions limit`.
- Have the site administrator check :menuselection:`Site --> Active
  sessions` and manually kill some dangling sessions.

Interactively testing session behaviour
=======================================

As a developer you can use the :mod:`lino_book.projects.apc` project to
interactively explore how Lino behaves regarding sessions. The
:file:`settings/__init__.py` contains some comments. The project also contains a
script :file:`show_sessions.py` to be run using the :manage:`run` admin
command::

  $ pm run show_sessions.py


Concepts
========

The following concepts have been covered by this documentation page.

.. glossary::

  sessions limit

    The maximum number of simultaneous :term:`user sessions <user session>`
    that are allowed on a Lino site.

  dangling session

    A :term:`user session` that is not yet expired, but isn't being used
    actively.

  user session

    A database entry that is automatically created when a given :term:`user`
    logs in from a given device or browser.
