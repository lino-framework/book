.. _noi.specs.care_de:

====================================
Lino Care - Technische Spezifikation
====================================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_care_de
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.care_de.settings')
    >>> from lino.api.doctest import *

Dieses Dokument ist eine technische Beschreibung der Funktionalitäten
von Lino Care. Es ist auch Teil der Test-Suite.

Die englische Version dieses Dokuments (:doc:`/specs/noi/care`) ist
umfangreicher.

.. contents::
  :local:



Das Hauptmenü
=============

**Systemverwalter** haben ei nkomplettes Menü:

>>> rt.login('rolf').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Kontakte : Personen, Organisationen
- Stimmabgaben : My vote invitations, Meine Aufgaben, Meine Kandidaturen, Meine Interessen
- Büro : Meine Auszüge, Meine Kommentare, Meine Benachrichtigungen, Meine Uploads
- Anfragen : Meine Anfragen, Wo ich helfen kann, Aktive Tickets, Alle Tickets, Nicht zugewiesene Tickets, Reference Tickets, My Sites
- Konfigurierung :
  - System : Site-Parameter, Hilfetexte, Benutzer
  - Orte : Länder, Orte
  - Kontakte : Organisationsarten, Funktionen
  - Themen : Themen, Themengruppen
  - Büro : Auszugsarten, Kommentar-Arten, Upload-Arten
  - Anfragen : Missions, Projekte (Hierarchie), Project Types, Ticket types, Sites
  - Fähigkeiten : Fähigkeiten (Hierarchie), Fähigkeiten (Alle), Fähigkeitsarten
- Explorer :
  - System : Datenbankmodelle, Vollmachten, Benutzerarten, Änderungen, Benachrichtigungen, All dashboard widgets
  - Kontakte : Kontaktpersonen, Partner
  - Themen : Interessen
  - Stimmabgaben : Alle Stimmabgaben, Stimmabgabezustände
  - Büro : Auszüge, Kommentare, Uploads, Upload-Bereiche
  - Anfragen : Verknüpfungen, Ticketzustände, Wishes
  - Fähigkeiten : Fähigkeitsangebote, Anfragen
- Site : Info


**Einfache** Benutzer haben ein eingeschränktes Menü:

>>> rt.login('berta').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Stimmabgaben : My vote invitations, Meine Aufgaben, Meine Kandidaturen, Meine Interessen
- Büro : Meine Kommentare, Meine Benachrichtigungen, Meine Uploads
- Anfragen : Meine Anfragen, Wo ich helfen kann, My Sites
- Explorer :
  - Anfragen : Wishes
- Site : Info

Bewertungen
===========


>>> base = '/choices/votes/Votes/rating'
>>> show_choices("rolf", base + '?query=')
<br/>
Sehr gut
Gut
Ausreichend
Mangelhaft
Ungenügend
Nicht bewertbar


