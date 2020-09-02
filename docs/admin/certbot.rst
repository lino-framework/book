.. _hosting.certbot:

=====================================
Using Certbot/Let's encrypt with Lino
=====================================

You activate this using the ``--https`` option of :ref:`getlino configure
<getlino>`.

This option will:

- install `certbot-auto` if needed

- Set up automatic certificate renewal by adding an entry to your
  :file:`/etc/crontab` that will run :cmd:`certbot-auto renew` automatically

On a Lino server with ``--https`` option, ``getlino startsite`` will
automatically do the following.

- create the nginx config file in :file:`/etc/nginx/sites-available`
- enable the site by linking it to :file:`/etc/nginx/sites-enabled`
- restart the nginx service
- run certbot-auto to register the new site at certbot as being served on this
  server.


Read the docs:

- https://certbot.eff.org/docs/using.html
- https://certbot.eff.org/lets-encrypt/debianbuster-nginx



Playing around manually
=======================

You can always run :cmd:`certbot-auto`::

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

How to remove a certbot certificate? E.g. after moving some site to a new server, you
should instruct certbot on the old server to no longer ask for a certificate for
that site. --> Simply remove all related config files.

Manually configure a new site on your server::

  $ certbot-auto -d www.example.com


You can create certificates that cover multiple domains::

  $ certbot-auto -d one.example.com -d two.example.com



::

  $ sudo apt-get install certbot python-certbot-nginx
  Reading package lists... Done
  Building dependency tree
  Reading state information... Done
  certbot is already the newest version (0.31.0-1).
  python-certbot-nginx is already the newest version (0.31.0-1).
  0 upgraded, 0 newly installed, 0 to remove and 124 not upgraded.

"A messy certificate is a certificate that covers a domain which is already
covered by another certificate."

How to find messy certificates?



Delete it::

  $ certbot-auto delete --cert-name team.new.lino-framework.org
  Requesting to rerun /usr/local/bin/certbot-auto with root privileges...
  Saving debug log to /var/log/letsencrypt/letsencrypt.log

  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  Deleted all files relating to certificate team.new.lino-framework.org.
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  (master) luc@lf:/usr/bin$


How to see all certificates that cover a given domain?

  TODO


How to see all enabled sites and the certificate they use::

  $ cd /etc/nginx/sites-enabled
  $ grep ssl_certificate_key *


Maintaining the list of domains in a separate file
==================================================

How to maintain the list of domains in a separate file.  Let's say you have a
certificate named ``example.com``, and you have a lot of subdomains that you
want to cover using that same certificate.

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
