.. doctest docs/specs/b2c.rst
.. _specs.cosi.b2c:

===============================================
``b2c`` : Import SEPA BankToCustomer statements
===============================================

This document describes the :mod:`lino_cosi.lib.b2c` plugin which adds
functionality for importing BankToCustomer SEPA statements from your
bank using the B2C CAMT.053 format.

This plugin is currently used only in Belgium.  Other countries should
be similar but are not tested.

.. contents::
   :depth: 1
   :local:
      
.. include:: /include/tested.rst


Code examples in this document use the
:mod:`lino_book.projects.pierre` demo project:

>>> from lino import startup
>>> startup('lino_book.projects.pierre.settings.doctests')
>>> from lino.api.doctest import *


The CAMT053 XML format
======================

The imported files must be in CAMT.053 format.

Excerpts of the Febelfin Implementation guidelines `XML message for
statement.
<https://www.febelfin.be/sites/default/files/files/Standard-XML-Statement-v1-en_0.pdf>`_
(version 1.0):

  This document contains the Belgian guidelines for the application of
  the Belgian subset of the MX.CAMT.053 B2C Statement.

  This message is sent by the bank to an account holder or a third
  person mandated by him.  It is used for informing the account holder
  or the third person mandated of the account balance s and account
  transactions

  The principle has been adopted for double encoding, i.e. encoding
  proper to ISO Bank Transaction Code list (§ 5.2 – Double encoding)
  together with ‘proprietary’ Febelfin encoding.

  Each item of the BankToCustomer Cash Management Standards message is
  referring to the corresponding index of the item in the (ISO 20022)
  Message Definition Report for Bank-to-Customer Cash Management. This
  Report can be found on www.iso20022.org, under “Catalogue of UNIFI
  messages”, with “camt.053.001.02” as reference for the EoD
  reporting.

  Any gaps in the index numbering are due to the fact that some
  message elements of the MX.CAMT.053.001.02 message are not supported
  in the Belgian subset


  
Manually importing SEPA statements
==================================

End-users invoke this via the menu command :menuselection:`Accounting
--> Import SEPA`.

>>> rt.login("robin").show_menu_path(system.SiteConfig.import_b2c)
Accounting --> Import SEPA

>>> rt.login("romain").show_menu_path(system.SiteConfig.import_b2c)
Comptabilité --> Import SEPA

           
.. class:: ImportStatements

    Import the .xml files found in the directory specified at
    :attr:`import_statements_path
    <lino_cosi.lib.b2c.Plugin.import_statements_path>`.

    When a file has been successfully imported, Lino deletes it.

    Note that if an .xml file gets downloaded a second time, Lino does
    not create these statements again.

    This action is invisible when :attr:`import_statements_path
    <lino_cosi.lib.b2c.Plugin.import_statements_path>` is empty.

   



Accounts, statements and transactions
=====================================

The imported data is stored in three tables.


.. class:: Account

    A bank account related to a partner.

    One partner can have more than one bank account.

    .. attribute:: account_name

        Name of the account, as assigned by the account servicing
        institution, in agreement with the account owner in order to
        provide an additional means of identification of the account.
        Usage: The account name is different from the
        :attr:`owner_name`. The account name is used in certain user
        communities to provide a means of identifying the account, in
        addition to the account owner's identity and the account
        number.

    .. attribute:: owner_name

        Name by which a party is known and which is usually used to
        identify that party.

.. class:: Statement

    A bank statement.

    This data is automaticaly imported by :class:`ImportStatements`.

    .. attribute:: sequence_number

        The legal sequential number of the statement, as assigned by
        the bank.

        See `LegalSequenceNumber
        <https://www.iso20022.org/standardsrepository/public/wqt/Content/mx/camt.053.001.02#mx/camt.053.001.02/Statement/LegalSequenceNumber>`_
        (`<LglSeqNb>`) for details.

    .. attribute:: start_date
    .. attribute:: end_date

        Note that year can differ between start_date and end_date for
        the first statement of every year.

    .. attribute:: unique_id

        A virtual field of the form `YYYY/NNNN` where YYYY is taken
        from the :attr:`end_date` and NNNN is taken from
        :attr:`electronic_sequence_number`.

    .. attribute:: electronic_sequence_number

           
           

