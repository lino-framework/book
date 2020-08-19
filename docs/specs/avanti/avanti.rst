.. doctest docs/specs/avanti/avanti.rst
.. _avanti.specs.avanti:

=================================
Clients in Lino Avanti
=================================

.. currentmodule:: lino_avanti.lib.avanti

This document describes the :mod:`lino_avanti.lib.avanti` plugin.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.avanti1.settings.doctests')
>>> from lino.api.doctest import *


Overview
========

A **client** is a person using our services.


The legacy file number
======================

Dossiernummern:

- wenn du "ip6" eintippst, macht er daraus "IP 6901" (wenn "IP 6900" die letzte Dossiernummer ist, die mit "IP 6" beginnt.
- du kannst jederzeit auch im Schnellsuche-Feld "ip 6900" eintippen
- wenn du "ip 1234" einzippst (also die Dossiernummer selber eine vierstellige Zahl angibst), dann lässt Lino diese Nummer stehen.
- ob du "ip" oder "IP" eintippst, ist egal, Lino macht daraus immer "IP".
- Auch das Leerzeichen kannst du beim Eintippen sparen, das setzt Lino automatisch rein.
- wenn die Dossiernummer nicht mit "ip" beginnt, lässt Lino sie unverändert


>>> other_client = avanti.Client.objects.get(pk=116)
>>> def update_other(ref):
...     other_client.ref = ref
...     other_client.full_clean()
...     other_client.save()

>>> update_other(None) # tidy up from previous test run

>>> def test(ref):
...     obj = avanti.Client(ref=ref, name="x")
...     obj.full_clean()
...     print(obj.ref)

>>> test("ip 1")
IP 1001

>>> update_other("IP 4010")

>>> test("ip 4")
IP 4011

>>> test("ip")
IP 4011

>>> update_other(None) # tidy up for the following tests


Clients
=======

.. class:: Client(lino.core.model.Model)

    .. attribute:: translator_type

        Which type of translator is needed with this client.

        See also :class:`TranslatorTypes`

    .. attribute:: professional_state

        The professional situation of this client.

        See also :class:`ProfessionalStates`

    .. attribute:: overview

        A panel with general information about this client.

    .. attribute:: client_state

        The state of this client record.

        This is a pointer to :class:`ClientStates` and can have the following
        values:

        >>> rt.show('clients.ClientStates')
        ======= ========== ============ =============
         value   name       text         Button text
        ------- ---------- ------------ -------------
         05      incoming   Incoming
         07      informed   Informed
         10      newcomer   Newcomer
         15      equal      Equal
         20      coached    Registered
         25      inactive   Inactive
         30      former     Ended
         40      refused    Abandoned
        ======= ========== ============ =============
        <BLANKLINE>


    .. attribute:: unemployed_since

       The date when this client got unemployed and stopped to have a
       regular work.

    .. attribute:: seeking_since

       The date when this client registered as unemployed and started
       to look for a new job.

    .. attribute:: work_permit_suspended_until

    .. attribute:: city

       The place (village or municipality) where this client lives.

       See :attr:`lino_xl.lib.contacts.Partner.city`.

    .. attribute:: municipality

       The *municipality* where this client lives. This is basically
       equal to :attr:`city`, except when :attr:`city` is a *village*
       and has a parent which is a *municipality* (which causes that
       place to be returned).


.. class:: ClientDetail

.. class:: Clients

    Base class for most lists of clients.

    .. attribute:: client_state

        If not empty, show only Clients whose `client_state` equals
        the specified value.


.. class:: AllClients(Clients)

   This table is visible for Explorer who can also export it.

   This table shows only a very limited set of fields because e.g. an auditor
   may not see all data for privacy reasons. For example the names are hidden.
   OTOH it includes the :attr:`municipality
   <lino_avanti.lib.avanti.Client.municipality>` virtual field.


>>> show_columns(avanti.AllClients, all=True)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
+-------------------+------------------------+-------------------------------------------------------------+
| Internal name     | Verbose name           | Help text                                                   |
+===================+========================+=============================================================+
| client_state      | State                  | The state of this client record.                            |
+-------------------+------------------------+-------------------------------------------------------------+
| starting_reason   | Starting reason        |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| ending_reason     | Ending reason          |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| city              | Locality               | The locality, i.e. usually a village, city or town.         |
+-------------------+------------------------+-------------------------------------------------------------+
| municipality      | Municipality           | The municipality where this client lives. This is basically |
|                   |                        | equal to city, except when city is a village                |
|                   |                        | and has a parent which is a municipality (which causes that |
|                   |                        | place to be returned).                                      |
+-------------------+------------------------+-------------------------------------------------------------+
| country           | Country                |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| zip_code          | Zip code               |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| nationality       | Nationality            | The nationality. This is a pointer to                       |
|                   |                        | countries.Country which should                              |
|                   |                        | contain also entries for refugee statuses.                  |
+-------------------+------------------------+-------------------------------------------------------------+
| gender            | Gender                 | The sex of this person (male or female).                    |
+-------------------+------------------------+-------------------------------------------------------------+
| birth_country     | Birth country          |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| in_belgium_since  | Lives in Belgium since | Uncomplete dates are allowed, e.g.                          |
|                   |                        | "00.00.1980" means "some day in 1980",                      |
|                   |                        | "00.07.1980" means "in July 1980"                           |
|                   |                        | or "23.07.0000" means "on a 23th of July".                  |
+-------------------+------------------------+-------------------------------------------------------------+
| needs_work_permit | Needs work permit      |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| translator_type   | Translator type        | Which type of translator is needed with this client.        |
+-------------------+------------------------+-------------------------------------------------------------+
| mother_tongues    | Mother tongues         |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| cef_level_de      | None                   |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| cef_level_fr      | None                   |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| cef_level_en      | None                   |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+
| user              | Primary coach          | The author of this object.                                  |
|                   |                        | A pointer to lino.modlib.users.models.User.                 |
+-------------------+------------------------+-------------------------------------------------------------+
| event_policy      | Recurrency policy      |                                                             |
+-------------------+------------------------+-------------------------------------------------------------+


.. class:: MyClients(Clients)

    Shows all clients having me as primary coach. Shows all client states.

    >>> rt.login('robin').show('avanti.MyClients')
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    =============================== ============ =============== ===== ================================= ========== ================ ======= ===== ====================
     Name                            State        National ID     GSM   Address                           Age        e-mail address   Phone   ID    Legacy file number
    ------------------------------- ------------ --------------- ----- --------------------------------- ---------- ---------------- ------- ----- --------------------
     ABDALLAH Aáish (127)            Registered   920417 001-91         Bellmerin, 4700 Eupen             24 years                            127
     ABDO Aásim (138)                Registered   831201 001-50         Gülcherstraße, 4700 Eupen         33 years                            138
     ABDULLAH Afááf (155)            Ended        760102 002-86         4730 Raeren                       41 years                            155
     ABOUD Ahláám (166)              Ended        690627 002-97         4730 Raeren                       47 years                            166
     ARENT Afánásiiá (124)           Ended        891219 002-23         Bergkapellstraße, 4700 Eupen      27 years                            124
     ASTAFUROV Agáfiiá (175)         Registered   820120 002-60         Aachen, Germany                   35 years                            175
     BARTOSZEWICZ Agáfokliiá (146)   Ended        781018 002-02         Herbesthaler Straße, 4700 Eupen   38 years                            146
     BERENDT Antoshá (165)           Ended        700602 001-93         4730 Raeren                       46 years                            165
     CONTEE Chike (131)              Registered   870822 001-58         Edelstraße, 4700 Eupen            29 years                            131
     DIOP Ashánti (142)              Registered   810214 002-32         Habsburgerweg, 4700 Eupen         36 years                            142
     JALLOH Diállo (158)             Registered   740810 001-48         4730 Raeren                       42 years                            158
    =============================== ============ =============== ===== ================================= ========== ================ ======= ===== ====================
    <BLANKLINE>


.. class:: ClientsByNationality(Clients)


.. class:: Residence(lino.core.model.Model)


.. class:: EndingReason(lino.core.model.Model)

>>> rt.show('avanti.EndingReasons')
==== ======================== ========================== ========================
 ID   Designation              Designation (de)           Designation (fr)
---- ------------------------ -------------------------- ------------------------
 1    Successfully ended       Erfolgreich beendet        Successfully ended
 2    Health problems          Gesundheitsprobleme        Health problems
 3    Familiar reasons         Familiäre Gründe           Familiar reasons
 4    Missing motivation       Fehlende Motivation        Missing motivation
 5    Return to home country   Rückkehr ins Geburtsland   Return to home country
 9    Other                    Sonstige                   Autre
==== ======================== ========================== ========================
<BLANKLINE>

.. class:: Category(BabelDesignated)

>>> rt.show('avanti.Categories')
==== =============================== =============================== ===============================
 ID   Designation                     Designation (de)                Designation (fr)
---- ------------------------------- ------------------------------- -------------------------------
 1    Language course                 Sprachkurs                      Language course
 2    Integration course              Integrationskurs                Integration course
 3    Language & integration course   Language & integration course   Language & integration course
 4    External course                 External course                 External course
 5    Justified interruption          Begründete Unterbrechung        Justified interruption
 6    Successfully terminated         Erfolgreich beendet             Successfully terminated
==== =============================== =============================== ===============================
<BLANKLINE>


.. class:: TranslatorTypes

    List of choices for the :attr:`Client.translator_type` field of a
    client.

    >>> rt.show(rt.models.avanti.TranslatorTypes, language="de")
    ====== ====== ==========
     Wert   name   Text
    ------ ------ ----------
     10            SETIS
     20            Sonstige
     30            Privat
    ====== ====== ==========
    <BLANKLINE>


.. class:: ProfessionalStates

    List of choices for the :attr:`Client.professional_state` field of
    a client.

    >>> rt.show(rt.models.avanti.ProfessionalStates, language="de")
    ... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
    ====== ====== ================================
     Wert   name   Text
    ------ ------ --------------------------------
     100           Student
     200           Arbeitslos
     300           Eingeschrieben beim Arbeitsamt
     400           Angestellt
     500           Selbstständig
     600           Pensioniert
     700           Arbeitsunfähig
    ====== ====== ================================
    <BLANKLINE>



>>> rt.show(checkdata.Checkers, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
================================= ========================================
 value                             text
--------------------------------- ----------------------------------------
 beid.SSINChecker                  Check for invalid SSINs
 cal.ConflictingEventsChecker      Check for conflicting calendar entries
 cal.EventGuestChecker             Entries without participants
 cal.LongEntryChecker              Too long-lasting calendar entries
 cal.ObsoleteEventTypeChecker      Obsolete generated calendar entries
 countries.PlaceChecker            Check data of geographical places.
 dupable.DupableChecker            Check for missing phonetic words
 dupable.SimilarObjectsChecker     Check for similar objects
 memo.PreviewableChecker           Check for previewables needing update
 printing.CachedPrintableChecker   Check for missing target files
 system.BleachChecker              Find unbleached html content
================================= ========================================
<BLANKLINE>


Career
======

Language knowledges
===================

Avanti adds an entry date to the language knowledge table of a client.
There can be multiple entries per language and client.
Because we want to report whether knowledge changed after attending a course.

Some example cases:

>>> client = rt.models.avanti.Client.objects.get(pk=120)
>>> rt.show('cv.LanguageKnowledgesByPerson', client, nosummary=True)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
========== =============== ============ ============ =========== ============= ============
 Language   Mother tongue   Spoken       Written      CEF level   Certificate   Entry date
---------- --------------- ------------ ------------ ----------- ------------- ------------
 Dutch      No              a bit        moderate     A2+         No            05/02/2017
 Dutch      No              moderate     quite well   A2          No            12/01/2016
 German     No              quite well   very well    A1+         No            12/01/2016
 French     Yes                                                   No            12/01/2016
========== =============== ============ ============ =========== ============= ============
<BLANKLINE>


>>> client = rt.models.avanti.Client.objects.get(pk=121)
>>> rt.show('cv.LanguageKnowledgesByPerson', client, nosummary=True)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
========== =============== ======== ========= =========== ============= ============
 Language   Mother tongue   Spoken   Written   CEF level   Certificate   Entry date
---------- --------------- -------- --------- ----------- ------------- ------------
 Estonian   Yes                                            No            12/01/2016
========== =============== ======== ========= =========== ============= ============
<BLANKLINE>


>>> client = rt.models.avanti.Client.objects.get(pk=122)
>>> rt.show('cv.LanguageKnowledgesByPerson', client, nosummary=True, language="de")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
============= =============== ============== ============== =============== ============ =================
 Sprache       Muttersprache   Wort           Schrift        CEF-Kategorie   Zertifikat   Erfassungsdatum
------------- --------------- -------------- -------------- --------------- ------------ -----------------
 Deutsch       Nein            gar nicht      ein bisschen   A1              Nein         05.02.17
 Deutsch       Nein            ein bisschen   mittelmäßig    A0              Nein         12.01.16
 Französisch   Ja                                                            Nein         12.01.16
============= =============== ============== ============== =============== ============ =================
<BLANKLINE>

The end user usually sees the summary of language knowledges , which shows the
CEF level of the languages defined in :attr:`lino.core.site.Site.languages`,
and only the most recent CEF level.  For above client the CEF level for German
is A1 (not A0):

>>> rt.show('cv.LanguageKnowledgesByPerson', client, language="de")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
en: Ohne Angabe
de: A1
fr: Ohne Angabe
Muttersprachen: Französisch



Creating a new client
=====================


>>> ses = rt.login("romain")
>>> url = '/api/avanti/MyClients/-99999?an=insert&fmt=json'
>>> test_client.force_login(ses.user)
>>> res = test_client.get(url)
>>> res.status_code
200
>>> d = AttrDict(json.loads(res.content))
>>> sorted(d.keys())
... #doctest: +NORMALIZE_WHITESPACE +IGNORE_EXCEPTION_DETAIL +ELLIPSIS
['data', 'phantom', 'title']
>>> d.phantom
True
>>> print(d.title)
Nouveau Bénéficiaire


The dialog window has 6 data fields:

>>> sorted(d.data.keys())  #doctest: +NORMALIZE_WHITESPACE
['disabled_fields', 'email', 'first_name', 'gender', 'genderHidden', 'last_name']


>>> fld = avanti.Clients.parameters['observed_event']
>>> rt.show(fld.choicelist, language="en")
No data to display


Miscellaneous
=============

Until 20200818 the help_text of the municipality field wasn't set at all, and
the help text of Partner.city talked about a client because it had been
overwritten by the help text of :attr:`lino_avanti.lib.contacts.Person.city`.

Compare (a) the specs (i.e. the target of the links) and (b) the help texts of
the following fields:

- :attr:`lino_avanti.lib.avanti.Client.city`
- :attr:`lino_avanti.lib.avanti.Client.municipality`
- :attr:`lino_avanti.lib.contacts.Person.city`
- :attr:`lino_avanti.lib.contacts.Person.municipality`

>>> print(avanti.Client._meta.get_field('municipality').help_text)
The municipality where this client lives. This is basically
equal to city, except when city is a village
and has a parent which is a municipality (which causes that
place to be returned).

>>> print(contacts.Person._meta.get_field('municipality').help_text)
The municipality, i.e. either the city or a parent of it.


>>> print(contacts.Person._meta.get_field('city').help_text)
The locality, i.e. usually a village, city or town.

>>> print(contacts.Person._meta.get_field('city').help_text)
The locality, i.e. usually a village, city or town.
