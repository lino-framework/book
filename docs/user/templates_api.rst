=====================
Template designer API
=====================

.. How to test just this file:

   $ doctest docs/user/templates_api.rst

.. _tplcontext:


The template context
====================

This is a list template context names available when parsing a
template.

This is just a start and far from being complete...


.. tcname:: this
          
    The printable object instance

.. tcname:: site
          
    shortcut for `settings.SITE`
        

.. tcname:: this
            
        The printable object instance
        
.. tcname:: mtos
            
        "amount to string" using :func:`decfmt`
        
.. tcname:: iif
            
        :func:`iif <atelier.utils.iif>`
        
.. tcname:: tr(**kw)
            
        Shortcut to :meth:`babelitem <lino.core.site.Site.babelitem>`.
        
.. tcname:: _(s)
            
        gettext
        
.. tcname:: E
            
        HTML tag generator, see :mod:`lino.utils.xmlgen.html`
        
.. tcname:: unicode()
            
        the builtin Python :func:`unicode` function
        
.. tcname:: len()
            
        the builtin Python :func:`len` function

.. tcname:: settings``
            
        The Django :xfile:`settings.py` module

.. tcname:: site`
            
        shortcut for `settings.SITE`
        
.. tcname:: ar
            
        a Lino :class:`lino.core.requests.BaseRequest` instance around 
        the calling Django request 


.. tcname:: request`
            
        the Django HttpRequest instance
        (available in :xfile:`admin_main.html`,
        rendered by :meth:`get_main_html <lino.ui.Site.get_main_html>`,
        which calls :func:`lino.core.web.render_from_request`)
        


.. initialization for doctest

    >>> from lino import startup
    >>> startup('lino_book.projects.docs.settings.demo')
    >>> from lino.api.shell import *
    >>> from lino.utils.format_date import fds, fdm, fdl, fdf
    >>> import datetime


.. _datefmt:

Date formatting functions
-------------------------

Lino includes shortcuts to `python-babel`'s 
`date formatting functions <http://babel.pocoo.org/docs/dates/>`_:

.. tcname:: fds
          
    "format date short", see :ref:`datefmt`
        
.. tcname:: fdm
            
    "format date medium", see :ref:`datefmt`
            
.. tcname:: fdl
            
    "format date long", see :ref:`datefmt`
            
.. tcname:: fdf
            
    "format date full", see :ref:`datefmt`
            
.. tcname:: dtos
            
    deprecated for :tcname:`fds`
        
.. tcname:: dtosl
            
    deprecated for :tcname:`fdl`

            

Examples:

>>> d = datetime.date(2013,8,26)
>>> print(fds(d)) # short
26/08/2013
>>> print(fdm(d)) # medium
26 Aug 2013
>>> print(fdl(d)) # long
26 August 2013
>>> print(fdf(d)) # full
Monday, 26 August 2013
