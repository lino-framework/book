.. doctest docs/specs/users.rst
.. _specs.users:

===========================
``users`` : user management
===========================

.. currentmodule:: lino.modlib.users

This document describes the :mod:`lino.modlib.users` plugin, which in Lino
replaces :mod:`django.contrib.auth`. See also :doc:`/dev/users` for getting
started with user management.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

Code examples in this document use the :mod:`lino_book.projects.min1` demo
project:

>>> from lino import startup
>>> startup('lino_book.projects.min1.settings.doctests')
>>> from lino.api.doctest import *

Concepts
========

.. glossary::

  user

    A human person who can sign in on this site.

  user type

    The type of a :term:`user`, mostly used to determine the permissions granted
    to this user. See `User types`_.

  authority

    The fact that one user gives another user the right to "represent" them,
    i.e. to act in their name.


Users
=====

If you wonder why Lino replaces Django's user management and permission system,
see :doc:`/dev/about/auth`.

The :term:`site administrator` can optionally specify a date when a user
started or stopped to be active.



.. class:: Users

    Base class for all tables of :class:`User`.

.. class:: AllUsers

    Shows the list of all users on this site.

.. class:: UsersOverview

    A variant of :class:`Users` showing only active users and only some
    fields.  This is used on demo sites in :xfile:`admin_main.html` to
    display the list of available users.

.. class:: User

    Django model used to represent a :term:`user`.

    .. attribute:: authenticated

        No longer used. See as :attr:`is_authenticated`.

    .. attribute:: is_authenticated

        This is always `True`.  Compare with
        :attr:`AnonymousUser.is_authenticated
        <lino.modlib.users.utils.AnonymousUser.authenticated>`.

   Fields:

    .. attribute:: username

        Must be unique and cannot be empty.

    .. attribute:: initials

        The nickname or initials of this user. This does not need to
        be unique but should provide a reasonably identifying
        function.

    .. attribute:: user_type

        The user_type of a user is what defines her or his permissions.

        Users with an empty `user_type` field are considered inactive and
        cannot log in.

        See also :doc:`/dev/perms`.


    .. attribute:: partner

        Pointer to the :class:`Partner
        <lino_xl.lib.contacts.models.Partner>` instance related to
        this user.

        Every user account can optionally point to a partner instance
        which holds extended contact information. One partner can have
        more than one user accounts.

        This is a :class:`DummyField` when :mod:`lino_xl.lib.contacts`
        is not installed or when User is a subclass of :class:`Partner
        <lino_xl.lib.contacts.models.Partner>` .

    .. attribute:: person

        A virtual read-only field which returns the :class:`Person
        <lino_xl.lib.contacts.Person>` MTI child of the :attr:`partner` (if it
        exists) and otherwise `None`.

    .. attribute:: last_login

        Not used in Lino.

    .. method:: __str__(self)

        Returns either the initials or :meth:`get_full_name`.

    .. method:: get_full_name(self)

        Return the first_name plus the last_name, with a space in
        between. If both fields are empty, return the :attr:`initials`
        or the :attr:`username`.

    .. method:: def get_row_permission(self, ar, state, ba)

        Only system managers may edit other users.
        See also :meth:`disabled_fields`.

        One exception is when AnonymousUser is not readonly. This
        means that we want to enable online registration. In this case
        everybody can modify an unsaved user.

    .. attribute:: end_date
    .. attribute:: start_date

        If :attr:`start_date` is given, then the user cannot sign in
        before that date.  If :attr:`end_date` is given, then the user
        cannot sign in after that date.

        These fields are also used for :doc:`userstats`.


Authorities : let other users work in your name
===============================================

.. class:: Authority

    Django model used to represent a :term:`authority`.

    .. attribute:: user

        The user who gives the right of representation. author of this
        authority

    .. attribute:: authorized

        The user who gets the right to represent the author


User types
==========

.. class:: UserTypes

    The list of user types available in this application.

    You can see the user types available in your application via
    :menuselection:`Explorer --> System --> User Types`.

    Every application should define at least three named user types:

    .. attribute:: anonymous

    .. attribute:: user

    .. attribute:: admin


.. class:: UserType

    Base class for all user types.
    Any instance if this represents a possible :term:`user type`.

    .. attribute:: role

        The role of users having this type. This is an instance of
        :class:`<lino.core.roles.UserRole>` or some subclass thereof.

    .. attribute:: readonly

        Whether users of this type get only write-proteced access.

    .. attribute:: hidden_languages

        A subset of :attr:`languages<lino.core.site.Site.languages>`
        which should be hidden for users of this type.  Default value
        is :attr:`hidden_languages<UserTypes.hidden_languages>`.  This
        is used on multilingual sites with more than 4 or 5 languages.

    .. method:: context(self)

        Return a context manager so you can write code to be run with
        this as `the current user type`_::

          with UserTypes.admin.context():
              # some code

User roles and their usage
==========================

.. class:: UserRoles

Shows a list of the user roles used in this application together with the user
type that have them.

This table can help when designing the list of user types and what permissions
each of them should have.

Example:

>>> rt.show(users.UserRoles)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======================== ===== ===== =====
 Name                     000   100   900
