.. _lino.specs.export_excel:
.. _lino.tested.export_excel:

==================
Exporting to Excel
==================

This document tests this functionality.


.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_export_excel
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.min2.settings.doctests')
    >>> from lino.api.doctest import *


Overview
========

When :mod:`lino.modlib.export_excel` is installed, every grid view has
a button `Export to Excel`.

Robin has twelve appointments in the period 20141023..20141122:

>>> from lino.utils import i2d
>>> pv = dict(start_date=i2d(20141023), end_date=i2d(20141122))
>>> rt.login('robin').show(cal.MyEvents, param_values=pv, header_level=1)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
=======================================================================
My appointments (Managed by Robin Rood, Dates 23.10.2014 to 22.11.2014)
=======================================================================
======================== ========= ===================== =============== =============================
 When                     Project   Calendar Event Type   Summary         Actions
------------------------ --------- --------------------- --------------- -----------------------------
 Thu 23/10/2014 (10:20)             Meeting               Meeting         **Took place** → [☐]
 Fri 24/10/2014 (11:10)             Meeting               Consultation    **Cancelled**
 Sat 25/10/2014 (08:30)             Meeting               Evaluation      **Suggested** → [☑] [☒]
 Sat 25/10/2014 (13:30)             Meeting               Seminar         **Published** → [☑] [☒] [☐]
 Sun 26/10/2014 (09:40)             Meeting               First meeting   **Draft** → [☑] [☒]
 Mon 27/10/2014 (10:20)             Meeting               Interview       **Took place** → [☐]
 Mon 27/10/2014 (11:10)             Meeting               Lunch           **Cancelled**
 Tue 28/10/2014 (13:30)             Meeting               Dinner          **Published** → [☑] [☒] [☐]
 Wed 29/10/2014 (08:30)             Meeting               Breakfast       **Suggested** → [☑] [☒]
 Wed 29/10/2014 (09:40)             Meeting               Meeting         **Draft** → [☑] [☒]
 Thu 30/10/2014 (10:20)             Meeting               Consultation    **Took place** → [☐]
 Fri 31/10/2014 (11:10)             Meeting               Seminar         **Cancelled**
======================== ========= ===================== =============== =============================
<BLANKLINE>


Building the file
=================

Let's export them to `.xls`.

When exporting to `.xls`, the URL is rather long because it includes
detailed information about the grid columns: their widths (``cw``),
whether they are hidden (``ch``) and their ordering (``ci``). This is
necessary because we want the resulting `.xls` sheet to reflect
if the client has changed these.

.. intermezzo 20150828

    >>> cal.MyEvents.model.manager_roles_required
    set([<class 'lino.modlib.office.roles.OfficeStaff'>])
    >>> ba = cal.MyEvents.get_action_by_name("export_excel")
    >>> u = rt.login('robin').user
    >>> ba.actor.get_view_permission(u.profile)
    True
    >>> ba.action.get_view_permission(u.profile)
    True
    >>> ba.allow_view(u.profile)
    True
    >>> ba.get_view_permission(u.profile)
    True

>>> url = "/api/cal/MyEvents?_dc=1414106085710"
>>> url += "&cw=411&cw=287&cw=411&cw=73&cw=274&cw=140&cw=274&cw=220&cw=220&cw=220&cw=287&cw=181&cw=114&cw=181&cw=114&cw=170&cw=73&cw=73&cw=274&cw=140&cw=274&cw=274&cw=181&cw=274&cw=140"
>>> url += "&ch=&ch=true&ch="
>>> url += "&ch=true&ch=true&ch=true&ch=true&ch=true&ch=false&ch=true&ch=true&ch=false&ch=false&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true"
>>> url += "&ci=when_text&ci=summary&ci=workflow_buttons&ci=id&ci=owner_type&ci=owner_id&ci=user&ci=modified&ci=created&ci=build_time&ci=build_method&ci=start_date&ci=start_time&ci=end_date&ci=end_time&ci=access_class&ci=sequence&ci=auto_type&ci=event_type&ci=transparent&ci=room&ci=priority&ci=state&ci=assigned_to&ci=owner&name=0"
>>> url += "&pv=23.10.2014&pv=22.11.2014&pv=&pv=&pv=2&pv=&pv=&pv=&pv=&pv=y"
>>> url += "&an=export_excel&sr=61"

