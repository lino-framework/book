.. doctest docs/specs/notify.rst
.. _book.specs.notify:

==================================
``notify``: Notification framework
==================================

.. currentmodule:: lino.modlib.notify

The :mod:`lino.modlib.notify` plugin adds a notification framework to your Lino
application.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst
   
>>> import lino
>>> lino.startup('lino_book.projects.chatter.settings.demo')
>>> from lino.api.shell import *
>>> from pprint import pprint

Overview
========

A **notification message** is a message sent by the application to a
user of the site.

Lino sends notifications as `Desktop notifications`_ and/or by email
depending on the user preferences of the recipient.
In addition, notification messages are sent via email to the user
according to his :attr:`mail_mode` field.

Don't mix up notifications with "system notes" (implemented by
:mod:`lino_xl.lib.notes`).  These are fundamentally different beasts
which partly resemble each other.  For example both types of messages
have a "subject" and a "body".  Both describe some event that happens
to some database object.  But while *notifications* are messages to be
quickly sent to their recipients, *system notes* are permanent
historic entries visible to every user (who has the required
permission).


The emitter of a notification message is currently not stored. That
is, you cannot currently request to see a list of all messages emitted
by a given user.

Notification messages are emitted by the application code

- Either manually by calling the class method
  :meth:`Message.create_message` to create a new message.

- Have your models inherit from :class:`ChangeNotifier`.

- Add actions that inherit from :class:`NotifyingAction`.



Desktop notifications
=====================

To enable desktop notifications, there are some requirements:

- :attr:`lino.core.site.Site.use_websockets` must be `True`
- notifications must be properly installed on the server
  
- the user must have their browser open and have
  signed in to the Lino site
  
- the user must give their browser permission to show desktop
  notifications from the Lino site
  

Marking notifications as seen
=============================
doctest docs/specs/notify.rst
In addition to sending notifications via email and as desktop
notification, Lino displays unseen notfication messages in the
dashboard where it also provides an action for marking individual
message as seen.

A common caveat is that Lino does not know whether you saw the desktop
notification or the email.  That's why all notifications remain on
your dashboard until you tick them off explicitly.  

- It can be disturbing to read a message again in the dasboard if you
  have just read by email or as a desktop notification.

- Some users tend to not care about marking their notifications as
  seen in the dashboard, which causes their "My notification messages"
  to become overfilled and useless.

- Some users misunderstand the my notifications widget as a to-do
  list, which is not a good idea.

There is no perfect solution for these problems.  One workaround is to
instruct Lino to also delete *unseen* notifications automatically, by
setting :attr:`keep_unseen <lino.modlib.notify.Plugin.keep_unseen>` to
`False`.  Here is an example which also increases :attr:`remove_after
<lino.modlib.notify.Plugin.remove_after>` to 240 hours (10 days)::

   SITE.plugins.notify.configure(remove_after=240, keep_unseen=False)

Users can hide the `MyMessages` widget in their preferences if
:mod:`lino.modlib.dashboard` is installed as well.  But that's not a
recommended solution.  If you see that users of your application are
doing this, you should analyze why they do it and e.g. add filtering
options.

Possible optimizations of the system:

- Marking notifications as seen in the dashboard can be a bit slow
  because Lino refreshes the whole dashboard after every click.  We
  could avoid this using javascript which sets the item to hidden
  instead of calling refresh.
  
- Add a &notify=123456" (the id of the message) to every link in the
  email so that when the user follows one of them, the message can get
  marked as seen.



Notification messages
=====================

.. class:: Message

    The Django model that represents a *notification message*.

    .. attribute:: subject
    .. attribute:: body
    .. attribute:: user

        The recipient.

    .. attribute:: owner
 
       The database object which controls this message. 

       This may be `None`, which means that the message has no
       controller.

       When a notification is controlled, then the recipient will
       receive only the first message for that object.  Any following
       message is ignored until the recipient has "confirmed" the
       first message. Typical use case are the messages emitted by
       :class:`ChangeNotifier`: you don't want to get 10 mails just
       because a colleague makes 10 small modifications when authoring
       the text field of a ChangeNotifier object.

    .. attribute:: created
    .. attribute:: sent
    .. attribute:: seen

    .. method:: emit_notification(cls, ar, owner, message_type, msg_func, recipients)

        Class method which creates one database object per recipient.

        `recipients` is an iterable of `(user, mail_mode)` tuples.
        Duplicate items, items with user being `None` and items having
        :attr:`mail_mode <lino.modlib.users.User.mail_mode>` set to
        :attr:`silent <lino.modlib.users.MailModes.silent>` are
        removed.

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


Application programmers need to understand the different meanings of
"subject" and "body":

- The body is expected to be a
  self-sufficient and complete description of the event.
  If a message has a *body*, then the *subject* is **not** being displayed
  in the MyMessages summary.

