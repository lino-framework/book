.. doctest docs/specs/beid.rst
.. _specs.lib.beid:

=======================
Belgian ID card holders
=======================

The :mod:`lino_xl.lib.beid` plugin adds functionality for reading
Belgian eID cards and storing that data in the database.

Examples in this document use the :mod:`lino_book.projects.adg` demo
project.

>>> import lino
>>> lino.startup('lino_book.projects.adg.settings.doctests')
>>> from lino.api.doctest import *


.. contents::
   :depth: 1
   :local:

.. currentmodule:: lino_xl.lib.beid

Introduction
============

Installing this package makes sense only if there is exactly one
subclass of the :class:`BeIdCardHolder` model mixin among your
application's models.  That model is referrable as
:attr:`lino_xl.lib.beid.Plugin.holder_model`.

>>> dd.plugins.beid.holder_model
<class 'lino_avanti.lib.avanti.models.Client'>
      

See unit tests in :mod:`lino_welfare.tests.test_beid`.

.. class:: BeIdCardHolder

    Mixin for models which represent an eid card holder.
    Currently only Belgian eid cards are tested.
    Concrete subclasses must also inherit from :mod:`lino.mixins.Born`.

    Class attributes:

    .. attribute:: validate_national_id = False
                   
        Whether to validate the :attr:`national_id` immediately before
        saving a record.  If this is `False`, the :attr:`national_id`
        might contain invalid values which would then cause data
        problems.


    Database fields:

    .. attribute:: national_id

        The SSIN. It is a *nullable char field* declared *unique*. It
        is not validated directly because that would cause problems
        with legacy data where SSINs need manual control. See also
        :class:`BeIdCardHolderChecker`.

    .. attribute:: nationality

        The nationality. This is a pointer to
        :class:`countries.Country
        <lino_xl.lib.statbel.countries.models.Country>` which should
        contain also entries for refugee statuses.

        Note that the nationality is *not* being read from eID card
        because it is stored there as a language and gender specific
        plain text.

    .. attribute:: image

        Virtual field which displays the picture.
           


ID card types
=============

>>> show_choicelist(beid.BeIdCardTypes)
======= ================== ======================================== ==================================================================================== ==============================================
 value   name               en                                       de                                                                                   fr
------- ------------------ ---------------------------------------- ------------------------------------------------------------------------------------ ----------------------------------------------
 01      belgian_citizen    Belgian citizen                          Belgischer Staatsbürger                                                              Citoyen belge
 06      kids_card          Kids card (< 12 year)                    Kind unter 12 Jahren                                                                 Kids card (< 12 year)
 11      foreigner_a        Foreigner card A                         A (Bescheinigung der Eintragung im Ausländerregister - Vorübergehender Aufenthalt)   Étranger A (Séjour temporaire)
 12      foreigner_b        Foreigner card B                         B (Bescheinigung der Eintragung im Ausländerregister)                                Foreigner card B
 13      foreigner_c        Foreigner card C                         C (Personalausweis für Ausländer)                                                    Foreigner card C
 14      foreigner_d        Foreigner card D                         D (Daueraufenthalt - EG)                                                             Foreigner card D
 15      foreigner_e        Foreigner card E                         E (Anmeldebescheinigung)                                                             Foreigner card E
 16      foreigner_e_plus   Foreigner card E+                        E+                                                                                   Foreigner card E+
 17      foreigner_f        Foreigner card F                         F (Aufenthaltskarte für Familienangehörige eines Unionsbürgers)                      Foreigner card F
 18      foreigner_f_plus   Foreigner card F+                        F+                                                                                   Foreigner card F+
 99      orange_card        Registration certificate (Orange card)   Eintragungsbescheinigung (Orange Karte)                                              Attestation d’immatriculation (Carte orange)
======= ================== ======================================== ==================================================================================== ==============================================
<BLANKLINE>


.. class:: BeIdCardTypes

    A list of Belgian identity card types.

    We didn't yet find any official reference document.
    
    The eID applet returns a field `documentType` which contains a
    numeric code.  For example 1 is for "Belgian citizen", 6 for "Kids
    card",...
    
    The eID viewer, when saving a card as xml file, doesn't save these
    values nowhere, it saves a string equivalent (1 becomes
    "belgian_citizen", 6 becomes "kids_card", 17 becomes
    "foreigner_f", 16 becomes "foreigner_e_plus",...
    
    Sources:

    - [1] `kuleuven.be <https://securehomes.esat.kuleuven.be/~decockd/wiki/bin/view.cgi/EidForums/ForumEidCards0073>`__
    - [2] The `be.fedict.commons.eid.consumer.DocumentType <http://code.google.com/p/eid-applet/source/browse/trunk/eid-applet-service/src/main/java/be/fedict/eid/applet/service/DocumentType.java>`__ enum.

    - http://www.adde.be/joomdoc/guides/les-titres-de-sejours-en-belgique-guide-pratique-dec12-g-aussems-pdf/download


    Excerpts from [1]:
    
    - Johan: A document type of 7 is used for bootstrap cards -- What
      is a bootstrap card (maybe some kind of test card?)  Danny: A
      bootstrap card was an eID card that was used in the early start
      of the eID card introduction to bootstrap the computers at the
      administration. This type is no longer issued.
    
    - Johan: A document type of 8 is used for a
      "habilitation/machtigings" card -- Is this for refugees or
      asylum seekers? Danny: A habilitation/machtigings card was aimed
      at civil servants. This type is also no longer used.

           
Residence types
===============
    
>>> rt.show(beid.ResidenceTypes)
======= ====== ========================
 value   name   text
------- ------ ------------------------
 1              Register of citizens
 2              Register of foreigners
 3              Waiting register
======= ====== ========================
<BLANKLINE>


.. class:: ResidenceTypes
           
    The list of Belgian resident registers
    (Einwohnerregister, Registre de résidents).

    https://en.wikipedia.org/wiki/Resident_registration

    ======================= =========================== =======================
    de                      fr                          nl
    ======================= =========================== =======================
    Bevölkerungsregister    Registre de la population   Bevolkingsregister
    Fremdenregister         Registre des étrangers      Vreemdelingenregister
    Warteregister           Registre d'attente
    ======================= =========================== =======================





.. class:: BeIdCardHolderChecker

    Invalid NISSes are not refused à priori using a ValidationError
    (see :attr:`BeIdCardHolder.national_id`), but this checker reports
    them.

    Belgian NISSes are stored including the formatting characters (see
    :mod:`lino.utils.ssin`) in order to guarantee uniqueness.
           



Tests
=====

The :attr:`national_id <lino_xl.lib.beid.BeIdCardHolder.national_id>`
field of a client. It nullable and unique: it can be empty, but must
be empty when it isn't.

>>> fld = rt.models.avanti.Client._meta.get_field('national_id')
>>> print(fld.help_text)
The SSIN. It is a nullable char field declared unique. It
is not validated directly because that would cause problems
with legacy data where SSINs need manual control. See also
BeIdCardHolderChecker.

>>> print(fld.null)
True
>>> print(fld.unique)
True
