=====================================
Using the Postfix mail transfer agent
=====================================

Installing Postfix is easy::

  $ sudo apt install postfix

But you need to understand how to answer the installation options.

Without relay host
===================

Make sure that the Reverse DNS is configured. The provider of your server is the
owner of the IP address and they usually have a means for you to tell them that
your server at that IP address is responding to your domain name.

Otherwise the SMTP servers of your recipients are likely to refuse to talk with
you.  You will see messages like the following in your
:file:`/var/log/mail.log` file::

  Oct 16 07:06:16 yourhostname postfix/smtp[28516]: 570517A73:
  host mx01.emig.gmx.net[212.227.17.5] refused to talk to me:
  554-gmx.net (mxgmx116) Nemesis ESMTP Service not available
  554-No SMTP service 554-Bad DNS PTR resource record.
  554 For explanation visit http://postmaster.gmx.com/en/error-messages?ip=167.114.229.225&c=rdns


With relay host
===============

A **smart host** or **relay host** is a third-party server that accepts outgoing
mails from your server and cares about forwarding them to their final
destination.

Using a relay host for outgoing mail
====================================

Some server providers provide a free mail relay host for the virtual machines
they provide.  In that case you simply need to know the name of that host.

Please also read
https://www.mailgun.com/smtp/free-smtp-service/free-open-smtp-relay/

Register an account for on mailgun and configure your postfix with mailgun as
smarthost.

The web interface for mailman is less urgent
than the lists themselves, so please start with postfix. You can send mails to
test@LF for testing (this list contains only me at the moment ("sudo
list_members test"). Try to add yourself using the mm command-line interface)




Inspect the mail queue
======================

Display a list of queued mail (deferred and pending)::

  $ mailq

Display the content of queued mail::

  $ sudo postcat -vq <QueueID>

Display the mail log::

  $ sudo less /var/log/mail.log

Delete all queued mail::

  $ sudo postsuper -d ALL

Delete deferred mail queue messages::

  $ sudo postsuper -d ALL deferred
