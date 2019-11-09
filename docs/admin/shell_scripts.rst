.. _admin.shell_scripts:
.. _admin.bash_scripts:

=============================================
Shell scripts to be used on a production site
=============================================

See also :xfile:`make_snapshot.sh` and :xfile:`pull.sh`.

The following files are designed as templates to be copied to a Lino project
directory and to be edited in order to adapt them to your system environment.

.. xfile:: import_sepa.sh

    Import bank statements to Lino (for applications that use
    :mod:`lino_xl.lib.b2c`).

    Installation notes:

    When you have tested this script, you can add a file
    :file:`/etc/cron.d/import_sepa` to run it e.g. every 30 minutes on
    workdays during office time::

        # m   h    dom mon dow  user  command
        15,45 7-18 *   *   1-5  www-data  /path/to/mysite/import_sepa.sh
