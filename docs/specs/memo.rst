.. doctest docs/specs/memo.rst
.. _dev.memo:

==========================
``memo`` : The memo parser
==========================

.. currentmodule:: lino.modlib.memo

The :mod:`lino.modlib.memo` plugin adds application-specific markup to
:doc:`text fields </dev/textfield>` .

One facet of this plugin is a simple built-in markup language called "memo". A
**memo markup command** is a fragment of text between square brackets (of the
form ``[foo bar baz]``)

Another facet are **suggesters**. A suggester is when you define that a
"trigger text" will pop up a list of suggestions for auto-completion.  For
example ``#`` commonly refers to a topic or a ticket, or ``@`` refers to
another user or person.

that will be "rendered" (converted into another fragment)
when your description text is being displayed at certain places.


A concrete real-world specification is in :doc:`/specs/noi/memo`


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst


>>> from lino import startup
>>> startup('lino_book.projects.team.settings.doctests')
>>> from lino.api.doctest import *


Basic usage
===========

The :class:`lino.modlib.memo.parser.Parser` is a simple markup parser that
expands "commands" found in an input string to produce a resulting output
string.  Commands are in the form ``[KEYWORD ARGS]``.  The caller defines
itself all commands, there are no predefined commands.

Instantiate a parser:

>>> from lino.modlib.memo.parser import Parser
>>> p = Parser()

We declare a "command handler" function `url2html` and register it:

>>> def url2html(parser, s):
...     print("[DEBUG] url2html() got %r" % s)
...     if not s: return "XXX"
...     url, text = s.split(None,1)
...     return '<a href="%s">%s</a>' % (url,text)
>>> p.register_command('url', url2html)

The intended usage of our example handler is ``[url URL TEXT]``, where
URL is the URL to link to, and TEXT is the label of the link:

>>> print(p.parse('This is a [url http://xyz.com test].'))
[DEBUG] url2html() got 'http://xyz.com test'
This is a <a href="http://xyz.com">test</a>.


A command handler will be called with one parameter: the portion of
text between the KEYWORD and the closing square bracket.  Not
including the whitespace after the keyword.  It must return the text
which is to replace the ``[KEYWORD ARGS]`` fragment.  It is
responsible for parsing the text that it receives as parameter.

If an exception occurs during the command handler, the final exception
message is inserted into the result.

To demonstrate this, our example implementation has a bug, it doesn't
support the case of having only an URL without TEXT (we use an
ellipsis because the error message varies with Python versions):

>>> print(p.parse('This is a [url http://xyz.com].'))  #doctest: +ELLIPSIS
[DEBUG] url2html() got 'http://xyz.com'
This is a [ERROR ... in ...'[url http://xyz.com]' at position 10-30].


Newlines preceded by a backslash will be removed before the command
handler is called:

>>> print(p.parse('''This is [url http://xy\
... z.com another test].'''))
[DEBUG] url2html() got 'http://xyz.com another test'
This is <a href="http://xyz.com">another test</a>.

The whitespace between the KEYWORD and ARGS can be any whitespace,
including newlines:

>>> print(p.parse('''This is a [url
... http://xyz.com test].'''))
[DEBUG] url2html() got 'http://xyz.com test'
This is a <a href="http://xyz.com">test</a>.

The ARGS part is optional (it's up to the command handler to react
accordingly, our handler function returns XXX in that case):

>>> print(p.parse('''This is a [url] test.'''))
[DEBUG] url2html() got ''
This is a XXX test.

The ARGS part may contain pairs of square brackets:

>>> print(p.parse('''This is a [url
... http://xyz.com test with [more] brackets].'''))
[DEBUG] url2html() got 'http://xyz.com test with [more] brackets'
This is a <a href="http://xyz.com">test with [more] brackets</a>.

Fragments of text between brackets that do not match any registered
command will be left unchanged:

>>> print(p.parse('''This is a [1] test.'''))
This is a [1] test.

>>> print(p.parse('''This is a [foo bar] test.'''))
This is a [foo bar] test.

>>> print(p.parse('''Text with only [opening square bracket.'''))
Text with only [opening square bracket.

Special handling
================

Leading and trailing spaces are always removed from command text:

>>> print(p.parse("[url http://example.com Trailing space  ]."))
[DEBUG] url2html() got 'http://example.com Trailing space'
<a href="http://example.com">Trailing space</a>.

>>> print(p.parse("[url http://example.com   Leading space]."))
[DEBUG] url2html() got 'http://example.com   Leading space'
<a href="http://example.com">Leading space</a>.

Non-breaking and zero-width spaces are treated like normal spaces:

>>> print(p.parse(u"[url\u00A0http://example.com example.com]."))
[DEBUG] url2html() got 'http://example.com example.com'
<a href="http://example.com">example.com</a>.

>>> print(p.parse(u"[url \u200bhttp://example.com example.com]."))
[DEBUG] url2html() got 'http://example.com example.com'
<a href="http://example.com">example.com</a>.

>>> print(p.parse(u"[url&nbsp;http://example.com example.com]."))
[DEBUG] url2html() got 'http://example.com example.com'
<a href="http://example.com">example.com</a>.

Limits
======

A single closing square bracket as part of ARGS will not produce the
desired result:

>>> print(p.parse('''This is a [url
... http://xyz.com The character "\]"].'''))
[DEBUG] url2html() got 'http://xyz.com The character "\\'
This is a <a href="http://xyz.com">The character "\</a>"].

Execution flow statements like `[if ...]` and `[endif ...]` or ``[for
...]`` and ``[endfor ...]`` would be nice.



The ``[=expression]`` form
==========================


>>> print(p.parse('''<ul>[="".join(['<li>%s</li>' % (i+1) for i in range(5)])]</ul>'''))
<ul><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li></ul>

You can specify a run-time context:

>>> ctx = { 'a': 3 }
>>> print(p.parse('''\
... The answer is [=a*a*5-a].''', context=ctx))
The answer is 42.

The :class:`Previewable` mixin
==============================



Technical reference
===================

.. function:: truncate_comment(html_str, max_p_len=None)

    Return a shortened preview of a html string, containing at most one
    paragraph with at most `max_p_len` characters.

    :html_str: the raw string of html
    :max_p_len: max number of characters in the paragraph.

    See usage examples in :doc:`/specs/comments`.

.. function:: rich_text_to_elems(ar, description)

    A RichTextField can contain HTML markup or plain text.

.. function:: body_subject_to_elems(ar, title, description)

    Convert the given `title` and `description` to a list of HTML
    elements.

    Used by :mod:`lino.modlib.notify` and by :mod:`lino_xl.lib.sales`

.. class:: Previewable

  Adds three rich text fields (:class:`lino.core.fields.RichTextField`):

  .. attribute:: body

    An editable text body.

  .. attribute:: short_preview

    A read-only short preview of :attr:`body`.

  .. attribute:: full_preview

    A read-only full preview of :attr:`body`.

.. class:: PreviewableChecker

  Check for previewables needing update.
