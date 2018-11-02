.. doctest tera_de/basics/suchen.rst
   
=======================
Suchen in der Datenbank
=======================

.. init doctest

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *
    >>> translation.activate("de")

Das erste Feld in der Werkzeugleiste jeder Tabelle ist das Feld
**Schnellsuche**.  Dort kannst Du einen Teil des Names eintippen, und
Lino zeigt dann nur die Zeilen an, die Deinen Suchtext enthalten.

Anders als TIM sucht Lino **auch in der Mitte**.  Also du brauchst
nicht unbedingt den Anfang des Namens zu schreiben.

Wenn der **Suchtext aus mehreren Wörtern** besteht (d.h. Leerzeichen
enthält), dann zeigt Lino nur Einträge, bei denen *alle* diese Wörter
enthalten sind.

Anders als TIM sucht Lino **nicht nur im Namen**, sonden auch in
gewissen anderen Feldern.

**Zum Beispiel für Partner** (also Personen, Klienten, Organisationen)
sucht Lino im Namen, der Telefonnummer und der Handynummer:

>>> show_quick_search_fields(contacts.Partner)
Partner
- Name prefix (prefix)
- Name (name)
- Telefon (phone)
- GSM (gsm)

**Oder für Akten** sucht er in der Referenz und in der Bezeichnung der
Akte, und zusätzlich auch im Namen des Partners:

>>> show_quick_search_fields(courses.Course)
Akten
- Referenz (ref)
- Bezeichnung (name)
- Name (partner__name)


