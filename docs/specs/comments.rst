.. doctest docs/specs/comments.rst
.. _book.specs.comments:

======================
The comments framework
======================

.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.team.settings.demo')
    >>> from lino.api.doctest import *


This describes the :mod:`lino.modlib.comments` plugin which is used
for handling simple comments.

A comment is always "about" something. This is the Topic of your
comment, internally represented by the :attr:`owner` field. This is a
Generic Foreign Key, i.e. it can be any database object.  It is
however the application developer who decides where comments can be
created and how they are being displayed.

A comment is something one user wants to say to "whoever is
interested".  A comment has no "recipient" .  When you submit a
comment, Lino notifies all users that registered their interest in the
topic.

Comments have no workflow management nor rating merchanism etc.
As in the real world it is the user's responsibility to think at
least a bit before they say something.


.. contents::
   :depth: 1
   :local:



.. module:: lino.modlib.comments

Comments
========
    
.. class:: Comment
           
    A **comment** is a short text which some user writes about some
    other database object. It has no recipient.

    .. attribute:: body

        The full body text of your comment.

    .. attribute:: body_preview

        The first paragraph of your :attr:`body`.

    .. attribute:: user

        The author of the comment.
        
    .. attribute:: owner

        A generic foreign key to the commentable database object to
        which this comment relates.
        
    .. attribute:: published

        When this comment has been published. A timestamp.

.. class:: Comments


    .. attribute:: show_published
                   
        Whether to show only (un)published comments, independently of
        the publication date.
   
    .. attribute:: start_date
    .. attribute:: end_date

       The date range to filter. 
           
    .. attribute:: observed_event

       Which event (created, modified or published) to consider when
       applying the date range given by :attr:`start_date` and
       :attr:`end_date`.
       
    .. method:: as_li(cls, self, ar)
                
        Return this comment for usage in a list item as a string with
        HTML tags.


.. class:: AllComments
           
.. class:: MyComments
.. class:: MyPendingComments        
          
.. class:: RecentComments
    Shows the comments for a given database object.

    .. attribute:: slave_summary


    .. method:: get_slave_summary(cls, obj, ar)
                
        The :meth:`summary view
        <lino.core.actors.Actor.get_slave_summary>` for this table.

.. class:: CommentsByX
.. class:: CommentsByType
.. class:: CommentsByRFC
           
    Shows the comments for a given database object.

    .. attribute:: slave_summary

    .. method:: get_slave_summary(cls, obj, ar)
                
        The :meth:`summary view
        <lino.core.actors.Actor.get_slave_summary>` for this table.


.. class:: ObservedTime

.. class:: CommentEvents

    The choicelist with selections for
    :attr:`Comments.observed_event`.
           
.. class:: PublishComment
    Publish this comment.
           
.. class:: PublishAllComments
    Publish all comments.



Comment types
=============

.. class:: CommentType
           
    The :class:`CommentType` model is not being used in production,
    one day we will probably remove it.

            
.. class:: CommentTypes
           
    The table with all existing comment types.

    This usually is accessible via the `Configure` menu.

           
Commentable
===========

.. class:: Commentable

    Mixin for models that can be subject to comments.

    .. method:: get_rfc_description(self, ar)

        Return a HTML formatted string with the description of this
        Commentable as it should be displayed by the slave summary of
        CommentsByOwner.

        It must be a string and not an etree element. That's because
        it usually includes the content of RichTextField. If the API
        required an element, it would require us to parse this content
        just in order to generate HTML from it.

    .. method:: on_commented(self, comment, ar, cw)

        This is automatically called when a comment has been created
        or modified.

           

Utilities
=========

.. function:: comments_by_owner        



The preview of a comment
========================



Usage examples:

>>> from lino.utils.soup import truncate_comment

>>> print(truncate_comment('<h1 style="color: #5e9ca0;">Styled comment <span style="color: #2b2301;">pasted from word!</span> </h1>'))
Styled comment pasted from word! 