- The subject might contain limited rich text (text formatting, links)
  but be aware that this formatting gets lost when the message is sent
  as an email.

Change notifiers
================

.. class:: ChangeNotifier
.. class:: ChangeNotifier

    Mixin for models which can emit notifications to a list of
    "observers" when an instance is modified.

    TODO: rename ChangeNotifier to ChangeNotifier

    .. method:: get_change_subject(self, ar, cw)
                
        Returns the subject text of the notification message to emit.

        The default implementation returns a message of style
        "{user} modified|created {object}" .  

        Returning None or an empty string means to suppress
        notification.

    .. method:: add_change_watcher(self, user)
                
        Parameters:

        :user: The user that will be linked to this object as a change watcher.

                
    .. method:: get_change_body(self, ar, cw)
                
        Returns the body text of the notification message to emit.

        The default implementation returns a message of style
        "{object} has been modified by {user}" followed by a summary
        of the changes.  

    .. method:: get_change_info(self, ar, cw)
        Return a list of HTML elements to be inserted into the body.

        This is called by :meth:`get_change_body`.
        Subclasses can override this. Usage example
        :class:`lino_xl.lib.notes.models.Note`

    .. method:: get_change_owner(self)
                
        Return the owner of the notification to emit.

        The "owner" is "the database object we are talking about"
        and decides who is observing this object.


Notifying actions
=================

.. class:: NotifyingAction

    An action which pops up a dialog window of three fields "Summary",
    "Description" and a checkbox "Don't notify others" to optionally
    suppress notification.

    Screenshot of a notifying action:

    .. image:: /images/screenshots/reception.CheckinVisitor.png
        :scale: 50

    Dialog fields:

    .. attribute:: notify_subject
    .. attribute:: notify_body
    .. attribute:: notify_silent

    .. method:: get_notify_subject(self, ar, obj)
                
        Return the default value of the `notify_subject` field.
        
    .. method:: get_notify_body(self, ar, obj)
                
        Return the default value of the `notify_body` field.

    .. method:: get_notify_owner(self, ar, obj)
           
        Expected to return the :attr:`owner
        lino.modlib.notify.Message.owner>` of the message.

        The default returns `None`.

        `ar` is the action request, `obj` the object on which the
        action is running,

    .. method:: get_notify_recipients(self, ar, obj)

        Yield a list of users to be notified.

        `ar` is the action request, `obj` the object on which the
        action is running, 


A :class:`NotifyingAction` is a dialog action which potentially sends
a notification.  It has three dialog fields ("subject", "body" and a
checkbox "silent").  You can have non-dialog actions (or actions with
some other dialog than a simple subject and body) which build a custom
subject and body and emit a notification.  If the emitting object also
has a method :meth:`emit_system_note`, then this is being called as
well.



Local configuration
===================

    
>>> from django.conf import settings
>>> settings.CHANNEL_LAYERS['default']['BACKEND'] in ['asgiref.inmemory.ChannelLayer','channels_redis.core.RedisChannelLayer']
True
>>> settings.CHANNEL_LAYERS['default'].get('ROUTING','') in ['lino.modlib.notify.routing.channel_routing','']
True


>>> settings.SITE.use_websockets
True

How to configure locally on a production site::

    SITE = Site(...)
    CHANNEL_LAYERS['default']['BACKEND'] = 'asgi_redis.RedisChannelLayer'
    CHANNEL_LAYERS['default']['CONFIG'] = {
    'hosts': [('localhost', 6379)],
    }




Utility functions
=================

.. function:: send_pending_emails_often()
.. function:: send_pending_emails_daily()

.. function:: clear_seen_messages
              
    Daily task which deletes messages older than :attr:`remove_after`
    hours.

Choicelists
===========

.. class:: MessageTypes
           
    The list of possible choices for the `message_type` field
    of a :class:`Message`.
              
.. class:: MailModes
           
    How the system should send email notifications to a user.

    .. attribute:: silent

        Disable notifications for this user.

    .. attribute:: never

        Notify in Lino but never send email.


Actions
=======
    
.. class:: MarkSeen
           
   Mark this message as seen.

.. class:: MarkAllSeen
           
   Mark all messages as seen.
   
.. class:: ClearSeen
           
   Mark this message as not yet seen.
   

Templates used by this plugin
=============================

.. xfile:: notify/body.eml

    A Jinja template used for generating the body of the email when
    sending a message per email to its recipient.

    Available context variables:

    - ``obj`` -- The :class:`Message` instance being sent.

    - ``E`` -- The html namespace :mod:`etgen.html`

    - ``rt`` -- The runtime API :mod:`lino.api.rt`

    - ``ar`` -- The action request which caused the message. a
      :class:`BaseRequest <lino.core.requests.BaseRequest>` instance.

