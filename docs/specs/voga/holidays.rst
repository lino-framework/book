.. _voga.specs.holidays:

=================
Defining holidays
=================

.. How to test just this document

   $ python setup.py test -s tests.DocsTests.test_holidays

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


Recurrent event rules
=====================

Here are the default holidays defined as recurrent event rules
:class:`RecurrentEvent <lino.modlib.cal.models.RecurrentEvent>` by
:mod:`lino.modlib.cal.fixtures.std`:

>>> rt.show(cal.RecurrentEvents)
... #doctest: -ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
============ ============ ============================ ===================== =================================== ==================== =====================
 Start date   End Date     Designation                  Designation (de)      Designation (fr)                    Recurrency           Calendar entry type
------------ ------------ ---------------------------- --------------------- ----------------------------------- -------------------- ---------------------
 01/01/2013                New Year's Day               Neujahr               Jour de l'an                        yearly               Holidays
 11/02/2013                Rosenmontag                  Rosenmontag           Lundi de carnaval                   Relative to Easter   Holidays
 13/02/2013                Ash Wednesday                Aschermittwoch        Mercredi des Cendres                Relative to Easter   Holidays
 29/03/2013                Good Friday                  Karfreitag            Vendredi Saint                      Relative to Easter   Holidays
 31/03/2013                Easter sunday                Ostersonntag          Pâques                              Relative to Easter   Holidays
 01/04/2013                Easter monday                Ostermontag           Lundi de Pâques                     Relative to Easter   Holidays
 01/05/2013                International Workers' Day   Tag der Arbeit        Premier Mai                         yearly               Holidays
 09/05/2013                Ascension of Jesus           Christi Himmelfahrt   Ascension                           Relative to Easter   Holidays
 20/05/2013                Pentecost                    Pfingsten             Pentecôte                           Relative to Easter   Holidays
 01/07/2013   31/08/2013   Summer holidays              Sommerferien          Vacances d'été                      yearly               Holidays
 21/07/2013                National Day                 Nationalfeiertag      Fête nationale                      yearly               Holidays
 15/08/2013                Assumption of Mary           Mariä Himmelfahrt     Assomption de Marie                 yearly               Holidays
 31/10/2013                All Souls' Day               Allerseelen           Commémoration des fidèles défunts   yearly               Holidays
 01/11/2013                All Saints' Day              Allerheiligen         Toussaint                           yearly               Holidays
 11/11/2013                Armistice with Germany       Waffenstillstand      Armistice                           yearly               Holidays
 25/12/2013                Christmas                    Weihnachten           Noël                                yearly               Holidays
============ ============ ============================ ===================== =================================== ==================== =====================
<BLANKLINE>
