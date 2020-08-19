.. _admin.mailman:

=============
Using Mailman
=============

**Mailman** is a mailing lists manager, an optional component on a :doc:`mail
server <mail>`.

Mailman 3 is in active developement, and --like Lino-- uses Django for its web
interface.  The Mailman web interface consists of two Django apps, Postorious
(lists management) and Hyperkitty (list archives), which may be used separately,
or integrated into another Django project together with custom apps, or,
--probably the most frequent use case-- are combined into a Django project
called the "Mailman Suite".  This is what we are going to install here.

We don't plan to use one mailman3 site for multiple domains. So the classical
Debian config file structure should be used.

Should we use the packaged version by saying :cmd:`sudo apt install
mainman3-full`? It seems that we prefer to use selected clones of the official
git repository in order to be able to easily switch between versions. Though we
didn't yet fully explore the package approach (see :blogref:`20200813`).


Configure postfix
=================

We assume that you have already installed and configured postfix
(:doc:`postfix`) and that your basic email system is working.

Get the sources
===============




Tips and tricks
===============

Add a new member on the command line

$ sudo add_members -r recipients.txt test



Sources
=======

- https://wiki.list.org/DOC/Howto_Install_Mailman3_On_Debian10
- https://gist.github.com/plepe/dab22fdbfec63d8632709065890124a3
