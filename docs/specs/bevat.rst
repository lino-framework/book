.. _xl.bevat:

========================
Belgian VAT declarations
========================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_bevat
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.apc.settings.doctests')
    >>> from lino.api.doctest import *


This document describes the :mod:`lino_xl.lib.bevat` plugin which adds
functionality for handling **Belgian VAT declarations**.

Table of contents:

.. contents::
   :depth: 1
   :local:

Overview
========

.. currentmodule:: lino_xl.lib.bevat

Installing this plugin will automatically install
:mod:`lino_xl.lib.vat`.

>>> dd.plugins.bevat.needs_plugins     
['lino_xl.lib.vat']




Models and actors reference
===========================

.. class:: Declaration
           
    A VAT declaration. 


Choicelists
===========

.. class:: DeclarationFields
           
    The list of fields in a VAT declaration.
    
