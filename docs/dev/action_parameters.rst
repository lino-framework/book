.. doctest docs/dev/action_parameters.rst
   
=================================
Introduction to action parameters
=================================

.. This document is work in progress.

A **parameter action** is an action which has :attr:`parameters
<lino.core.utils.Parametrizable.parameters>`.  These parameters are to
be entered by the user in a dialog window before the action *per se*
is being run.


>>> import lino
>>> lino.startup('lino_book.projects.ui5.settings.doctests')
>>> from lino.api.doctest import *

The merge action is an example of an action with parameters.  When you
click the merge button on a ticket, Lino reacts by popping up a dialog
window asking for parameters.  The action request is submitted only
when you confirm this window.

.. image:: /specs/noi/tickets.Ticket.merge.png
   :width: 80%


>>> ba = rt.models.tickets.AllTickets.get_action_by_name('merge_row')
>>> action = ba.action
>>> p = action.parameters
>>> p['merge_to']
<django.db.models.fields.related.ForeignKey: merge_to>

>>> p['reason']
<django.db.models.fields.CharField: reason>



How to get the layout elements of an action parameter window,

>>> ui = settings.SITE.kernel.default_ui
>>> ui
lino.modlib.openui5 (media_name=openui5)

>>> lh = action.params_layout.get_layout_handle(ui)
>>> lh #doctest: +ELLIPSIS
<lino.core.layouts.LayoutHandle object at ...>

>>> lh.main
<ActionParamsPanel main in lino.core.layouts.ActionParamsLayout on <lino.core.merge.MergeAction merge_row ('Merge')>>

>>> lh['main'] is lh.main
True

>>> lh['merge_to']
<ForeignKeyElement merge_to in lino.core.layouts.ActionParamsLayout on <lino.core.merge.MergeAction merge_row ('Merge')>>

>>> lh['reason']
<CharFieldElement reason in lino.core.layouts.ActionParamsLayout on <lino.core.merge.MergeAction merge_row ('Merge')>>

You can **walk** over the elements of a panel:

>>> ses = rt.login('robin')
>>> with ses.get_user().user_type.context():
...     for e in lh.walk():
...        print("{} {}".format(e.name, e.__class__.__name__))
merge_to ForeignKeyElement
merge_to_ct Wrapper
reason CharFieldElement
reason_ct Wrapper
main ActionParamsPanel

Calling a parameter action programmatically
===========================================

In doctests we sometimes want to call an action programmatically
without doing a web request.

In that case we must specify the `action_param_values`.  It must be a
dict.  Lino checks whether the keys of the dict corresponds to the
names of the parameter fields:

>>> pv = dict(foo=1, reason="test")
>>> ar = ba.request_from(ses, action_param_values=pv)
Traceback (most recent call last):
...
Exception: Invalid key 'foo' in action_param_values of tickets.AllTickets request (possible keys are ['merge_to', 'reason'])

Lino does not validate the values when calling it programmatically.
For example `merge_to` should be a Ticket instance.
But here we specify an integer value instead, and Lino does not complain:

>>> pv = dict(merge_to=1, reason="test")
>>> ar = ba.request_from(ses, action_param_values=pv)
>>> ar.action_param_values
{'merge_to': 1, 'reason': 'test'}

Basically the following should work as well. (But nobody ever asked us
to make it possible).

>>> o1 = rt.models.tickets.Ticket.objects.get(pk=1)
>>> o2 = rt.models.tickets.Ticket.objects.get(pk=2)
>>> pv = dict(merge_to=o2, reason="test")
>>> ar = ba.request_from(ses, action_param_values=pv)
>>> ar.set_confirm_answer(False)
>>> response = o1.merge_row(ar)
>>> ar.response.has_key('xcallback')
True
>>> msg = ar.response['message']
>>> print(tostring(msg))
<div class="htmlText"><p>Are you sure you want to merge #1 (⛶ Föö fails to bar when baz) into #2 (☎ Bar is not always baz)?</p><ul><li>1 Wishes, 1 Dependencies, 3 Sessions, 1 Comments, 7 Stars <b>will get reassigned.</b></li><li>#1 (⛶ Föö fails to bar when baz) will be deleted</li></ul></div>

