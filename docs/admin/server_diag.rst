.. _admin.server_diag:

=====================================
Getting information about your server
=====================================

This is just a cheat sheet for quick reference. No warranty whatsoever.

.. contents::
    :local:
    :depth: 1

.. highlight:: console

What operating system is running on this machine::

 $ uname -a
 $ hostnamectl

For how long has this server been running since book::

 $ uptime

Show a list of other system users (only those who can open a shell)::

  $ grep sh$ /etc/passwd

List of users who are working on this server at the moment::

  $ who -Hu

What type of hardware this server is running on::

 $ cat /sys/class/dmi/id/sys_vendor
 $ cat /sys/class/dmi/id/product_name

What processes are running on this server::

 $ pstree -pa 1

See the main system logs::

  $ sudo dmesg
  $ sudo journalctl


External links:

- https://opensource.com/article/20/12/linux-server
