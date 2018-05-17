.. _dev.table_summaries:

===============
Table summaries
===============


A **table summary** is an alternative non-tabular way of displaying
the data in the table.

You can see the summary of a table by setting its :attr:`display_mode
<lino.core.tables.Table.display_mode>` to ``'summary'`` (instead of
its default value ``'grid'``).

For any table you can define a customized summary view by writing a 
:meth:`get_table_summary
<lino.core.actors.Actor.get_table_summary>` method.

For example the detail window of a :class:`Site
<lino_xl.lib.tickets.Site>` in :ref:`noi` (the :mod:`team
<lino_book.projects.team>` demo project):

.. image:: /specs/noi/tickets.SiteDetail.png

Here is the layout for this window::

    class SiteDetail(SiteDetail):

        main = """general more history"""

        general = dd.Panel("""
        id name 
        company contact_person reporting_type workflow_buttons:20
        stars.StarsByController:30 TicketsBySite
        """, label=_("General"))
        
        more = dd.Panel(...)
        history = dd.Panel(...)

  
Note that the lower part of the :guilabel:`General` tab is occupied by
two :ref:`slave tables <slave_tables>`,
:class:`stars.StarsByController <lino_xl.lib.stars.StarsByController>`
and :class:`TicketsBySite <lino_xl.lib.tickets.TicketsBySite>`.

The :attr:`display_mode <lino.core.tables.Table.display_mode>` of
:class:`TicketsBySite <lino_xl.lib.tickets.TicketsBySite>` is
``'summary'``, while for :class:`stars.StarsByController
<lino_xl.lib.stars.StarsByController>` it is the default (``'grid'``).


If we changed the display mode of :class:`TicketsBySite
<lino_xl.lib.tickets.TicketsBySite>` to ``grid``, we would get:

.. image:: /specs/noi/tickets.SiteDetail-2.png


If the :attr:`display_mode` of :class:`StarsByController` was
``summary``, we would get:

.. image:: /specs/noi/tickets.SiteDetail-3.png


Note that :class:`StarsByController` has no *custom summary view*
defined, so when we ask a summary, we get the default view, which
simply displays all items using their :meth:`__str__` method, which
for a :class:`lino_xl.lib.stars.Star` object is defined as follows::
        
    def __str__(self):
        return _("{} starring {}").format(self.user, self.owner)


Here is how the customized summary for :class:`TicketsBySite
<lino_xl.lib.tickets.TicketsBySite>` is defined::

    @classmethod
    def get_table_summary(self, master, ar):

        # request the rows of the slave table:
        sar = self.request_from(ar, master_instance=master)

        # rows are ordered by state. we just group them 
        # every element of `items` is a tuple `(state,
        # list-of-objects)`.
        items = []
        ci = None

        for obj in sar:
            btn = obj.obj2href(ar)
            if ci is not None and ci[0] is obj.state:
                ci[1].append(btn)
            else:
                ci = (obj.state, [btn])
                items.append(ci)

        # now render them as a UL containing on LI per item
        items = [E.li(str(i[0]), ' : ', *join_elems(i[1], ", "))
                 for i in items]

        return E.ul(*items)


Other usage examples of custom table summaries:

- :class:`lino_xl.lib.households.models.SiblingsByPerson`

        
