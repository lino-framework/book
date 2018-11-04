.. _tera.coming: 

=====================
Lino Tera die Nächste
=====================

Offene Entscheidungen
=====================

- Soll Luc für eine weitere Intensivwoche im Dezember nach Eupen
  kommen, und zwar in der KW49 (vom 3. bis 7. Dezember)?

- Wird die Bargeldkasse der Therapeuten abgeschafft?  Abrechnungen
  würden sich erübrigen.
  
- Wie steht es mit eurer Tarifordnung? Zählen die Anwesenheiten auch
  für Fakturierung? Stattdessen könnten wir Abonnements einführen
  (eine Rechnung pro Monat für alle Termine einer Therapie).


TODO:

- Anwesenheiten pro Person und pro Akte: "tabular" view (wenn mehr als
  ein Jahr) wieder raus, denn die braucht zu viel Platz. Das Panel
  sollte auf einen halben Bildschirm passen,
  
- Anwesenheiten pro Person und pro Akte: Monate chronologisch
  rückwärts anzeigen statt vorwärts.

- Die Krankenkassen will ich doch nicht als ClientContact importieren,
  sondern pro Akte soll man die "Versicherungsart" auswählen.
  Insbesondere, weil wir ja später auch Rechnungen an die
  Krankenkassen schicken wollen.

  Neues Feld Course.health_insurance und neues Plugin health mit einem
  Modell "Insurance" (description, company, project, contrib_account).

- invoicing.OrderTypes: once, monthly, yearly, number gives additional
  information about how to understand what the InvoiceGenerator says.
  "once" is as it was now. "number" is similar to what we have in Voga
  for what they call "Abo-Kurse". Monthly means one invoice per month.
  
- Jeder Therapeut, der eine Bargeldkasse macht, ist ein POS (Point of
  sale). Neues Plugin `posale` mit einem voucher type "Transaction".
  A transaction is similar to a finan.BankStatement
