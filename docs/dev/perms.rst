.. _permissions:

===========
Permissions
===========


..  You can test only this document by issuing:

      $ python setup.py test -s tests.DocsTests.test_perms

    Doctest initialization:

    >>> from lino import startup
    >>> startup('lino_book.projects.min2.settings.demo')
    >>> from lino.api.shell import *


Lino adds enterprise-level concepts for definining permissions. This
includes class-based user roles and a replacement for Django's User
model.

See also: :doc:`users`.


User roles
==========

A **user role** is the role of a user in the system. It tells Lino
whether a given user has permission to see a given resource or to
execute a given action.  For example, a system administrator can see
certain resources which a simple user cannot see.

Lino comes with a few built-in user roles which are defined in
:mod:`lino.core.roles`.

User roles are just class objects which represent conditions for
getting permission to access the functionalities of the application.

Every plugin may define its own user roles.  And then --the most fun--
a role can inherit from one or several other roles.

Just a fictive example::

    from lino.core.roles import SiteUser, SiteAdmin
    
    class Secretary(SiteUser):
        """Can write letters."""

    class Accountant(SiteUser):
        """Can write invoices and read accounting reports."""

    class Director(Secretary, Accountant):
        """Can write letters and invoices, can read accounting and
        statistic reports """

    class MySiteAdmin(Director, SiteAdmin):
        """Can everything, including user management."""
  
A real-world application can define *many* user roles. For example
here is an inheritance diagram of the roles used by :ref:`noi`:

.. inheritance-diagram:: lino_noi.lib.noi.roles
                         
And if you think that above hierarchy is complex, then don't look at
the following one (that of :ref:`welfare`)...

.. inheritance-diagram:: lino_welfare.modlib.welfare.roles
 
Above examples illustrate that *not* every single user role is
meaningful in practice.

So we need to define a *subset of all available roles* for that
application.  This is done using the :class:`UserTypes
<lino.modlib.users.choicelists.UserTypes>` choicelist.


User types
==========

When creating a new user, the site administrator needs to assign a
role to every user. This is done indirectly by setting what we call
the **user type**.

A user *type* contains a bit more information than a user role.  A
user type has the following fields:

- :attr:`role`, a pointer to the user role
- :attr:`text`, a translatable name
- :attr:`value`, a value for storing it in the database

- :attr:`readonly
  <lino.modlib.users.choicelists.UserType.readonly>` defines a user
  type which shows everything that a given user role can see, but
  unlike the original user role it cannot change any data.

- :attr:`hidden_languages
  <lino.modlib.users.choicelists.UserType.hidden_languages>`
  (experimental), a set of languages to *not* show to users of this
  type. This is used on sites with more than three or four
  :attr:`languages <lino.core.site.Site.languages>`.

Here is the default list of user types:
        
>>> rt.show(users.UserTypes)
======= =========== ===============
 value   name        text
------- ----------- ---------------
 000     anonymous   Anonymous
 100     user        User
 900     admin       Administrator
======= =========== ===============
<BLANKLINE>


>>> users.UserTypes.admin
users.UserTypes.admin:900

>>> users.UserTypes.admin.role  #doctest: +ELLIPSIS
<lino.modlib.office.roles.SiteAdmin object at ...>

>>> users.UserTypes.admin.readonly
False

>>> users.UserTypes.admin.hidden_languages


The type of a user is stored in a field whose internal name is
:attr:`profile <lino.modlib.users.models.User.profile>`. This is is
because at the beginnings of Lino we called them **user
profiles**. Now we prefer to call them **user types**. The web
interface already calls them "types", but it will take some time to
change all internal names from "profile" to "type".

>>> robin = users.User.objects.get(username='robin')
>>> robin.profile  #doctest: +ELLIPSIS
users.UserTypes.admin:900
>>> robin.profile.role  #doctest: +ELLIPSIS
<lino.modlib.office.roles.SiteAdmin object at ...>



Defining required roles
=======================

The application programmer specifies which roles are required for a
given resource.

Where "resource" is one of the following:

- an actor (a subclass of :class:`lino.core.actors.Actor`)
- an action (an instance of :class:`lino.core.actions.Action` or a
  subclass thereof)
- a panel (an instance of :class:`lino.core.layouts.Panel`)

All these objects have a :attr:`required_roles
<lino.core.permissions.Permittable.required_roles>` attribute which
specifies the user roles required for getting permission to access
this resource.

For example, the :class:`lino.modlib.users.models.Users` table is
visible only for users who have the :class:`SiteAdmin
<lino.core.roles.SiteAdmin>` role:

>>> users.Users.required_roles
set([<class 'lino.core.roles.SiteAdmin'>])

>>> from lino.core.roles import SiteUser, SiteAdmin
>>> user = SiteUser()
>>> admin = SiteAdmin()
>>> user.has_required_roles(users.Users.required_roles)
False
>>> admin.has_required_roles(users.Users.required_roles)
True



Local customizations
====================

You may have noted that :class:`UserTypes
<lino.modlib.users.choicelists.UserTypes>` is a choicelist, not a
database table.  This is because it depends on the application and is
usually not locally modified.  

Local site administrators may nevertheless decide to change the set of
available user profiles.


The user profiles module
========================

The :attr:`roles_required
<lino.core.permissions.Permittable.roles_required>` attribute is being
ignored when :attr:`user_types_module
<lino.core.site.Site.user_types_module>` is empty.


.. xfile:: roles.py

The :xfile:`roles.py` is used for both defining roles and profiles the
user roles that we want to make available in a given application.
Every profile is assigned to one and only one user role. But not every
user role is made available for selection in the




.. _debug_permissions:

Permission debug messages
-------------------------

Sometimes you want to know why a given action is available (or not
available) on an actor where you would not (or would) have expected it
to be.

In this situation you can temporarily set the `debug_permissions`
attributes on both the :attr:`Actor <lino.core.actors.Actor.debug_permissions>` and
the :attr:`Action <lino.core.actions.Action.debug_permissions>` to True.

This will cause Lino to log an info message for each invocation of a
handler on this action.

Since you probably don't want to have this feature accidentally
activated on a production server, Lino will raise an Exception if this
happens when :setting:`DEBUG` is False.
