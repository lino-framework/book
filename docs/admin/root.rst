===================================
Setting up a Lino production server
===================================

A :term:`production server` is  a *Linux machine*, i.e. a virtual or physical
machine with a Linux operating system running in a network.

The :term:`server provider` is responsible for keeping root access to the server
and creating user accounts for each :term:`site maintainer`.

The :term:`site maintainer` needs shell access to that machine in order to
install Lino-specific system packages.


System requirements
===================

We recommend a **stable Debian** as operating system.  Currently this means
Debian 10 "Buster".

You need at least 2 GB of disk space.

You need at least 500MB of RAM.  How to see how much memory you have::

    $ free -h


Creating system users
=====================

The system should have installed the `sudo` package::

  # apt-get install sudo

Create a use account for a  :term:`site maintainer`, e.g. ``joe``::

  # adduser joe

Site maintainers must be members of the `sudo` and `www-data` groups::

  # adduser joe sudo
  # adduser joe www-data

Note that `useradd` is a native binary compiled with the system, while `adduser`
is a perl script which uses `useradd` in back-end.

All maintainers must have a umask `002` or `007` (not `022` or `077` as is the
default value).

Edit either the file :file:`~/.bashrc` of each user or the file
:file:`/etc/bash.bashrc` (site-wide for all users) and add the following line at
the end::

    umask 002

The umask is used to mask (disable) certain file permissions from any new file
created by a given user. See :doc:`umask` for more detailed information.

Grant SSH access to a site maintainer
=====================================

Finally grant SSH access to that new account, e.g. by creating the user's
:file:`.ssh/authorized_keys` file with the maintainer's public ssh key.
