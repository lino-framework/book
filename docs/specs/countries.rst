.. doctest docs/specs/countries.rst
.. _book.specs.countries:

====================================
``countries`` : Countries and cities
====================================

.. currentmodule:: lino_xl.lib.countries

The :mod:`lino_xl.lib.countries` plugin defines models and choicelists for
managing names of geographical places.

.. contents::
   :local:
   :depth: 2
           
.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.doctests')
>>> from lino.api.doctest import *

See also :mod:`lino_xl.lib.statbel.countries`.


Overview
========

A **country** (aka *nation*) is a geographic region with a national government.
A **place** is any other type of named geographic region.


Countries
=========

.. class:: Country
           
    Django model to represent a *country*.



    .. attribute:: name

        The designation of this country.

        This is a babel field.

    .. attribute:: isocode

        The two-letter code for this country as defined by ISO 3166-1.
        For countries that no longer exist it may be a 4-letter code.

    .. attribute:: short_code

        A short abbreviation for regional usage. Obsolete.

    .. attribute:: iso3

        The three-letter code for this country as defined by ISO 3166-1.

    .. method:: allowed_city_types()

        Return the place types that are used in this country.

        Return all place types for countries without a country driver (see
        :class:`CountryDrivers`).


.. class:: Countries

    The table of all countries.

Places
======
           
