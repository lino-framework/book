======================
Writing custom actions
======================

A custom action is an action written by the application or plugin
developer.

.. _dialog_actions:

Dialog actions
==============

When you specify `parameters` on a custom action, then your action
becomes a "dialog action". When a user invokes a dialog action, Lino
opens a dialog window which asks for the values of these
parameters. The action itself is being run only when the user submits
the dialog window.

Examples of dialog actions:

- users.Users.change_password

  
- pcsw.Clients.refuse_client
- countries.Places.merge_row
- contacts.Persons.create_household  
- coachings.Coachings.create_visit
- cal.Guests.checkin
- lino_xl.lib.sales.VatProductInvoice.make_copy MakeCopy

