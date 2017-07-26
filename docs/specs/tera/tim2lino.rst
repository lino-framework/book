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

Klienten
========

Lino unterscheidet zwischen einfachen **Personen** und
**Klienten**. Ein Klient ist immer automatisch auch eine Person, aber
über einen Klienten weiß man mehr als über eine einfache Person. Einen
Klienten kann man auch als Person ansehen und dann sieht man nur Name,
Vorname, Adresse... aber nicht z.B. das Passfoto oder die
Nationalregisternummer.  Pro physischer Person gibt es einen einzigen
Eintrag in der Personentabelle.

Der **Tarif** (oder eher "Preisklasse"?) eines Klienten bestimmt, ob
dieser Klient Anrecht auf Sonderregelung bzgl. Teilnahmegebühren hat.

Eine **Teilnahmegebühr** ist das, was die Klienten (oder deren
Rechnungsempfänger) auf die Rechnung geschrieben bekommen. Sozusagen
das Produkt, das hier verkauft wird.

Der **Zahler** ("Rechnungsempfänger") eines Klienten ist ein
optionaler anderer Partner (d.h. Organisation, Haushalt oder Person),
an den die Rechnungen verschickt werden, die dieser Klient verursacht.

Der **Primärbegleiter** eines Klienten ist der Systembenutzer, der
sich primär um diese Person kümmert.

.. Eine **Personenakte** heißt in Lino "Begleitung" (oder lieber
   "Therapie"?), eine **Gruppenakte** heißt in Lino "Aktivität".

Eine **Aktivität** ist, wenn ein Klient oder eine Gruppe von Klienten
sich regelmäßig trifft, um unter der Leitung eines Therapeuten über
ein bestimmtes Thema zu reden.  Es gibt drei Arten von Aktivitäten:
**Einzeltherapien**, **Lebensgruppen** und **Therapeutische Gruppen**
(diese Liste ist jedoch relativ leicht änderbar).

Pro Aktivität haben wir eine Liste der **Teilnehmer**. Das sind die
Klienten, die eingeschrieben sind.

Ebenfalls pro Aktivität haben wir eine Liste der **Kalendereinträge**.
Diese werden je nach Art der Aktivität "Sitzungen" oder "Treffen" oder
noch anders genannt.

.. - Sollen wir Einzeltherapien vielleicht einfachheitshalber auch als
      eine Art von Aktivität mit nur einem Teilnehmer betrachten?  Dann
      könnten Begleitungen (Coachings) komplett wegfallen. Tarif und
      Zahlungsempfänger kämen dann pro Einschreibung.

    - Soll pro Einschreibung auch die eventuelle Begleitung festgehalten
      werden? Wie soll Lino den Tarif wissen?

- Was machen wir mit einem Kind geschiedener Eltern, bei dem die
  Rechnung mal an den einen und mal an den anderen Elternteil geht?

**Erstgespräche** sind Kalendereinträge ohne Aktivität, bei denen der
Klient einfach nur anwesend ist.


Die **Anwesenheiten** werden in Lino pro Person festgehalten. Man muss
als Person registriert sein, um bei Terminen anwesend sein zu
können. Es können auch andere Personen

In Lino gibt es auch **Haushalte**. Ein Haushalt ist eine Gruppe von
*Personen*, die miteinder wohnen (oder gewohnt haben) und dabei eine
bestimmte *Rolle* haben (oder hatten). Wenn man zuerst die
Haushaltsmitglieder eingibt und dann eine Therapie für diesen Haushalt
startet, dann trägt Lino automatisch die Haushaltsmitglieder als
Teilnehmer der Therapie ein. Man kann die Teilnehmerliste dann aber
trotzdem noch verändern, ohne dass dadurch der Haushalt verändert
wird.

Man könnte in Lino auch **familiäre Beziehungen** erfassen (also wer
mit wem verwandt ist, unabhängig der Wohnsituation). Das scheint aber
zur Zeit unnötig.

Regeln beim Datenimport aus TIM
===============================

In TIM hatten wir bis zu drei Therapeuten pro Akte (`IdUsr1`, `IdUsr2`
und `IdUsr3`).  Nummer 1 ist der, der das Erstgespräch gemacht
hat. Nummer 2 ist der aktuelle Verantwortliche.  Es gibt auch
Wiederaufnahmen (Klient war hier, hatte ein paar DL, kommt eine
Zeitlang nicht. Und dann wird eine neue Akte angelegt, mit neuem
Erstgespräch.  Dieses System in TIM ist recht komplex und suboptimal
und wird höchstwahrscheinlich revidiert werden. Zu besprechen mit DD.
  
Wenn `PAR->IdPar2` nicht leer ist (und einen anderen Wert als `IdPar`
enthält), dann gilt dieser Partner als obsolet.
