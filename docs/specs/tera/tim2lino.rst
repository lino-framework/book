.. _tera.specs.tim2lino:

================================
Migration von TIM nach Lino Tera
================================

.. to run only this test:

    $ doctest docs/specs/tera/tim2lino.rst
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db import models


This document describes (in German) the migration plan for a TIM user
who is changing their database to Lino.

Zahler, Krankenkassen und Lieferanten sind in Lino alle unter
"Organisationen".

Patienten
=========

Pro physischer Person gibt es einen einzigen Eintrag in der
Personentabelle.  Lino unterscheidet zwischen **Personen** (im
Allgemeinen) und **Patienten**.  Ein Patient ist immer auch eine Person,
aber über einen Patienten weiß man mehr als über eine einfache Person.
Einen Patienten kann man auch als Person ansehen und dann sieht man nur
Name, Vorname, Adresse... aber nicht z.B. das Passfoto oder die
Nationalregisternummer.

Anders als in TIM gibt es für Patienten mit mehreren Akten nur einen
einzigen Eintrag in der Patientenliste.  Denn der Patient (die
physische Person) bleibt ja die gleiche.  Die verschiedenen Akten
dieses Patienten heißen jetzt **Aktivitäten** und sind im
gleichnamigen Reiter des Patienten aufgelistet.

Der **Tarif** (oder eher "Preisklasse"?) eines Patienten bestimmt, ob
dieser Patient Anrecht auf Sonderregelung bzgl. Teilnahmegebühren hat.

Eine **Teilnahmegebühr** ist das, was die Patienten (oder deren
Rechnungsempfänger) auf die Rechnung geschrieben bekommen. Sozusagen
das Produkt, das hier verkauft wird.

Der **Zahler** ("Rechnungsempfänger") eines Patienten ist ein
optionaler anderer Partner (d.h. Organisation, Haushalt oder Person),
an den die Rechnungen verschickt werden, die dieser Patient verursacht.
NB: Was machen wir mit einem Kind geschiedener Eltern, bei dem die
Rechnung mal an den einen und mal an den anderen Elternteil geht?

Der **Primärbegleiter** eines Patienten ist der Therapeut, der sich
momentan primär um diese Person kümmert.  Weitere "besondere
Begleiter" waren in TIM direkt ersichtlich.  Siehe `Regeln beim
Datenimport aus TIM`_.

.. Eine **Personenakte** heißt in Lino "Begleitung" (oder lieber
   "Therapie"?), eine **Gruppenakte** heißt in Lino "Aktivität".

Eine **Aktivität** ist, wenn ein Patient oder eine Gruppe von Patienten
sich regelmäßig trifft, um unter der Leitung eines Therapeuten über
ein bestimmtes Thema zu reden.  Es gibt drei Arten von Aktivitäten:
**Einzeltherapien**, **Lebensgruppen** und **Therapeutische Gruppen**
(diese Liste ist jedoch relativ leicht änderbar).

Pro Aktivität haben wir eine Liste der **Teilnehmer**. Das sind die
Patienten, die eingeschrieben sind.  Bei Einzeltherapien gibt es
normalerweise nur einen Teilnehmer.

Ebenfalls pro Aktivität haben wir eine Liste der **Kalendereinträge**.
Diese werden je nach Art der Aktivität "Sitzungen" oder "Treffen" oder
noch anders genannt.

TALK: **Erstgespräche** sind Kalendereinträge ohne Aktivität, bei
denen der Patient einfach nur anwesend ist.

Die **Anwesenheiten** werden in Lino pro Person festgehalten.  Man
muss als Person registriert sein, um bei Terminen anwesend sein zu
können.  Es können auch andere Personen an einem Termin teilnehmen,
z.B. Verwandte, Sozialarbeiter, Dolmetscher, ...

In Lino gibt es auch **Haushalte**. Ein Haushalt ist eine Gruppe von
*Personen*, die miteinder wohnen (oder gewohnt haben) und dabei eine
bestimmte *Rolle* haben (oder hatten).  Wenn man zuerst die
Haushaltsmitglieder eingibt und dann eine Therapie für diesen Haushalt
startet, dann trägt Lino automatisch die Haushaltsmitglieder als
Teilnehmer der Therapie ein.  Man kann die Teilnehmerliste dann aber
trotzdem noch verändern, ohne dass dadurch der Haushalt verändert
wird.

Man könnte in Lino auch **familiäre Beziehungen** erfassen (also wer
mit wem verwandt ist, unabhängig der Wohnsituation). Das scheint aber
zur Zeit unnötig.

Regeln beim Datenimport aus TIM
===============================

In TIM hatten wir bis zu drei Therapeuten pro Akte (`IdUsr1`, `IdUsr2`
und `IdUsr3`).  Nummer 1 ist der, der das Erstgespräch gemacht hat.
Nummer 2 ist der aktuelle Verantwortliche.  Es gibt auch
Wiederaufnahmen (Patient war hier, hatte ein paar DL, kommt eine
Zeitlang nicht.  Und dann wird eine neue Akte angelegt, mit neuem
Erstgespräch.  Dieses System in TIM ist recht komplex und suboptimal
und wird höchstwahrscheinlich revidiert werden. Zu besprechen mit DD.
  
Wenn `PAR->IdPar2` nicht leer ist (und einen anderen Wert als `IdPar`
enthält), dann gilt dieser Partner als obsolet.
