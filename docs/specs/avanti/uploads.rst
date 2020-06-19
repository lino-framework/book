.. doctest docs/specs/avanti/uploads.rst
.. _avanti.specs.uploads:

=======================================
Uploads with expiration date management
=======================================

.. currentmodule:: lino_xl.lib.uploads

The :mod:`lino_xl.lib.uploads` plugin extends :mod:`lino.modlib.uploads` by
adding "expiration date management" for uploads.  This is used by social agents
("coaches") to manage certain documents about their "clients". For example the
coach might want to get a reminder when the driving license of one of their
clients is going to expire.
This plugin requires the :mod:`lino_xl.lib.clients` plugin.



.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.avanti1.settings.doctests')
>>> from lino.api.doctest import *

Although this plugin requires the :mod:`lino_xl.lib.clients` plugin, it does not
handle this dependency automatically.  This is because making it automatic would
cause changes in the menu item ordering in welfare.

>>> dd.plugins.uploads.needs_plugins
[]

>>> rt.login(dd.plugins.clients.demo_coach).show("uploads.MyExpiringUploads")
==================== ================== ================== ============= ============ ============= ========
 Client               Upload type        Description        Uploaded by   Valid from   Valid until   Needed
-------------------- ------------------ ------------------ ------------- ------------ ------------- --------
 ABAD Aábdeen (114)   Residence permit   Residence permit   nathalie                   10/02/2018    Yes
 ABAD Aábdeen (114)   Work permit        Work permit        nathalie                   10/02/2018    Yes
==================== ================== ================== ============= ============ ============= ========
<BLANKLINE>

>>> dd.plugins.clients.demo_coach
'nathalie'
