.. doctest docs/specs/tera/misc.rst
.. _tera.specs.misc:
.. _presto.specs.psico:

=============================
Lino Tera : a first overview
=============================

.. doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db import models

The demo project :mod:`lino_book.projects.lydia` is used for testing
the following document.

>>> settings.SETTINGS_MODULE
'lino_book.projects.lydia.settings.doctests'


All :ref:`tera` application have a :xfile:`settings.py` module which
inherits from :mod:`lino_tera.lib.tera.settings`.

>>> from lino_tera.lib.tera.settings import Site
>>> isinstance(settings.SITE, Site)
True

>>> dd.is_installed('addresses')
False


Partner types
=============

>>> dd.plugins.contacts
lino_tera.lib.contacts

>>> print([m.__name__ for m in rt.models_by_base(rt.models.contacts.Partner)])
['Company', 'Partner', 'Person', 'Household', 'Client']

.. py2rst::

   from lino import startup
   startup('lino_book.projects.lydia.settings.demo')
   from lino.api import rt
   rt.models.contacts.Partner.print_subclasses_graph()


Activities
==========

>>> print(settings.SITE.project_model)
<class 'lino_tera.lib.courses.models.Course'>


Therapeutical groups
====================

>>> rt.show(courses.CourseAreas)
======= ============= ======================
 value   name          text
------- ------------- ----------------------
 10      therapies     Individual therapies
 20      life_groups   Life groups
 30      default       Other groups
======= ============= ======================
<BLANKLINE>


.. _presto.specs.teams:

Teams
=====

>>> rt.show(teams.Teams)
=========== ============= ================== ==================
 Reference   Designation   Designation (de)   Designation (fr)
----------- ------------- ------------------ ------------------
 E           Eupen
 S           St.Vith
=========== ============= ================== ==================
<BLANKLINE>


The following just repeats on the first payment order what has been
done for all orders when :mod:`lino_xl.lib.finan.fixtures.demo`
generated them:

>>> from unipath import Path
>>> ses = rt.login()
>>> obj = rt.models.finan.PaymentOrder.objects.all()[0]
>>> rv = obj.write_xml.run_from_session(ses)  #doctest: +ELLIPSIS
xml render <django.template.backends.jinja2.Template object at ...> -> .../media/xml/xml/finan.PaymentOrder-63.xml ('en', {})

>>> rv['success']
True
>>> print(rv['open_url'])
/media/xml/xml/finan.PaymentOrder-63.xml

Let's check whether the XML file has been generated and is a valid
SEPA payment initiation:

>>> fn = Path(settings.SITE.cache_dir + rv['open_url'])
>>> fn.exists()
True

>>> from etgen.sepa.validate import validate_pain001
>>> validate_pain001(fn)


Voucher types
=============

>>> rt.show(ledger.VoucherTypes)
=============================== ====== ================================================================
 value                           name   text
------------------------------- ------ ----------------------------------------------------------------
 sales.InvoicesByJournal                Product invoice (sales.InvoicesByJournal)
 finan.JournalEntriesByJournal          Journal Entry (finan.JournalEntriesByJournal)
 finan.PaymentOrdersByJournal           Payment Order (finan.PaymentOrdersByJournal)
 finan.BankStatementsByJournal          Bank Statement (finan.BankStatementsByJournal)
 ana.InvoicesByJournal                  Analytic invoice (ana.InvoicesByJournal)
 vat.InvoicesByJournal                  Invoice (vat.InvoicesByJournal)
 bevats.DeclarationsByJournal           Special Belgian VAT declaration (bevats.DeclarationsByJournal)
=============================== ====== ================================================================
<BLANKLINE>


>>> # rt.show(ledger.Journals, filter=models.Q(must_declare=True))



Internal details
=================


The following shows that :ticket:`1975` is a duplicate of
:ticket:`492`:

>>> a = rt.models.ana.InvoicesByJournal.actions.get('wf1')
>>> a.action.auto_save
True




Technical stuff (don't read)
============================

Verify whether we can select an `invoice_recipient` on a client.  It's
an editable remote field.

>>> base = "/choices/tera/Clients/salesrule__invoice_recipient"
>>> show_choices("robin", base + '?query=')  #doctest: +ELLIPSIS
<br/>
AS Express Post
AS Matsalu Veevärk
Adam Albert
Adam Ilja
Adam Noémie
...
Õunapuu Õie
Östges Otto
