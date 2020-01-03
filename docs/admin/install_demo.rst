.. _getlino.install.demo:

======================================
Setting up a Lino demo server
======================================

.. _pip: http://www.pip-installer.org/en/latest/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv


Warning : This is the deeper Python jungle. Don't try this before you have
installed a few contributor environments and production servers.

Read also :doc:`install` before proceeding.

A demo server is like a production server, but we want all the sites to share a same environment.

Set up a global shared environment and source it in your :file:`.bashrc`.

Run :cmd:`getlino configure` as root::

   $ sudo -H env PATH=$PATH getlino configure --shared-env /usr/local/lino/shared/master --clone

That is, you tell getlino to clone all repositories and to create a shared :term:`virtualenv`.

You may create other shared virtualenvs by changing the branch and clone another
set of repositories::

   $ sudo -H env PATH=$PATH getlino configure --shared-env /usr/local/lino/shared/stable --clone --branch stable

Specify ``--shared-env`` when creating demo sites::

   $ sudo -H env PATH=$PATH getlino startsite noi first --shared-env /usr/local/lino/shared/stable
   $ sudo -H env PATH=$PATH getlino startsite tera second --shared-env /usr/local/lino/shared/master
