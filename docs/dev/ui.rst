.. _dev.ui:

============================
Elements of a user interface
============================

In :doc:`/about/ui` we say that Lino separates business logic and user
interface.  That's a noble goal, but the question is *where exactly*
you are going to separate.  The actual challenge is the API between
them.

Lino has a rather high-level API because we target a rather wide range
of possible interfaces.  That API is still evolving and not yet very
well documented, but the basics seem to have stabilized.  Some general
elements of every Lino user interface are:

- the **main menu** : a hierarchical representation of the
  application's functions.  In multi-user applications the main menu
  changes depending on the user permissions.

- a highly customizable **grid widget** for rendering tabular data in
  an editable way.  This description is used for **

- form input using **detail windows** which can contain slave tables,
  custom panels, ...

- Context-sensitive ComboBoxes with dynamic data store.

- Keyboard navigation for areas are where manual data entry is needed.

- WYSIWYG rich text editor

- Support for multi-lingual database content

- Unlike some desktop applications Lino does *not* reimplement an
  internal method to open several windows: users simply open several
  browser windows.


