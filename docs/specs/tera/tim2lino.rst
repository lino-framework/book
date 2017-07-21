.. _tera.specs.tim2lino:

===============================
Migrating from TIM to Lino Tera
===============================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_tera_tim2lino
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db import models


This document describes (in German) the migration plan for a TIM user
who is changing their database to Lino.

Zahler, Krankenkassen und Lieferanten sind in Lino alle unter
"Organisationen".

Lino unterscheidet zwischen einfachen **Personen** und
**Klienten**. Ein Klient ist immer automatisch auch eine Person, aber
über einen Klienten weiß man mehr als über eine einfache Person. Einen
Klienten kann man auch als Person ansehen und dann sieht man nur Name,
Vorname, Adresse... aber nicht z.B. das Passfoto oder die
Nationalregisternummer.  Pro physischer Person gibt es einen einzigen
Eintrag in der Personentabelle. 

Eine **Personenakte** heißt in Lino "Begleitung" (oder lieber
"Therapie"?), eine **Gruppenakte** heißt in Lino "Aktivität".

Eine **Begleitung** ist, wenn ein bestimmter Therapeut sich um einen
bestimmten Klienten kümmert, um eine bestimmte Serie von *Problemen*
zu lösen.  Normalerweise gibt es *eine* aktive Begleitung pro Klient
zu einem bestimmten Zeitpunkt. Es kann aber durchaus vorkommen, dass
ein Klient zwei Therapien parallel macht, bei zwei verschiedenen
Therapeuten.  Pro Begleitung wird auch der Tarif und der Zahler
("Rechnungsempfänger") festgelegt.

Eine **Aktivität** ist, wenn eine Gruppe von Personen sich regelmäßig
trifft, um unter der Leitung eines Therapeuten über ein bestimmtes
Thema zu reden. Das sind sowohl Lebensgruppen als auch Therapeutische
Gruppen.

Pro Aktivität haben wir eine Liste der **Teilnehmer**. Das sind die
Personen, die eingeschrieben sind.

Ebenfalls pro Aktivität haben wir eine Liste der **Kalendereinträge**.
Diese werden je nach Art der Aktivität "Sitzungen" oder "Treffen" oder
noch anders genannt.

- Sollen wir Einzeltherapien vielleicht einfachheitshalber auch als
  eine Art von Aktivität mit nur einem Teilnehmer betrachten?  Dann
  könnten Begleitungen (Coachings) komplett wegfallen. Tarif und
  Zahlungsempfänger kämen dann pro Einschreibung.

- Soll pro Einschreibung auch die eventuelle Begleitung festgehalten
  werden? Wie soll Lino den Tarif wissen?

- Was machen wir mit einem Kind geschiedener Eltern, bei dem die
  Rechnung mal an den einen und mal an den anderen Elternteil geht?

- Erstgespräche sind Kalendereinträge ohne Aktivität, bei denen der
  Klient einfach nur anwesend ist.

Die **Anwesenheiten** werden in Lino *pro Klient* und nicht pro Person
festgehalten. Man muss Klient sein, um bei Terminen anwesend sein zu
können.

In Lino gibt es auch "Haushalte". WEnn man zuerst die
Haushaltsmitglieder eingibt und dann eine Therapie für diesen Haushalt
startet, dann trägt Lino die Haushaltsmitglieder automatisch als
Teilnehmer ein. Man kann die Teilnehmerliste dann aber trotzdem noch
verändern, ohne dass dadurch der Haushalt verändert wird.

In TIM hatten wir bis zu drei Therapeuten pro Akte (`IdUsr1`, `IdUsr2`
und `IdUsr3`).  Nummer 1 ist der, der das Erstgespräch gemacht
hat. Nummer 2 ist der aktuelle Verantwortliche.  Es gibt auch
Wiederaufnahmen (Klient war hier, hatte ein paar DL, kommt eine
Zeitlang nicht. Und dann wird eine neue Akte angelegt, mit neuem
Erstgespräch.  Dieses System in TIM ist recht komplex und suboptimal
und wird höchstwahrscheinlich revidiert werden. Wahrscheinlich sind
die Begleitungen genau das, was sie brauchen. Zu besprechen mit DD.
  
