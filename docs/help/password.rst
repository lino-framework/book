===========================
How to change your password
===========================

We assume that you are signed in.

- Click the :guilabel:`[My settings]` link in the quick links of the
  main window or select :guilabel:`My settings` from the user menu
  (the menu that opens when you click your name in the upper right
  corner). Lino will show the detail page of your record in the
  :class:`lino.modlib.users.Users` table.

- Click the :guilabel:`✱` button in the toolbar. Lino opens the dialog
  window of the :class:`ChangePassword
  <lino.modlib.users.ChangePassword>` action

  .. image:: ChangePassword.png
      :scale: 50%
                   
- Fill in the three fields and confirm the dialog window.  Voilà!

  
Notes:

- Changing your password does not cause your session to sign out. You
  will need your new password only when Lino asks you to sign in
  again.  Depending on the site's configuration that might happen only
  when you signed out explicitly.

- System administrators can invkoke that action on any user, and they
  can leave the :guilabel:`Current password` field empty.
