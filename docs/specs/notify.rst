.. _book.specs.notify:

=============
Notifications
=============

.. to test only this document:
   
    $ python setup.py test -s tests.SpecsTests.test_notify
   
    doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.max.settings.demo')
    >>> from lino.api.shell import *
    >>> from pprint import pprint

    
>>> from django.conf import settings
>>> pprint(settings.CHANNEL_LAYERS)
{'default': {'BACKEND': 'asgiref.inmemory.ChannelLayer',
             'ROUTING': 'lino.modlib.notify.routing.channel_routing'}}


How to configure locally::

    SITE = Site(...)
    CHANNEL_LAYERS['default']['BACKEND'] = 'asgi_redis.RedisChannelLayer'
    CHANNEL_LAYERS['default']['CONFIG'] = {
    'hosts': [('localhost', 6379)],
    }
