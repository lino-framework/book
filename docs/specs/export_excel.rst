.. doctest docs/specs/export_excel.rst
.. _lino.specs.export_excel:
.. _lino.tested.export_excel:

==================
Exporting to Excel
==================

When :mod:`lino.modlib.export_excel` is installed, every grid view has
a button `Export to Excel`.



.. include:: /include/tested.rst
             
>>> from lino import startup
>>> startup('lino_book.projects.min3.settings.doctests')
>>> from lino.api.doctest import *


Overview
========

Robin has twelve appointments in the period 20141023..20141122:

>>> settings.SITE.the_demo_date
datetime.date(2017, 8, 19)

>>> from lino.utils import i2d
>>> pv = dict(start_date=i2d(20170801), end_date=i2d(20170831))
>>> rt.login('robin').show(cal.MyEntries, param_values=pv, header_level=1)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
=======================================================================
My appointments (Managed by Robin Rood, Dates 01.08.2017 to 31.08.2017)
=======================================================================
=========================================== ===============================
 Description                                 Workflow
------------------------------------------- -------------------------------
 `Breakfast (31.08.2017 10:20) <Detail>`__   **☑ Took place** → [☐]
 `Interview (29.08.2017 13:30) <Detail>`__   **☼ Published** → [☒] [☐]
 `Seminar (27.08.2017 09:40) <Detail>`__     **☐ Draft** → [☼] [☒]
 `Breakfast (25.08.2017 11:10) <Detail>`__   **☒ Cancelled**
 `Interview (23.08.2017 08:30) <Detail>`__   **? Suggested** → [☼] [☒]
 `Seminar (21.08.2017 10:20) <Detail>`__     **☑ Took place** → [☐]
 `Breakfast (19.08.2017 13:30) <Detail>`__   **☼ Published** → [☑] [☒] [☐]
 `Interview (17.08.2017 09:40) <Detail>`__   **☐ Draft** → [☑] [☒]
 `Seminar (15.08.2017 11:10) <Detail>`__     **☒ Cancelled**
 `Breakfast (13.08.2017 08:30) <Detail>`__   **? Suggested** → [☑] [☒]
 `Interview (11.08.2017 10:20) <Detail>`__   **☑ Took place** → [☐]
 `Seminar (09.08.2017 13:30) <Detail>`__     **☼ Published** → [☑] [☒] [☐]
 `Breakfast (07.08.2017 09:40) <Detail>`__   **☐ Draft** → [☑] [☒]
 `Interview (05.08.2017 11:10) <Detail>`__   **☒ Cancelled**
 `Seminar (03.08.2017 08:30) <Detail>`__     **? Suggested** → [☑] [☒]
 `Breakfast (01.08.2017 10:20) <Detail>`__   **☑ Took place** → [☐]
=========================================== ===============================
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

    >>> from lino.modlib.office.roles import OfficeStaff, OfficeOperator
    >>> cal.MyEntries.model.manager_roles_required == {(OfficeStaff, OfficeOperator)}
    True
    >>> ba = cal.MyEntries.get_action_by_name("export_excel")
    >>> u = rt.login('robin').user
    >>> ba.actor.get_view_permission(u.user_type)
    True
    >>> ba.action.get_view_permission(u.user_type)
    True
    >>> ba.allow_view(u.user_type)
    True
    >>> ba.get_view_permission(u.user_type)
    True


>>> url = "/api/cal/MyEntries?_dc=1414106085710"
>>> url += "&cw=411&cw=287&cw=411&cw=73&cw=274&cw=140&cw=274&cw=220&cw=220&cw=220&cw=287&cw=181&cw=114&cw=181&cw=114&cw=170&cw=73&cw=73&cw=274&cw=140&cw=274&cw=274&cw=181&cw=274&cw=140"
>>> url += "&ch=&ch=true&ch="
>>> url += "&ch=true&ch=true&ch=true&ch=true&ch=true&ch=false&ch=true&ch=true&ch=false&ch=false&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true"
>>> url += "&ci=when_text&ci=summary&ci=workflow_buttons&ci=id&ci=owner_type&ci=owner_id&ci=user&ci=modified&ci=created&ci=build_time&ci=build_method&ci=start_date&ci=start_time&ci=end_date&ci=end_time&ci=access_class&ci=sequence&ci=auto_type&ci=event_type&ci=transparent&ci=room&ci=priority&ci=state&ci=assigned_to&ci=owner&name=0"
>>> url += "&pv=01.08.2017&pv=31.08.2017&pv=&pv=&pv=2&pv=&pv=&pv=&pv=y"
>>> url += "&an=export_excel&sr=61"

