================================
Details zum Datenimport auis TIM
================================

Der **Tarif** einer Akte aus TIM kommt in Lino nach `Enrolment.fee`.

Der **Zahler** in TIM ist in Lino der *Rechnungsempfänger* der Akte.
Wenn das Feld *Zahler* in TIM leer war, dann steht in Lino der Patient
bzw. der Haushalt als *Rechnungsempfänger*.

Der Zahler einer Akte kommt in Lino auch in die *Fakturierungsadresse*
des Patienten (*Partner.invoice_decipient*).
