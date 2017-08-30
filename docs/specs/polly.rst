.. _book.specs.polly:

Lino Polly
==========

..  doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.polly.settings.demo')
    >>> from lino.api.shell import *

>>> ses = rt.login("robin")

>>> ses.show("polls.Polls")
=========== ============================== ============= ========
 Reference   Heading                        Author        State
----------- ------------------------------ ------------- --------
             Customer Satisfaction Survey   Rolf Rompen   Active
             Participant feedback           Robin Rood    Active
             Political compass              Rolf Rompen   Active
=========== ============================== ============= ========
<BLANKLINE>

>>> obj = polls.Poll.objects.get(
...    title="Customer Satisfaction Survey")
>>> ses.show("polls.PollResult", obj)
======================================================== ============ ========== ====
 Question                                                 Choice Set   #Answers   A1
-------------------------------------------------------- ------------ ---------- ----
 First section
 1) Polls Mentor Ltd. has a good quality/price ratio.
 2) Polls Mentor Ltd. is better than their concurrents.
 3) Polls Mentor Ltd. has an attractive website.
 Second section
 1) Polls Mentor Ltd. values my money.
 2) I am proud to be a customer of Polls Mentor Ltd..
 3) I would recommend Polls Mentor Ltd. to others.
======================================================== ============ ========== ====
<BLANKLINE>

