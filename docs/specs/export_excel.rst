.. _lino.specs.export_excel:
.. _lino.tested.export_excel:

Exporting to Excel
==================

When :mod:`lino.modlib.export_excel` is installed, every grid view has
a button `Export to Excel`.

This document tests this functionality.


.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_export_excel
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.min1.settings.doctests')
    >>> from lino.api.doctest import *


Robin has twelve appointments in the period 20141023..20141122:

>>> from lino.utils import i2d
>>> pv = dict(start_date=i2d(20141023), end_date=i2d(20141122))
>>> rt.login('robin').show(cal.MyEvents, param_values=pv, header_level=1)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
=======================================================================
My appointments (Managed by Robin Rood, Dates 23.10.2014 to 22.11.2014)
=======================================================================
======================== ===================== =============== ================
 When                     Calendar Event Type   Summary         Workflow
------------------------ --------------------- --------------- ----------------
 Thu 23/10/2014 (13:30)   Meeting               Evaluation      **Omitted**
 Fri 24/10/2014 (08:30)   Meeting               First meeting   **Suggested**
 Sat 25/10/2014 (09:40)   Meeting               Interview       **Draft**
 Sat 25/10/2014 (10:20)   Meeting               Lunch           **Took place**
 Sun 26/10/2014 (11:10)   Meeting               Dinner          **Cancelled**
 Mon 27/10/2014 (08:30)   Meeting               Meeting         **Suggested**
 Mon 27/10/2014 (13:30)   Meeting               Breakfast       **Omitted**
 Tue 28/10/2014 (09:40)   Meeting               Consultation    **Draft**
 Wed 29/10/2014 (10:20)   Meeting               Seminar         **Took place**
 Wed 29/10/2014 (11:10)   Meeting               Evaluation      **Cancelled**
 Thu 30/10/2014 (13:30)   Meeting               First meeting   **Omitted**
 Fri 31/10/2014 (08:30)   Meeting               Interview       **Suggested**
======================== ===================== =============== ================
<BLANKLINE>

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
>>> url += "&pv=23.10.2014&pv=22.11.2014&pv=&pv=&pv=2&pv=&pv=&pv=&pv=y"
>>> url += "&an=export_excel&sr=61"

>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> print(result.keys())
[u'open_url', u'success']
>>> print(result['open_url'])
/media/cache/appyxlsx/127.0.0.1/cal.MyEvents.xlsx

The action performed without error.
But does the file exist?

>>> from unipath import Path
>>> p = Path(settings.MEDIA_ROOT, 
...    'cache', 'appyxlsx', '127.0.0.1', 'cal.MyEvents.xlsx')
>>> p.exists()
True

Now test whether the file is really okay.

>>> from openpyxl import load_workbook
>>> wb = load_workbook(filename=p)
>>> print(wb.get_sheet_names())
[u'My appointments (Managed by Rol']
>>> ws = wb.active
>>> print(ws.title)
My appointments (Managed by Rol


Note that long titles are truncated because Excel does not support
worksheet names longer than 32 characters.

It has 5 columns and 13 rows:

>>> print(len(ws.columns), len(ws.rows))
(5, 13)

The first row contains our column headings. Which differ from those of
the table above because our user had changed them manually:

>>> print(' | '.join([cell.value for cell in ws.rows[0]]))
When | Workflow | Created | Start date | Start time

>>> print(' | '.join([str(cell.value) for cell in ws.rows[1]]))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
Thu 23/10/2014 (10:20) | **Took place** → `[img flag_green] <javascript:Lino.cal.MyEvents.take(null,114,{  })>`__ | ... | 2014-10-23 00:00:00 | 10:20:00

Note that the Workflow column (`workflow_buttons`) contains
images. Since these are not available in Excel, we made a compromise.


Unicode
=======

>>> res = test_client.get(url, REMOTE_USER='romain')
>>> print(res.status_code)
200
>>> wb = load_workbook(filename=p)
>>> ws = wb.active
>>> print(ws.title)
Mes rendez-vous (Traité par Rol

>>> print(' | '.join([cell.value for cell in ws.rows[0]]))
Quand | État | Créé | Date début | Heure de début

>>> print(' | '.join([str(cell.value) for cell in ws.rows[1]]))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
jeu. 23/10/2014 (10:20) | **Terminé** → `[img flag_green] <javascript:Lino.cal.MyEvents.take(null,114,{  })>`__ | ... | 2014-10-23 00:00:00 | 10:20:00
