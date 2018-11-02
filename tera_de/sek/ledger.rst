===========
Buchhaltung
===========

.. |insert|  image:: /images/buttons/insert.png
.. |own_window|  image:: /images/buttons/own_window.png
.. |search|  image:: /images/buttons/search.png
.. |refresh|  image:: /images/buttons/refresh.png



Einkaufsrechnungen
==================

Um eine neue EKR zu erfassen, wähle im Hauptmenü
:menuselection:`Buchhaltung --> Einkauf --> Einkaufsrechnungen` und
klicke dann auf |insert| um eine neue Rechnung einzufügen.

Der Partner einer EKR ist der Lieferant. Das ist üblicherweise eine
Firma oder Organisation, kann aber potentiell auch eine Einzelperson
oder ein Haushalt sein.

Das Buchungsdatum ist fast immer das gleiche wie das
Rechnungsdatum. Ausnahme: Wenn eine Rechnung n einem anderen
Kalenderjahr gebucht wird, dann muss als Buchungsdatum der 01.01. oder
31.12. des Buchungsjahres genommen werden.

In Total inkl. MWSt. gib den Gesamtbetrag der Rechnung ein. Lino wird
diesen Betrag ggf im folgenden Bildschirm verteilen.

Tipp : tippe :kbd:`Ctrl-S`, um dieses Dialogfenster ohne Maus zu
bestätigen.

Hier hat Lino den Gesamtbetrag so gut es ging aufgeteilt. Im Idealfall
kannst du hier auf "Registriert" klicken, um die Rechnung zu
registrieren. Und dann wieder auf um die nächste Rechnung einzugeben.

Alternativ kannst du Konto, Analysekonto, MWSt-Klasse und Beträge
manuell für diese eine Rechnung ändern.

Lino schaut beim Partner nach, welches Konto Einkauf dieser Partner
hat. Falls das Feld dort leer ist, nimmt Lino das Gemeinkonto
„Wareneinkäufe“. Das MWSt-Regime der Rechnung nimmt Lino ebenfalls vom
Partner. Beide Felder kannst du in den Partnerstammdaten nachschauen
gehen, indem du auf die Lupe (|search|) hinterm Feld „Partner“
klickst. Dort kannst du diese beiden Felder dann für alle zukünftigen
Rechnungen festlegen.

Analysekonten
=============

Analysekonten und Generalkonten sind zwei unterschiedliche
Klassierungen der Kosten. Der Buchhalter interessiert sich nur für die
G-Konten und weiß von den A-Konten nichts. Der VWR dagegen
interessiert sich eher für die A-Konten.

Über :menuselection:`Konfigurierung --> Buchhaltung --> Konten` kann
man den Kontenplan (d.h. die Liste aller Generalkonten) sehen und
ggf. verändern.

Pro Generalkonto kann man sagen :

- Braucht AK : wenn angekreuzt, dann muss für Buchungen auf dieses
  Konto auch ein A-Konto angegeben werden. Wenn nicht angekreuzt, dann
  darf für Buchungen auf dieses Konto kein A-Konto angegeben werden.
  
- Analysekonto : welches A-Konto Lino vorschlagen soll, wenn man
  dieses Generalkonto für eine Buchung auswählt.
  
NB das A-Konto des Generalkontos ist lediglich der Vorschlag
bzw. Standardwert. Man kann das A-Konto einer individuellen Buchung
manuell dennoch ändern.

Pro Generalkonto kannst du das Analysekonto angeben, das Lino
vorschlagen soll, wenn du eine neue Einkaufsrechnung (EKR)
eingibst. In der EKR kannst du dann immer noch ein anderes AK
auswählen. Du kannst das AK im Generalkonto auch leer lassen (selbst
wenn "Braucht AK" angekreuzt ist). Das bedeutet dann, dass Lino in der
EKR keinen Vorschlag machen soll. Dann ist man sozusagen gezwungen,
bei jeder Buchung zu überlegen, welches AK man auswählt.

.. rubric:: Tipps

Pro Partner kannst Du das Konto Einkauf festlegen. Dieses Konto trägt
Lino dann automatisch als Generalkonto in Einkaufsrechnungen von
diesem Partner ein.

Nach Ändern des Generalkontos in einer Rechnungszeile setzt Lino immer
das Analysekonto, selbst wenn dieses Feld schon ausgefüllt war.

Verkaufsrechnungen
==================

