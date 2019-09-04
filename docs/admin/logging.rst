.. _host.logging:

=============
About logging
=============

This document explains everything you need to know about logging for
Lino applications.

We presume that you have read the Django's doc about `Logging
<https://docs.djangoproject.com/en/2.2/topics/logging/>`__.


The Lino application log
========================

.. xfile:: log

When a Lino process starts up and sees a subdirectory named
:xfile:`log` in the project directory, then it automatically starts
logging.

The main logger file
====================
      
.. xfile:: lino.log
.. xfile:: system.log

    The name of Lino's main logger file Default value is
    :xfile:`lino.log`. Until 20160729 it was :xfile:`system.log`.


Lino logging configuration
==========================

Some settings influence logging:

- :attr:`lino.core.site.Site.history_aware_logging`
- :attr:`lino.core.site.Site.logger_filename`
- :attr:`lino.core.site.Site.auto_configure_logger_names`
- :attr:`lino.core.site.Site.log_each_action_request`
- :meth:`lino.core.site.Site.setup_logging`
  
  

Setting the log level via the environment
=========================================


.. envvar:: LINO_LOGLEVEL

If an environment variable :envvar:`LINO_LOGLEVEL` is set, then it
should contain the log level to use for both console and file
handlers. It should be one of `INFO`, `DEBUG` etc.


.. _logrotate:

Configuring logrotate
=====================


To activate logging to a file, you simply add a symbolic link named
:xfile:`log` which points to the actual location::

    $ sudo mkdir -p /var/log/lino/
    $ sudo chown :www-data /var/log/lino/
    $ sudo chmod g+ws /var/log/lino/
    $ sudo mkdir /var/log/lino/prj1/
    $ cd ~/mypy/prj1/
    $ ln -s /var/log/lino/prj1/ log/

                    
We recommend a file :file:`/etc/logrotate.d/lino` with something like::

    /path/to/lino_sites/prod/log/lino.log {
            weekly
            missingok
            rotate 156
            compress
            delaycompress
            notifempty
            create 660 root www-data
            su root www-data
            sharedscripts
    }
  

After changes in the config you can tell logrotate to force them::
   
  $ sudo logrotate -f /etc/logrotate.d/lino



.. _log2syslog:

Logging all bash commands to syslog
===================================


Add the following to your system-wide :file:`/etc/bash.bashrc`:
                  
.. literalinclude:: log2syslog



