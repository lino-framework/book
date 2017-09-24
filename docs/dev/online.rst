.. _online_registration:


===================
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


