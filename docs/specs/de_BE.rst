.. _tutorials.de_BE:

======================================================
Using mldbc with different variants of a same language
======================================================

.. How to run only this test:

    $ doctest docs/specs/de_BE.rst

    >>> from lino import startup
    >>> startup('lino_book.projects.de_BE.settings')
    >>> from lino.api.doctest import *

This article uses the :mod:`lino_book.projects.de_BE` project to
test and document the support for :ref:`mldbc` with different variants
of a same language on a same Site.

We have two variants of German in :attr:`languages
<lino.core.site.Site.languages>`: "normal" ('de') and "Belgian"
('de_BE'):

.. literalinclude:: /../../book/lino_book/projects/de_BE/settings.py

The :xfile:`models.py` file defines a single model:

.. literalinclude:: /../../book/lino_book/projects/de_BE/models.py

The model inherits from :class:`BabelNamed
<lino.utils.mldbc.mixins.BabelNamed>`.

We wrote a Python fixture with some differences between those two
languages.


.. literalinclude:: /../../book/lino_book/projects/de_BE/fixtures/demo.py
   :lines: 1-14

To verify whether it worked as expected, we ask Lino to show us the
`Expressions` table:

>>> rt.show('de_BE.Expressions')
==== ============================ ============================ =================================
 ID   Designation                  Designation (de)             Designation (de-be)
---- ---------------------------- ---------------------------- ---------------------------------
 1    the workshop                 die Werkstatt                das Atelier
 2    the lorry                    der Lastwagen                der Camion
 3    the folder                   der Ordner                   die Farde
 4    the fridge                   der Kühlschrank              der Frigo
 5    That's what it depends on.   Darauf kommt es an.          Darauf kommt es sich an.
 6    It's about health.           Es geht um die Gesundheit.   Es geht sich um die Gesundheit.
==== ============================ ============================ =================================
<BLANKLINE>

See also

- :meth:`lino.core.site.Site.get_language_info`
