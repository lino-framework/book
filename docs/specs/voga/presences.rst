.. _voga.specs.presences:

=========
Presences
=========

.. to test only this doc:

    $ python setup.py test -s tests.DocsTests.test_presences

    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *
    
    

Filtering courses by their start/end date
=========================================

The parameter panel of most courses tables has two fields
:guilabel:`Period from` and :guilabel:`until`. Here are some usage
examples.

>>> kwargs = dict(column_names="id line weekdays_text start_date end_date")

All courses that were active **already before March 2014**:

>>> pv = dict(end_date=i2d(20140301))
>>> rt.show(rt.actors.courses.Courses, param_values=pv, **kwargs)
==== ================================ ============== ============ ==========
 ID   Activity line                    When           Start date   End Date
---- -------------------------------- -------------- ------------ ----------
 22   MED (Finding your inner peace)   Every Monday   19/09/2013
 24   Yoga                             Every Monday   08/11/2013
 25   Yoga                             Every Friday   08/11/2013
==== ================================ ============== ============ ==========
<BLANKLINE>


All activities that were still **active after 20140807**.  This
includes all activities which have no :attr:`end_date` and those whose
end_date is after 20140807.

>>> pv = dict(start_date=i2d(20140807))
>>> rt.show(rt.actors.courses.Activities, param_values=pv, **kwargs)
==== ================================ ======================= ============ ============
 ID   Activity line                    When                    Start date   End Date
---- -------------------------------- ----------------------- ------------ ------------
 13   Rücken (Swimming)                Every Monday            11/07/2015
 15   Rücken (Swimming)                Every Tuesday           11/07/2015
 17   Rücken (Swimming)                Every Thursday          11/07/2015
 12   Rücken (Swimming)                Every Monday            11/07/2015
 14   Rücken (Swimming)                Every Tuesday           11/07/2015
 16   Rücken (Swimming)                Every Thursday          11/07/2015
 26   Europe                           Every month             19/06/2015   21/06/2015
 19   SV (Self-defence)                Every Friday            03/03/2015
 18   SV (Self-defence)                Every Friday            03/03/2015
 23   MED (Finding your inner peace)   Every Friday            01/02/2015
 7    WWW (Internet for beginners)     Every Wednesday         24/10/2014
 6    WWW (Internet for beginners)     Every Monday            24/10/2014
 8    WWW (Internet for beginners)     Every Friday            24/10/2014
 11   FG (Functional gymnastics)       Every Monday            04/10/2014
 10   FG (Functional gymnastics)       Every Monday            04/10/2014
 1    Europe                           14/08/2014-20/08/2014   14/08/2014   20/08/2014
 21   GLQ (GuoLin-Qigong)              Every Friday            16/07/2014
 20   GLQ (GuoLin-Qigong)              Every Monday            16/07/2014
 9    BT (Belly dancing)               Every Wednesday         28/03/2014
 4    comp (First Steps)               Every Wednesday         18/03/2014
 3    comp (First Steps)               Every Monday            18/03/2014
 5    comp (First Steps)               Every Friday            18/03/2014
 25   Yoga                             Every Friday            08/11/2013
 24   Yoga                             Every Monday            08/11/2013
 22   MED (Finding your inner peace)   Every Monday            19/09/2013
==== ================================ ======================= ============ ============
<BLANKLINE>

Courses which were active on at least one day of the **period between
20140303 and 20140422**:

>>> pv = dict(start_date=i2d(20140303), end_date=i2d(20140422))
>>> rt.show(rt.actors.courses.Courses, param_values=pv, **kwargs)
==== ================================ ================= ============ ==========
 ID   Activity line                    When              Start date   End Date
---- -------------------------------- ----------------- ------------ ----------
 3    comp (First Steps)               Every Monday      18/03/2014
 4    comp (First Steps)               Every Wednesday   18/03/2014
 5    comp (First Steps)               Every Friday      18/03/2014
 9    BT (Belly dancing)               Every Wednesday   28/03/2014
 22   MED (Finding your inner peace)   Every Monday      19/09/2013
 24   Yoga                             Every Monday      08/11/2013
 25   Yoga                             Every Friday      08/11/2013
==== ================================ ================= ============ ==========
<BLANKLINE>

