.. _tera.coming: 

===============================
Der nächste Tera kommt bestimmt
===============================

Änderungen seit der Besprechung vom 2018-10-09.
Nächste Besichtigung geplant am 2018-11-06.

.. contents::
  :local:



Offene Entscheidungen
=====================

- Soll Luc für eine weitere Intensivwoche im Dezember nach Eupen
  kommen, und zwar in der KW49 (vom 3. bis 7. Dezember)?

- Wird die Bargeldkasse der Therapeuten abgeschafft?  Abrechnungen
  würden sich erübrigen.
  
- Wie steht es mit eurer Tarifordnung? Zählen die Anwesenheiten auch
  für Fakturierung? Stattdessen könnten wir Abonnements einführen
  (eine Rechnung pro Monat für alle Termine einer Therapie).
  

Zeitplan
========

- **November 2018** : letzte Arbeiten.  Ziel ist, dass die Therapeuten
  ihre alltägliche Arbeit in Lino erledigen können wie bisher in TIM:
  Akten, Termine und Notizen erfassen und verwalten.
  
- **Dezember 2018** : Daniel, Harry und Gregor beginnen die anderen
  Therapeuten zu schulen.  Alle Endbenutzer sollten das Erfassen und
  Verwalten ihrer Akten und Dienstleistungen im Lino üben.
 
- **1. Januar 2019** : Umstieg auf Produktionsbetrieb. Ab jetzt werden
  keine Daten mehr aus TIM importiert.

- **Januar 2019** : Das Sekretariat kann Verkaufsrechnungen
  generieren.

- Weiterentwicklungsprojekt **Kalenderplanung** : Lino könnte dann
  Terminvorschläge generieren und hilft bei der Erstellung des
  Wochenplans.  Wichtig insbesondere für die Termine im KITZ.  Es gäbe
  einen Stundenplan und Ausnahmeregelungen.  Dazu gehört auch
  eventuelle Integration mit Kopano und Hochladen von Dateien.  Die
  Kalenderfunktionen soll entweder in Lino so gut werden, dass Kopano
  nicht mehr nötig ist oder mit Kopano synchronisiert sein.
  

Tagesordnung 2018-11-06
=======================

**Lagebericht**

- Das, was wir am 2018-10-09 besprochen haben ist theoretisch gemacht.
  Ich habe nicht jedes Detail hier dokumentiert, weil wir noch in der
  iterativen Entwicklungsphase sind.  Siehe auch :doc:`/intro`,
  :doc:`/the/index` und :doc:`/sek/index`.

- Dienstleistungen (Termine und Anwesenheiten) werden regelmäßig aus
  TIM nach Lino importiert.  In Lino sind sie bisher nur zum Spielen.
  Alle Änderungen in Lino gehen beim jeweils nächsten Import verloren.

- Buchhaltung: Einkaufsrechnungen und Kontoauszüge könnten schon jetzt
  direkt in Lino erfasst werden, aber Vera ist noch nicht bei.
  Buchhaltung 2018 wird parallel auch beim Steuerberater erfasst. Die
  Daten in Lino sind da, um zu überprüfen.
  
  Verkaufsrechnungen werden noch mit TIM erstellt und ausgedruckt und
  dann aus TIM nach Lino importiert (tl3.py).
  
**Wichtige Fragen:**

- Werden die Notizen richtig importiert? Momentan kann man Notizen nur
  pro Akte anzeigen/erfassen.
  
- Beispiel Patient 2070105.  Lino zeigt immer alle Akten an, auch die
  stornierten und inaktiven.  Ist das okay?

- Beruf, Lebensweise und Zivilstand werden pro *Patient* (nicht pro
  Akte) importiert.
  Abteilung und Bereich pro Akte.
  Tarif pro Einschreibung.
  Stimmt das?

- Wir haben gesagt, dass bei Akten mit zwei Therapeuten der
  Cotherapeut mit den Patienten in der Liste der Teilnehmer kommt.
  Ich bin noch nicht sicher, ob euch das gefällt.  Jedenfalls muss das
  momentan nach dem Import nachgearbeitet werden: Akten mit zwei
  Therapeuten haben zur Zeit noch alle Termine doppelt nach dem
  Import, weil in TIM jeder Therapeut seine DLS eingibt. Dubletten
  kann ich wahrscheinlich automatisch rausklamüsern, aber bin noch
  nicht sicher, ob das schwer ist. Zu klären, ob sich die Arbeit
  überhaupt lohnt.

- Sind die PAR->IdUsrN aus TIM jetzt korrekt importiert?  

**Falls Zeit bleibt**

- Abrechnung an Krankenkassen
  
- Wir hatten ein Fallbeispiel "Kylie B hat ET in Lino, was nicht
  stimmt" gesehen. Das kam, weil in TIM für Kylie ein PAR mit IdPrt P
  steht, weil sie ja als Kind in einer Lebensgruppe mitmacht.  Woher
  soll Lino wissen, dass Kylie keine Einzeltherapie hat sondern nur
  als Kind einer anderen Therapie benutzt wird? Okay, normalerweise
  haben Personen, die in einer LG oder TG mitmachen, nicht auch noch
  eine Einzeltherapie... aber da gibt es bestimmt Ausnahmen.  Ich habe
  einen Nachlauf programmiert, der alle ET löscht, für die keine Notiz
  existiert und deren Patient auch in anderen Akten Teilnehmer ist.
  
- Momentan habt ihr nur eine Telefonnummer, GSM-Nr und E-Mail-Adresse
  pro Partner. In Lino könnte man auch mehrere "Kontaktdaten" pro
  Partner haben. Daniel und ich haben irgendwann im Juni mal
  "beschlossen", dass eine reicht. Nachteil von mehreren ist, dass die
  Bearbeitung dann anders funktioniert als aus TIM gewohnt. Man kann
  auch später von single-contact nach multi-contact wechseln, falls
  sich rausstellt, dass es Sinn macht.

- Could not import zahler 1025, 8, 15, 5, 22, 24

- Es gibt in TIM Akten mit ungültigem Tarif 0, 3, 33

- Gekoppelte Termine : für bestimmte Therapien gilt, dass wenn ein
  Patient mehrer Termine hintereinander am gleichen Tag hat, diese für
  die Rechnung als ein einziger betrachtet werden.  Dieses Konzept
  wird überflüssig, falls wir monatliche Abo-Fakturierung einführen.
  
- Klären, wie die Securex-Rechnungen verbucht werden sollen.

- "endet um" kann bis auf weiteres leer sein
  
- Tagesplaner

- Terminplanung : Wochen-Master (Stundenplan), Monatsplaner (Wo sind
  Lücken? Ausnahmen regeln), Wochenansicht mit diversen
  Filtermöglichkeiten, Terminblätter drucken zum
  Verteilen. Zugewiesene Termine werden nicht angezeigt im Dashboard.

- Themen sind pro Familie und pro Klient, Notizen nur pro Klient.

- MTI Navigator can be irritating. Possibility to hide certain links &
  conversions. e.g. Person -> Houshold, Person -> Partner should be
  hidden for normal users.

testing
=======

- Dienstleistungsarten haben ein Feld "ref", und im Tagesplaner wird
  diese angezeigt.
  
- Im Feld *Rolle* von Familienakten steht momentan die Nummer. Liegt
  am Datenimport.

- Feld *Verwalter* aller Akten ist leer. Hier muss der Therapeut rein
  importiert werden.

- Im Feld *Therapieart* steht die Auswahl nach einem Import auf EN und
  muss manuell nach DE übersetzt werden.
  
TODO
====

