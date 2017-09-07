===========================
Reloading the Lino services
===========================

.. xfile:: reload_services.sh

When you have modified the :xfile:`settings.py` file of a project,
then you must restart the services which use this file. This is
usually at least Apache, and potentially Supervisor, and maybe even
some other services.

You do this by issuging::

  $ reload_services.sh

This will ask you for the root password.
This will of course shortly interrupt all Lino sites on that machine.

