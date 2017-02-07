.. _lino.think_python:

============
Think Python
============

When using Lino, you should understand a fundamental design choice of
the Lino framework: we believe that database structure, screen layouts
and business logic should be written *in plain Python*, and not in
some additional text file format like XML, or using a visual GUI
editor.

Yes, this requires you to know Python before you can see a result.

The advantage is better maintainability and reusability.  This choice
is important when it comes to maintaining complex database
applications in a sustainable way.

Rob Galanakis explains a similar opinion in `GeoCities and the Qt
Designer
<http://www.robg3d.com/2014/08/geocities-and-the-qt-designer/>`_:
"We’ve had WYSIWYG editors for the web for about two decades (or
longer?), yet I’ve never run into a professional who works that way. I
think WYSIWYG editors are great for people new to GUI programming or a
GUI framework, or for mock-ups, but it’s much more effective to do
production GUI work through code. Likewise, we’ve had visual
programming systems for even longer, but we’ve not seen one that
produces a result anyone would consider maintainable."

For example, one of Lino's powerful features are :ref:`layouts
<layouts>` whose purpose is to describe an input form programmatically
in the Python language. Compare the :class:`UserDetail` classes
defined in :class:`lino.modlib.users.desktop` and
:class:`lino_noi.lib.users.desktop`.

Imagine a customer 1 who asks you to write an application 1. Then a
second customer asks you to write a similar application, but with a
few changes. You create application 2, using application 1 as
template. One year later customer 1 asks for an upgrade. And during
that year you have been working on application 2. You will have added
new features, fixed bugs, written optimizations... some of these
changes are interesting for customer 1, and they will be grateful if
they get them for free, without having asked for them. (Some other
changes not.)

Thinking in Python is optimal when you are working for a software
house with more than a few customers using different variants of some
application for which you offer long-term maintenance.

Python is a powerful and well-known parser, why should we throw away a
subset of its features by introducing yet another textual description
language?

Or another example: Lino has no package manager because we have pip
and git. We don't need to reinvent them.

Why do other frameworks reinvent these wheels?  Because it enables
them to have non-programmers do the database design, screen layout and
deployment.  Which is a pseudo-advantage.  Lino exists because we
believe that database design, screen layout and deployment should be
done to people who *think in Python*.

This does not exclude usage of templates when meaningful, nor projects
like :ticket:`1053` or features like user-defined views
(:ticket:`848`) because end-users of course sometimes want (and should
have a possibility) to save a given grid layout.

