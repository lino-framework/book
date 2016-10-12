.. _admin.oood:

============================
Running a LibreOffice server
============================

When your Lino applicaton uses :mod:`lino_xl.lib.appypod`, then you
need to have a LibreOffice server running so that the users of your
site can print documents.

This is because :mod:`lino_xl.lib.appypod` uses `appy.pod
<http://appyframework.org/pod.html>`_ which in turn uses `python3-uno
<https://packages.debian.org/de/sid/python3-uno>`__ to connect to a
`LibreOffice` server.

Installation
============

`appy.pod` is part of the ``appy`` Python package and was
automatically installed together with Lino into your Python
environment.  But `libreoffice` and `python3-uno` must be installed by
the system administrator using something like this::

  $ sudo apt-get install libreoffice python3-uno

Starting the LibreOffice server
===============================

Then you need to run a LO server. For **occasional or experimental
usage** you can fire it up using something like this::

  $ libreoffice '--accept=socket,host=127.0.0.1,port=8100;urp;' &

You might create an executable bash script named :cmd:`oood` in your
``PATH`` with above line.

For **regular usage** and especially on a production server you will
want to use a startup script.  Vic Vijayakumar has written such a
script, and for convenience the Lino repository contains a copy of it
:file:`/bash/openoffice-headless`.

- Make your local copy of the startup script::

    $ sudo cp ~/repositories/lino/bash/openoffice-headless /etc/init.d

- Edit your copy::
    
    $ sudo nano /etc/init.d/openoffice-headless
    
  Check the value of the `OFFICE_PATH` variable in that script::
  
    OFFICE_PATH=/usr/lib/libreoffice

- Make it executable::
  
    $ sudo chmod 755 /etc/init.d/openoffice-headless
    
- Finally, run ``update-rc.d`` to have the daemon 
  automatically start when the server boots::

    $ sudo update-rc.d openoffice-headless defaults
    

Setting ``appy_params``
=======================

If you have Python 3 installed under :file:`/usr/bin/python3`, then
you don't need to read this section.  Otherwise you must set your
:attr:`appy_params <lino.core.site.Site.appy_params>` to point to your
`python3` executable, e.g. by specifying in your
:xfile:`settings.py`::

  SITE.appy_params.update(pythonWithUnoPath='/usr/bin/python3')

This is because Lino runs under Python **2** while `python-uno` needs
Python **3**.  To resolve that conflict, `appy.pod` has this
configuration option which causes it to run its UNO call in a
subprocess with Python 3.

If you don't want to do this again and again for every Lino site on
your machine, then you should put this to your :xfile:`lino_local.py`
file.

