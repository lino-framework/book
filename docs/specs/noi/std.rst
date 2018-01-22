.. doctest docs/specs/noi/std.rst
.. _noi.specs.std:

================================
The Standard variant of Lino Noi
================================

..  doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.team.settings.doctests')
    >>> from lino.api.doctest import *



Overview
========

>>> dd.is_installed('products')
False

>>> dd.plugins.topics
lino_noi.lib.topics

>>> dd.plugins.tickets
lino_noi.lib.tickets (extends_models=['Ticket'])

>>> dd.plugins.working
lino_xl.lib.working


Testing ticket #352
===================


>>> A = rt.models.working.SessionsByTicket
>>> obj = rt.models.tickets.Ticket.objects.get(pk=1)

>>> ses = rt.login('robin', renderer=settings.SITE.kernel.default_renderer)
>>> ses.is_on_main_actor
True
>>> ar = rt.models.tickets.Tickets.request(parent=ses)
>>> ar.is_on_main_actor
True
>>> ar.actor
lino_xl.lib.tickets.ui.Tickets
>>> html = A.get_slave_summary(obj, ar)
>>> print(E.tostring(html))  #doctest: +SKIP
<div class="htmlText"><p><a href="javascript:Lino.tickets.Tickets.start_session(null,true,1,{  })" style="text-decoration:none">&#9654;</a></p><p>Total 0:00 hours.</p><p>Active sessions: <span><a href="javascript:Lino.working.SessionsByTicket.detail.run(null,{ &quot;record_id&quot;: 1 })">Jean since 09:00:00</a> <a href="javascript:Lino.working.Sessions.end_session(null,true,1,{  })" style="text-decoration:none">&#9632;</a></span>, <span><a href="javascript:Lino.working.SessionsByTicket.detail.run(null,{ &quot;record_id&quot;: 5 })">Luc since 09:00:00</a> <a href="javascript:Lino.working.Sessions.end_session(null,true,5,{  })" style="text-decoration:none">&#9632;</a></span>, <span><a href="javascript:Lino.working.SessionsByTicket.detail.run(null,{ &quot;record_id&quot;: 9 })">Mathieu since 09:00:00</a> <a href="javascript:Lino.working.Sessions.end_session(null,true,9,{  })" style="text-decoration:none">&#9632;</a></span></p></div>

>>> soup = BeautifulSoup(E.tostring(html), 'lxml')
>>> # print(soup.body.prettify())
>>> links = soup.body.find_all('a')
>>> len(links)
7
>>> for lnk in links:
...    print(lnk['href'])
javascript:Lino.tickets.Tickets.start_session(null,true,1,{  })
javascript:Lino.working.Sessions.detail.run(null,{ "record_id": 1 })
javascript:Lino.working.Sessions.end_session(null,false,1,{  })
javascript:Lino.working.Sessions.detail.run(null,{ "record_id": 5 })
javascript:Lino.working.Sessions.end_session(null,false,5,{  })
javascript:Lino.working.Sessions.detail.run(null,{ "record_id": 9 })
javascript:Lino.working.Sessions.end_session(null,false,9,{  })


