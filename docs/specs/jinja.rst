.. doctest docs/specs/jinja.rst
.. _specs.jinja:

===========================
``jinja`` : Jinja printing
===========================

.. currentmodule:: lino.modlib.jinja

This document describes the :mod:`lino.modlib.jinja` plugin

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

Code examples in this document use the :mod:`lino_book.projects.min1` demo
project:

>>> from lino import startup
>>> startup('lino_book.projects.min1.settings.doctests')
>>> from lino.api.doctest import *



.. class:: JinjaBuildMethod

  Inherits from :class:`lino.modlib.printing.DjangoBuildMethod`.

Management commands
===================

This plugin defines two :term:`management commands <management command>`.

.. management_command:: showsettings

Print to stdout all the Django settings that are active on this :term:`Lino
site`.

Usage example:

>>> from atelier.sheller import Sheller
>>> shell = Sheller("lino_book/projects/min1")
>>> shell("python manage.py showsettings | grep EMAIL")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
DEFAULT_FROM_EMAIL = webmaster@localhost
EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST = mail.example.com
EMAIL_HOST_PASSWORD =
EMAIL_HOST_USER =
EMAIL_PORT = 25
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_SUBJECT_PREFIX = [Django]
EMAIL_TIMEOUT = None
EMAIL_USE_LOCALTIME = False
EMAIL_USE_SSL = False
EMAIL_USE_TLS = False
SERVER_EMAIL = root@localhost


.. management_command:: status

Write a diagnostic status report about this :term:`Lino site`.

A functional replacement for the :manage:`diag` command.

>>> shell = Sheller("lino_book/projects/apc")
>>> shell("python manage.py status")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
Plugins
=======
<BLANKLINE>
- lino : lino
- staticfiles : django.contrib.staticfiles
- about : lino.modlib.about
- jinja : lino.modlib.jinja (needed_by=lino.modlib.bootstrap3 (media_name=bootstrap-3.3.4, needed_by=lino.modlib.extjs (media_name=ext-3.3.1)))
- bootstrap3 : lino.modlib.bootstrap3 (media_name=bootstrap-3.3.4, needed_by=lino.modlib.extjs (media_name=ext-3.3.1))
- extjs : lino.modlib.extjs (media_name=ext-3.3.1)
- printing : lino.modlib.printing (needed_by=lino.modlib.system (needed_by=lino.modlib.gfks))
- system : lino.modlib.system (needed_by=lino.modlib.gfks)
- contenttypes : django.contrib.contenttypes (needed_by=lino.modlib.gfks)
- gfks : lino.modlib.gfks
- users : lino.modlib.users
- office : lino.modlib.office (needed_by=lino_xl.lib.countries)
- xl : lino_xl.lib.xl (needed_by=lino_xl.lib.countries)
- countries : lino_xl.lib.countries
- cosi : lino_cosi.lib.cosi (needed_by=lino_cosi.lib.contacts)
- contacts : lino_cosi.lib.contacts
- excerpts : lino_xl.lib.excerpts
- uploads : lino.modlib.uploads
- weasyprint : lino.modlib.weasyprint
- export_excel : lino.modlib.export_excel
- tinymce : lino.modlib.tinymce (media_name=tinymce-3.5.11)
- ledger : lino_xl.lib.ledger (needed_by=lino_xl.lib.sepa)
- sepa : lino_xl.lib.sepa
- products : lino_cosi.lib.products (extends_models=['Product'])
- memo : lino.modlib.memo (needed_by=lino_xl.lib.sales)
- checkdata : lino.modlib.checkdata (needed_by=lino_xl.lib.vat (needed_by=lino_xl.lib.sales))
- bevat : lino_xl.lib.bevat (needed_by=lino_xl.lib.vat (needed_by=lino_xl.lib.sales))
- vat : lino_xl.lib.vat (needed_by=lino_xl.lib.sales)
- sales : lino_xl.lib.sales
- finan : lino_xl.lib.finan
- sheets : lino_xl.lib.sheets
- sessions : django.contrib.sessions
<BLANKLINE>
Config directories
==================
<BLANKLINE>
- .../lino_book/projects/apc/settings/config [writeable]
- .../lino_xl/lib/sheets/config
- .../lino_xl/lib/finan/config
- .../lino_xl/lib/sales/config
- .../lino_xl/lib/sepa/config
- .../lino_xl/lib/ledger/config
- .../lino/modlib/tinymce/config
- .../lino/modlib/weasyprint/config
- .../lino_xl/lib/excerpts/config
- .../lino_xl/lib/contacts/config
- .../lino/modlib/users/config
- .../lino/modlib/printing/config
- .../lino/modlib/extjs/config
- .../lino/modlib/bootstrap3/config
- .../lino/modlib/jinja/config
- .../lino/config

The output may be
customized by overriding the :xfile:`jinja/status.jinja.rst` template.

.. xfile:: jinja/status.jinja.rst

The template file used by the :manage:`status` command.
