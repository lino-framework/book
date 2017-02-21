.. _dev.ar:

=====================
Using action requests
=====================


.. To run only this test:

   $ python setup.py test -s tests.DocsTests.test_ar


An action request is when a given user asks to run a given action of a
given actor.

Action requests are instances of the
:class:`BaseRequest<lino.core.requests.BaseRequest>` class or one of
its subclasses (:class:`ActorRequest<lino.core.requests.ActorRequest>`
:class:`ActionRequest<lino.core.requests.ActionRequest>`
:class:`TableRequest<lino.core.tablerequest.TableRequest>`.

The traditional variable name for action requests in application code
and method signatures is ``ar``.  Except for the plain `BaseRequest`
instance returned by :func:`rt.login<lino.api.rt.login>`. This is
often called ``ses`` since you can imagine it as a session.

As a rough approximation you can say that every Django web request
gets wrapped into an action request.  The ActionRequest adds some more
information about the "context" (like the "renderer" being used) and
provides the application with methods to communicate with the user.

But there are exceptions to this approximaton.


- :meth:`show <lino.core.requests.BaseRequest.show>` 

- :meth:`set_response <lino.core.requests.BaseRequest.set_response>` 


- :meth:`ba.request_from <lino.core.boundaction.BoundAction.request_from>`
- :meth:`lino.core.request.get_permission`
- :meth:`lino.core.request.set_action_param_values`
- :meth:`lino.core.request.ar2button`



Iterating over table requests

A tablerequest has two iterators: data_iterator and
sliced_data_iterator.

>>> from lino import startup
>>> startup('lino_book.projects.min1.settings.demo')
>>> from lino.api.doctest import *

>>> rt.show('countries.Places', limit=10)
========= ======================== ==================== ================== ============ ========== ==================
 Country   Designation              Designation (de)     Designation (fr)   Place Type   zip code   Part of
--------- ------------------------ -------------------- ------------------ ------------ ---------- ------------------
 Belgium   Aalst                    Aalst                Alost              City         9300       Flandre de l'Est
 Belgium   Aalst-bij-Sint-Truiden                                           Village      3800       Limbourg
 Belgium   Angleur                                                          City         4031
 Belgium   Ans                                                              City         4430
 Belgium   Anvers                   Antwerpen            Anvers             Province
 Belgium   Baardegem                                                        Village      9310       Aalst
 Belgium   Baelen                   Baelen               Baelen             City         4837       Liège
 Belgium   Blégny                                                           City         4670
 Belgium   Brabant flamant          Flämisch-Brabant     Brabant flamant    Province
 Belgium   Brabant wallon           Wallonisch-Brabant   Brabant wallon     Province
========= ======================== ==================== ================== ============ ========== ==================
<BLANKLINE>

>>> rt.show('countries.Places', offset=5, limit=3)
========= ============= ================== ================== ============ ========== =========
 Country   Designation   Designation (de)   Designation (fr)   Place Type   zip code   Part of
--------- ------------- ------------------ ------------------ ------------ ---------- ---------
 Belgium   Baardegem                                           Village      9310       Aalst
 Belgium   Baelen        Baelen             Baelen             City         4837       Liège
 Belgium   Blégny                                              City         4670
========= ============= ================== ================== ============ ========== =========
<BLANKLINE>

>>> rt.show('countries.Places', offset=-5, limit=3)
Traceback (most recent call last):
...
AssertionError: Negative indexing is not supported.

>>> ar = countries.Places.request(offset=5, limit=3)  #doctest: +ELLIPSIS

>>> print(' '.join([pl.name for pl in ar]))
Aalst Aalst-bij-Sint-Truiden Angleur Ans Anvers Baardegem Baelen Blégny Brabant flamant Brabant wallon Brussels Burdinne Burg-Reuland Butgenbach Büllingen Cerfontaine Cuesmes Erembodegem Eupen Flandre de l'Est Flandre de l'Ouest Gijzegem Hainaut Herdersem Hofstade Kelmis Kettenis La Reid Limbourg Liège Liège Luxembourg Meldert Mons Moorsel Mortier Namur Namur Nieuwerkerken Nispert Ostende Ottignies Ouren Raeren Recht Sankt Vith Thieusies Trembleur Aachen Berlin Cologne Hamburg Monschau Munich Harju Kesklinn Narva Pärnu Pärnu Põhja-Tallinn Rapla Rapla Tallinn Tartu Vigala Ääsmäe Marseille Metz Nancy Nice Paris Strasbourg Amsterdam Breda Den Haag Maastricht Rotterdam Utrecht

>>> print(' '.join([pl.name for pl in ar.sliced_data_iterator]))
Baardegem Baelen Blégny


(TODO: write much more text. we would need a good explanation of how
to ceate subrequests etc.)
