.. _mysql.cheat_sheet:

=================
MySQL cheat sheet
=================

If you use MySQL as database engine, then here is a cheat sheet for some routine
situations that you might want to get into.  No warranty.  See also the Django
documentation at `MySQL notes
<https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-notes>`__

.. contents:: Table of contents
    :local:
    :depth: 1


Installation
============

To install the server, run :cmd:`getlino configure` with :option:`getlino
configure --db-engine`.  This will install either mariadb (Debian) or mysql
(Ubuntu).

Every subsequent :cmd:`getlino startsite` run will

- install the `mysqlclient` Python package into the site's virtualenv.
- create a database named PRJNAME
- create a user PRJNAME with a password and grant all privileges to that user
- set :setting:`DATABASES` in your :xfile:`settings.py`


.. Install mysql on your site::

    $ sudo apt install mysql-server
    $ sudo apt install libmysqlclient-dev
    $ sudo apt install python-dev
    $ sudo apt install libffi-dev libssl-dev
    $ sudo apt install mysql-server

    $ sudo mysql_secure_installation

.. Install the mysql client into your project's virtualenv::

    $ pip install mysqlclient

  Note that we recommended `mysql-python` before but modified this to
  `mysqlclient` in accordance with `Django
  <https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-db-api-drivers>`__.

Users
=====


.. For the first project on your site create a user ``django`` which you
  can reuse for all projects::

    $ sudo mysql -u root -p
    mysql> create user 'django'@'localhost' identified by 'my cool password';

To see all users defined on the site::

    $ sudo mysql -u root -p
    mysql> select host, user, password from mysql.user;
    +-----------+------------------+------------------------------+
    | host      | user             | password                     |
    +-----------+------------------+------------------------------+
    | localhost | root             | 6FD6D9512034462391B7154E5ADF |
    | 127.0.0.1 | root             | 6FD6D9512034462391B7154E5ADF |
    | localhost |                  |                              |
    | localhost | debian-sys-maint | A14910957D8F261196A210B4C82F |
    | localhost | django           | 42214E1C5E6EF5119DD86A2A2F8C |
    | %         | django           | 42214E1C5E6EF5119DD86A2A2F8C |
    +-----------+------------------+------------------------------+
    6 rows in set (0.00 sec)


How to change the password of an existing user::

    $ sudo mysql -u root -p
    mysql> set password for PRJNAME@localhost = password('my cool password');


Databases
=========

.. For each new project you must create a database and grant permissions
  to ``django``::

    $ mysql -u root -p
    mysql> create database mysite charset 'utf8';
    mysql> grant all on mysite.* to django with grant option;
    mysql> quit;


See which databases are installed on this server::

    $ sudo mysql -u root -p
    mysql> show databases;


.. And then of course you set DATABASES in your :xfile:`settings.py`
  file::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mysite',
            # The following settings are not used with sqlite3:
            'USER': 'django',
            'PASSWORD': 'my cool password',
            'HOST': '',
            'PORT': '',
        }
    }


Deleting a site
===============

What to do when you created a site and then changed your mind and want to delete
it again?

Or when :cmd:`getlino startsite` successfully creates the database and user, but
then fails for some reason? You can simply overwrite an existing site by running
:cmd:`getlino startsite` again, but mysql or pgsql will try to create a new
database and user of same name, and of course they will fail. The easiest
workaround is to manually delete both the user and the database before running
:cmd:`getlino startsite` again.

Here is how to manually delete a database and user ``prjname``::

  $ sudo mysql -u root -p
  mysql> drop database prjname;
  mysql> drop user prjname@localhost;


Resetting the root password
===========================

In case you forgot the mysql root password (but have root access to the server)::

  $ sudo service mysql stop
  $ sudo mysqld_safe --skip-grant-tables &
  $ mysql
  mysql> UPDATE mysql.user set password=password('My cool password') where user='root';
  mysql> flush privileges;
  mysql> exit;

  $ sudo mysqladmin -u root -p shutdown
  $ sudo service mysql restart

Notes about certain MySQL configuration settings
================================================

See the following chapters of the MySQL documentation

-  Lino is tested only with databases using the 'utf8' charset.
   See `Database Character Set and Collation
   <http://dev.mysql.com/doc/refman/5.0/en/charset-database.html>`_


Tuning
======

See separate document :doc:`/admin/mysql_tune`.
