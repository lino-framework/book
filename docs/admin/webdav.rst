======
WebDAV
======

Running a Lino site with webdav means that users can edit documents generated
and managed by Lino.

The default behaviour for editable print methods (i.e. which produce a
:file:`.odt`, :file:`.doc` or :file:`.rtf` ) is to simply let the user download
the document and edit it on their client.  That's nice, but it is not enough if
you want to share your manual changes with your colleagues.

This is where webdav enters the game.

When webdav is enabled and an *editable* printable document has been generated,
Lino does not open a new browser window on that document but invokes the
client's Office application.  That application accesses the document either via
a WebDAV link (on a production server) or a ``file://`` link (on a development
server).

Activating webdav
=================

.. currentmodule:: lino.core.site

In order to activate webdav, you need to

- set the :attr:`webdav_protocol <Site.webdav_protocol>` site attribute in your
  :xfile:`settings.py` file to a string like ``'wdav'``.

- configure your web server to serve
  the :attr:`webdav_url
  <Site.webdav_url>` location using the WebDAV protocol on
  the files
  below :attr:`webdav_root <Site.webdav_root>`.

- configure the browsers of your client devices so that they
  "understand" the webdav protocol, i.e. tell them to
  invoke your office
  suite when they get an URI starting with ``wdav://``.


    When you click the "print" button of a Printable,
    and when the ´AppyRtfBuildMethod` is being used,
    then Lino redirects your browser to a location like
    ´http://lino/media/webdav/userdocs/appyrtf/notes.Note-473.rtf`.

    This will cause IE users to have the file opened within
    the browser window (but having in fact Word control it).
    Saving the file will automatically send it back to the WebDAV server.

Possible problems
=================

The file's rtf content is displayed as plain text
-------------------------------------------------

Note: .rtf content looks something like this::

  {\rtf1\ansi\deff1\adeflang1025
  {\fonttbl{\f0\froman\fprq2\fcharset128 DejaVu Serif;}{\f1\froman\fprq2\fcharset128 Times New Roman;}{\f2\fswiss\fprq2\fcharset128 Arial;}{\f3\fnil\fprq0\fcharset128 StarSymbol{\*\falt Arial Unicode MS};}{\f4\fswiss\fprq0\fcharset128 Tahoma;}{\f5\fnil\fprq2\fcharset128 SimSun;}{\f6\fnil\fprq2\fcharset128 Tahoma;}{\f7\fnil\fprq0\fcharset128 Tahoma;}}
  {\colortbl;\red0\green0\blue0;\red128\green12



- Check whether web server is correctly configured to return a mime type of ``application/rtf``.

- Test with different browsers.


The file is correctly opened, but read-only
-------------------------------------------

- Maybe somebody else is just editing the file?

- Office 2003 needs Service Pack 2, otherwise if will open .rtf 
  files as read-only:
  http://support.microsoft.com/kb/884050/en-us

- LibreOffice users, see
  http://help.libreoffice.org/Common/Opening_a_Document_Using_WebDAV_over_HTTPS
  
  You must manually open the webdav location once, to trigger LO's dialog 
  that asks for username and password.
  
  http://forums.mozillazine.org/viewtopic.php?p=3203256
  http://user.services.openoffice.org/en/forum/viewtopic.php?f=47&t=14017
  http://user.services.openoffice.org/en/forum/viewtopic.php?f=7&t=1614#p32570
  http://extensions.geckozone.org/DownloadWith
  

If your Office suite doesn't support editing of webdav documents
----------------------------------------------------------------

Tell your browser that it is okay to open "local" files

- FF users must install Michael J Gruber's
  `LocalLink add-on <https://addons.mozilla.org/en-US/firefox/addon/locallink/>`_.

- Chrome users must install Leonid Borisenko's
  `LocalLinks add-on <https://chrome.google.com/webstore/detail/jllpkdkcdjndhggodimiphkghogcpida>`_.

- all windows users must map a drive letter (e.g. ``W:`` to the 
  :attr:`lino.Lino.webdav_root` directory on the Lino server.
  
- Set :attr:`lino.Lino.webdav_url` to ``"file://W:/"``


