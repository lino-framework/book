==========================
Deploying Django channels
==========================

If you plan to activate desktop notifications using `Django Channels
<https://channels.readthedocs.io/en/stable/>`__, you need to need to go through the next steps

Install and activate
======================

Django channels requires to install the channels package using the following command::

    $ pip install -U channels
    $ sudo apt-get -y install redis-server

And activate it for your site by setting use_websockets to True.

Deploy
=======

The above commands are enough to get your desktop notifications works fine in development mode. But
for the production server things get more complicated.

In this document, I will use asgi_redis as the redis backend and apache is our webserver.

Three configurations should be done.
- Setup worker servers
- Setup interface servers
- Update Apache configuration

Worker Servers
==============

To run a worker server, just run ::

    python manage.py runworker

You should place this inside an init system or something like supervisord to ensure it is re-run
if it exits unexpectedly.

An example for a supervisord could be::

    [program:my_runworker]
    command=/path/to/my/script/runworker.sh
    user = www-data
    umask = 002

With runworker.sh like the following::

    #!/bin/bash
    set -e  # exit on error
    . /path/to/my/env/bin/activate
    exec python /path/to/manage.py runworker  -v2

Interface servers
=================

Django channels is shipped with Daphne as interface servers. But first
we need to create an asgi module in your project file::

    import os
    from channels.asgi import get_channel_layer

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my.settings")

    channel_layer = get_channel_layer()

Now we can run the server::

    daphne my.asgi:channel_layer

If everything goes right, the interface server should start running!

As runworker, Daphne should also be configured with a supervisord. Here an example for daphne.sh ::

    #!/bin/bash
    set -e  # exit on error
    . /path/to/my/env/bin/activate
    exec daphne -b localhost -p 8080 asgi:channel_layer

I have used 8080 as the port of daphne , we will use this port in apache configuration.
And for supervisord config::

    [program:daphne_jane]
    directory=/path/to/script/
    command=/path/to/script/daphne.sh
    user = www-data
    umask = 002

If everything is okay, we need to restart supervisord and our Worker
Servers and Interface servers should be running.

Apache configuration
====================

Finally here’s the apache conf that we need to add. Please note that
we should redirect all our websocket incoming requests to the daphne
server and keep the other requests to get handled by our usual wsgi
module.::

    RewriteEngine on
    RewriteCond %{HTTP:UPGRADE} ^WebSocket$ [NC,OR]
    RewriteCond %{HTTP:CONNECTION} ^Upgrade$ [NC]
    RewriteRule .* ws://127.0.0.1:8080%{REQUEST_URI} [P,QSA,L]

Note that this config used be used for regardless the http protocol
used, http or https.  If the mod_rewrite is not activated for your
apache server, you could activate is using the following command::

    a2enmod rewrite

And then a apache restart is required to load the new apache
configuration.

Don't forget to set your :attr:`use_websockets
<lino.core.site.Site.use_websockets>` to True in your
:xfile:`settings.py`::

    use_websockets = True

And then you should also run::

    $ python manage.py collectstatic
