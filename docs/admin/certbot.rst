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


Miscellaneous
=============

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

Read `the manual
<https://certbot.eff.org/docs/using.html#where-are-my-certificates>`__

The ``certificates`` command displays information about every certificate
managed by certbot::

  $ certbot-auto certificates

How to remove a certbot certificate? E.g. after moving some site to a new server, you
should instruct certbot on the old server to no longer ask for a certificate for
that site. --> Simpli remove all related config files.



Manually configure a new site on your server::

  $ certbot-auto -d www.example.com


You can create certificates that cover multiple domains::

  $ certbot-auto -d one.example.com -d two.example.com
