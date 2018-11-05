.. doctest docs/specs/avanti/avanti.rst
.. _avanti.specs.avanti:

=================================
Clients in Lino Avanti
=================================

.. doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *

This document describes the :mod:`lino_avanti.lib.avanti` plugin.    

.. contents::
  :local:

.. currentmodule:: lino_avanti.lib.avanti


Clients
=======

.. class:: Client(lino.core.model.Model)
           
    A **client** is a person using our services.

    .. attribute:: translator_type
                   
        Which type of translator is needed with this client.
                   
        See also :class:`TranslatorTypes`
        
    .. attribute:: professional_state
                   
        The professional situation of this client.

        See also :class:`ProfessionalStates`
                   
    .. attribute:: overview

        A panel with general information about this client.

    .. attribute:: client_state
    
        Pointer to :class:`ClientStates`.

        >>> rt.show('clients.ClientStates')
        ======= ========== ============ =============
         value   name       text         Button text
        ------- ---------- ------------ -------------
         05      incoming   Incoming
         10      newcomer   Newcomer
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
       
       This is a pointer to a
       :class:`lino_xl.lib.countries.Place`.

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

   For privacy reasons this table shows only a very limited set of
   fields. For example the names are hidden. OTOH it includes the
   :attr:`municipality <lino_avanti.lib.avanti.Client.municipality>`
   virtual field.


>>> show_columns(avanti.AllClients, all=True)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
+-------------------+------------------------+--------------------------------------------------------------+
| Internal name     | Verbose name           | Help text                                                    |
+===================+========================+==============================================================+
| client_state      | State                  | Pointer to ClientStates.                                     |
+-------------------+------------------------+--------------------------------------------------------------+
| starting_reason   | Starting reason        |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| ending_reason     | Ending reason          |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| city              | Locality               | The place (village or municipality) where this client lives. |
+-------------------+------------------------+--------------------------------------------------------------+
| municipality      | Municipality           |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| country           | Country                |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| zip_code          | Zip code               |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| nationality       | Nationality            | The nationality. This is a pointer to                        |
|                   |                        | countries.Country which should                               |
|                   |                        | contain also entries for refugee statuses.                   |
+-------------------+------------------------+--------------------------------------------------------------+
| gender            | Gender                 | The sex of this person (male or female).                     |
+-------------------+------------------------+--------------------------------------------------------------+
| birth_country     | Birth country          |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| in_belgium_since  | Lives in Belgium since | Uncomplete dates are allowed, e.g.                           |
|                   |                        | "00.00.1980" means "some day in 1980",                       |
|                   |                        | "00.07.1980" means "in July 1980"                            |
|                   |                        | or "23.07.0000" means "on a 23th of July".                   |
+-------------------+------------------------+--------------------------------------------------------------+
| needs_work_permit | Needs work permit      |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| translator_type   | Translator type        | Which type of translator is needed with this client.         |
+-------------------+------------------------+--------------------------------------------------------------+
| mother_tongues    | Mother tongues         |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| cef_level_de      | None                   |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| cef_level_fr      | None                   |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| cef_level_en      | None                   |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+
| user              | Primary coach          | The author of this object.                                   |
|                   |                        | A pointer to lino.modlib.users.models.User.                  |
+-------------------+------------------------+--------------------------------------------------------------+
| event_policy      | Recurrency policy      |                                                              |
+-------------------+------------------------+--------------------------------------------------------------+

   
           
.. class:: MyClients(Clients)

    Shows all clients having me as primary coach. Shows all client states.

    >>> rt.login('robin').show('avanti.MyClients')
    =========================== ============ =============== ===== ================================= ========== ================ ======= ===== ==================
     Name                        State        National ID     GSM   Address                           Age        e-mail address   Phone   ID    Contact language
    --------------------------- ------------ --------------- ----- --------------------------------- ---------- ---------------- ------- ----- ------------------
     ABDALLA Aádil (120)         Registered   950201 001-38         August-Thonnar-Str., 4700 Eupen   22 years                            120
     ABDELRAHMAN Aáqil (133)     Ended        870305 001-48         Euregiostraße, 4700 Eupen         29 years                            133
     ABDOU Abeer (143)           Ended        800828 002-21         Heidberg, 4700 Eupen              36 years                            143
     ABED Abdul Báári (159)      Ended        740221 001-64         4730 Raeren                       43 years                            159   en
     ABOUD Ahláám (166)          Ended        690627 002-97         4730 Raeren                       47 years                            166   en
     ANKUNDINOV Aleksi (149)     Ended        911030 001-13         4730 Raeren                       25 years                            149   en
     ARSHUN Aloyoshenká (135)    Ended        850424 001-25         Gewerbestraße, 4700 Eupen         31 years                            135
     BAH Aráli (119)             Ended        970531 001-74         Am Waisenbüschchen, 4700 Eupen    19 years                            119
     BASHMAKOV Agáfoniká (153)   Ended        761207 002-13         4730 Raeren                       40 years                            153   en
     BERENDT Antoshá (165)       Ended        700602 001-93         4730 Raeren                       46 years                            165   en
     CONGO Chiámáká (126)        Registered   890702 001-14         Bergstraße, 4700 Eupen            27 years                            126
     DIA Deion (137)             Ended        840519 001-64         Gospert, 4700 Eupen               32 years                            137
     FALL Dembe (145)            Ended        790923 001-61         Heidhöhe, 4700 Eupen              37 years                            145
     KEITA Cácey (161)           Ended        730318 002-42         4730 Raeren                       43 years                            161   en
    =========================== ============ =============== ===== ================================= ========== ================ ======= ===== ==================
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
 printing.CachedPrintableChecker   Check for missing target files
 countries.PlaceChecker            Check data of geographical places.
 cal.EventGuestChecker             Entries without participants
 cal.ConflictingEventsChecker      Check for conflicting calendar entries
 cal.ObsoleteEventTypeChecker      Obsolete generated calendar entries
 cal.LongEntryChecker              Too long-lasting calendar entries
 beid.BeIdCardHolderChecker        Check for invalid SSINs
 dupable.DupableChecker            Check for missing phonetic words
 dupable.SimilarObjectsChecker     Check for similar objects
================================= ========================================
<BLANKLINE>
    
