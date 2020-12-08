.. doctest docs/specs/comments.rst
.. _book.specs.comments:

=====================================
``comments`` : The comments framework
=====================================

.. currentmodule:: lino.modlib.comments

The :mod:`lino.modlib.comments` plugin adds a framework for handling comments.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.noi1e.settings.demo')
>>> from lino.api.doctest import *

Overview
========

.. glossary::

  comment

    A written text that one user wants to share with others.

    A comment is always "about" something, called the :term:`discussion topic`.

    A comment has no "recipient". When you submit a comment, Lino notifies all
    users who registered their interest in the :term:`discussion topic`.

    A comment can be a *reply* to another comment. All comments replying directly
    or indirectly to a given comment are called a *discussion thread*.

    Comments are stored in the :class:`Comment` database model.

  discussion topic

    A database object that is the "topic" of a series of comments.

  commentable database model

    The application developer decides which database models can serve as topics
    for commenting by having these database models inherit from the
    :class:`Commentable` mixin.

  commenting group

    A group of users who discuss with each other using comments.


Comments
========

.. class:: Comment

    Django model to represent a :term:`comment`.

    .. attribute:: user

        The author of the comment.

    .. attribute:: owner

        The *topic* this comment is about. This field is a Generic Foreign Key,
        i.e. users can basically comment on any database object.  It is however
        the :term:`application developer` who decides where comments can be
        created and how they are being displayed.

        The :attr:`owner` of a comment is always an instance of a subclass of
        :class:`Commentable`.

    .. attribute:: body

        The full body text of your comment.

    .. attribute:: short_preview

        The first paragraph of your :attr:`body`.

    .. attribute:: emotion

        The emotion of this comment.

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


    .. method:: get_table_summary(cls, obj, ar)

        The :meth:`summary view
        <lino.core.actors.Actor.get_table_summary>` for this table.

.. class:: CommentsByX
.. class:: CommentsByType
.. class:: CommentsByRFC

    Shows the comments for a given database object.

    .. attribute:: slave_summary

    .. method:: get_table_summary(cls, obj, ar)

        The :meth:`summary view
        <lino.core.actors.Actor.get_table_summary>` for this table.


.. class:: ObservedTime

.. class:: CommentEvents

    The choicelist with selections for
    :attr:`Comments.observed_event`.

.. class:: PublishComment
    Publish this comment.

.. class:: PublishAllComments
    Publish all comments.


Emotions
========

.. class:: Emotions

    The list of available values for the :attr:`Comment.emotion` field.

>>> rt.show("comments.Emotions")
========== ========== ========== =============
 value      name       text       Button text
---------- ---------- ---------- -------------
 ok         ok         Okay
 agree      agree      Agree      ✅
 disagree   disagree   Disagree   ❎
========== ========== ========== =============
<BLANKLINE>


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

    Mixin for models whose instances can be :term:`discussion topic` of
    comments.

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

    .. method:: get_comment_group(self)

        Return either `None` or a database object that represents the :term:`commenting group`
        where this comment is being done.

        If not None, the object must have a field :attr:`ref` which will be
        shown in the summary of :class:`RecentComments`.

    .. method:: get_comments_filter(cls, user):

        Return the filter to be added when a given user requests comments about
        commentables of this type.

        Return `None` to not add any filter.  Otherwise the return value should
        be a :class:`django.db.models.Q` object.

        Default behaviour is that public comments are visible even to anonymous
        while private comments are visible only to their author and to
        :class:`PrivateCommentsReader`.

        You can override this class method to define your own privacy settings.

        Usage example in
        :class:`lino_xl.lib.groups.Group` and
        :class:`lino_xl.lib.tickets.Ticket`.

        If you override this method, you probably want to define a
        :class:`django.contrib.contenttypes.fields.GenericRelation` on your Commentable
        in order to write filter conditions based on the owner of the comment.



Utilities
=========

.. function:: comments_by_owner



The preview of a comment
========================


Usage examples:

>>> from lino.modlib.memo.mixins import truncate_comment

>>> print(truncate_comment('<h1 style="color: #5e9ca0;">Styled comment <span style="color: #2b2301;">pasted from word!</span> </h1>'))
... #doctest: +NORMALIZE_WHITESPACE
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