>>> print(' '.join(cal.MyEntries.params_layout.main.split()))
start_date end_date observed_event state user assigned_to project event_type room show_appointments

>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content.decode())
>>> len(result)
2
>>> result['success']
True
>>> print(result['open_url'])
/media/cache/appyxlsx/127.0.0.1/cal.MyEntries.xlsx


Testing the generated file
==========================

The action performed without error.
But does the file exist?

>>> from unipath import Path
>>> p = Path(settings.MEDIA_ROOT, 
...    'cache', 'appyxlsx', '127.0.0.1', 'cal.MyEntries.xlsx')
>>> p.exists()
True

In order to test whether the file is really okay, we load it using
`openpyxl`.

>>> from openpyxl import load_workbook
>>> wb = load_workbook(filename=p)

>>> print(wb.get_sheet_names()[0])
My appointments (Managed by Rol

>>> ws = wb.active
>>> print(ws.title)
My appointments (Managed by Rol


Note that long titles are truncated because Excel does not support
worksheet names longer than 32 characters.

It has 5 columns and 13 rows:

>>> rows = list(ws.rows)
>>> print("{}, {}".format(len(list(ws.columns)), len(rows)))
5, 16

The first row contains our column headings. Which differ from those of
the table above because our user had changed them manually:

>>> print(' | '.join([cell.value for cell in rows[0]]))
When | Workflow | Created | Start date | Start time

>>> print(' | '.join([str(cell.value) for cell in rows[1]]))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
Wed 30/08/2017 (09:40) | **☐ Draft** → ` ☼  <javascript:Lino.cal.MyEntries.wf1(null,true,193,{  })>`__ ` ☒  <javascript:Lino.cal.MyEntries.wf3(null,true,193,{  })>`__ | ... | 2017-08-30 00:00:00 | 09:40:00



Unicode
=======

>>> test_client.force_login(rt.login('romain').user)
>>> res = test_client.get(url, REMOTE_USER='romain')
>>> print(res.status_code)
200
>>> wb = load_workbook(filename=p)
>>> ws = wb.active
>>> print(ws.title)
Mes rendez-vous (Traité par Rol

>>> rows = list(ws.rows)
>>> print(' | '.join([cell.value for cell in rows[0]]))
Quand | Workflow | Créé | Date début | Heure de début

>>> print(' | '.join([str(cell.value) for cell in rows[1]]))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
mer. 30/08/2017 (09:40) | **☐ Brouillon** → ` ☼  <javascript:Lino.cal.MyEntries.wf1(null,true,193,{  })>`__ ` ☒  <javascript:Lino.cal.MyEntries.wf3(null,true,193,{  })>`__ | ... | 2017-08-30 00:00:00 | 09:40:00




More queries
============

>>> url = "/api/cal/Events?an=export_excel"
>>> test_client.get(url, REMOTE_USER='robin').status_code
200

>>> url = "/api/cal/EntriesByDay?an=export_excel"
>>> test_client.get(url, REMOTE_USER='robin').status_code
200


The following failed with :message:`ValueError: Cannot convert
1973-07-21 to Excel` until 20161014:
    
>>> url = "/api/contacts/Persons?an=export_excel"
>>> url += "&cw=123&cw=185&cw=129&cw=64&cw=64&cw=34&cw=64&cw=129&cw=129&cw=123&cw=123&cw=70&cw=123&cw=129&cw=129&cw=129&cw=70&cw=70&cw=129&cw=129&cw=366&cw=129&cw=129&cw=129&cw=129&cw=58&cw=76&cw=185&cw=185&cw=185&cw=185"
>>> url += "&ch=&ch=&ch=&ch=&ch=&ch=&ch=&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=true&ch=false&ch=true&ch=true&ch=true&ch=true&ch=true"
>>> url += "&ci=name_column&ci=address_column&ci=email&ci=phone&ci=gsm&ci=id&ci=language&ci=url&ci=fax&ci=country&ci=city&ci=zip_code&ci=region&ci=addr1&ci=street_prefix&ci=street&ci=street_no&ci=street_box&ci=addr2&ci=name&ci=remarks&ci=title&ci=first_name&ci=middle_name&ci=last_name&ci=gender&ci=birth_date&ci=workflow_buttons&ci=age&ci=overview&ci=mti_navigator"
>>> url += "&name=0&&pv=&pv=&pv=&pv="
>>> test_client.get(url, REMOTE_USER='robin').status_code
200

