=====================================
Using the Postfix mail transfer agent
=====================================

Installing Postfix is easy::

  $ sudo apt install postfix

But you need to understand how to answer the installation options.

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
