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

The plugin has two custom settings, which are the default values for the
:class:`MyExpiringUploads` table:

>>> dd.plugins.uploads.expiring_start
-30
>>> dd.plugins.uploads.expiring_end
365

The demo_coach is the user who uploaded all demo uploads.

>>> dd.plugins.clients.demo_coach
'nathalie'

We have two social workers Nathalie and Nelly.

>>> rt.show("users.AllUsers")
========== ===================== ============ ===========
 Username   User type             First name   Last name
---------- --------------------- ------------ -----------
 audrey     300 (Auditor)
 laura      100 (Teacher)         Laura        Lieblig
 martina    400 (Coordinator)
 nathalie   200 (Social worker)
 nelly      200 (Social worker)
 robin      900 (Administrator)   Robin        Rood
 rolf       900 (Administrator)   Rolf         Rompen
 romain     900 (Administrator)   Romain       Raffault
 sandra     410 (Secretary)
========== ===================== ============ ===========
<BLANKLINE>

>>> rt.login('robin').show("uploads.Uploads", column_names="id user project project__user end_date needed")
==== ============= ====================== ================= ============= ========
 ID   Uploaded by   Client                 Primary coach     Valid until   Needed
---- ------------- ---------------------- ----------------- ------------- --------
 10   nathalie      ABDALLAH Aáish (127)   Robin Rood        22/03/2018    Yes
 9    nathalie      ABDALLAH Aáish (127)   Robin Rood        22/03/2018    No
 8    nathalie      ABDALLA Aádil (120)    Rolf Rompen       12/03/2018    No
 7    nathalie      ABDALLA Aádil (120)    Rolf Rompen       12/03/2018    No
 6    nathalie      ABBASI Aáishá (118)    Romain Raffault   02/03/2018    No
 5    nathalie      ABBASI Aáishá (118)    Romain Raffault   02/03/2018    No
 4    nathalie      ABBAS Aábid (115)      nelly             20/02/2018    Yes
 3    nathalie      ABBAS Aábid (115)      nelly             20/02/2018    Yes
 2    nathalie      ABAD Aábdeen (114)     nathalie          10/02/2018    Yes
 1    nathalie      ABAD Aábdeen (114)     nathalie          10/02/2018    Yes
==== ============= ====================== ================= ============= ========
<BLANKLINE>

Note that uploads #4 and #3 were not uploaded by the client's primary coach.

>>> obj = rt.models.uploads.Upload.objects.get(pk=3)
>>> rec = rt.login("nathalie").spawn(uploads.UploadsByProject).elem2rec_detailed(obj)
>>> print(rec['disable_delete'])
None

Nelly (another social worker) and Sandra (secretary) can also modify the upload

>>> rec = rt.login("nelly").spawn(uploads.UploadsByProject).elem2rec_detailed(obj)
>>> print(rec['disable_delete'])
None
>>> rec = rt.login("sandra").spawn(uploads.UploadsByProject).elem2rec_detailed(obj)
>>> print(rec['disable_delete'])
None

But laura (a teacher) cannot edit them:

>>> rec = rt.login("laura").spawn(uploads.UploadsByProject).elem2rec_detailed(obj)
>>> print(rec['disable_delete'])
You have no permission to delete this row.

Note about security. You might wonder why Sandra is able to see data that she
isn't allow to see:

>>> print(rec['data']['project'])
ABBAS Aábid (115)

This is *not* a security issue because we are at the command line interface
where access rights are not verified.  If Sandra would do a manual AJAX call,
she would not be able to see data that she isn't allow to see. Here is the proof:

>>> test_client.force_login(rt.login("laura").user)
>>> url = "/api/avanti/Clients?fmt=json&&limit=23&start=0"
>>> test_client.get(url)  #doctest: +ELLIPSIS
Forbidden (Permission denied): /api/avanti/Clients
Traceback (most recent call last):
...
django.core.exceptions.PermissionDenied: As 100 (Teacher) you have no view permission for this action.
<HttpResponseForbidden status_code=403, "text/html; charset=utf-8">

>>> url = "/api/avanti/uploads.UploadsByProject?fmt=json&&limit=23&start=0&mt=31&mk=114"
>>> test_client.get(url)  #doctest: +ELLIPSIS
Not Found: /api/avanti/uploads.UploadsByProject
<HttpResponseNotFound status_code=404, "text/html">






Extended uploads
================

.. class:: Upload

    Extends :class:`lino.modlib.uploads.Upload` by adding some fields.

    .. attribute:: start_date

    .. attribute:: end_date

      Date until which the original document is valid.

    .. attribute:: needed

      Whether the responsible user should be reminded when validity of this
      upload reaches its end.



My expiring upload files
========================

When you want Lino to remind you when some important document (e.g. a driving
licence) is going to expire, then you should store the document's expiry date in
the  :attr:`Upload.end_date` field and check the :attr:`Upload.needed` field.

.. class:: MyExpiringUploads

    Shows the upload files that are marked as :attr:`Upload.needed` and whose
    :attr:`Upload.end_date` is within a given period.


>>> rt.login(dd.plugins.clients.demo_coach).show("uploads.MyExpiringUploads")
==================== ================== ================== ============= ============ ============= ========
 Client               Upload type        Description        Uploaded by   Valid from   Valid until   Needed
-------------------- ------------------ ------------------ ------------- ------------ ------------- --------
 ABAD Aábdeen (114)   Residence permit   Residence permit   nathalie                   10/02/2018    Yes
 ABAD Aábdeen (114)   Work permit        Work permit        nathalie                   10/02/2018    Yes
==================== ================== ================== ============= ============ ============= ========
<BLANKLINE>
