.. _admin.libreoffice:

============================
Lino and LibreOffice
============================

When at least one :term:`Lino site` of a server uses :mod:`lino_xl.lib.appypod`,
then the server must have a LibreOffice service running so that the users of
your site can print documents.

You say this using the :cmd:`getlino configure --appy` option.

For background information see :doc:`oood`.

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