------------------------ ----- ----- -----
 cal.GuestOperator              ☑     ☑
 comments.CommentsStaff               ☑
 comments.CommentsUser          ☑     ☑
 contacts.ContactsStaff               ☑
 contacts.ContactsUser          ☑     ☑
 excerpts.ExcerptsStaff               ☑
 excerpts.ExcerptsUser          ☑     ☑
 notes.NotesStaff                     ☑
 notes.NotesUser                ☑     ☑
 office.OfficeStaff                   ☑
 office.OfficeUser              ☑     ☑
 polls.PollsAdmin                     ☑
 polls.PollsUser                ☑     ☑
 xl.SiteAdmin                         ☑
 xl.SiteUser                    ☑
======================== ===== ===== =====
<BLANKLINE>



The table doesn't show *all* user roles, only those that are "meaningful".

Where meaningful means: those which are mentioned (either imported or defined)
in the global context of the :attr:`user_types_module
<lino.core.site.Site.user_types_module>`. We tried more "intelligent"
approaches, but it is not trivial for Lino to guess which roles are
"meaningful".

.. _current_user_type:


The current user type
=====================

This is used by :mod:`lino.utils.jsgen`, i.e. when generating the
:xfile:`linoweb.js` file for a given user type.




Plugin configuration
====================

.. class:: Plugin

    See :doc:`/dev/plugins`.

    .. attribute:: online_registration

        Whether this site offers :ref:`online registration
        <online_registration>` of new users.



Roles
=====

.. class:: Helper

    Somebody who can help others by running :class:`AssignToMe`
    action.


.. class:: AuthorshipTaker

    Somebody who can help others by running :class:`TakeAuthorship`
    action.


Actions
=======

.. class:: SendWelcomeMail

    Send a welcome mail to this user.


.. class:: ChangePassword

    Change the password of this user.

    .. attribute:: current

        The current password. Leave empty if the user has no password
        yet. And SiteAdmin users don't need to specify this at all.

    .. attribute:: new1

        The new password.

    .. attribute:: new2

        The new password a second time. Both passwords must match.


.. class:: SignIn

    Open a window which asks for username and password and which
    authenticates as this user when submitted.

.. class:: SignOut

    Sign out the current user and return to the welcome screen for
    anonymous visitors.




Mixins
======

.. class:: Authored

    .. attribute:: manager_roles_required

        The list of required roles for getting permission to edit
        other users' work.

        By default, only :class:`SiteStaff
        <lino.core.roles.SiteStaff>` users can edit other users' work.

        An application can set :attr:`manager_roles_required` to some
        other user role class or a tuple of such classes.

        Setting :attr:`manager_roles_required` to ``[]`` will **disable**
        this behaviour (i.e. everybody can edit the work of other users).

        This is going to be passed to :meth:`has_required_roles
        <lino.core.users.choicelists.UserType.has_required_roles>` of
        the requesting user's profile.

        Usage examples see :class:`lino_xl.lib.notes.models.Note` or
        :class:`lino_xl.lib.cal.models.Component`.


    .. attribute:: author_field_name

        No longer used. The name of the field that defines the author
        of this object.



.. class:: UserAuthored

    Inherits from :class:`Authored`.

    Mixin for models that have a :attr:`user` field which points to
    the "author" of this object. The default user of new instances is
    automatically set to the requesting user.

    .. attribute:: user

        The author of this object.
        A pointer to :class:`lino.modlib.users.models.User`.


.. class:: StartPlan

    .. attribute:: update_after_start

        Whether to run :meth:`Plan.update_plan` after starting the plan.

.. class:: UserPlan

    Mixin for anything that represents a "plan" of a given user on a given day.

    What a "plan" means, depends on the inheriting child.  Usage examples are an
    invoicing plan (:class:`lino_xl.lib.invoicing.Plan`) or an accounting report
    ():class:`lino_xl.ledger.Report`).

    The mixin makes sure that there is only one database instance per user. A
    plan is considered a low value database object to be reused frequently.

    Inherits from :class:`UserAuthored`.

    .. attribute:: user

         The user who owns and uses this plan.

    .. attribute:: today

         This date of this plan.  This is automatically set to today
         each time the plan is called or updated.

    .. attribute:: update_plan_button

    .. method:: run_start_plan(self, user)

        Return the database object for this plan and user.
        or create

    .. method:: update_plan(self, ar)

        Implementing models should provide this method.


.. class:: UpdatePlan

    Build a new list of suggestions.
    This will remove all current suggestions.





doctests
========

Verify whether the help_text of the change_password action is set:

>>> ba = rt.models.users.AllUsers.get_action_by_name('change_password')
>>> print(ba.action.help_text)
Change the password of this user.

Verify whether :ticket:`3766` is fixed:

>>> show_choices('robin', '/choices/users/Users/partner')
... #doctest: +ELLIPSIS
<br/>
Altenberg Hans
Arens Andreas
...
Õunapuu Õie
Östges Otto

>>> show_choices('robin', '/choices/users/Users/user_type')
<br/>
000 (000 (Anonymous))
100 (100 (User))
900 (900 (Administrator))
