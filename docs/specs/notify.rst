.. _book.specs.notify:

==========================
The notification framework
==========================

.. to test only this document:
   
    $ python setup.py test -s tests.SpecsTests.test_notify
   
    doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.chatter.settings.demo')
    >>> from lino.api.shell import *
    >>> from pprint import pprint

The :mod:`lino.modlib.notify` plugin adds a notification framework to
your Lino application.

A **notification message** is a message sent by the application to a
system user.

If :attr:`lino.core.site.Site.use_websockets` is `True` and the user
is online, then he will see it as a desktop notification.

Unseen notfication messages are displayed by the `MyMessages` table
which is usually part of the dashboard in admin main view. This table
also provides an action for marking a message as seen.

In addition, notification messages are sent via email to the user
according to his :attr:`mail_mode` field.

The emitter of a notification message is currently not stored. That
is, you cannot currently request to see a list of all messages emitted
by your system activity.


Emitting notifications
======================

Notification messages are emitted by the application code.

The easiest way for doing this is by having a model inherit from
:class:`lino.modlib.notify.mixins.ChangeObservable`.

Application programmers need to understand the different meanings of
"subject" and "body":

- The body is expected to be a
  self-sufficient and complete description of the event.
  If a message has a *body*, then the *subject* is **not** being displayed
  in the MyMessages summary.

- The subject might contain limited rich text (text formatting, links)
  but be aware that this formatting gets lost when the message is sent
  as an email.

   


Local configuration
===================

    
>>> from django.conf import settings
>>> pprint(settings.CHANNEL_LAYERS)
{'default': {'BACKEND': 'asgiref.inmemory.ChannelLayer',
             'ROUTING': 'lino.modlib.notify.routing.channel_routing'}}


>>> settings.SITE.use_websockets
True

How to configure locally on a production site::

    SITE = Site(...)
    CHANNEL_LAYERS['default']['BACKEND'] = 'asgi_redis.RedisChannelLayer'
    CHANNEL_LAYERS['default']['CONFIG'] = {
    'hosts': [('localhost', 6379)],
    }
