=======
Tickets
=======

This section is obsolete.
As the Lino community grew, we needed an
independant ticketing system which is currently hosted at
http://bugs.lino-framework.org

It is kept here because it is the only known usage of
:rst:dir:`tickets_table`.

Open for contribution
---------------------

The following tickets are selected for future Lino Core Contributors.
If you understand at least one of them, then you are a potential `Lino
Core Developer <http://saffre-rumma.net/jobs/coredev>`_
candidate.

.. tickets_table:: 
   :filter: e.meta.get('state') in ('contrib', )

   *


Active
----------

.. tickets_table:: 
   :filter: e.meta.get('state') in ('open', 'todo', 'active')

   *

Waiting
-------

Tickets that are **waiting for feedback** from others.

.. tickets_table:: 
   :filter: e.meta.get('state') in ('discussion', 'testing')

   *

Long-term
----------

.. tickets_table:: 
   :filter: e.meta.get('state') in ('longterm', )

   *

Sleeping
--------

.. tickets_table:: 
   :filter: e.meta.get('state') in ('sleeping',)

   *

Done
--------

.. tickets_table:: 
   :filter: e.meta.get('state') in ('done', 'closed', 'fixed')

   *


Other
-----

.. tickets_table:: 
   :filter: e.meta.get('state') and not e.meta.get('state') in ('open', 'todo', 'active', 'discussion', 'testing', 'sleeping', 'longterm', 'contrib', 'done', 'closed', 'fixed')

   *


List of all tickets
-------------------

.. toctree::
   :maxdepth: 1
   :glob:
   
   ?
   ??
   ???
