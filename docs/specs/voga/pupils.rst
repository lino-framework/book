.. doctest docs/specs/voga/pupils.rst
.. _voga.specs.pupils:

==================================
Managing participants in Lino Voga
==================================

..  doctest init:
   
    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *
    

Displaying all pupils who are either Member or Non-Member (using
gridfilter):


>>> from django.utils.http import urlquote
>>> url = '/api/courses/Pupils?'
>>> url += 'limit=10&start=0&fmt=json&'
>>> # url += "rp=ext-comp-1213&"
>>> # url += "pv=&pv=&pv=&pv=&pv=&pv=&pv=&"
>>> url += "filter=" + urlquote('[{"type":"string","value":"mem","field":"pupil_type"}]')
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200

The response to this AJAX request is in JSON:

>>> d = json.loads(res.content.decode())
>>> d['count']
24



Filtering pupils
=================

Select pupils who participate in a given course:

>>> obj = rt.models.courses.Course.objects.get(pk=1)
>>> obj
Course #1 ('001 Greece 2014')
>>> pv = dict(course=obj)
>>> rt.show('courses.Pupils', param_values=pv)
============================= ============================= ================== ========= ===== ===== ======== ==============
 Name                          Address                       Participant Type   Section   LFV   CKK   Raviva   Mitglied bis
----------------------------- ----------------------------- ------------------ --------- ----- ----- -------- --------------
 Hans Altenberg (MEL)          Aachener Straße, 4700 Eupen   Member                       Yes   No    No       31/12/2015
 Bernd Brecht (ME)             Aachen, Germany               Member                       No    No    No       31/12/2015
 Jacqueline Jacobs (ME)        Fränzel, 4700 Eupen           Helper                       No    No    No       31/12/2016
 Christian Radermacher (MEL)   4730 Raeren                   Non-member                   Yes   No    No       31/12/2015
============================= ============================= ================== ========= ===== ===== ======== ==============
<BLANKLINE>

Note that above table contains the same pupils but not the same
columns as :class:`EnrolmentsByCourse
<lino_voga.lib.courses.desktop.EnrolmentsByCourse>`:

>>> rt.show('courses.EnrolmentsByCourse', obj)
==================== ============================= ============ ============ ============= ======== ========== ============= ============== ===============
 Date of request      Participant                   Start date   End date     Places used   Remark   Fee        Free events   Amount         Workflow
-------------------- ----------------------------- ------------ ------------ ------------- -------- ---------- ------------- -------------- ---------------
 25/07/2014           Hans Altenberg (MEL)                                    1                      Journeys                 295,00         **Confirmed**
 25/07/2014           Bernd Brecht (ME)                                       1                      Journeys                 295,00         **Confirmed**
 09/08/2014           Jacqueline Jacobs (ME)                     18/09/2014   2                      Journeys                 590,00         **Confirmed**
 29/08/2014           Christian Radermacher (MEL)   29/08/2014                1                      Journeys                 295,00         **Confirmed**
 **Total (4 rows)**                                                           **5**                             **0**         **1 475,00**
==================== ============================= ============ ============ ============= ======== ========== ============= ============== ===============
<BLANKLINE>

