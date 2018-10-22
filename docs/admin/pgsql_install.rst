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
    

Show all users::

    $ sudo -u postgres psql -c \\du postgres

                                 List of roles
    Role name |                   Attributes                   | Member of 
    ----------+------------------------------------------------+-----------
    django    |                                                | {}
    postgres  | Superuser, Create role, Create DB, Replication | {}
    

Show all databases::

    $ sudo -u postgres psql -c \\l postgres
                                      List of databases
       Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
    -----------+----------+----------+-------------+-------------+-----------------------
     cfoo      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
     dfoo      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
     postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
     bfoo      | django   | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
     template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
     template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
               |          |          |             |             | postgres=CTc/postgres
    (6 rows)
  

Create a new database::

    $ sudo -u postgres createdb efoo

Remove a database

    $ sudo -u postgres dropdb bfoo



