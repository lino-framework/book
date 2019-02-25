.. _belref:
.. _lino.tutorial.belref:

======================
The ``belref`` project
======================

.. To test only this document, run::

       $ doctest docs/specs/projects/belref.rst

   doctest init:

   >>> from lino import startup
   >>> startup('lino_book.projects.belref.settings.demo')
   >>> from lino.api.doctest import *


.. contents::
   :local:


A way for publishing structured data
====================================

Lino Belref is a website with various structured information about
Belgium in three national languages.  An early prototype is running at
http://belref.lino-framework.org and is mentioned on our :ref:`demos`
page.

The primary goal of this project is to describe a way for storing,
maintaining and publishing certain kind of **structured data** about a
given topic.  The system would publish that data in many different
ways.

The `belref` project shows a dictionary with specific "Belgian"
vocabulary and a database of Belgian cities and other geographic
names. That choice is just illustrative and not a definitive
decision. There is also :mod:`lino_book.projects.estref`.

The data on such a site would be *stored* as :ref:`Python fixtures
<dpy>` which makes it possible to maintain the content using
established development tools for version control, issue tracking and
testing.  This mixture of data and source code is currently published
and maintained as part of Lino's repository in the
:mod:`lino_book.projects.belref` package.


Project status
==============

A side benefit of this project is to be our test field for the
:mod:`lino.modlib.bootstrap3` front end.

The project itself grows very slowly because I know no single person
who believes that this might make sense (and even I wouldn't give my
hand for it).  See also :doc:`/topics/gpdn`.


Tests
=====

>>> def test(url):
...     res = test_client.get(url)
...     assert(res.status_code == 200)
...     soup = BeautifulSoup(res.content, "lxml")
...     print(soup.get_text(' ', strip=True))

>>> test('/?ul=fr')
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF +ELLIPSIS
Lino Belref demo fr nl de Concepts Concepts Pays Endroits Bienvenue sur Lino Belref demo .
<BLANKLINE>
Ce site héberge le logiciel libre Lino Belref version ...

>>> test('/?ul=de')
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF +ELLIPSIS
Lino Belref demo fr nl de Begriffe Begriffe Länder Orte Willkommen auf Lino Belref demo .
<BLANKLINE>
Hier läuft Lino Belref ...



The API
==============

This section is currently deactivated.

..
    The current implementation has only one HTTP API which is the JSON API
    of :mod:`lino.modlib.extjs`

    >> res = test_client.get("/api/concepts/Concepts?fmt=json&start=0&limit=100")
    >> res.status_code
    200
    >> data = json.loads(res.content)
    >> rmu(data.keys())
    ['count', 'rows', 'success', 'no_data_text', 'title']
    >> data['count']
    14
    >> rmu(data['rows'][0])
    ['Institut National de Statistique', 'Nationaal Instituut voor Statistiek', 'Nationales Institut f\xfcr Statistik', 1, 'INS', 'NIS', 'NIS', {'id': True}, False]


    Get the list of places in Belgium:

    >> res = test_client.get("/api/countries/Places?fmt=json&start=0&limit=100")
    >> res.status_code
    200
    >> data = json.loads(res.content)
    >> data['count']
    2878
    >> rmu(data['rows'][0])
    ['Belgique', 'BE', "'s Gravenvoeren", '', '', 'Ville', '50', '3798', None, None, 2147, False, '73109', '<p />', '<span />', '<div><a href="javascript:Lino.countries.Places.detail.run(null,{ &quot;record_id&quot;: 2147 })">\'s Gravenvoeren</a></div>', '<div><a href="javascript:Lino.countries.Places.detail.run(null,{ &quot;record_id&quot;: 2147 })">\'s Gravenvoeren</a></div>', {'id': True}, False]

    The JSON API of :mod:`lino.modlib.extjs` is actually not written for
    being public, that's why we have strange items like
    ``delete_selected`` which are used by the ExtJS front end.

    So a next step might be to write an XML-based API for publishing data
    from a database, maybe SOAP or XML-RPC.

    In a project like belref where data does not change very often, a
    dynamic API would be overhead. So another step might be to write an
    admin command which generates a set of static files to be published.
    These static files can be XML, JSON or OpenDocument.  Maybe even some
    proprietary format like `.xls`.

    One application might be to write some Wikipedia pages with that data
    and a `Wikipedia bot <https://en.wikipedia.org/wiki/Wikipedia:Bots>`_
    which maintains them by accessing our API.

