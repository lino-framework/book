=============================
Installing Lino using getlino
=============================

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

Configure a Lino development environment
========================================

Activate the virtual environment which you want to use for your Lino projects.

  $ . path/to/my/env/bin/activate
  $ pip install getlino
  $ getlino configure --sites-base .
  $ getlino startsite noi first --batch
  $ cd first
  $ python manage.py runserver



.. _ss:

The ``startsite`` template
==========================

The `cookiecutter-startsite
<https://github.com/lino-framework/cookiecutter-startsite>`__ project contains
a cookiecutter template used by :cmd:`getlino startsite`.


Notes
=====

When you maintain a Lino server, then you don't want to decide for each new
site which database engine to use. You decide this once for all during
:cmd:`getlino configure`. In general, `apt-get install` is called only during
:cmd:`getlino configure`, never during :cmd:`getlino startsite`. If you have a
server with some mysql sites and exceptionally want to install a site with
postgres, you simply call :cmd:`getlino configure` before calling
:cmd:`getlino startsite`.