.. class:: Place

    Django model to represent a *place*.

    Inherits from :class:`lino.mixins.sequenced.Hierarchical`.


    .. attribute:: parent

        The superordinate geographic place of which this place is a part.

    .. attribute:: country

        The country this place is in.

    .. attribute:: zip_code

    .. attribute:: type

        The type of this place (whether it's a city. a village, a province...)

        This contains one of the items in :class:`PlaceTypes`.
        The list of choices may be limited depending on the country.


    .. attribute:: show_type

    .. method:: get_choices_text

        Extends the default behaviour (which would simply diplay this
        city in the current language) by also adding the name in other
        languages and the type between parentheses.

.. class:: Places

    The table of known geographical places.
    A geographical place can be a city, a town, a suburb,
    a province, a lake... any named geographic entity,
    except for countries because these have their own table.

Place types
===========

.. class:: PlaceTypes

    A choicelist of possible place types.

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

    Sources used:

    - http://en.wikipedia.org/wiki/List_of_subnational_entities

           
           
Model mixins
============

.. class:: CountryCity
           
    Model mixin that adds two fields `country` and `city` and defines
    a context-sensitive chooser for `city`, a `create_city_choice`
    method, ...

    .. attribute:: country
                   
    .. attribute:: zip_code
    
    .. attribute:: city
    
        The locality, i.e. usually a village, city or town. 

        The choicelist for this field shows only places returned by
        :meth:`lino_xl.lib.countries.Place.get_cities`.

        This is a pointer to :class:`Place`.
        The internal name `city` is for historical reasons.

.. class:: CountryRegionCity

    Adds a `region` field to a :class:`CountryCity`.

.. _tutorials.addrloc:

The AddressLocation mixin
=========================

.. class:: AddressLocation

    A mixin for models which contain a postal address location.

    .. attribute:: addr1
                   
       Address line before street
       
    .. attribute:: street_prefix

       Text to print before name of street, but to ignore for sorting.
       
    .. attribute:: street

       Name of street, without house number.
                   
    .. attribute:: street_no

       House number.
       
    .. attribute:: street_box

        Text to print after street number on the same line.
                   
    .. attribute:: addr2

        Address line to print below street line.
    
    .. attribute:: addess_column

        Virtual field which returns the location as a comma-separated
        one-line string.

    .. method:: address_location(self, linesep="\n")
        
        Return the plain text postal address location part.  Lines are
        separated by `linesep` which defaults to ``"\\n"``.

        The country is displayed only for foreigners (i.e. whose
        country is not :attr:`my_country
        <lino_xl.lib.countries.Plugin.my_country>`)

        For example:

        >>> be = countries.Country.objects.get(isocode="BE")
        >>> ee = countries.Country.objects.get(isocode="EE")
        >>> tpl = u"{name}\n{addr}"

        >>> obj = contacts.Company.objects.filter(country=be)[0]
        >>> print(tpl.format(name=obj.name, addr=obj.address_location()))
        Bäckerei Ausdemwald
        Vervierser Straße 45
        4700 Eupen

        >>> obj = contacts.Company.objects.filter(country=ee)[0]
        >>> print(tpl.format(name=obj.name, addr=obj.address_location()))
        Rumma & Ko OÜ
        Uus tn 1
        Vigala vald
        78003 Rapla maakond
        Estonia

    
Utilities
=========

.. class:: CountryDriver
.. class:: CountryDrivers           

>>> rt.show(countries.Countries)
============================= ================== ================================= ==========
 Designation                   Designation (et)   Designation (fr)                  ISO code
----------------------------- ------------------ --------------------------------- ----------
 Belgium                       Belgia             Belgique                          BE
 Congo (Democratic Republic)   Kongo vabariik     Congo (République democratique)   CD
 Estonia                       Eesti              Estonie                           EE
 France                        Prantsusmaa        France                            FR
 Germany                       Saksamaa           Allemagne                         DE
 Maroc                         Marokko            Maroc                             MA
 Netherlands                   Madalmaad          Pays-Bas                          NL
 Russia                        Venemaa            Russie                            RU
============================= ================== ================================= ==========
<BLANKLINE>

>>> rt.show(countries.Places)
============= ======================== ==================== ==================== ============== ========== ====================
 Country       Designation              Designation (et)     Designation (fr)     Place Type     zip code   Part of
------------- ------------------------ -------------------- -------------------- -------------- ---------- --------------------
 Belgium       Aalst                    Aalst                Alost                City           9300       Flandre de l'Est
 Belgium       Aalst-bij-Sint-Truiden                                             Village        3800       Limbourg
 Belgium       Angleur                                                            City           4031
 Belgium       Ans                                                                City           4430
 Belgium       Anvers                   Anvers               Anvers               Province
 Belgium       Baardegem                                                          Village        9310       9300 Aalst / Alost
 Belgium       Baelen                   Baelen               Baelen               City           4837       Liège
 Belgium       Blégny                                                             City           4670
 Belgium       Brabant flamant          Brabant flamant      Brabant flamant      Province
 Belgium       Brabant wallon           Brabant wallon       Brabant wallon       Province
 Belgium       Brussels                 Brussels             Bruxelles            City           1000
 Belgium       Burdinne                                                           City           4210
 Belgium       Burg-Reuland                                                       City           4790
 Belgium       Butgenbach               Butgenbach           Butgenbach           City           4750       Liège
 Belgium       Büllingen                Büllingen            Bullange             City           4760       Liège
 Belgium       Cerfontaine                                                        City           5630
 Belgium       Cuesmes                                                            City           7033
 Belgium       Erembodegem                                                        Village        9320       9300 Aalst / Alost
 Belgium       Eupen                                                              City           4700
 Belgium       Flandre de l'Est         Flandre de l'Est     Flandre de l'Est     Province
 Belgium       Flandre de l'Ouest       Flandre de l'Ouest   Flandre de l'Ouest   Province
 Belgium       Gijzegem                                                           Village        9308       9300 Aalst / Alost
 Belgium       Hainaut                  Hainaut              Hainaut              Province
 Belgium       Herdersem                                                          Village        9310       9300 Aalst / Alost
 Belgium       Hofstade                                                           Village        9308       9300 Aalst / Alost
 Belgium       Kelmis                   Kelmis               La Calamine          City           4720
 Belgium       Kettenis                                                           Village        4701
 Belgium       La Reid                                                            City           4910
 Belgium       Limbourg                 Limbourg             Limbourg             Province
 Belgium       Liège                    Liège                Liège                Province
 Belgium       Liège                    Liège                Liège                City           4000       Liège
 Belgium       Luxembourg               Luxembourg           Luxembourg           Province
 Belgium       Meldert                                                            Village        9310       9300 Aalst / Alost
 Belgium       Mons                     Mons                 Mons                 City           7000
 Belgium       Moorsel                                                            Village        9310       9300 Aalst / Alost
 Belgium       Mortier                                                            City           4670
 Belgium       Namur                    Namur                Namur                Province
 Belgium       Namur                    Namur                Namur                City           5000
 Belgium       Nieuwerkerken                                                      Village        9320       9300 Aalst / Alost
 Belgium       Nispert                                                            Township                  4700 Eupen
 Belgium       Ostende                  Ostende              Ostende              City           8400
 Belgium       Ottignies                                                          City           1340
 Belgium       Ouren                                                              Township                  4790 Burg-Reuland
 Belgium       Raeren                                                             Village        4730
 Belgium       Recht                    Recht                Recht                City           4780       Liège
 Belgium       Sankt Vith               Sankt Vith           Saint-Vith           City           4780       Liège
 Belgium       Thieusies                                                          City           7061
 Belgium       Trembleur                                                          City           4670
 Germany       Aachen                   Aachen               Aix-la-Chapelle      City
 Germany       Berlin                                                             City
 Germany       Cologne                  Köln                 Cologne              City
 Germany       Hamburg                                                            City
 Germany       Monschau                 Monschau             Montjoie             City
 Germany       Munich                   München              Munich               City
 Estonia       Harju                                                              County
 Estonia       Kesklinn                                                           Township                  Tallinn
 Estonia       Narva                                                              Town
 Estonia       Pärnu                                                              County
 Estonia       Pärnu                                                              Town                      Pärnu
 Estonia       Põhja-Tallinn                                                      Township                  Tallinn
 Estonia       Rapla                                                              County
 Estonia       Rapla                                                              Town                      Rapla
 Estonia       Tallinn                                                            Town                      Harju
 Estonia       Tartu                                                              Town
 Estonia       Vigala                                                             Municipality              Rapla
 Estonia       Ääsmäe                                                             Town                      Harju
 France        Marseille                                                          City
 France        Metz                                                               City
 France        Nancy                                                              City
 France        Nice                     Nizza                Nice                 City
 France        Paris                    Pariis               Paris                City
 France        Strasbourg                                                         City
 Netherlands   Amsterdam                                                          City
 Netherlands   Breda                                                              City
 Netherlands   Den Haag                                                           City
 Netherlands   Maastricht                                                         City
 Netherlands   Rotterdam                                                          City
 Netherlands   Utrecht                                                            City
============= ======================== ==================== ==================== ============== ========== ====================
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



>>> base = "/choices/countries/Places/type?country=BE"
>>> show_choices("robin", base + '&query=')
<br/>
Province
City
Municipality
Village

>>> show_choices("robin", base + '&query=ll')
Village

>>> show_choices("robin", base + '&query=lll')


>>> countries.CountryDrivers.BE.city_types
[<PlaceTypes.city:50>, <PlaceTypes.municipality:52>, <PlaceTypes.village:70>]

>>> countries.CountryDrivers.BE.region_types
[<PlaceTypes.province:21>]

Reproducing #2079
=================

The following verifies bug :ticket:`2079` introduced `20170821
<https://github.com/lino-framework/lino/commit/37b2d0e9ee9117ddc81edf6df2c1ad5d394c9e2f>`__
and fixed 20170924 : when specifying a limit (which is always done by
a Combobox), Lino reported not the full count but only the number of
rows after applying limit (5 instead of 36 in below example):

>>> base = "/choices/contacts/Partners/city?country=BE&limit=5"
>>> show_choices("robin", base + '&query=', show_count=True)
<br/>
9300 Aalst / Alost
3800 Aalst-bij-Sint-Truiden
4031 Angleur
4430 Ans
9310 Baardegem
36 rows

Data checkers
=============

.. class:: PlaceChecker

    The name of a geographical place should not consist of only digits.

