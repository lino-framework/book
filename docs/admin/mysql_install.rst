.. _mysql.cheat_sheet:

=================
MySQL cheat sheet
=================

If you use MySQL as database engine, then here is a cheat sheet for some routine
situations that you might want to get into.  See also the Django documentation
at `MySQL notes
<https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-notes>`__

.. contents:: Table of contents
    :local:
    :depth: 1


Users
=====


.. For the first project on your site create a user ``django`` which you
  can reuse for all projects::

    $ sudo mysql -u root -p
    mysql> create user 'django'@'localhost' identified by 'my cool password';

To see all users defined on the site::

    $ sudo mysql -u root -p
    mysql> select host, user from mysql.user;
    +-----------+------------------+
    | host      | user             |
    +-----------+------------------+
    | localhost | root             |
    | 127.0.0.1 | root             |
    | localhost |                  |
    | localhost | debian-sys-maint |
    | localhost | django           |
    | %         | django           |
    +-----------+------------------+
    6 rows in set (0.00 sec)


How to change the password of an existing user::

    $ sudo mysql -u root -p
    mysql> set password for PRJNAME@localhost = password('my cool password');



Databases
=========

How getlino creates a database and grants permissions::

    $ mysql -u root -p
    mysql> create database DBNAME charset 'utf8';
    mysql> grant all on mysite.* to DBUSER with grant option;
    mysql> quit;


See which databases are installed on this server::

    $ sudo mysql -u root -p -e "show databases;"


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
