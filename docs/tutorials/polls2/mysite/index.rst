.. _lino.tutorial.polls.solved:

========================
Solutions Polls tutorial
========================

.. how to test:
    $ python setup.py test -s tests.DocsTests.test_polls


.. contents:: Table of Contents
 :local:
 :depth: 2


Computing a sum
---------------

::

    def results_overview(self):
        lst = []
        total_votes = self.choice_set.aggregate(models.Sum('votes'))['votes__sum']
        for choice in self.choice_set.all():
            chunk = "{0}x {1}".format(choice.votes, choice)
            if total_votes:
                chunk += " ({0:.0f}%)".format(100.0 * choice.votes / total_votes)
            lst.append(chunk)
        s = " / ".join(lst)
        return s

  
({{100.0 * choice.votes / (question.choice_set.aggregate(Sum('votes'))['votes__sum'] or 1)}} %)

>>> x = 100.0 / 6
>>> "{:6.2f}".format(x)
' 16.67'
>>> "{:.1f}".format(x)
'16.7'
>>> "{:.0f}".format(x)
'17'

