===============
Installing Lino
===============

This page gives an overview on how to install Lino on your computer. Follow the
links for more details.

From the following list, choose the one which matches your profile:

- I just want to try Lino on my computer and maybe  write my own application.
  --> `Configure a minimal Lino site`_

- I want to write my own application and maybe contribute to the project.
  --> `Configure a Lino development environment`_

- I want to run a Lino server and host Lino production sites for myself or
  others. --> `Configure a Lino production server`_


Configure a minimal Lino site
=============================

Create a new virtual environment, activate it, install getlino, run
:cmd:`getlino configure` followed by :cmd:`getlino startsite`, then run
:manage:`runserver`::

  $ sudo apt-get install -y python3-pip
  $ mkdir ~/lino
  $ cd ~/lino
  $ virtualenv -p python3 env
  $ . env/bin/activate
  $ pip install getlino
  $ getlino configure --batch --sites-base .
  $ getlino startsite noi first --batch
  $ cd first
  $ python manage.py runserver

Point your browser to http://localhost:8000


Configure a Lino development environment
========================================

Activate the virtual environment which you want to use for your Lino projects.

::

  $ . path/to/my/virtualenv/bin/activate
  $ pip install getlino
  $ getlino configure --sites-base .
  $ getlino startsite noi first --dev-repos "lino xl noi book"
  $ cd first
  $ python manage.py runserver

Point your browser to http://localhost:8000

Configure a Lino production server
==================================

To make a production server you install getlino into the system-wide Python 3
environment.

   $ sudo -H pip3 install getlino
   $ sudo -H getlino configure --sites-base .
   $ sudo -H getlino startsite noi first --batch

Point your browser to http://first.localhost
