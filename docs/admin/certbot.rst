=====================================
Using Certbot/Let's encript with Lino
=====================================

You activate this using the :option:`getlino configure --https` option.

This option will:

- install `certbot-auto` if needed

- Set up automatic certificate renewal by adding an entry to your
  :file:`/etc/crontab` that will run ``certbot-auto renew`` automatically
