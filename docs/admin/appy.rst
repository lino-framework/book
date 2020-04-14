.. _admin.libreoffice:

============================
Lino and LibreOffice
============================

When at least one :term:`Lino site` of a server uses :mod:`lino_xl.lib.appypod`,
then the server must have a LibreOffice service running so that the users of
your site can print documents using the appypdf, appydoc or appyrtf methods (the
appyodt method does not require a LO service).

You say this using the :cmd:`getlino configure --appy` option.

For background information see :doc:`oood`.
