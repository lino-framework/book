.. _user.install:

===============
Installing Lino
===============

This document explains how to install Lino on your machine in order to
write application.  For deploying Lino applications on a production
site you will read :doc:`/admin/install`.  If you want the latest
version, then you should rather follow :doc:`/dev/install`.

Work in progress.  Basically it will be easy::


    $ virtualenv env
    $ . env/bin/activate
    $ pip install lino_start
    $ lino startproject mylino
    $ cd mylino
    $ django manage.py prep
    $ django manage.py runserver
