.. doctest docs/dev/matrix/index.rst
.. _lino.tutorial.matrix:

=========================
Dynamic tables (Matrixes)
=========================

This tutorial shows how to use tables with dynamic columns.  It also
introduces a usage example for :doc:`/dev/parameters`.

It extends the application created in :doc:`/dev/tables/index` (so you
might follow that tutorial before reading on here).

We add an :class:`EntryType` model and a
:class:`CompaniesWithEntryTypes` table which is a matrix with one row
per `Company` and one column per `EntryType`.

.. image:: a.png
  :scale: 50  

This table shows for each cell the number of entries (of that company
and that type).

TODO: clicking on the number in every cell should open the list 
of these entries.

Doctest initialization:

>>> from lino import startup
>>> startup('lino_book.projects.watch2.settings')
>>> from lino.api.doctest import *

Check some permissions:

>>> pprint(list(rt.models.watch2.Companies.required_roles))
[<class 'lino.core.roles.SiteUser'>]

>>> from lino.core.roles import SiteUser
>>> albert = rt.models.users.User.objects.get(username="Albert")
>>> rt.models.watch2.Companies.get_view_permission(albert.user_type)
True

Here is our :xfile:`models.py` module. 
We also introduce filter parameters for the `Entries` table.

.. literalinclude:: ../../../lino_book/projects/watch2/models.py

You can play with this application as follows::

    $ go watch2
    $ python manage.py prep
    $ python manage.py runserver
    

   
A known problem is that after changing or adding an EntryType, 
the server must restart before the modified column becomes visible.

Note also the :file:`fixtures/demo.py` file which 
generates the demo entries 
using :ref:`dpy`:

.. literalinclude:: ../../../lino_book/projects/watch2/fixtures/demo.py

  

>>> rt.login("Albert").show(watch2.CompaniesWithEntryTypes)
==================== ============== ============ ======= ========== ============= ========
 Description          Consultation   Evaluation   Test    Analysis   Observation   Total
-------------------- -------------- ------------ ------- ---------- ------------- --------
 AllTech inc.         **3**          **3**        **4**   **2**      **2**         **14**
 BestTech inc.        **3**          **3**        **2**   **2**      **4**         **14**
 CoolTech inc.        **2**          **2**        **3**   **4**      **3**         **14**
 **Total (3 rows)**   **8**          **8**        **9**   **8**      **9**         **42**
==================== ============== ============ ======= ========== ============= ========
<BLANKLINE>
