.. _dev.ui:

============================
Elements of a user interface
============================

In :doc:`/about/ui` we say that Lino separates business logic and user
interface.

It is not enough to say that you want to separate "business logic" and
"user interface". The question is *where exactly* you are going to
separate.  The actual challenge is the API between them.

Lino has a rather high-level API because we target a rather wide range
of possible interfaces.

That API is still evolving and not yet very well documented, but the
basics seem to have stabilized.  Some general elements of every Lino
user interface are:

- the main menu : a hierarchical representation of the 
  application's functions. 
  In multi-user applications the main menu heavily changes 
  depending on the user profile.

- sophistacated grids to display tabular data

- Tabbed form input for detail windows.

- ComboBoxes with dynamic data store.

- Context-sensitive ComboBoxes.

- Keyboard navigation for areas are where manual data entry is needed.

- WYSIWYG rich text editor

- Support for multi-lingual database content

- Unlike some desktop applications Lino does *not* reimplement an
  internal method to open several windows: users simply open several
  browser windows.


TODO: Answer to comments in `this discussion on twitter
<https://twitter.com/LucSaffre/status/716809890489049088>`_ where
Christophe asks "il ne suffit pas juste d'un format d'échange
clairement spécifié?"  and SISalp comments "On ne parle pas de la même
chose. Dans Flask + Tryton, l'application Flask fait "import trytond"
et ça change tout.  See also :ref:`tryton`.
