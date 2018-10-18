=========================
Use a PostgreSQL database
=========================

If you decided to use PostgreSQL as database engine, then here is a
cheat sheet for quickly doing so.  No warranty.

.. contents:: Table of contents
    :local:
    :depth: 1
            



Installation
============


Install PostgreSQL on your site::

    $ sudo apt install postgresql
    
Install the PostgreSQL client into your project's virtualenv::
  
    $ pip install psycopg2

Create a new database::    

  $ sudo -u postgres createdb mydb



Show all users::

    $ sudo -u postgres psql postgres

    postgres=# \du
                                 List of roles
    Role name |                   Attributes                   | Member of 
    ----------+------------------------------------------------+-----------
    django    |                                                | {}
    postgres  | Superuser, Create role, Create DB, Replication | {}


Show all users::

    $ sudo -u postgres psql mydb

    postgres=# \du
  
