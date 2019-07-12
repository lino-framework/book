.. _monit:

============================================
Using `monit` to monitor a production server
============================================

This page collects some hints for configuring monit on a Lino production
server.

Installation
============

Simply run::

    $ sudo apt install monit



Configuration
=============

.. xfile:: healthcheck.conf

A file in :file:`/etc/monit/conf.d` with the following content::

  check program status with path /usr/local/bin/healthcheck.sh
      if status != 0 then alert




.. xfile:: healthcheck.sh

A system-wide script (in :file:`/usr/local/bin`) to be executed either manually
as root or by monit. The script outputs some readable information about what it
is doing. If something is not perfect, it reports what is wrong and then sets
its exit status to non-zero.

Example content::

    #! bin/bash
    set -e  # exit on error
    echo -n "Checking supervisor status: "
    supervisorctl status | awk '{if ( $2 != "RUNNING" ) { print "ERROR: " $1 " is not running"; exit 1}}'
    echo "... OK"



.. xfile:: /etc/monit/monitrc

The system-wide monit configuration file.

Maintenance
===========

You can say :command:`monit status` at any moment.


Weblinks
========

- https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-monit
- https://www.tecmint.com/how-to-install-and-setup-monit-linux-process-and-services-monitoring-program/
- https://tutorialinux.com/monitor-all-the-things-with-monit/
- `monit documentation <https://mmonit.com/monit/documentation/monit.html>`__


