.. _lino.admin.install:

======================================
Installing Lino on a production server
======================================

.. _pip: http://www.pip-installer.org/en/latest/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv

Here is a set of conventions which we suggest to use as a :term:`site
maintainer` when setting up a Lino :term:`production server`.


.. _getlino.install.prod:
.. _getlino.install.admin:

Configure a Lino production server
==================================

Install :mod:`getlino` into a shared virtual environment outside of your home::

    $ sudo mkdir /usr/local/lino/shared/env
    $ cd /usr/local/lino/shared/env
    $ sudo chown root:www-data .
    $ sudo chmod g+ws .
    $ virtualenv -p python3 master
    $ . master/bin/activate
    $ pip install getlino

Run :cmd:`getlino configure` as root::

   $ sudo env PATH=$PATH getlino configure

The ``env PATH=$PATH`` is needed to work around the controversial Debian feature
of overriding the :envvar:`PATH` for security reasons (`source
<https://stackoverflow.com/questions/257616/why-does-sudo-change-the-path>`__).

Install a first site.  You will do the following for every new site on your
server.

   $ sudo env PATH=$PATH getlino startsite noi first

Point your browser to http://first.localhost

.. program:: getlino configure

If your customers want to access their Lino from outside of their intranet, then
you need to setup a domain name and add the :option:`--https` option in above
command line.


Some useful additions to your shell
===================================

Add the following to your system-wide :file:`/etc/bash.bashrc`:

.. literalinclude:: bash_aliases

If you want :ref:`log2syslog`, then add also this:

.. literalinclude:: log2syslog

After these changes you must close and reopen your terminal to activate them.
You can now do the following to quickly cd to a project directory and activate
its Python environment::

  $ go prj1
  $ a


.. _getlino.install.demo:

Configure a Lino demo server
============================

Warning : This is the deeper Python jungle. Don't try this before you have
installed a few contributor environments and production servers.

Run :cmd:`getlino configure` as root::

   $ sudo -H env PATH=$PATH getlino configure --shared-env /usr/local/lino/shared/master --clone

.. program:: getlino configure

That is, you say :option:`--clone` and create a :option:`--shared-env`.

You may create other shared envs by changing the branch and clone another set of
repositories::

   $ sudo -H env PATH=$PATH getlino configure --shared-env /usr/local/lino/shared/stable --clone --branch stable

.. program:: getlino startsite

Specify :option:`--shared-env` when creating demo sites::

   $ sudo -H env PATH=$PATH getlino startsite noi first --shared-env /usr/local/lino/shared/stable
   $ sudo -H env PATH=$PATH getlino startsite tera second --shared-env /usr/local/lino/shared/master
