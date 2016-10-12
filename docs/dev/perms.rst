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

Certain objects in Lino have a :attr:`required_roles
<lino.core.permissions.Permittable.required_roles>` attribute which
specifies the user roles required for getting permission to access
this resource.  Where "resource" is one of the following:

- an actor (a subclass of :class:`lino.core.actors.Actor`)
- an action (an instance of :class:`lino.core.actions.Action` or a
  subclass thereof)
- a panel (an instance of :class:`lino.core.layouts.Panel`)

Lino comes with a few built-in user roles whic are defined in
:mod:`lino.core.roles`.

User roles are just class objects which represent conditions for
getting permission to access the functionalities of the application.
They *may* act as a requirement.  Every plugin may define its own user
roles which may inherit from other roles defined by other plugins

For example, the :class:`lino.modlib.users.models.Users` table is
visible only for users who have the :class:`SiteAdmin
<lino.core.roles.SiteAdmin>` role:

>>> from lino.core.roles import SiteUser, SiteAdmin
>>> user = SiteUser()
>>> admin = SiteAdmin()
>>> user.has_required_roles(rt.actors.users.Users.required_roles)
False
>>> admin.has_required_roles(rt.actors.users.Users.required_roles)
True



User types
==========

At some moment, a site administrator needs to assign a role to every
user. But it would be irritating to see all imaginable roles of the
application. Because a real-world application can define *many* user
roles. For example here is an inheritance diagram of the roles used by
:ref:`noi`:

.. inheritance-diagram:: lino_noi.lib.noi.roles
                         
And if you think that above hierarchy is complex, then look at at the
following one (that of :ref:`welfare`)...

.. inheritance-diagram:: lino_welfare.modlib.welfare.roles
 
Not all these user roles are meaningful in practice.

So we need to define a *subset of all available roles* for that
application.  This is done using the :class:`UserTypes
<lino.modlib.users.choicelists.UserTypes>` choicelist.

We now call them user **types** and no longer just user **roles**
because they contain a bit more than a user role.  A user type has the
following fields:

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


About the name: at the beginnings of Lino we called them **user
profiles**, but now we prefer to call them **user types**. The web
interface already calls them "types", but it will take some time to
change all internal names from "profile" to "type".        

>>> rt.show(users.UserTypes)
======= =========== ===============
 value   name        text
------- ----------- ---------------
 000     anonymous   Anonymous
 100     user        User
 900     admin       Administrator
======= =========== ===============
<BLANKLINE>

>>> robin = users.User.objects.get(username='robin')
>>> robin.profile.role  #doctest: +ELLIPSIS
<lino.modlib.office.roles.SiteAdmin object at ...>

And then the :attr:`profile <lino.modlib.users.models.User.profile>`
field of :class:`users.User <lino.modlib.users.models.User>` model is
used to assign such a type to a given user.



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
