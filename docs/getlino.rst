=======================
The ``getlino`` package
=======================

The :mod:`getlino` package is still work in progress, so use it only for
testing purposes. When finished, it will help to install Lino to your computer.

If you just want to quickly try a Lino, read :doc:`/dev/quick/install`.


Configure a virgin Debian system as a Lino production server
============================================================

Get root permissions, install getlino into the system-wide Python, then run
:cmd:`getlino configure`::

   $ sudo pip3 install getlino
   $ sudo getlino configure

This will ask you some questions about the general layout of this Lino server.
You can answer ENTER if your don't care. You can also instruct getlino to not
ask any question::

   $ sudo getlino configure --batch

Your answers will be stored in the system-wide getlino config file.

To actually install everything according to your configfile, run :cmd:`getlino
setup`::

   $ sudo getlino setup

Now install a first site (this time you don't need to be root anymore)::

   $ getlino startsite

The script will ask you some questions:

- The project name or internal name of this Lino site. We recommend lower-case
  only and no "-" or "_", maybe a number.  Examples:  foo, foo2, mysite, first,

- Which application to run


Install a Lino development environment
======================================

Install getlino into your default Python environment, then run :cmd:`getlino
setup`::

   $ . path/to/virtualenv/bin/activate
   $ sudo pip3 install getlino
   $ sudo getlino configure
   $ sudo getlino setup




Combining getlino and Docker
============================



The `getlino <https://github.com/lino-framework/getlino>`__ repository contains a
:xfile:`Dockerfile` which you

To create and run the docker image, you need to the run the following command:

docker build -t getlino .

This will create the docker image and use the current getlino.py script (It
will not install getlino from pip servers ) , so be sure the also update your
getlino.py local file.

