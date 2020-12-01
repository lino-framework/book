.. _admin.mailman:

=============
Using Mailman
=============

**Mailman** is a mailing lists manager, an optional component on a :doc:`mail
server <index>`.

Mailman 3 is in active developement, and --like Lino-- uses Django for its web
interface.  The Mailman web interface consists of two Django apps, Postorious
(lists management) and Hyperkitty (list archives), which may be used separately,
or integrated into another Django project together with custom apps, or,
--probably the most frequent use case-- are combined into a Django project
called the "Mailman Suite".  This is what we are going to install here.

Should we use the packaged version by saying :cmd:`sudo apt install
mainman3-full`? It seems that we prefer to use selected clones of the official
git repository in order to be able to easily switch between versions. Though we
didn't yet fully explore the package approach (see :blogref:`20200813`).

The following is not finished.

We assume that you have already installed and configured postfix
(:doc:`postfix`) and that your basic email system is working.

Get the sources
===============

The mailman suite is like any other Lino site, except that the
:xfile:`settings.py` file is copied from
https://gitlab.com/mailman/mailman-suite.

We assume that the :term:`master environment` is installed (see
:ref:`lino.admin.install`).

Draft installation instructions with getlino::

  $ sudo env PATH=$PATH getlino startsite --db-engine=postgresql std lists

Manually install mailman repository::

  $ go mailman
  $ a
  $ mkdir env/repositories
  $ cd $_
  $ git clone https://gitlab.com/mailman/mailman.git
  $ pip install -e mailman/
  $ go mailman

Download config files from https://gitlab.com/mailman/mailman-suite::

  $ mv settings.py local_settings.py
  $ wget https://gitlab.com/mailman/mailman-suite/-/raw/master/mailman-suite_project/settings.py
  $ wget https://gitlab.com/mailman/mailman-suite/-/raw/master/mailman-suite_project/urls.py

Install Python wrappers for using memcached and the Whoosh backend for
HyperKitty archive search::

  $ pip install pylibmc Whoosh







Tips and tricks
===============

Add a new member on the command line

$ sudo add_members -r recipients.txt test



Troubleshooting
===============

The following simulates quite closely what mailman does when sending its mails.

::

  $ sudo apt install sendemail
  $ dig gmx.net MX
  $ sendemail -f mylist@abc.org -t myrcpt@gmx.net -u test -m test -s mail.ghi.org:25 -v -o tls=no

Sources
=======

- https://wiki.list.org/DOC/Howto_Install_Mailman3_On_Debian10
- https://gist.github.com/plepe/dab22fdbfec63d8632709065890124a3
