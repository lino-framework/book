.. _hosting.certbot:

=====================================
Using Certbot/Let's encrypt with Lino
=====================================

`What's Certbot? <https://certbot.eff.org/about/>`__

The recommended way to activate Certbot on a :term:`Lino server` is by using the
``--https`` option of :ref:`getlino configure <getlino>`.

This option will:

- install `certbot` or `certbot-auto` (unless one of them is already installed)

- add an entry to your :file:`/etc/crontab` that will run :cmd:`certbot-auto
  renew` automatically every 12 hours.

On a Lino server with ``--https`` option, ``getlino startsite`` will
automatically do the following.

- create the nginx config file in :file:`/etc/nginx/sites-available`
- enable the site by linking it to :file:`/etc/nginx/sites-enabled`
- restart the nginx service
- run :cmd:`certbot-auto` to register the new site at certbot as being served on this
  server.

Read the docs:

- https://certbot.eff.org/docs/using.html
- https://certbot.eff.org/lets-encrypt/debianbuster-nginx


.. highlight:: console

Troubleshooting
===============

Here are some hints for playing around manually when something doesn't work as
expected.

You can run :cmd:`certbot-auto` at any moment in interactive mode::

  $ certbot-auto
  Requesting to rerun /usr/local/bin/certbot-auto with root privileges...
  Saving debug log to /var/log/letsencrypt/letsencrypt.log
  Plugins selected: Authenticator nginx, Installer nginx

  Which names would you like to activate HTTPS for?
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  1: example.com
  2: lists.example.com
  3: www.example.com
  4: emil.example.com
  5: jane.example.com
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  Select the appropriate numbers separated by commas and/or spaces, or leave input
  blank to select all options shown (Enter 'c' to cancel): c

The ``certificates`` command displays information about every certificate
managed by certbot::

  $ certbot-auto certificates

How to remove a certbot certificate? E.g. after moving some site to a new
server, you should instruct certbot on the old server to no longer ask for a
certificate for that site::

  $ certbot delete --certname www.example.com-0001

How to manually add a certificate for a new site on your server::

  $ certbot-auto -d www.example.com


You can create certificates that cover multiple domains::

  $ certbot-auto -d one.example.com -d two.example.com

How to install certbot using the Debian package::

  $ sudo apt-get install certbot python-certbot-nginx
  Reading package lists... Done
  Building dependency tree
  Reading state information... Done
  certbot is already the newest version (0.31.0-1).
  python-certbot-nginx is already the newest version (0.31.0-1).
  0 upgraded, 0 newly installed, 0 to remove and 124 not upgraded.


Messy certificates
==================

There are different ways to mess up certificates.  For example you can have a
certificate that covers a domain which is already covered by another
certificate.

How to see all certificates that cover a given domain?

::

  $ certbot-auto certificates | grep mydomain.org

How to see all enabled sites and the certificate they use::

  $ cd /etc/nginx/sites-enabled
  $ grep ssl_certificate_key *

How to set the email address used by the ACME server for sending notifications::

  $ certbot-auto update_account --email postmaster@mydomain.org


You can simply delete a certificate::

  $ certbot-auto delete --cert-name team.new.lino-framework.org
  Requesting to rerun /usr/local/bin/certbot-auto with root privileges...
  Saving debug log to /var/log/letsencrypt/letsencrypt.log

  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  Deleted all files relating to certificate team.new.lino-framework.org.
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  (master) luc@lf:/usr/bin$


One certificate covering many domains
=====================================

On LF we have a lot of subdomains (but no wildcard certificate). Here is how to
maintain the list of domains for a given certificate in a separate file.

Let's say you have a certificate named ``example.com``, and you have a lot of
subdomains that you want to cover using that same certificate.

Create a file named :file:`~/domains.txt` with one line per domain, each line
starts with `-d`::

  -d example.com
  -d www.example.com
  -d sub1.example.com
  ...
  -d sub9.example.com

You can now update this file at any moment and then run the following to updated
your certificate::

  $ xargs -a ~/domains.txt certbot-auto certonly --cert-name example.com
