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

A :term:`site administrator` can select :menuselection:`Site --> Active
sessions` to open the :class:`Sessions` table and to see who is currently
working on this site.

This feature is popular on production sites with relatively few users (less than
100), It requires the database back-end for managing sessions,  which is the
default behaviour for a Lino site (Lino site maintainers usually don't need to
care about `How to use sessions
<https://docs.djangoproject.com/en/3.1/topics/http/sessions/>`__).

Note that :term:`user sessions <user session>` are deleted only when the user
logs out explicitly. When a user just closes their browser on one device and
logs in from a different device, they get a second session, and their first
session will remain in the database. Don't expect Lino to remove this session
automatically because after all the user might open their first browser again
after some time and expect Lino to remember them. On the other hand, no website
remembers users forever. Sessions have a given time to live, and they *expire*
after that time. The site maintainer can configure how long Lino should remember
user sessions.

Limit the number of simultaneous user sessions
==============================================

A :term:`hosting provider` can base the pricing of their hosting service on a
:term:`sessions limit`, i.e. a maximum number of allowed :term:`user sessions
<user session>`.

An :term:`end user` might potentially get a message "There are more than X
active user sessions. Please try again later" when trying to to log in on a site
with a :term:`sessions limit`.

The :term:`site maintainer` can configure this value by setting the
:attr:`active_sessions_limit <lino.modlib.users.Plugin.active_sessions_limit>`
setting of the :mod:`lino.modlib.users` plugin.


Cleaning up inactive user sessions
==================================

The default value for :setting:`SESSION_COOKIE_AGE` is two weeks. This means
that user sessions can remain in the database for two weeks even when the user
doesn't actually work in Lino.

*Expired* sessions are never shown in this table, but

The *Last activity* column in the table is important because


That's why a site operator with a :term:`sessions limit` can experience "false
alerts", i.e. Lino would say "There are more than X active user sessions. Please
try again later" although in reality these users aren't actively working on the
site.

There are several methods to handle these situations:

- Reduce the value of :setting:`SESSION_COOKIE_AGE`, e.g. two days instead
  of two weeks.
- Instruct users to explicitly log out when they don't use Lino.
- Increase the :term:`sessions limit`.
- Have the site administrator check :menuselection:`Site --> Active
  sessions` and manually kill some sessions.


Concepts
========

The following concepts have been covered by this documentation page.

.. glossary::

  sessions limit

    The maximum number of simultaneous :term:`user sessions <user session>`
    that are allowed on a Lino site.

  user session

    A database entry that is automatically created when a given :term:`user`
    logs in from a given device or browser.
