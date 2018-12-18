.. doctest docs/specs/polls.rst
.. _tested.polly:
.. _book.specs.polls:

=================================================
``polls`` : managing questionnaires and responses
=================================================

This document describes the :mod:`lino_xl.lib.polls` plugin which
adds database models and functionality for managing polls.


.. currentmodule:: lino_xl.lib.polls


>>> import lino
>>> lino.startup('lino_book.projects.polly.settings.demo')
>>> from lino.api.doctest import *

                   

Overview
========

A :class:`Poll` is a collection of :class:`Questions <Question>` which
we want to ask repeatedly to different people. Each Question has a
*question text* and a :class:`ChoiceSet`, i.e. a stored ordered set of
possible choices.

A :class:`Response` is when somebody answers to a `Poll`.  A response
has a user (the guiy who asked and/or entered the data) and the
partner (the guy who answered).

The virtual table :class:`AnswersByResponse` then combines the answers
which are stored in the database as a set of :class:`AnswerChoices
<AnswerChoice>`, each of which represents a given Choice selected by
the questioned person for a given `Question` of the `Poll`.  If the
Question is *multiple choice*, then there may be more than one
`AnswerChoice` per `Question`.  A `Response` can also contain a set of
`AnswerRemarks`, each of with represents a remark written by the
responding person for a given question.

Model reference
===============


.. class:: Poll
           
    A series of questions.

.. class:: Polls
           
.. class:: AllPolls
           
    Show all polls of all users.


.. class:: Question
    
    A question of a poll.

    .. attribute:: number

       The number of this question within this poll.
       
    .. attribute:: poll

    .. attribute:: title
    .. attribute:: details
    .. attribute:: choiceset
    .. attribute:: multiple_choices
    .. attribute:: is_heading
    .. attribute:: seqno

.. class:: Questions
.. class:: QuestionsByPoll


    
.. class:: ChoiceSet
           
.. class:: ChoiceSets

.. class:: Choice

    .. attribute:: choiceset

.. class:: Choices
.. class:: ChoicesBySet

.. class:: Response           
           
    .. attribute:: poll
    .. attribute:: date
    .. attribute:: state
    .. attribute:: remark
    .. attribute:: partner
                   
    .. attribute:: toggle_choice

       See :class:`ToggleChoice`

.. class:: Responses
.. class:: AllResponses
.. class:: MyResponses
.. class:: ResponsesByPoll
.. class:: ResponsesByPartner

    Show all responses for a given partner.  Default view shows a
    summary of all responses for a that partner using a bullet list
    grouped by poll.

           
.. class:: AnswerChoice
           
    .. attribute:: response
    .. attribute:: question
    .. attribute:: choice
           
.. class:: AnswerRemark
           
    .. attribute:: response
    .. attribute:: question
    .. attribute:: remark

Answers by response
===================

.. class:: AnswersByResponse
           
    The table used for answering to a poll. This is a virtual table
    and its rows are volatile :class:`AnswersByResponseRow` instances.

    .. attribute:: answer_buttons

        A virtual field that displays the currently selected answer(s) for
        this question, eventually (if editing is permitted) together with
        buttons to modify the selection.

          
.. class:: AnswersByResponseRow
           
    Volatile object to represent the one and only answer to a given
    question in a given response.

    Used by :class:`AnswersByResponse` whose rows are instances of
    this.

.. class:: AnswerRemarkField
           
    An editable virtual field.

Answers by question
===================

.. class:: AnswersByQuestion
    
    The rows of this table are volatile :class:`AnswersByQuestionRow`
    instances.


.. class:: AnswersByQuestionRow
           
    Volatile object to represent a row of :class:`AnswersByQuestion`.

.. class:: PollResult
           
    Shows a summay of responses to this poll.



Roles
=====

.. class:: PollsUser
           
    A user who has access to polls functionality.

.. class:: PollsStaff
           
    A user who manages configuration of polls functionality.


