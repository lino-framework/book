====================================
The :cmd:`getlino configure` command
====================================

.. command:: getlino configure

.. program:: getlino configure

The :cmd:`getlino configure` command configures your machine as a :term:`Lino
server`.  This is required before you can run :cmd:`getlino startsite`.

If you run :cmd:`getlino` as root (using :cmd:`sudo`), it will potentially also
install system packages and create or overwrite system-wide configuration files.
Otherwise it will install Lino into a :term:`virtualenv`. If you want Lino to
install into an existing :term:`virtualenv`, you should activate it before
running :cmd:`getlino configure` in order to use it as your
:option:`--shared-env`.

:cmd:`getlino configure` asks a lot of questions, one question for each server
configuration option. Read the docs below for more explanations. You can answer
ENTER to each question if you don't care.

:cmd:`getlino configure` creates or reads and updates a configuration file where
it stores your answers.  Depending on whether you are root, the configuration
file will be either :xfile:`/etc/getlino/getlino.conf` or
:xfile:`~/.getlino.conf`.

If you specify :option:`--batch`, every option gets its default value, which you
may override by specifying command-line arguments. Use this option only when you
know what you want (e.g. in a Dockerfile).

After running :cmd:`getlino configure` as root, you may want to run it once more
without being root, because only then it will also write a
:xfile:`.bash_aliases` file in your home directory.

.. rubric:: Run-time behaviour options:

.. option:: --batch

    Run in batch mode, i.e. without asking any questions.
    Assume yes to all questions.


.. rubric:: Server configuration options

.. option:: --shared-env

    Full path to a shared :term:`virtualenv` to be used by all new sites.

    If this is empty, every new site will get its own virgin environment.

    When configure is running as root, the default value is an empty string (you
    don't want a shared virtualenv on a production site). Otherwise the default
    value is taken from the :envvar:`VIRTUAL_ENV` environment value (all your
    sites will use a same environment).

.. option:: --repos-base

    An optional base directory for all code repositories on this server.
    If this is given, getlino will use this
    for :option:`getlino configure --clone`
    or :option:`getlino startsite --dev-repos`.

    If this is empty, repositories will
    be stored in a directory named :option:`--repos-link` below the :term:`virtualenv` dir.

.. option:: --clone

    Clone all known repositories to your ``--repos-base`` and install them
    into your ``--shared-env``. Used when configuring a :term:`contributor
    environment` or a :term:`demo server`.

.. option:: --branch

    The git branch to use for :option:`--clone`.

.. option:: --devtools

    Whether to install development tools (used to build docs and run tests).

.. option:: --log-base

    The root directory for Lino's log files on this server.  Each new site
    will get its entry below that directory.

.. option:: --backups-base

    The root directory for backups on this server.  Each new site will get
    its entry below that directory.  Used e.g. by :xfile:`make_snapshot.sh`.

.. option:: --sites-base

    The root directory for sites on this server.

    New sites will get created below that directory (with another level
    named by :option:`--local-prefix`).

    This will be added to the :envvar:`PYTHONPATH` of every Lino process
    (namely in :xfile:`manage.py` and :xfile:`wsgi.py`).

    The :envvar:`PYTHONPATH` is needed because the :xfile:`settings.py` of
    a site says ``from lino_local.settings import *``, and the
    :xfile:`manage.py` sets :setting:`DJANGO_SETTINGS_MODULE` to
    ``'lino_local.mysite1.settings'``.

.. option:: --local-prefix

    Prefix for local server-wide importable packages.

.. option:: --env-link

    Relative directory or symbolic link to the virtualenv.

.. option:: --repos-link

    Relative directory or symbolic link to repositories.

.. option:: --server-domain

    Fully qualified domain name of this server.  Default is 'localhost'.

.. rubric:: Default settings for new sites

.. option:: --front-end

    Which front end (:attr:`default_ui <lino.core.Site.default_ui>`) to use
    on new sites.

.. option:: --languages

    Default value for :attr:`languages <lino.core.site.Site.languages>` of
    new sites.

.. option:: --linod

    Whether new sites should have a :xfile:`linod.sh` script which runs the
    :manage:`linod` command.

    When running as root, this will also add a :mod:`supervisor`
    configuration file which runs the :manage:`linod` command automatically.

.. option:: --db-engine

    Default value is 'mysql' when running as root or 'sqlite3' otherwise.

.. option:: --db-user

    A shared database username to use for all sites on this server.

    If this is set, you must also set :option:`--db-password`.

    Used during development and testing when you prefer to have a single
    database user for all databases.  For security reasons these options should
    not be used on a :term:`production server`.

.. option:: --db-password

    The password for the :option:`--db-user`.

.. option:: --db-port

    The port to use for connecting to the database server when
    :option:`--db-engine` is ``mysql`` or ``postgresql``.

.. rubric:: Server features

.. option:: --appy

    Whether this server provides LibreOffice service needed by sites that use
    :mod:`lino_xl.lib.appypod`.

.. option:: --redis

    Whether this server provides redis service needed by sites that use
    :mod:`lino.modlib.notify`.

.. option:: --webdav

    Whether new sites should have webdav.

.. option:: --ldap

    Whether this server provides an LDAP service.  Not tested.

.. option:: --https

    Whether this server provides secure http.

    This option will cause getlino to install certbot.

    When you use this option, you must have your domain name
    (:option:`--server-domain`) registered so that it points to the server.
    If your server has a dynamic IP address, you may use some dynamic DNS
    service like `FreedomBox
    <https://wiki.debian.org/FreedomBox/Manual/DynamicDNS>`__ or `dynu.com
    <https://www.dynu.com/DynamicDNS/IPUpdateClient/Linux>`__.
