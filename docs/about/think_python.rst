.. _lino.think_python:

============
Think Python
============

When using Lino, you should understand a fundamental design choice of
the Lino framework: we believe that database structure, screen layouts
and business logic should be written in *Python*, not via a graphical
user interface.

Yes, this requires you to know Python before you can see a result.

The advantage is better maintainability and reusability.  We don't
believe that a visual GUI editor is a good thing when it comes to
maintaining complex database applications in a sustainable way. Rob
Galanakis explains a similar opinion in `GeoCities and the Qt Designer
<http://www.robg3d.com/2014/08/geocities-and-the-qt-designer/>`_

For example, one of Lino's powerful features are :ref:`layouts
<layouts>` whose purpose is to describe user interfaces
programmatically in the Python language.  Python is a powerful and
well-known parser, why should we throw away a subset of its features
by introducing yet another textual description language?

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