>>> print(truncate_comment('<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>', 30))
Lorem ipsum dolor sit amet, co...

>>> print(truncate_comment('<p>Lorem ipsum dolor sit amet</p><p>consectetur adipiscing elit.</p>', 30))
Lorem ipsum dolor sit amet (...)

>>> print(truncate_comment('<p>A short paragraph</p><p><ul><li>first</li><li>second</li></ul></p>'))
A short paragraph (...)

>>> html = u'<p>Ich habe Hirn, ich will hier raus! &ndash; Wie im Netz der Flachsinn regiert.</p>\\n<ul>\\n<li>Ver&ouml;ffentlicht:&nbsp;6. Mai 2017</li>\\n<li>Vorgestellt in:&nbsp;<a href="https://www.linkedin.com/pulse/feed/channel/deutsch"><span>Favoriten der Redaktion</span></a>,&nbsp;<a href="https://www.linkedin.com/pulse/feed/channel/jobs"><span>Job &amp; Karriere</span></a>,&nbsp;<a href="https://www.linkedin.com/pulse/feed/channel/verkauf"><span>Marketing &amp; Verkauf</span></a>,&nbsp;<a href="https://www.linkedin.com/pulse/feed/channel/technologie"><span>Technologie &amp; Internet</span></a>,&nbsp;<a href="https://www.linkedin.com/pulse/feed/channel/wochenendLekture"><span>Wochenend-Lekt&uuml;re</span></a></li>\\n</ul>\\n<ul>\\n<li><span><span>Gef&auml;llt mir</span></span><span>Ich habe Hirn, ich will hier raus! &ndash; Wie im Netz der Flachsinn regiert</span>\\n<p>&nbsp;</p>\\n<a href="https://www.linkedin.com/pulse/ich-habe-hirn-hier-raus-wie-im-netz-der-flachsinn-regiert-dueck"><span>806</span></a></li>\\n<li><span>Kommentar</span>\\n<p>&nbsp;</p>\\n<a href="https://www.linkedin.com/pulse/ich-habe-hirn-hier-raus-wie-im-netz-der-flachsinn-regiert-dueck#comments"><span>42</span></a></li>\\n<li><span>Teilen</span><span>Ich habe Hirn, ich will hier raus! &ndash; Wie im Netz der Flachsinn regiert teilen</span>\\n<p>&nbsp;</p>\\n<span>131</span></li>\\n</ul>\\n<p><a href="https://www.linkedin.com/in/gunterdueck"><span>Gunter Dueck</span></a> <span>Folgen</span><span>Gunter Dueck</span> Philosopher, Writer, Keynote Speaker</p>\\n<p>Das Smartphone vibriert, klingelt oder surrt. Zing! Das ist der Messenger. Eine Melodie von eBay zeigt an, dass eine Auktion in den n&auml;chsten Minuten endet. Freunde schicken Fotos, News versprechen uns "Drei Minuten, nach denen du bestimmt lange weinen musst" oder "Wenn du dieses Bild siehst, wird sich dein Leben auf der Stelle f&uuml;r immer ver&auml;ndern".</p>\\n<p>Politiker betreiben statt ihrer eigentlichen Arbeit nun simples Selbstmarketing und fordern uns auf, mal schnell unser Verhalten zu &auml;ndern &ndash; am besten nat&uuml;rlich "langfristig" und "nachhaltig". Manager fordern harsch immer mehr Extrameilen von uns ein, die alle ihre (!) Probleme beseitigen, und es gibt f&uuml;r jede Schieflage in unserem Leben Rat von allerlei Coaches und Therapeuten, es gibt Heilslehren und Globuli.</p>'
>>> print(truncate_comment(html))
Ich habe Hirn, ich will hier raus! – Wie im Netz der Flachsinn regiert. (...)

>>> print(truncate_comment('Some plain text.'))
Some plain text.

>>> print(truncate_comment('Two paragraphs of plain text.\n\n\nHere is the second paragraph.'))
Two paragraphs of plain text. (...)

              