.. class:: Transaction

    A transaction within a bank statement.

    This data is automaticaly imported by :class:`ImportStatements`.


    
    .. attribute:: statement

    .. attribute:: seqno

    .. attribute:: booking_date

    .. attribute:: value_date

    .. attribute:: transfer_type

       The actual historic name of the :attr:`txcd`.

    .. attribute:: txcd

        The Bank Transaction Code (`<BkTxCd>`) or "transfer type".
        Actually it is the "proprietary" part of this code.

    .. attribute:: txcd_issuer

        The issuer or the :attr:`txcd`.

    .. attribute:: txcd_text

        Virtual field with the textual translated description of the
        :attr:`txcd`.  Currently this works only for Belgian codes
        where :attr:`txcd_issuer` is `"BBA"` as defined in
        :mod:`lino_cosi.lib.b2c.febelfin`).

    .. attribute:: remote_account
    .. attribute:: remote_bic
    .. attribute:: remote_owner
    .. attribute:: remote_owner_address
    .. attribute:: remote_owner_city
    .. attribute:: remote_owner_postalcode
    .. attribute:: remote_owner_country_code



Plugin configuration
====================


The action can be configured via your :xfile:`settings.py` using the
parameters :attr:`import_statements_path
<Plugin.import_statements_path>` and :attr:`delete_imported_xml_files
<Plugin.delete_imported_xml_files>`.

Example of a :xfile:`settings.py` file::

    configure_plugin('b2c',
      delete_imported_xml_files=True,
      import_statements_path="/path/to/sepa_incoming")


Define a cron job
=================

How to configure your Lino server to import bank to Lino.

You have a cron job :file:`/etc/cron.d/import_sepa` defined as
follows::

    # Import SEPA statements into Lino on workdays between 7:15 and 18:45 every 30 minutes
    # m h dom mon dow user  command
    15,45 7-18 * * 1-5      www-data        /path/to/my/project/import_sepa.sh



The file :xfile:`import_sepa.sh` contains::

    #!/bin/bash
    # also called from /etc/cron.d/import_sepa
    set -e
    PROJECT_DIR=/usr/local/django/cpas_eupen

    # Virtual environment to activate:
    # Relative to PROJECT_DIR.
    ENVDIR=env

    cd $PROJECT_DIR
    . $ENVDIR/bin/activate

    python manage.py run import_sepa.py

The file :xfile:`import_sepa.py` contains::

    from django.conf import settings
    from lino.api import rt
    ses = rt.login()
    settings.SITE.site_config.import_b2c(ses)

Every import is being logged in the :xfile:`lino.log` file.

Febelfin Bank Transaction Code designations
===========================================

The :mod:`lino_xl.lib.b2c.febelfin` module defines a utility function
:func:`code2desc` which returns the designation of a *bank transaction
code*, as specified by the `XML message for statement Implementation
guidelines
<https://www.febelfin.be/sites/default/files/files/Standard-XML-Statement-v1-en_0.pdf>`_
of the Belgian Federation of Financial Sector.

This function is being used by the :attr:`txcd_text
<lino_xl.lib.b2c.models.Movement.txcd_text>` field of an imported
movement.

Usage examples:

>>> from lino_cosi.lib.b2c.febelfin import code2desc

>>> with translation.override('en'):
...     print(code2desc('0103'))
Standing order

>>> with translation.override('fr'):
...     print(code2desc('0103'))
Ordre permanent

>>> with translation.override('en'):
...     print(code2desc('0150'))
Transfer in your favour

>>> with translation.override('fr'):
...     print(code2desc('0150'))
Virement en votre faveur

>>> with translation.override('en'):
...     print(code2desc('8033'))
Miscellaneous fees and commissions


Did you know that there are 274 different Febelfin bank transaction codes?

>>> from lino_cosi.lib.b2c.febelfin import DESCRIPTIONS
>>> len(DESCRIPTIONS)
274

