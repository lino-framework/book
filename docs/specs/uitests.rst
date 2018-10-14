========
UI tests
========

- runserver in :mod:`lino_book.projects.adg`.

Test whether row-level edit lock works:

- Open My clients. In grid mode there should be no button "Unlock" or
  "Edit" in the toolbar.
  
- Create a client. Click "Edit". Change the reference field.  Do not
  submit.
- In another browser log in as another user.  Start editing
  the same client.  In detail window Lino should say that it is locked
  by another user.  In grid edit, change the language field.
- Now submit your new reference field in the first browser.
- Note that the language put from grid has been lost.
