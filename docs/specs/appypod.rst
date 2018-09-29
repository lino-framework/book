.. doctest docs/specs/appypod.rst
.. _xl.specs.appypod:
   
==================
The appypod plugin
==================

This document adds some tests to :mod:`lino_xl.lib.appypod`.  We chose
a simple Lino table request and then have a look how such a request is
being rendered into a pdf document using appypod.

Recommended readings

- :ref:`lino.admin.appypod` 
- https://lxml.de/
- http://appyframework.org/pod.html
- http://appyframework.org/podWritingTemplates.html
  
   
>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *

>>> from lxml import etree
>>> from unipath import Path
>>> import tempfile

Here is a simple Lino table request:

>>> ar = rt.login('robin').spawn(countries.Countries)
>>> ar.show()
============================= ================================ ================================= ==========
 Designation                   Designation (de)                 Designation (fr)                  ISO code
----------------------------- -------------------------------- --------------------------------- ----------
 Belgium                       Belgien                          Belgique                          BE
 Congo (Democratic Republic)   Kongo (Demokratische Republik)   Congo (République democratique)   CD
 Estonia                       Estland                          Estonie                           EE
 France                        Frankreich                       France                            FR
 Germany                       Deutschland                      Allemagne                         DE
 Maroc                         Marokko                          Maroc                             MA
 Netherlands                   Niederlande                      Pays-Bas                          NL
 Russia                        Russland                         Russie                            RU
============================= ================================ ================================= ==========
<BLANKLINE>



The :file:`lino_xl/lib/appypod/config/Table.odt` template uses the
:func:`table` function to insert a chunk of ODF XML.
      
This code is produced by the :meth:`insert_table
<lino_xl.lib.appy_pod.appy_renderer.AppyRenderer.insert_table>` method
which dynamically creates a style for every column and respects the
widths it gets from the request's :meth:`get_field_info
<lino.core.tablerequest.TableRequest.get_field_info>`, which returns
`col.width or col.preferred_width` for each column.


To get an AppyRenderer for this test case, we must give a template
file and a target file.  As the template we will use
:file:`Table.odt`.  The target file must be in a temporary directory
 and every test run will create a temporary directory next to
the target.

>>> from lino_xl.lib.appypod.appy_renderer import AppyRenderer
>>> ctx = {}
>>> template = rt.find_config_file('Table.odt')
>>> target = Path(tempfile.gettempdir()).child("out.odt")
>>> rnd = AppyRenderer(ar, template, ctx, target)


>>> odf = rnd.insert_table(ar)
>>> print(odf)  #doctest: +ELLIPSIS
<table:table ... table:...name="countries.Countries" ...name="countries.Countries">...

Let's parse that long string so that we can see what it contains.

>>> root = etree.fromstring(odf)

The root element is of course our table

>>> root  #doctest: +ELLIPSIS
<Element {urn:oasis:names:tc:opendocument:xmlns:table:1.0}table at ...>

Every ODF table has three children:

>>> children = list(root)
>>> len(children)
3
>>> print('\n'.join(e.tag for e in children))
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-columns
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-header-rows
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-rows

>>> columns = children[0]
>>> header_rows = children[1]
>>> rows = children[2]

The rows

>>> len(rows)
8
>>> len(rows) == ar.get_total_count()
True

>>> cells = list(rows[0])
>>> print('\n'.join(e.tag for e in cells))
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-cell
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-cell
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-cell
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-cell

The columns

>>> print('\n'.join(e.tag for e in columns))
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-column
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-column
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-column
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-column

>>> print('\n'.join(e.tag for e in header_rows))
{urn:oasis:names:tc:opendocument:xmlns:table:1.0}table-row


