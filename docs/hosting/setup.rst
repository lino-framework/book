.. _hosting.setup:

==============================
Setting up a Lino hosting site
==============================


Cheat sheet for setting up a new Lino site::

  $ cd /usr/local/python/lino_sites
  $ ls xxx  # must give error
  $ cp -a TPL xxx

  $ mkdir /var/log/lino/xxx
  $ go xxx
  
  $ ln -s /var/log/lino/xxx log
  $ virtualenv env
  $ cp -a /usr/local/python/lino_sites/TPL/env/repositories env

  $ nano pull.sh  # check which repositories are used by this project
  $ pip install -U setuptools pip
  $ pip install -e env/repositories/lino
  $ pip install -e env/repositories/xl
  $ ...

  $ cd /etc/supervisor/conf.d
  $ sudo cp linod_TPL.conf linod_xxx.conf
  $ nano xxx.conf  # ALT-R and replace TPL by xxx
  
  $ cd /etc/apache2/sites-available
  $ sudo cp TPL.conf xxx.conf
  $ nano xxx.conf  # ALT-R and replace TPL by xxx
  $ sudo a2ensite xxx.conf

  $ reload_services


- TPL : some existing_site  
- xxx : name of new site
  

The :file:`/usr/local/python` directory is our customized site-wide
Python path::

  $ mkdir /usr/local/python
  $ touch /usr/local/python/__init__.py

Add the following to your system-wide :file:`/etc/bash.bashrc`::

.. literalinclude:: bash_aliases

Here is a template for your :xfile:`lino_local.py`::

.. literalinclude:: lino_local.py


The following files are the same for every project:

:xfile:`manage.py`::

    #!/usr/bin/env python
    if __name__ == "__main__":
        import sys ; sys.path.append('/usr/local/python')
        from lino_local import manage ; manage(__file__)

