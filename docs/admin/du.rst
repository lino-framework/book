.. _admin.du:

=====================
Monitoring disk usage
=====================

These are just my personal notes. No warranty whatsoever.

.. contents:: Table of contents
    :local:
    :depth: 1


Manually diagnose
=================

Manually see the overall disk usage::

    $ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/simfs       15G  7.0G  8.1G  47% /
    tmpfs           205M  2.1M  203M   2% /run
    tmpfs           5.0M  4.0K  5.0M   1% /run/lock
    tmpfs           820M     0  820M   0% /run/shm

Install `ncdu <https://dev.yorhel.nl/ncdu>`_


Automated diagnose
==================

Install `monit` (`sudo apt-get install monit` ) and get alerts per
email.  In :file:`/etc/monit/monitrc` you can write for example::

    check filesystem datafs with path /
       if space usage > 80% for 5 times within 15 cycles then alert
       if space usage > 99% then stop



Routine actions
===============

Clean up the cache of the packet manager::

  $ sudo apt-get clean


Find the guilty
===============

Show all directories which have more than a GB::

  $ du ~ -h | grep '[0-9\.]\+G'

(thanks to `Tracking down where disk space has gone
<http://unix.stackexchange.com/questions/125429/tracking-down-where-disk-space-has-gone-on-linux>`_)


Cleaning the packaging system
=============================

To erase downloaded archive files:: 

    $ sudo apt-get clean

To remove packages that were automatically installed to satisfy
dependencies for some package and that are no more needed::

    $ sudo apt-get autoremove

To see which kernel versions are installed::

    $ dpkg --get-selections | grep linux-image

To remove an unused kernel image::

    $ sudo apt-get remove --purge linux-image-X.X.XX-XX-generic

