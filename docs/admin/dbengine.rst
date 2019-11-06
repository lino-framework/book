=============================
Selecting the database engine
=============================

.. program:: getlino configure

To select a database server, run :cmd:`getlino configure` with
:option:`--db-engine`. This option has currently three choices: mysql,
postgresql or sqlite3.  The default value is either mysql (when running as root)
or sqlite3 otherwise. mysql will install either mariadb (Debian) or mysql
(Ubuntu).

For mysql and postgresql you *may* additionally specify a db-port, a db-user and
db-password.

Shared database user

The db-user and db-password will not be used directly, but they will be stored
as the default values for all subsequent calls to :cmd:`getlino startsite`.

If :option:`--db-user` is empty, :cmd:`getlino startsite` will create a new user for each
new site.  If it is not empty, all sites will share the same database username.
The latter is less secure but convenient on a server having all sites owned by a
same :term:`site operator`.

On a server with a shared database user you must also specify a
:option:`--db-password` for :cmd:`getlino configure`.

Every subsequent :cmd:`getlino startsite` run will

- install the Python packages required by the selected db-engine into the site's virtualenv.
- create a database named PRJNAME
- create a user PRJNAME with a password and grant all privileges to that user
- Store these in the :setting:`DATABASES` of the site's :xfile:`settings.py`
- Run the :manage:`install` command to install additional dynamic dependencies.

If you run :cmd:`getlino startsite` with a given database engine and then
manually change the :setting:`DATABASES` setting of your site, you must yourself
care about installing the corresponding Python package. Lino's :manage:`install`
command cannot automatically install the Python package for the database engine.
This is explicitly done by :cmd:`getlino startsite`.



.. toctree::
    :maxdepth: 1

    mysql_install
    pgsql_install
