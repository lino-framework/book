.. _dev.querysets:

==========================
Customizing your querysets
==========================

Lino has a complex set of hooks for customizing Django querysets.

- `Model.get_request_queryset(self, ar, **filter)`:
  Used to add `select_related()`.
  Calls `Model.get_user_queryset()`.

- `Model.get_user_queryset(self, user, **filter)`: used for user level row
  filtering. The default implementation doesn't filter anything. Customized
  examples :class:`lino.modlib.comments.Comment`,
  :class:`lino_xl.lib.tickets.Site` and
  :class:`lino_xl.lib.tickets.Ticket`.

- `Actor.get_queryset(self, ar)`:

- `DbTable.get_queryset(self, ar)`:
  default implementation calls `self.model.get_request_queryset(ar, **filter)`

- `DbTable.get_request_queryset(self, ar, **filter)`: used to define how filter parameters of the actor should influence the queryset.

- `Actor.get_request_queryset(self, ar)`: used to define how filter parameters of the actor should influence the queryset.
