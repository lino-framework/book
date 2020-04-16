.. _admin.postfix:

===================
Postfix cheat sheet
===================

**Postfix** is a mail transfer agent (MTA). We recommend it over exim4 just because
we have a cheat sheet for it. There have been long debates on what (if any)
should be the default MTA for Debian (`more
<https://wiki.debian.org/Debate/DefaultMTA>`__).

Installing Postfix on Debian is easy::

  $ sudo apt install postfix

This will automatically uninstall exim4.

.. xfile:: /etc/postfix/main.cf

Installing postfix will ask you a few important questions.
See below for explanations about how to answer them.
The configuration is then stored in a file
:xfile:`/etc/postfix/main.cf`, which you can modify afterwards.


Using a relay host for outgoing mail
====================================

"Internet with smarthost"

A **smart host** or **relay host** is a third-party server that accepts outgoing
mails from your server and cares about forwarding them to their final
destination.

Some server providers have a free mail relay host for the virtual machines they
provide.  In that case you simply need to know the name of that host.

If the relay host requires a username and password::

  $ sudo nano /etc/postfix/sasl_passwd
  $ sudo postmap /etc/postfix/sasl_passwd

Or you can register an account for
a third-party SMTP service like Mailgun
and configure your postfix
to use it as smarthost.
`Mailgun <https://www.mailgun.com/smtp/free-smtp-service/free-open-smtp-relay/>`__
gives you 10000 free emails every month.

Or you can configure postfix `without relay host`_ as described hereafter.

Without relay host
===================

To run your own mail server, you need a static IP address and a fully qualified
domain name pointing to it.  There can be only one postfix per IP address. Make
sure that the **Reverse DNS** of your IP address is configured correctly.  While
DNS maps a domain name to an IP address, reverse DNS maps an IP address to a
domain name.  It is a way of publicly declaring that your server at that IP
address is responding to your domain name. The provider of your server is the
owner of the IP address and they usually have a means for you to tell them the
Reverse DNS.

Without a reverse DNS the SMTP servers of your recipients are likely to refuse
to talk with your server.  You will see messages like the following in your
:file:`/var/log/mail.log` file::

  Oct 16 07:06:16 yourhostname postfix/smtp[28516]: 570517A73:
  host mx01.emig.gmx.net[212.227.17.5] refused to talk to me:
  554-gmx.net (mxgmx116) Nemesis ESMTP Service not available
  554-No SMTP service 554-Bad DNS PTR resource record.
  554 For explanation visit http://postmaster.gmx.com/en/error-messages?ip=167.114.229.225&c=rdns

Here is our suggestion for your :xfile:`/etc/postfix/main.cf` file::

  myhostname = mail.myname.org
  myorigin = /etc/mailname
  mydestination = $myhostname localhost.$mydomain localhost $mydomain
  relayhost =
  mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
  mynetworks_style = host
  relay_domains =
  inet_interfaces = all


Here is what status should say::

  $ sudo service postfix status
  ● postfix.service - Postfix Mail Transport Agent
     Loaded: loaded (/lib/systemd/system/postfix.service; enabled; vendor preset: enabled)
     Active: active (exited) since Thu 2019-12-12 12:01:59 UTC; 7s ago
    Process: 2262 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
   Main PID: 2262 (code=exited, status=0/SUCCESS)

  Dec 12 12:01:59 my-host-name systemd[1]: Starting Postfix Mail Transport Agent...
  Dec 12 12:01:59 my-host-name systemd[1]: Started Postfix Mail Transport Agent.


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
