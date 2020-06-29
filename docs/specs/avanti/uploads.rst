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
declare this dependency because making it automatic would
cause changes in the menu item ordering in :ref:`welfare`.

The plugin has two custom settings:

>>> dd.plugins.uploads.expiring_start
-30
>>> dd.plugins.uploads.expiring_end
365

These are the default values for the :class:`MyExpiringUploads`  table

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


Extended uploads
================

.. class:: Upload

    Extends :class:`lino.modlib.uploads.Upload` by adding some fields.

    .. attribute:: needed

    .. attribute:: start_date

    .. attribute:: end_date




My expiring upload files
========================

When you want Lino to remind you when some important document (e.g. a driving
licence) is going to expire, then you should store the document's expiry date in
the  :attr:`Upload.end_date` field and check the :attr:`Upload.needed` field.

.. class:: MyExpiringUploads

    Shows the upload files that are marked as :attr:`Upload.needed` and whose
    :attr:`Upload.end_date` is within a given period.
