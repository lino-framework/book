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

Don't mix up notifications with "system notes" (implemented by
:mod:`lino_xl.lib.notes`).  These are fundamentally different beasts
which partly resemble each other.  For example both types of messages
have a "subject" and a "body".  Both describe some event that happens
to some database object.  But while *notifications* are messages to be
quickly sent to their recipients, *system notes* are permanent
historic entries visible to every user (who has the required
permission).

A :class:`NotifyingAction` is a dialog action which potentially sends
a notification.  It has three dialog fields ("subject", "body" and a
checkbox "silent").  You can have non-dialog actions (or actions with
some other dialog than a simple subject and body) which build a custom
subject and body and emit a notification.  If the emitting object also
has a method :meth:`emit_system_note`, then this is being called as
well.

Notification messages
=====================

.. class:: Message

    A **Notification message** is an instant message sent by the
    application to a given user.

    Applications can either use it indirectly by sublassing
    :class:`ChangeObservable
    <lino.modlib.notify.mixins.ChangeObservable>` or by directly
    calling the class method :meth:`create_message` to create a new
    message.


    .. attribute:: subject
    .. attribute:: body
    .. attribute:: user

        The recipient.

    .. attribute:: owner
 
       The database object which controls this message. 

       This may be `None`, which means that the message has no
       controller. When a notification is controlled, then the
       recipient will receive only the first message for that object.
       Any following message is ignored until the recipient has
       "confirmed" the first message. Typical use case are the
       messages emitted by :class:`ChangeObservable`: you don't want
       to get 10 mails just because a colleague makes 10 small
       modifications when authoring the text field of a
       ChangeObservable object.

    .. attribute:: created
    .. attribute:: sent
    .. attribute:: seen

    .. method:: emit_notification(cls, ar, owner, message_type,
                msg_func, recipients)

        Class method which creates one database object per recipient.

        `recipients` is an iterable of `(user, mail_mode)` tuples.
        Duplicate items, items with user being None and items having
        :attr:`lino.modlib.users.User.mail_mode` set to
        :attr:`lino.modlib.users.MailModes.silent` are removed.

        `msg_func` is a callable expected to return a tuple `(subject,
        body)`. It is called for each recipient in the recipient's
        language.

        The emitting user does not get notified, except when working
        as another user or when notify_myself is set.
           
    .. method:: create_message(cls, user, owner=None, **kwargs)
               
        Create a message unless that user has already been notified
        about that object.

    .. method:: send_summary_emails(cls, mm)

        Send summary emails for all pending notifications with the
        given mail_mode `mm`.

    .. method:: send_browser_message_for_all_users(self, user)
                
        Send_message to all connected users
        
    .. method:: send_browser_message(self, user)
                
        Send_message to the user's browser


.. class:: Messages
           
    Base for all tables of messages.

.. class:: AllMessages(Messages)
           
    The gobal list of all messages.

.. class:: MyMessages(Messages)
           
    Shows messages emitted to me.


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
by a given user.


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


.. class:: Plugin

    .. attribute:: remove_after
    

Utility functions
=================

.. function:: send_pending_emails_often()
.. function:: send_pending_emails_daily()
    

    