Abgesehen von den automatisch erstellten Rechnungen kannst Du
jederzeit auch manuell Verkaufsrechnungen (VKR) erstellen und
ausdrucken. Manuelle VKR stehen üblicherweise in einem eigenen
Journal, um sie nicht mit den automatisch erstellten VKR zu
vermischen.

Um eine neue VKR zu erfassen, wähle im Hauptmenü :menuselection:`
Buchhaltung --> Verkauf --> (gewünschtes Journal)` und klicke dann auf
|insert| um eine neue Rechnung einzufügen.

Anders als bei Einkaufsrechnungen gibst Du in VKR keinen Gesamtbetrag
ein und wählst einen „Tarif“ statt eines Generalkontos. Ansonsten ist
die Bedienung ähnlich.

Kontoauszüge
============

Für jedes Bankkonto gibt es in Lino ein entsprechendes Journal. Für
jeden Kontoauszug der Bank gibst du einen Kontoauszug in Lino
ein. Achte dabei auf Übereinstimmung der Nummern sowie der alten und
neuen Salden. Jeder Kontoauszug wiederum enthält eine oder mehrere
Zeilen, je eine pro Transaktion.

Um einen neuen Kontoauszug zu erfassen, wähle zunächst im Hauptmenü
:menuselection:`Buchhaltung --> Finanzjournale` und dort das
gewünschte Journal. Lino zeigt dann eine Tabelle mit den bereits
erfassten Kontoauszügen. Hier kannst du sehen, wo du beim letzten Mal
aufgehört hast.

Doppelklick auf einem bestehenden Auszug zeigt dessen
Vollbild-Ansicht.

Klicke auf |insert| in der Werkzeugleiste, um einen neuen Kontoauszug
einzufügen.

Als Buchungsdatum gib das Datum des Kontoauszugs ein. Der Alte Saldo
sollte der gleiche sein wie der Neue Saldo des vorigen Kontoauszugs.

Dieses Fenster kannst du auch per Tastatur mit :kbd:`Ctrl+S`
bestätigen.  Jetzt zeigt Lino den noch leeren Kontoauszug:

Hier musst du auf |own_window| klicken, um das untere Panel in einem
eigenen Fenster zu öffnen.

Das Feld Nr füllt Lino automatisch aus. (Du kannst auf einer
bestehenden Nummer :kbd:`F2` drücken und sie ändern, um die
Reihenfolge der Zeilen zu beeinflussen).

Das Feld Datum kann leer bleiben, dann trägt Lino das Datum des
Kontoauszugs ein.

Wenn es sich um die Zahlung einer Rechnung handelt, muss im Feld
Partner der Kunde oder Lieferant ausgewählt werden. Lino schaut dann
nach, ob offene Rechnungen vorliegen und tut folgendes.

Wenn es genau eine offene Rechnung gibt, füllt Lino in den Feldern
Match und Einnahme bzw. Ausgabe die Zahlungsreferenz und den Betrag
der Rechnung ein.

Wenn es mehrere offene Rechnungen gibt, trägt Lino im Feld Match den
Text „x Vorschläge“ ein. Das bedeutet, dass du auf das Wort
*Vorschläge* klicken solltest.  Siehe weiter unten.

Wenn es keine offene Rechnung gibt, musst du die Felder Match und
Einnahme bzw. Ausgabe selber ausfüllen.

Wenn Lino den Betrag ausgefüllt hast, kannst du diesen trotzdem noch
abändern. Zum Beispiel bei Teilzahlung oder Zahlungsdifferenz.

Das Feld Partner bleibt leer, wenn es sich um eine allgemeine Buchung
(Generalbuchung oder partnerlose Buchung) handelt, die nicht an einen
bestimmten Geschäftspartner bezogen ist und nicht beglichen werden
müssen. Zum Beispiel interne Transfers von einem Bankkonto zum
anderen, Abbuchung von Zahlungsaufträgen, Bankunkosten,
Kreditrückzahlungen, Mieten, Zuschüsse.

Im Feld Konto kommt das Generalkonto zu stehen. Dieses Feld muss immer
ausgefüllt sein. Wenn du einen Partner ausgewählt hast, dann steht
hier eines der Konten „Kunden“ oder „Lieferanten“.

Buchhaltungsberichte drucken
============================

Menü :menuselection:`Berichte --> Buchhaltung --> Buchhaltungsbericht`.

Tipp: nachdem Du **Periode vom** (und optional **bis**) eingegeben
hast, musst du auf den Blitz klicken, damit Lino die Daten berechnet
und anzeigt.

Tipp: wenn Du *Periode bis* leer lässt, wird nur *Periode vom*
berücksichtigt.
