.. _book.specs.cosi_ee:

Estonia
=======

The Estonian version of :ref:`cosi` imports every place in Estonia
from :mod:`commondata.ee`.

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.cosi_ee.settings.demo')
>>> from lino.api.doctest import *

>>> ses = rt.login("rando")
>>> dd.translation.activate('et')


The Estonian `Wikipedia
<https://et.wikipedia.org/wiki/Rapla_maakond>`_ says:

    Rapla maakonnas on 10 omavalitsusüksust (valda):

    Juuru vald - Järvakandi vald - Kaiu vald - Kehtna vald - Kohila vald - Käru vald - Märjamaa vald - Raikküla vald - Rapla vald - Vigala vald
    
Lino and :mod:`commondata.ee` agree with this:

>>> raplamaa = countries.Place.objects.get(
...    name="Rapla", type=countries.PlaceTypes.county)
>>> ses.show("countries.PlacesByPlace", raplamaa)
========================= =========== ==========
 Asum                      Asumiliik   zip code
------------------------- ----------- ----------
 `Juuru <Detail>`__        Vald
 `Järvakandi <Detail>`__   Vald
 `Kaiu <Detail>`__         Vald
 `Kehtna <Detail>`__       Vald
 `Kohila <Detail>`__       Vald
 `Käru <Detail>`__         Vald
 `Märjamaa <Detail>`__     Vald
 `Raikküla <Detail>`__     Vald
 `Rapla <Detail>`__        Linn
 `Vigala <Detail>`__       Vald
========================= =========== ==========
<BLANKLINE>

Another test is the 
`municipality of Juuru
<https://et.wikipedia.org/wiki/Juuru_vald>`_ for which Wikipedia 
announces one small borough and 14 villages:

    Juuru vallas on üks alevik (Juuru, elanikke 597) ja 14 küla: Atla (91), Helda, Hõreda (80), Härgla (84), Jaluse (40), Järlepa (235), Kalda, Lõiuse (103), Mahtra (99), Maidla (124), Orguse (43), Pirgu (102), Sadala ja Vankse (30).

Lino and :mod:`commondata.ee` again agree with this:

>>> juuru = countries.Place.objects.get(name="Juuru", 
...    type=countries.PlaceTypes.municipality)
>>> ses.show("countries.PlacesByPlace", juuru)
====================== =========== ==========
 Asum                   Asumiliik   zip code
---------------------- ----------- ----------
 `Atla <Detail>`__      Küla        79403
 `Helda <Detail>`__     Küla        79417
 `Härgla <Detail>`__    Küla        79404
 `Hõreda <Detail>`__    Küla        79010
 `Jaluse <Detail>`__    Küla        79410
 `Juuru <Detail>`__     Alevik
 `Järlepa <Detail>`__   Küla
 `Kalda <Detail>`__     Küla        79418
 `Lõiuse <Detail>`__    Küla        79405
 `Mahtra <Detail>`__    Küla        79407
 `Orguse <Detail>`__    Küla
 `Pirgu <Detail>`__     Küla
 `Sadala <Detail>`__    Küla        79419
 `Vankse <Detail>`__    Küla        79406
====================== =========== ==========
<BLANKLINE>


Formatting postal addresses
---------------------------


The country is being printed in the address, depends on the
:attr:`country_code <Plugin.country_code>` setting.

>>> rmu(dd.plugins.countries.country_code)
'EE'
>>> dd.plugins.countries.get_my_country()
Country #EE ('Estonia')



>>> eesti = countries.Country.objects.get(isocode="EE")
>>> sindi = countries.Place.objects.get(name="Sindi")
>>> p = contacts.Person(first_name="Malle", last_name="Mets", 
...     street=u"M\xe4nni tn", street_no="5", street_box="-6", 
...     zip_code="86705", country=eesti, city=sindi)
>>> print(p.address)
Malle Mets
Männi tn 5-6
86705 Sindi

Townships in Estonia get special handling: their name is replaced by
the town's name when a zip code is known:

>>> city = countries.Place.objects.get(name="Kesklinn")
>>> print(city)
Kesklinn
>>> city.type
<countries.PlaceTypes.township:55>
>>> p = contacts.Person(first_name="Kati", last_name="Kask", 
...     street="Tartu mnt", street_no="71", street_box="-5", 
...     zip_code="10115", country=eesti, city=city)
>>> print(p.address)
Kati Kask
Tartu mnt 71-5
10115 Tallinn

And yet another rule for countryside addresses:

>>> city = countries.Place.objects.get(name="Vana-Vigala")
>>> city.type
<countries.PlaceTypes.village:70>
>>> p = contacts.Person(first_name="Kati", last_name="Kask", 
...     street="Hirvepargi", street_no="123", 
...     zip_code="78003", country=eesti, city=city)
>>> print(p.address)
Kati Kask
Hirvepargi 123
Vana-Vigala küla
Vigala vald
78003 Rapla maakond
