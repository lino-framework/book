.. _admin.ram:

=========================
Analyzing RAM usage
=========================

These are just my personal notes. No warranty whatsoever.

.. contents::
    :local:
    :depth: 1


Show available memory::

  $ free -h

Show active processes sorted by memory usage in percent::

  $ ps -o pid,user,%mem,command ax | sort -b -k3 -r

Thanks to https://linuxhint.com/check_memory_usage_process_linux/
