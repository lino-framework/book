=====================================
Using Certbot/Let's encript with Lino
=====================================

You activate this using the ``--https`` option of :ref:`getlino configure
<getlino>`.

This option will:

- install `certbot-auto` if needed

- Set up automatic certificate renewal by adding an entry to your
  :file:`/etc/crontab` that will run ``certbot-auto renew`` automatically

How to define a new vhost on your nginx server (no warranties)::

  $ cd /etc/nginx/sites-available
  $ sudo cp existingsite.conf newsite.conf
  $ sudo nano newsite.conf  # edit as needed

Here is how a simple nginx conf for a static website looks like::

  server {
         server_name newsite.example.com;
         root /var/www/public_html/newsite;
         index index.html;
         location / {
                 try_files $uri $uri/ =404;
         }
  }

Then enable the site::

  $ cd /etc/nginx
  $ sudo ln sites-available/newsite-example-com.conf sites-enabled/
  $ sudo service nginx restart

Finally run certbot::

  $ certbot-auto

This last step will register the new site at certbot as being served on this
server.
