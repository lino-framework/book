=====================================
Using Certbot/Let's encript with Lino
=====================================

You activate this using the :option:`getlino configure --https` option.

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
      listen [::]:443 ssl; # managed by Certbot
      listen 443 ssl; # managed by Certbot
      include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
      ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
      ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem; # managed by Certbot
      ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem; # managed by Certbot
  }
  server {
      if ($host = newsite.example.com) {
          return 301 https://$host$request_uri;
      } # managed by Certbot
      server_name timtools.lino-framework.org;
      listen 80;
      listen [::]:80;
      return 404; # managed by Certbot
  }

Then enable the site::

  $ cd /etc/nginx
  $ sudo ln sites-available/newsite-example-com.conf sites-enabled/
  $ sudo service nginx restart

Finally run certbot::

  $ certbot-auto

This last step will register the new site at certbot as being served on this
server.
