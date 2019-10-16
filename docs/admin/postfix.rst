.. _admin.postfix:

===================
Postfix cheat sheet
===================

Postfix is a mail transfer agent (MTA). We recommend it over exim4 (which is the Debian favourite)

Installing Postfix is easy::

  $ sudo apt install postfix

This will automatically uninstall exim4.

You need to understand how to answer the installation options.

Using a relay host for outgoing mail
====================================

A **smart host** or **relay host** is a third-party server that accepts outgoing
mails from your server and cares about forwarding them to their final
destination.

Some server providers have a free mail relay host for the virtual machines they
provide.  In that case you simply need to know the name of that host.

Otherwise you can register an account for
a third-party SMTP service like Mailgun
and configure your postfix
to use it as smarthost.
`Mailgun <https://www.mailgun.com/smtp/free-smtp-service/free-open-smtp-relay/>`__
gives you 10000 free emails every month.


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
