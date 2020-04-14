===================================
Providing a Lino server
===================================

A :term:`Lino server` is a virtual or physical machine used to run one or
several :term:`Lino sites <Lino site>`. It must have a Linux operating system
and be connected to a network. A :term:`server provider` is responsible for
installing and maintaining that machine.

The :term:`server provider` holds root access to the server and creates user
accounts with sudo rights for each :term:`site maintainer`. He configures secure
remote shell access (SSH) to that machine for each site maintainer. He is *not*
responsible for installing and maintaining specific system packages, Lino source
code and configuration (these are the job of the :term:`site maintainers <site
maintainer>`).

System requirements
===================

We recommend a `stable Debian <https://www.debian.org/releases/stable/>`__ as
operating system.  Currently this means Debian 10 "Buster".

You need at least 10 GB of disk space. You can see how much disk space you have
by saying::

    $ df -h

You need at least 2GB of RAM.  How to see how much memory you have::

    $ free -h


Creating system users
=====================

The system should have installed the `sudo` package::

  # apt-get install sudo

Create a user account for a :term:`site maintainer`, e.g. ``joe``::

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

Finally the :term:`server provider` must grant SSH access to that new account,
e.g. by creating the user's :file:`.ssh/authorized_keys` file with the
maintainer's public ssh key.
