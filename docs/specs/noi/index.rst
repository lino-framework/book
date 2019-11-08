.. _noi.specs:

=======================
Lino Noi specs
=======================

This section contains specs for :ref:`noi`.


.. toctree::
    :maxdepth: 1
    :glob:

    general
    tickets
    working
    smtpd
    hosts
    as_pdf
    ddh
    memo
    db
    std
    public
    bs3
    export_excel
    mailbox

    projects
    faculties
    votes
    deploy
    github
    stars
    sql
    cal
    suggesters
    users



.. currentmodule:: lino_noi.lib.noi

.. module:: lino_noi.lib.noi.workflows

The default :attr:`workflows_module
<lino.core.site.Site.workflows_module>` for :ref:`noi` applications.

This workflow requires that both :mod:`lino_xl.lib.tickets` and
:mod:`lino_xl.lib.votes` are installed.
