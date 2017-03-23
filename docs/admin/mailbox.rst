==============
Mailbox Plugin
==============


The mailbox plugin allows you to emails entered into your lino-application databace


Installation
------------

The mailbox plugin requires the django plugin django_mailbox.
To install it run:

        $ pip install -e git+https://github.com/CylonOven/django-mailbox.git#egg=django-mailbox

Add 'lino_xl.lib.mailbox' to your sites's get_installed_apps function

Configuration
-------------

In Configure > Mailbox > mailboxes you can add new mailboxes.
The relevant documentation can be found in django_mailbox's docs.

  http://django-mailbox.readthedocs.io/en/stable/topics/mailbox_types.html

Postfix and Mboxs
-----------------

Currently we only have Maibox's running using mboxs and postfix to allow emails to system users be entered into the db.

/etc/aliases

        mbox: /path/to/mbox/mbox
	user: user mbox

This will have postfix send mail to both the user's inbox and the devined mbox

Lino's supervisor user must have write access to the folder as well as mbox inorder to read/write and lock the mbox.
