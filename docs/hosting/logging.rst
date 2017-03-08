=============
About logging
=============

The Lino application log
========================

When a Lino process starts up and sees a subdirectory named `log` in
the project directory, then it automatically starts logging.

- :attr:`lino.core.site.Site.history_aware_logging`
- :attr:`lino.core.site.Site.logger_filename`
- :attr:`lino.core.site.Site.auto_configure_logger_names`
  


.. _log2syslog:

Logging all bash commands to syslog
===================================


Add the following to your system-wide :file:`/etc/bash.bashrc`:
                  
.. literalinclude:: log2syslog