.. class:: PollsAdmin


Actions
=======

.. class:: ToggleChoice
           
    Toggle the given choice for the given question in this response.
    
           
Choicelists
===========

.. class:: PollStates
           
    The list of possible states of a :class:`Poll`.

    >>> rt.show(polls.PollStates)
    ======= ======== ======== =============
     value   name     text     Button text
    ------- -------- -------- -------------
     10      draft    Draft
     20      active   Active
     30      closed   Closed
    ======= ======== ======== =============
    <BLANKLINE>
    
.. class:: ResponseStates
           
    The list of possible states of a :class:`Response`.
    
    >>> rt.show(polls.ResponseStates)
    ======= ============ ============ =============
     value   name         text         Button text
    ------- ------------ ------------ -------------
     10      draft        Draft
     20      registered   Registered
    ======= ============ ============ =============
    <BLANKLINE>
    
Example fixtures
================

- :mod:`lino_xl.lib.polls.fixtures.bible`
- :mod:`lino_xl.lib.polls.fixtures.feedback`
- :mod:`lino_xl.lib.polls.fixtures.compass`


Miscellaneous tests
===================

>>> print(settings.SETTINGS_MODULE)
lino_book.projects.polly.settings.demo

>>> pk = 2
>>> obj = polls.Response.objects.get(pk=pk)
>>> print(obj)
Robin Rood's response to Participant feedback

>>> rt.login(obj.user.username).show(polls.AnswersByResponse, obj)
Question 23/10/2014 
<BLANKLINE>
1) There was enough to eat. **1** **2** **3** **4** **5** (**Remark**)
<BLANKLINE>
2) The stewards were nice and attentive. **1** **2** **3** **4** **5** (**Remark**)
<BLANKLINE>
3) The participation fee was worth the money. **1** **2** **3** **4** **5** (**Remark**)
<BLANKLINE>
4) Next time I will participate again. **1** **2** **3** **4** **5** (**Remark**)


>>> mt = contenttypes.ContentType.objects.get_for_model(obj.__class__).id
>>> url = '/api/polls/AnswersByResponse?rp=ext-comp-1351&fmt=json&mt=%d&mk=%d' % (mt, pk)
>>> test_client.force_login(obj.user)
>>> res = test_client.get(url, REMOTE_USER=obj.user.username)


>>> print(res.status_code)
200
>>> d = json.loads(res.content.decode())

>>> len(d['rows'])
5

>>> print(d['rows'][0][0])
<span class="htmlText">1) There was enough to eat.</span>


The "My answer" column for the first row has 5 links:

>>> soup = BeautifulSoup(d['rows'][0][1], 'lxml')
>>> links = soup.find_all('a')
>>> len(links)
5

The first of them displays a "1":

>>> print(links[0].string)
... #doctest: +NORMALIZE_WHITESPACE
1

And clicking on it would run the following Javascript code:

>>> print(links[0].get('href'))
javascript:Lino.polls.Responses.toggle_choice("ext-comp-1351",false,2,{ "fv": [ 9, 17 ] })

The 2 is the id of the Response we are acting on:

>>> polls.Response.objects.get(pk=2)
Response #2 ("Robin Rood's response to Participant feedback")


"fv" stands for "field values". 
It refers to the two `parameters` of the 
:class:`lino.modlib.polls.models.ToggleChoice` action.
The 9 is the id of a `polls.Question`, 
the 17 is the id of a `polls.Choice`.


>>> a = polls.Responses.toggle_choice
>>> len(a.parameters)
2
>>> a.parameters['question']
<django.db.models.fields.related.ForeignKey: question>
>>> a.parameters['choice']
<django.db.models.fields.related.ForeignKey: choice>


>>> polls.Question.objects.get(pk=9)
Question #9 ('1) There was enough to eat.')

>>> polls.Choice.objects.get(pk=17)
Choice #17 ('1')


