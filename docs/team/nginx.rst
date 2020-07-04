========================================
Setting up a simulated production server
========================================

For testing nginx-specific issues you might want to run a "simulated" production
server that unlike a real production server uses your local repositories but
otherwise runs as a series of real nginx and wsgi and :manage:`linod` processes.

Set shared permissions in your default :term:`virtualenv`::

      $ sudo chown root:www-data .
      $ sudo chmod g+ws .

Otherwise it might happen that nginx compiles a :xfile:`.pyc` file that you
cannot modify afterwards.

Run :cmd:`getlino configure` and :cmd:`getlino startsite` as root (remember
:ref:`getlino.install.prod` for details)::

   $ sudo env PATH=$PATH getlino configure
   $ sudo env PATH=$PATH getlino startsite noi first

Point your browser to http://first.localhost

.. rubric:: Pitfalls

When using nginx and you want to restart it, you must restart *supervisor*
(not nginx) because the wsgi process of the site is running there. nginx
itself usually doesn't need to be restarted.
