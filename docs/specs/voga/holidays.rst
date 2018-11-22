.. doctest docs/specs/voga/holidays.rst
.. _voga.specs.holidays:

==============================
Holidays in Lino Voga
==============================

See also :ref:`xl.specs.holidays`.

..  Some initialization:

    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.demo')
    >>> from lino.api.doctest import *
    >>> settings.SITE.verbose_client_info_message = True
    >>> from lino.api import rt, _
    >>> from atelier.utils import i2d
    >>> RecurrentEvent = cal.RecurrentEvent
    >>> Recurrencies = cal.Recurrencies


A series of weekends
====================


>>> obj = courses.Course.objects.get(name__contains="Weekends")
>>> print(obj)
Five Weekends 2015
>>> print(obj.start_date)
2015-06-19
>>> print(dd.today())
2015-05-22


>>> rt.show(cal.EntriesByController, obj, column_names="when_text overview state", nosummary=True)
=============================== =================== ===========
 When                            Description         State
------------------------------- ------------------- -----------
 Fri 06/11/2015-Sun 08/11/2015   *Activity #26  5*   Suggested
 Fri 02/10/2015-Sun 04/10/2015   *Activity #26  4*   Suggested
 Fri 28/08/2015-Sun 30/08/2015   *Activity #26  3*   Suggested
 Fri 24/07/2015-Sun 26/07/2015   *Activity #26  2*   Suggested
 Fri 19/06/2015-Sun 21/06/2015   *Activity #26  1*   Suggested
=============================== =================== ===========
<BLANKLINE>


