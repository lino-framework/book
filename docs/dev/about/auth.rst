.. _about.auth:

================================
Lino has its own user management
================================

This document explains why Lino replaces Django's user management and permission
system.  See :doc:`/dev/perms` for an introduction to Lino's permission system.
See :doc:`/dev/users` for getting started with user management.

In Lino we opted to replace Django's database-stored user groups and permissions
system by a system that uses pure Python code objects. While Django stores
permissions as rows in the database, in Lino they are entirely defined by the
:term:`application developer` as class-based user roles.

Defining, granting and managing permissions can become a hell when you maintain
a complex application that runs on different sites, with different variants,
different versions. Permission management is complex. Lino doesn't turn it into
something simple, but it brings light into the dark...

We believe that a purely code-based approach is more suitable than information
stored in a database because

- you can use powerful features of the Python language (inheritance,
  modularization, ...)
- every detail and every change is version-controllable and documentable

This radically different approach required us to replace Django's
:mod:`django.contrib.auth` module, including the :class:`User` model, by our own
plugin :mod:`lino.modlib.users`.

Reconciling Lino and Django
===========================

This design decision of course has a price : application code developed for the
Lino framework won't work in plain Django, and applications for Django need a
wrapper for making them usable in Lino. Also they cannot easily be mixed
together. Though there are exceptions, e.g. :mod:`django.contrib.sessions`.

It shouldn't be too difficult to reconcile Lino with Django  by optionally
supporting the standard :mod:`django.contrib.auth` plugin instead of
:mod:`lino.modlib.users`. Next step would be to add an attribute
:attr:`lino.core.actions.Action.required_permissions` and have the
:fixture:`std` fixture generate one Django user group for each :term:`user type`
in Lino.
