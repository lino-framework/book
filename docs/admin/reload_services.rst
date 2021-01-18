===========================
Reloading the Lino services
===========================

As a :term:`site maintainer`, when you have modified the :xfile:`settings.py`
file of a project, then you must restart the system services that use this file.
This is usually the web server, the Lino daemon (:manage:`linod`) and
potentially some other services.


.. xfile:: reload_services.sh


You do this by issuing::

  $ reload_services.sh

This will ask you for your password, you need to have sudo

This will of course shortly interrupt all Lino sites on that machine.