>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> print(result.keys())
[u'open_url', u'success']
>>> print(result['open_url'])
/media/cache/appyxlsx/127.0.0.1/cal.MyEvents.xlsx


Testing the generated file
==========================

The action performed without error.
But does the file exist?

>>> from unipath import Path
>>> p = Path(settings.MEDIA_ROOT, 
...    'cache', 'appyxlsx', '127.0.0.1', 'cal.MyEvents.xlsx')
>>> p.exists()
True

In order to test whether the file is really okay, we load it using
`openpyxl`.

>>> from openpyxl import load_workbook
>>> wb = load_workbook(filename=p)

>>> print(wb.get_sheet_names()[0])
My appointments (Managed by Ran

>>> ws = wb.active
>>> print(ws.title)
My appointments (Managed by Ran


Note that long titles are truncated because Excel does not support
worksheet names longer than 32 characters.

It has 5 columns and 13 rows:

>>> rows = list(ws.rows)
>>> print(len(list(ws.columns)), len(rows))
(5, 13)

The first row contains our column headings. Which differ from those of
the table above because our user had changed them manually:

>>> print(' | '.join([cell.value for cell in rows[0]]))
When | Actions | Created | Start date | Start time

>>> print(' | '.join([str(cell.value) for cell in rows[1]]))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
Thu 23/10/2014 (13:30) | **Published** → ` ☑  <javascript:Lino.cal.MyEvents.close_meeting(null,126,{  })>`__ ` ☒  <javascript:Lino.cal.MyEvents.wf3(null,126,{  })>`__ ` ☐  <javascript:Lino.cal.MyEvents.wf4(null,126,{  })>`__ | ... | 2014-10-23 00:00:00 | 13:30:00



Unicode
=======

>>> res = test_client.get(url, REMOTE_USER='romain')
>>> print(res.status_code)
200
>>> wb = load_workbook(filename=p)
>>> ws = wb.active
>>> print(ws.title)
Mes rendez-vous (Traité par Ran

>>> rows = list(ws.rows)
>>> print(' | '.join([cell.value for cell in rows[0]]))
Quand | Actions | Créé | Date début | Heure de début

>>> print(' | '.join([str(cell.value) for cell in rows[1]]))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
jeu. 23/10/2014 (13:30) | **Publié** → ` ☑  <javascript:Lino.cal.MyEvents.close_meeting(null,126,{  })>`__ ` ☒  <javascript:Lino.cal.MyEvents.wf3(null,126,{  })>`__ ` ☐  <javascript:Lino.cal.MyEvents.wf4(null,126,{  })>`__ | ... | 2014-10-23 00:00:00 | 13:30:00




More queries
============

>>> url = "/api/cal/Events?an=export_excel"
>>> test_client.get(url, REMOTE_USER='robin').status_code
200

>>> url = "/api/cal/EventsByDay?an=export_excel"
>>> test_client.get(url, REMOTE_USER='robin').status_code
200


The following failed with :message:`ValueError: Cannot convert
1973-07-21 to Excel` until 20161014:
    
>>> url = "/api/contacts/Persons?an=export_excel"
>>> url += "&cw=123&cw=185&cw=129&cw=64&cw=64&cw=34&cw=64&cw=101&cw=101&cw=129&cw=129&cw=123&cw=123&cw=70&cw=123&cw=129&cw=129&cw=129&cw=70&cw=70&cw=129&cw=129&cw=366&cw=129&cw=129&cw=129&cw=129&cw=58&cw=76&cw=185&cw=185&cw=185&cw=185&cw=185&cw=185&ch=&ch=&ch=&ch=&ch=&ch=&ch=&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=false&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ci=name_column&ci=address_column&ci=email&ci=phone&ci=gsm&ci=id&ci=language&ci=modified&ci=created&ci=url&ci=fax&ci=country&ci=city&ci=zip_code&ci=region&ci=addr1&ci=street_prefix&ci=street&ci=street_no&ci=street_box&ci=addr2&ci=name&ci=remarks&ci=title&ci=first_name&ci=middle_name&ci=last_name&ci=gender&ci=birth_date&ci=workflow_buttons&ci=description_column&ci=age&ci=overview&ci=mti_navigator&ci=created_natural&name=0&pv=&pv=&pv="
>>> test_client.get(url, REMOTE_USER='robin').status_code
200

