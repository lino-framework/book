=============
Radio buttons
=============

A **radio button** is a widget used to edit a field that can have a relatively
small number of choices.

There are two types of radio buttons:

- Static radio buttons : the available choices are known at startup and don't
  change within a process.

  Examples : the :attr:`lino.core.model.Model.workflow_buttons` field.

- Dynamic radio buttons : the available choices are stored in the database.

  Examples :
  The  :attr:`lino_xl.lib.tickets.Ticket.assigned_to` field
  (visible e.g. in the :mod:`lino_book.projects.noi1e` demo).
  The  :attr:`lino_xl.lib.polls.AnswersByResponse.answer_buttons` field.
  (visible e.g. in the :mod:`lino_book.projects.polly` demo)
