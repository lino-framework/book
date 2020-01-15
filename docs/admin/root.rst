===================================
Setting up a Lino production server
===================================

A :term:`production server` is a virtual or physical machine running a Linux
operating system and connected to a network.

The :term:`server provider` is responsible for installing and maintaining that
machine. He holds root access to the server and creates user accounts with sudo
rights for each :term:`site maintainer`. He configures secure remote shell
access (SSH) to that machine for each site maintainer.

The :term:`site maintainer` is responsible for installing and maintaining any
specific system packages required by Lino as well as the Lino source code and
configuration.


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
