.. _man:
.. _dev.manuals:

=====================
Manuals for end-users
=====================

The Lino team maintains a series of user manuals targeted at
non-programmers:

- `Lino Noi (en) <http://noi.lino-framework.org>`__
- `Lino Tera (de) <http://de.tera.lino-framework.org>`__
- `Lino Welfare var. Eupen (de) <http://de.welfare.lino-framework.org>`__
- `Lino Welfare var. Châtelet (fr) <http://fr.welfare.lino-framework.org>`__

Every pilot customer with a customized Lino application get their user
manual in the language agreed with the customer.  The quality and
coverage of user manuals is as good as the customer demands and agrees
to pay for.

The source code for these manuals is in a separate repository `manuals
<https://github.com/lino-framework/manuals/>`__.  Each user manual is
a doctree on its own in this repository.

The manuals doctrees are *not in the same repository as the source
code* they talk about because we want to reduce the size of code
repositories.  The production sites of our pilot customers usually
work with a git clone of the source repository, and if these would
contain its docs as well, we would waste quite some disk space.

The manuals doctrees are *gathered into one repository* (and not
maintained in one independant repository per application) because they
use common resources like the `/shared/include/defs.rst
<https://github.com/lino-framework/manuals/blob/master/shared/include/defs.rst>`__
include file.

The manuals doctrees are *not part of the Lino Book repository*
because that repository is already big enough without end-user docs.

