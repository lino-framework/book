.. doctest docs/specs/search.rst
.. _specs.search:

=============================
Site-wide search
=============================

..  doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *

The demo project :mod:`lino_book.projects.lydia` is used for testing
the following document.

>>> rt.show('about.SiteSearch', quick_search="foo")
No data to display

>>> rt.show('about.SiteSearch', quick_search="est land")
============================== ===================================================================================================
 Description                    Matches
------------------------------ ---------------------------------------------------------------------------------------------------
 *Estonia* (Country)            name:**Est**onia, name_de:**Est****land**, name_fr:**Est**onie
 *Flandre de l'Est* (Place)     name:F**land**re de l'**Est**, name_de:Ostf**land**ern, name_fr:F**land**re de l'**Est**
 *Flandre de l'Ouest* (Place)   name:F**land**re de l'Ou**est**, name_de:W**est**f**land**ern, name_fr:F**land**re de l'Ou**est**
============================== ===================================================================================================
<BLANKLINE>

>>> rt.show('about.SiteSearch', quick_search="123")
===================================================== ========================
 Description                                           Matches
----------------------------------------------------- ------------------------
 *Arens Andreas* (Partner)                             phone:+32 87**123**456
 *Arens Annette* (Partner)                             phone:+32 87**123**457
 *Dobbelstein-Demeulenaere Dorothée* (Partner)         id:123
 *Mr Andreas Arens* (Person)                           phone:+32 87**123**456
 *Mrs Annette Arens* (Person)                          phone:+32 87**123**457
 *Mrs Dorothée Dobbelstein-Demeulenaere* (Person)      id:123
 *+32 87123456* (Contact detail)                       value:+32 87**123**456
 *+32 87123457* (Contact detail)                       value:+32 87**123**457
 *Diner (09.05.2015 13:30)* (Calendar entry)           id:123
 *SLS 9.2* (Movement)                                  id:123
 *DOBBELSTEIN-DEMEULENAERE Dorothée (123)* (Patient)   id:123
===================================================== ========================
<BLANKLINE>
