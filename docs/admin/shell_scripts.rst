.. _admin.shell_scripts:
.. _admin.bash_scripts:

=============================================
Shell scripts to be used on a production site
=============================================

The following files are designed as templates to be copied to every
Lino project directory and to be edited in order to adapt them to
your system environment.

.. xfile:: make_snapshot.sh

    Make a snapshot of the project database.
    
    Usage: See :ref:`admin.snapshot`.
    
    Template: :srcref:`/bash/make_snapshot.sh` 
    
    Installation notes:
    
    When you have tested this script, you can add a file
    :file:`/etc/cron.d/lino_backup` to run it every day at **6h33**::
    
        # Backup Lino database (Python dump) once a day
        # m h dom mon dow user  command
        33 6 * * *       www-data        /path/to//mysite/make_snapshot.sh



.. xfile:: pull.sh

    Update the source code repositories used by this project.

    Usage: see :ref:`admin.upgrade`.


.. xfile:: import_sepa.sh

    Import bank statements to Lino (for applications that use
    :mod:`lino_cosi.lib.b2c`).
    
    Installation notes:
    
    When you have tested this script, you can add a file
    :file:`/etc/cron.d/import_sepa` to run it e.g. every 30 minutes on
    workdays during office time::
    
        # m   h    dom mon dow  user  command
        15,45 7-18 *   *   1-5  www-data  /path/to/mysite/import_sepa.sh


