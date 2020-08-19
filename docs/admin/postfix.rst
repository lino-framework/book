.. _admin.postfix:

===================
Postfix cheat sheet
===================

**Postfix** is a mail transfer agent (MTA), one of the components on a
:doc:`mail server <mail>`.

We prefer postfix over exim4 just because we have a cheat sheet for it. There
have been long debates on what (if any) should be the default MTA for a Debian
system (`more <https://wiki.debian.org/Debate/DefaultMTA>`__).


Installation
============

Installing Postfix on Debian is easy and will automatically uninstall exim4::

  $ sudo apt install libsasl2-modules postfix

The configuration is less easy. Installing postfix will start by asking you to
select the *configuration type*. Choose "Internet site".

It will then ask for your "mail name", this is the fully qualified domain name
of your server, without any special subdomain, i.e. just the name after the
``@`` of the email addresses for which you want to manage mails.

Your answers are stored in a file :xfile:`/etc/postfix/main.cf`, which you will
probably continue to modify afterwards (see below).

There is another config file, :xfile:`/etc/postfix/master.cf`. You should
activate (uncomment) the ``smtps`` line in this file if you plan to use an ssh
certificate.

The ``main.cf`` configuration file
==================================

.. xfile:: /etc/postfix/main.cf

This is the main configuration file for postfix. See the `postfix documentation
<http://www.postfix.org/postconf.5.html>`__ about the syntax and meaning of the
parameters in this file. Summary of the most common ones:

- relayhost : Empty when this server speaks directly to the smtp servers of the
  recipients. Otherwise the name of a relay host.  See `Using a relay host`_.

- relay_domains :

- mydomain : ``example.com`` (the "mail name" you specified during configuration)

- myhostname : ``mail.$mydomain`` (the FQDN of the mail server, which in our case
  points to the same machine as the one where our web server is running)

- myorigin
- mydestination

Using a relay host
==================

Set the name of the relay host in the ``relayhost`` parameter::

  relayhost = relay.ovh.com

If the relay host requires a username and password::

  $ sudo nano /etc/postfix/sasl_passwd
  $ sudo postmap /etc/postfix/sasl_passwd

Here is our suggestion for your :xfile:`/etc/postfix/main.cf` file::

  myhostname = mail.example.com
  myorigin = /etc/mailname
  mydestination = $myhostname localhost.$mydomain localhost $mydomain
  relayhost =  # where to send all outgoing mail
  mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
  mynetworks_style = host
  relay_domains =  # fqdn for which you accept incoming mail
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

Diagnostic tips and tricks
==========================

How to see which version of postfix is running::

  $ sudo postconf mail_version
  mail_version = 3.4.10

To quickly see the value of a given parameter, type::

  $ sudo postconf mydomain

To see a list of all parameters and their values::

  $ sudo postconf | grep mydomain

Send a simple mail for testing the mail system::

  $ mail -s "some test" joe@example.com mike@example.com


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


Common problems when running your own mail server
=================================================

:message:`550 Email blocked` means that the recipient's mail server refuses to
accept an incoming mail because the sender's mail server is blacklisted.

To see whether your server is blacklisted, you can ask
http://multirbl.valli.org/lookup/

For some nice examples of why blacklisting is needed, see  `bobcares.com
<https://bobcares.com/blog/550-email-blocked/>`__.
