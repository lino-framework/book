.. _admin.pyanywhere:

==============================
Running Lino on PythonAnywhere
==============================

.. note::

  The following does not yet work because we hit the 512 MB limit of a free PA
  account.

PythonAnywhere is limited: There is no sudo command and you cannot select
another operating system than Ubuntu 16.04.6.  And then you get only 512 MB of
disk space on a free PA account.

But even then it works... almost. Here we go:

Open an account on `PythonAnywhere
<https://www.pythonanywhere.com/user/lsaffre/>`__.

Create a MySQL database.

Open a bash console and type::

  $ virtualenv -p python3.7 env
  $ . env/bin/activate
  $ pip install getlino
  $ getlino configure --admin-email you@yourdomain.com  --db-engine mysql
  This is getlino version 20.7.2 running on Ubuntu 16.04.6 LTS.
  This will write to configuration file /home/lsaffre/.getlino.conf
  - sites_base (Base directory for Lino sites on this server) [/home/lsaffre/lino]:
    ...
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
  - user name [voga1]: <enter your username from database tab>
  - user password [5YYU5ODzgjQ]: <enter your password from database tab>
  - port [3306]:
  - host name [localhost]: <enter your hostname from database tab>
  Shared virtualenv [/home/lsaffre/env]:
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
  ...
  ERROR: Failed building wheel for lino
  ...
  ERROR: Could not install packages due to an EnvironmentError: [Errno 122] Disk quota exceeded

Voilà. That's where we get stuck. Yes, a Lino site needs more than 512MB of disk
space.  We might check whether that disk usage can be reduced, and we did
already some work, but we decided to stop here because (a) at the moment we have
no more ideas about how to save more disk space would and (b) PythonAnywhere has
serious limitations (e.g. cannot choose another OS or another database engine,
cannot install system packages) and (c) a paying PA site with 5GB of disk space
costs $12 per month, which is more expensive than simply getting a full Debian
virtual private server. So why should we invest more time into this (other than
technical curiosity)?
