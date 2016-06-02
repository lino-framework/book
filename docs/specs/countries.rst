.. _book.specs.countries:

======================
Countries
======================

This document describes the functionality implemented by the
:mod:`lino.modlib.countries` module.

TODO: Write explanations between the examples.

..  To test only this document:

    $ python setup.py test -s tests.SpecsTests.test_countries

    doctest initialization:

    >>> from lino import startup
    >>> startup('lino_book.projects.min2.settings.doctests')
    >>> from lino.api.doctest import *

.. contents::
   :local:
   :depth: 2


>>> rt.show(countries.Countries)
============================= ============================= ==========
 Designation                   Designation (et)              ISO code
----------------------------- ----------------------------- ----------
 Belgium                       Belgia                        BE
 Congo (Democratic Republic)   Congo (Democratic Republic)   CD
 Estonia                       Eesti                         EE
 France                        France                        FR
 Germany                       Saksamaa                      DE
 Maroc                         Maroc                         MA
 Netherlands                   Netherlands                   NL
 Russia                        Russia                        RU
============================= ============================= ==========
<BLANKLINE>

>>> rt.show(countries.Places)
============= ======================== ==================== ============== ========== ==================
 Country       Designation              Designation (et)     Place Type     zip code   Part of
------------- ------------------------ -------------------- -------------- ---------- ------------------
 Belgium       Aalst                    Aalst                City           9300       Flandre de l'Est
 Belgium       Aalst-bij-Sint-Truiden                        Village        3800       Limbourg
 Belgium       Angleur                                       City           4031
 Belgium       Ans                                           City           4430
 Belgium       Anvers                   Anvers               Province
 Belgium       Baardegem                                     Village        9310       Aalst
 Belgium       Baelen                   Baelen               City           4837       Liège
 Belgium       Blégny                                        City           4670
 Belgium       Brabant flamant          Brabant flamant      Province
 Belgium       Brabant wallon           Brabant wallon       Province
 Belgium       Brussels                 Brussels             City           1000
 Belgium       Burdinne                                      City           4210
 Belgium       Burg-Reuland                                  City           4790
 Belgium       Butgenbach               Butgenbach           City           4750       Liège
 Belgium       Büllingen                Büllingen            City           4760       Liège
 Belgium       Cerfontaine                                   City           5630
 Belgium       Cuesmes                                       City           7033
 Belgium       Erembodegem                                   Village        9320       Aalst
 Belgium       Eupen                                         City           4700
 Belgium       Flandre de l'Est         Flandre de l'Est     Province
 Belgium       Flandre de l'Ouest       Flandre de l'Ouest   Province
 Belgium       Gijzegem                                      Village        9308       Aalst
 Belgium       Hainaut                  Hainaut              Province
 Belgium       Herdersem                                     Village        9310       Aalst
 Belgium       Hofstade                                      Village        9308       Aalst
 Belgium       Kelmis                   Kelmis               City           4720
 Belgium       Kettenis                                      Village        4701
 Belgium       La Reid                                       City           4910
 Belgium       Limbourg                 Limbourg             Province
 Belgium       Liège                    Liège                Province
 Belgium       Liège                    Liège                City           4000       Liège
 Belgium       Luxembourg               Luxembourg           Province
 Belgium       Meldert                                       Village        9310       Aalst
 Belgium       Mons                     Mons                 City           7000
 Belgium       Moorsel                                       Village        9310       Aalst
 Belgium       Mortier                                       City           4670
 Belgium       Namur                    Namur                Province
 Belgium       Namur                    Namur                City           5000
 Belgium       Nieuwerkerken                                 Village        9320       Aalst
 Belgium       Nispert                                       Township                  Eupen
 Belgium       Ostende                  Ostende              City           8400
 Belgium       Ottignies                                     City           1340
 Belgium       Ouren                                         Township                  Burg-Reuland
 Belgium       Raeren                                        Village        4730
 Belgium       Recht                    Recht                City           4780       Liège
 Belgium       Sankt Vith               Sankt Vith           City           4780       Liège
 Belgium       Thieusies                                     City           7061
 Belgium       Trembleur                                     City           4670
 Germany       Aachen                   Aachen               City
 Germany       Berlin                                        City
 Germany       Cologne                  Köln                 City
 Germany       Hamburg                                       City
 Germany       Monschau                 Monschau             City
 Germany       Munich                   München              City
 Estonia       Harju                                         County
 Estonia       Kesklinn                                      Township                  Tallinn
 Estonia       Narva                                         Town
 Estonia       Pärnu                                         County
 Estonia       Pärnu                                         Town                      Pärnu
 Estonia       Põhja-Tallinn                                 Township                  Tallinn
 Estonia       Rapla                                         County
 Estonia       Rapla                                         Town                      Rapla
 Estonia       Tallinn                                       Town                      Harju
 Estonia       Tartu                                         Town
 Estonia       Vigala                                        Municipality              Rapla
 Estonia       Ääsmäe                                        Town                      Harju
 France        Marseille                                     City
 France        Metz                                          City
 France        Nancy                                         City
 France        Nice                     Nizza                City
 France        Paris                    Pariis               City
 France        Strasbourg                                    City
 Netherlands   Amsterdam                                     City
 Netherlands   Breda                                         City
 Netherlands   Den Haag                                      City
 Netherlands   Maastricht                                    City
 Netherlands   Rotterdam                                     City
 Netherlands   Utrecht                                       City
============= ======================== ==================== ============== ========== ==================
<BLANKLINE>

>>> rt.show(countries.PlaceTypes)
======= ============== ================
 value   name           text
------- -------------- ----------------
 10                     Member State
 11                     Division
 12                     Region
 13                     Community
 14                     Territory
 20      county         County
 21      province       Province
 22                     Shire
 23                     Subregion
 24                     Department
 25                     Arrondissement
 26                     Prefecture
 27      district       District
 28                     Sector
 50      city           City
 51      town           Town
 52      municipality   Municipality
 54      parish         Parish
 55      township       Township
 56      quarter        Quarter
 61      borough        Borough
 62      smallborough   Small borough
 70      village        Village
======= ============== ================
<BLANKLINE>



>>> # url = '/choices/countries/Places/type?country=BE&query=a'
>>> base = "/choices/countries/Places/type?country=BE"
>>> show_choices("robin", base + '&query=')
<br/>
Province
City
Village

>>> show_choices("robin", base + '&query=ll')
Village

>>> show_choices("robin", base + '&query=lll')


>>> countries.CountryDrivers.BE.city_types
[<PlaceTypes.city:50>, <PlaceTypes.village:70>]

>>> countries.CountryDrivers.BE.region_types
[<PlaceTypes.province:21>]


