.. doctest docs/dev/users.rst
.. _dev.users:

=========================
User management à la Lino
=========================

This document explains how to get started with Lino's user management
system.
See :doc:`/specs/users`
for a more detailed documentation of the :mod:`lino.modlib.users`
plugin.

.. contents::
    :depth: 1
    :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min1.settings.demo')
>>> from lino.api.doctest import *

Creating a root user
====================

The most Linoish way to create a root user (or a set of demo users) is to run
:manage:`prep`.  This will reset the database to a virgin state and then load
the :fixture:`demo` fixture, which will create our well-known demo users Robin,
Rolf, Romain, Rando, Rik, Ronaldo ... depending on your
:attr:`lino.core.site.Site.languages`.

If you don't want to reset your database, then you can write a script
and run it with :manage:`run`. For example::

    from lino.api.shell import users
    obj = users.User(username="root")
    obj.set_password("1234!")
    obj.full_clean()
    obj.save()



Passwords
=========

Note that the `password` field of a newly created user is empty,
and the account therefore cannot be used to log in.  If you create
a new user manually using the web interface, you must click their
:class:`ChangePassword` action and set their password.

.. # tidy up
  >>> try:
  ...     users.User.objects.get(username="test").delete()
  ... except users.User.DoesNotExist:
  ...    pass


>>> u = users.User(username="test")
>>> u.full_clean()
>>> u.save()

Since we didn't set a `password`, Django stores a "non usable" password, and the
:meth:`User.check_password` method returns `False`:

>>> u.password  #doctest: +ELLIPSIS
'!...'
>>> u.check_password('')
False

>>> u.has_usable_password()
False


When setting the password for a newly created user, leave the
field :guilabel:`Current password` empty.

>>> ses = rt.login('robin')
>>> values = dict(current="", new1="1234", new2="1234")
>>> rv = ses.run(u.change_password, action_param_values=values)
>>> print(rv['message'])
New password has been set for test.

Note that a site administrator (a user having the
:class:`lino.core.roles.SiteAdmin` role) never needs to specify the current
password when setting a new password for any user.
