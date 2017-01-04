==============
Managing users
==============

Django's permission system is not suitable for developing complex
applications because maintaining permissions becomes a hell when you
develop an application which runs on different sites. Also it provides
no means for defining instance-specific permissions and has no
built-in concept of user profiles.

That's why Lino replaces Django's `django.contrib.auth
<https://docs.djangoproject.com/en/dev/topics/auth/>`_ plugin by its
own plugin :mod:`lino.modlib.users`.

.. This is a tested document. You can test it using:

    $ python setup.py test -s tests.LibTests.test_users

   doctests initialization:
    
    >>> import os
    >>> os.environ['DJANGO_SETTINGS_MODULE'] = \
    ...     'lino_book.projects.docs.settings.demo'
    >>> from lino.api.doctest import *

.. contents::


 
Creating a root user
====================

The most Linoish way to create a root user (or a set of demo users) is
to run :manage:`initdb_demo`.  This will reset the database to a
virgin state and then load all your demo data, which includes
:mod:`lino.modlib.users.fixtures.demo_users` (except if you changed
your :attr:`lino.core.site.Site.demo_fixtures`).

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

>>> try:
...     users.User.objects.get(username="test").delete()
... except users.User.DoesNotExist:
...    pass
>>> u = users.User(username="test")
>>> u.save()
>>> print u.has_usable_password()
False


The `password` field is empty, and the :meth:`User.check_password`
method returns `False`:

>>> print repr(u.password)
u''
>>> print u.check_password('')
False

When setting the password for a newly created user, leave the
field :guilabel:`Current password` empty.

>>> ses = rt.login('robin')
>>> values = dict(current="", new1="1234", new2="1234")
>>> rv = ses.run(u.change_password, action_param_values=values)
>>> print(rv['message'])
New password has been set for test.


.. _online_registration:



Online registration
===================

To enable online registration on your site, you must

- use :mod:`lino_noi.lib.users` instead of :mod:`lino.modlib.users` in
  your :setting:`INSTALLED_APPS`.

- set :attr:`lino.modlib.users.Plugin.online_registration` to `True`.

- define your :attr:`anonymous
  <lino.modlib.users.choicelists.UserTypes.anonymous>` user type with
  :attr:`readonly <lino.modlib.users.choicelists.UserType.readonly>`
  set to `False`.
  
This is done e.g. by :mod:`lino_noi.projects.care.roles`.

.. currentmodule:: lino_noi.lib.users.models
                   
When a new user is created, Lino sets a random
:attr:`verification_code <User.verification_code>`.

:attr:`user_state <User.user_state>`.

:class:`lino_noi.lib.users.choicelists.UserStates`


