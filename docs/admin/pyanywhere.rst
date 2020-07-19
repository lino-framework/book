==============================
Running Lino on PythonAnywhere
==============================

PythonAnywhere is limited: There is no sudo command and you cannot select
another operating system than  Ubuntu 16.04.6.  But let's try.

Open an account on `PythonAnywhere
<https://www.pythonanywhere.com/user/lsaffre/>`__.

Open a bash console and type::

  $ virtualenv -p python3.7 env
  $ . env/bin/activate
  $ pip install getlino
  $ getlino configure
  $ getlino configure --admin-email you@yourdomain.com  --db-engine mysql
  This is getlino version 20.7.2 running on Ubuntu 16.04.6 LTS.
  This will write to configuration file /home/lsaffre/.getlino.conf
  - sites_base (Base directory for Lino sites on this server) [/home/lsaffre/lino]:
  - local_prefix (Prefix for local server-wide importable packages) [lino_local]:
  - shared_env (Directory with shared virtualenv) []:
  - repos_base (Base directory for shared code repositories) []:
  - clone (Clone all contributor repositories and install them to the shared-env) [False]:
  - branch (The git branch to use for --clone) [master]:
  - usergroup (User group for files to be shared with the web server) [www-data]:
  - env_link (link to virtualenv (relative to project dir)) [env]:
  - repos_link (link to code repositories (relative to virtualenv)) [repositories]:
  - redis (Whether this server provides redis) [False]:
  - devtools (Whether to install development tools (build docs and run tests)) [True]:
  - server_domain (Domain name of this server) [localhost]:
  - db_engine (Default database engine for new sites.) (mysql, postgresql, sqlite3) [sqlite3]:
  - db_port (Default database port to use for new sites.) []:
  - db_host (Default database host name for new sites.) [localhost]:
  - db_user (Default database user name for new sites. Leave empty to use the project name.) []:
  - db_password (Default database password for new sites. Leave empty to generate a secure password.) []:
  - admin_name (The full name of the server administrator) [Joe Dow]:
  - admin_email (The email address of the server administrator) [luc.saffre@gmail.com5~]:
  - time_zone (The TIME_ZONE to set on new sites) [Europe/Brussels]:
  - languages (The languages to set on new sites) [en]:
  - front_end (The front end to use on new sites) (lino.modlib.extjs, lino_react.react) [lino.modlib.extjs]:
  Start configuring your system using above options? [y or n] Yes
  Wrote config file /home/lsaffre/.getlino.conf
  run sudo apt-get install python3-setuptools supervisor python3-dev libssl-dev python3-pip sqlite3 libffi-dev git graphviz swig python3 subversion build-essential [y or n] No
  Create shared settings package /home/lsaffre/lino/lino_local ? [y or n] Yes
  add '. /home/lsaffre/.lino_bash_aliases' to your bashrc file for some cool bash shortcut commands
  getlino configure completed.



  $ getlino startsite voga voga1
  This is getlino version 20.7.3 running on Ubuntu 16.04.6 LTS.
  Create a new Lino voga site into /home/lsaffre/lino/lino_local/voga1
  User credentials (for mysql on localhost:):
  - user name [voga1]:
  - user password [5YYU5ODzgjQ]:
  - port [3306]:
  - host name [localhost]:
  Shared virtualenv []:
  Site's secret key [tqHrw8CaoaMTik7yAwDUuVDmYis]:
  OK to create /home/lsaffre/lino/lino_local/voga1 with above options? [y or n]
  Create virtualenv in /home/lsaffre/lino/lino_local/voga1/env [y or n] Yes
  Installing 3 Python packages...
  run . /home/lsaffre/lino/lino_local/voga1/env/bin/activate && pip install --upgrade mysqlclient lino lino-voga [y or n] Yes
  . /home/lsaffre/lino/lino_local/voga1/env/bin/activate && pip install --upgrade mysqlclient lino lino-voga
  Looking in links: /usr/share/pip-wheels
  Collecting mysqlclient
    Downloading mysqlclient-2.0.1.tar.gz (87 kB)
       |████████████████████████████████| 87 kB 1.8 MB/s
  Collecting lino
    Downloading lino-20.7.2.tar.gz (10.0 MB)
       |████████████████████████████████| 10.0 MB 19.1 MB/s
  Collecting lino-voga
    Downloading lino-voga-19.12.0.tar.gz (98 kB)
       |████████████████████████████████| 98 kB 2.7 MB/s
  Collecting Django
    Downloading Django-3.0.8-py3-none-any.whl (7.5 MB)
