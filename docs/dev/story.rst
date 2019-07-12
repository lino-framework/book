.. doctest docs/dev/story.rst
.. _dev.story:

=======
Stories
=======

A story is an iterable of things that can be rendered.  Each item or "chunk" of
a story is one of the following:

- a table or other actor (a subclass of :class:`lino.core.actors.ACtor`)
- an action request on a table or other actor (an instance of :class:`lino.core.tablerequest.TableRequest`)
- an etree element (:doc:`etree`)
- a dashboard item (an instance of :class:`lino.core.dashboard.DashboardItem`)

:class:`lino.core.renderer.Render` has a method :meth:`show_story
<lino.core.renderer.Render.show_story>` which "renders" a story.  Different
renderer subclasses render stories (and tables and other things) differently.

The base class does the actual work of looping over the story and deciding how
to render it.  It returns an HTML elementtree ``DIV`` element.

TextRenderer does almost the same, but prints everything to stdout.  This is
used in doctests where we don't want to worry about implementation details.