.. _getlino.install.prod:
.. _getlino.install.admin:
.. _lino.admin.install:

===================================
Setting up a Lino production server
===================================

.. _pip: http://www.pip-installer.org/en/latest/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv

Here is a set of conventions we suggest to use as a :term:`site maintainer` when
setting up a Lino :term:`production server`.


Install getlino and run ``getlino configure``
=============================================

Install :mod:`getlino` into a shared virtual environment outside of your home::

    $ sudo mkdir /usr/local/lino/shared/env
    $ cd /usr/local/lino/shared/env
    $ sudo chown root:www-data .
    $ sudo chmod g+ws .
    $ virtualenv -p python3 master
    $ . master/bin/activate
    $ pip install getlino

Run :cmd:`getlino configure` as root::

   $ sudo env PATH=$PATH getlino configure --appy --https

The ``env PATH=$PATH`` is needed to work around the controversial Debian feature
of overriding the :envvar:`PATH` for security reasons (`source
<https://stackoverflow.com/questions/257616/why-does-sudo-change-the-path>`__).

If your customers want to access their Lino from outside of their intranet, then
you need to setup a domain name and add the ``--https`` option in above
command line.

When at least one :term:`Lino site` of a server uses :mod:`lino_xl.lib.appypod`,
then the server must have a LibreOffice service running so that the users of
your site can print documents using the appypdf, appydoc or appyrtf methods (the
appyodt method does not require a LO service). You say this using the
:cmd:`getlino configure --appy` option. For background information see
:doc:`oood`.

For details see the documentation about :ref:`getlino`.


Install your first site
=======================

You will do the following for every new site on your server.

   $ sudo env PATH=$PATH getlino startsite application_name site_name

Point your browser to http://first.localhost

- ``application_name`` is one of the known Lino applications (noi, cosi, avanti, voga...)

- ``site_name`` is the unique internal name of your site on this server.


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
