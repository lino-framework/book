.. _book.specs.polls:

The Polls plugin
================

..  doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.polly.settings.demo')
    >>> from lino.api.shell import *

This document describes the :mod:`lino_xl.lib.polls` plugin which
adds database models and functionality for managing polls.


.. currentmodule:: lino_xl.lib.polls

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
    ======= ======== ========
     value   name     text
    ------- -------- --------
     10      draft    Draft
     20      active   Active
     30      closed   Closed
    ======= ======== ========
    <BLANKLINE>
    
.. class:: ResponseStates
           
    The list of possible states of a :class:`Response`.
    
    >>> rt.show(polls.ResponseStates)
    ======= ============ ============
     value   name         text
    ------- ------------ ------------
     10      draft        Draft
     20      registered   Registered
    ======= ============ ============
    <BLANKLINE>
    
Example fixtures
================

- :mod:`lino_xl.lib.polls.fixtures.bible`
- :mod:`lino_xl.lib.polls.fixtures.feedback`
- :mod:`lino_xl.lib.polls.fixtures.compass`
