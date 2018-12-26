.. doctest docs/specs/printing.rst
.. _specs.printing:

==================
Printing documents
==================

..  Initialize doctest:

    >>> from lino import startup
    >>> startup('lino_book.projects.max.settings.doctests')
    >>> from lino.api.shell import *
    >>> from lino.api.doctest import *

See also :doc:`/admin/printing`.

.. currentmodule:: lino.modlib.printing

Lino applications can use several approaches for offering "printing
functionality" to the end user:

- :class:`Printable` adds a hard-coded "Print" button to a database
  model.
- :doc:`excerpts` also cause a "Print" button to be added to database
  models, but in a configurable way.
- :mod:`lino_xl.lib.appypod` adds a button which prints the current
  grid as a table to pdf.
- A "report" (:mod:`lino.utils.report`) is a hard-coded sequence of
  tables and arbitrary content.
     
Lino has the following plugins related to printing:

- :mod:`lino.modlib.printing` -- general functionality for printing 
- :mod:`lino.modlib.jinja`

Additional build methods:

- :mod:`lino.modlib.weasyprint`
- :mod:`lino_xl.lib.appypod`
- :mod:`lino.modlib.wkhtmltopdf`
  


>>> rt.show(printing.BuildMethods)  #doctest: +NORMALIZE_WHITESPACE
============ ============ ======================
 value        name         text
------------ ------------ ----------------------
 latex        latex        LatexBuildMethod
 rtf          rtf          RtfBuildMethod
 xml          xml          XmlBuildMethod
 weasy2html   weasy2html   WeasyHtmlBuildMethod
 weasy2pdf    weasy2pdf    WeasyPdfBuildMethod
 appyodt      appyodt      AppyOdtBuildMethod
 appydoc      appydoc      AppyDocBuildMethod
 appypdf      appypdf      AppyPdfBuildMethod
 appyrtf      appyrtf      AppyRtfBuildMethod
============ ============ ======================
<BLANKLINE>


Printing a normal pdf table
===========================

>>> settings.SITE.appy_params.update(raiseOnError=True)
>>> url = 'http://127.0.0.1:8000/api/contacts/Partners?an=as_pdf'
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> print(result['success'])
True
>>> print(result['open_url'])
/media/cache/appypdf/127.0.0.1/contacts.Partners.pdf



Printing address labels
=======================

>>> settings.SITE.appy_params.update(raiseOnError=True)
>>> url = 'http://127.0.0.1:8000/api/contacts/Partners?an=print_labels'
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> print(result['success'])
True
>>> print(result['open_url'])
/media/cache/appypdf/127.0.0.1/contacts.Partners.pdf


Reference
=========

.. currentmodule:: lino.modlib.printing

Model mixins
------------

.. class:: Printable

    Mixin for models for which Lino can generate a printable
    document.

    Extended by :class:`CachedPrintable` and :class:`TypedPrintable`.
    Other methods for printing a printable is to add an excerpt type
    or to provide your own subclass of DirectPrintAction.

    .. method:: get_print_language(self)
                
        Return a Django language code to be activated when an instance
        of this is being printed.  The default implementation returns
        the Site's default language.
        
        Returning `None` is equivalent to the Site's default language.

    .. method:: get_print_templates(self, bm, action)
                
        Return a list of filenames of templates for the specified
        build method.  Returning an empty list means that this item is
        not printable.  For subclasses of :class:`SimpleBuildMethod`
        the returned list may not contain more than 1 element.

        The default method calls
        :meth:`BuildMethod.get_default_template` and returns this as a
        list with one item.

    .. method:: get_printable_context(self, ar=None, **kw)

        Adds a series of names to the context used when rendering
        printable documents.

        :class:`lino_xl.lib.notes.models.Note` extends this.

    .. method:: get_body_template(self)
                
        Return the name of the body template to use when rendering this
        object in a printable excerpt (:mod:`lino_xl.lib.excerpts`).
        An empty string means that Lino should use the default value
        defined on the ExcerptType.

    .. method:: get_printable_demo_objects(self)
                
        Return an iterable of database objects for which Lino should
        generate a printable excerpt.

        This is being called by
        :mod:`lino_xl.lib.excerpts.fixtures.demo2`.


    .. method:: get_build_method(self)
                
        Return the build method to use when printing this object.

        This is expected to rather raise an exception than return
        `None`.

    .. method:: get_excerpt_options(self, ar, **kw)
                
        Set additional fields of newly created excerpts from this.  Called
        from
        :class:`lino_xl.lib.excerpts.models.ExcerptType.get_or_create_excerpt`.

    .. method:: before_printable_build(self, bm)
                
        This is called by print actions before the printable is being
        generated.  Application code may e.g. raise a `Warning`
        exception in order to refuse the print action.  The warning
        message can be a translatable string.


.. class:: CachedPrintable
           
    Mixin for Models that generate a unique external file at a
    determined place when being printed.
    
    Adds a "Print" button, a "Clear cache" button and a `build_time`
    field.
    
    The "Print" button of a :class:`CachedPrintable
    <lino.mixins.printable.CachedPrintable>` transparently handles the
    case when multiple rows are selected.  If multiple rows are
    selected (which is possible only when :attr:`cell_edit
    <lino.core.tables.AbstractTable.cell_edit>` is True), then it will
    automatically:
    
    - build the cached printable for those objects who don't yet have
      one
      
    - generate a single temporary pdf file which is a merge of these
      individual cached printable docs

    Database fields:

    .. attribute:: build_time

        Timestamp of the built target file. Contains `None`
        if no build hasn't been called yet.

    Actions:
           
    .. attribute:: do_print

        The action used to print this object.
        This is an instance of
        :class:`DirectPrintAction` or :class:`CachedPrintAction` by
        default.  And if :mod:`lino_xl.lib.excerpts` is installed,
        then :func:`set_excerpts_actions
        <lino_xl.lib.excerpts.set_excerpts_actions>` possibly replaces
        :attr:`do_print` by a
        :class:`lino_xl.lib.excerpts.CreateExcerpt` instance.

    .. attribute:: edit_template

.. class:: TypedPrintable
           
    A :class:`CachedPrintable` that uses a "Type" for deciding which
    template to use on a given instance.
    
    A TypedPrintable model must define itself a field ``type`` which
    is a ForeignKey to a Model that implements :class:`PrintableType`.
    
    Alternatively you can override :meth:`get_printable_type` if you
    want to name the field differently. An example of this is
    :attr:`ml.sales.SalesDocument.imode`.


.. class:: PrintableType

    Base class for models that specify the
    :attr:`TypedPrintable.type`.

    .. attribute:: templates_group

        Default value for `templates_group` is the model's full name.
    
    .. attribute:: build_method

        A pointer to an item of
        :class:`lino.modlib.printing.choicelists.BuildMethods`.

    .. attribute:: template

        The name of the file to be used as template.
    
        If this field is empty, Lino will use the filename returned by
        :meth:`lino.modlib.printing.Plugin.get_default_template`.
    
        The list of choices for this field depend on the
        :attr:`build_method`.  Ending must correspond to the
        :attr:`build_method`.

Utilities
---------

.. class:: CachedPrintableChecker

    Checks for missing cache files on all objects which inherit
    :class:`CachedPrintable`.

    When a CachedPrintable has a non-empty :attr:`build_time
    <CachedPrintable.build_time>` field, this means that the target
    file has been built.  That file might no longer exists for several
    reasons:

    - it has really beeen removed from the cache directory.

    - we are working in a copy of the database, using a different
      cache directory.

    - the computed name of the file has changed due to a change in
      configuration or code.

    An easy quick "fix" would be to set `build_time` to None, but this
    is not automatic because in cases of real data loss a system admin
    might want to have at least that timestamp in order to search for
    the lost file.

           

Actions
-------

.. class:: BasePrintAction
           
    Base class for all "Print" actions.

.. class:: DirectPrintAction

    Print using a hard-coded template and without cache.

.. class:: CachedPrintAction
           
    A print action which uses a cache for the generated printable
    document and builds is only when it doesn't yet exist.

.. class:: ClearCacheAction

    Defines the :guilabel:`Clear cache` button on a Printable record.
    
    The `run_from_ui` method has an optional keyword argmuent
     `force`. This is set to True in `docs/tests/debts.rst`
     to avoid compliations.
    

.. class:: EditTemplate

    Edit the print template, i.e. the file specified by
    :meth:`Printable.get_print_templates`.

    The action available only when :mod:`lino.modlib.davlink` is
    installed, and only for users with `SiteStaff` role.

    If it is available, then it still works only when

    - your site has a local config directory
    - your :xfile:`webdav` directory (1) is published by your server under
      "/webdav" and (2) has a symbolic link named `config` which points
      to your local config directory.
    - the local config directory is writable by `www-data`

    **Factory template versus local template**
    
    The action automatically copies a factory template to the local
    config tree if necessary. Before doing so, it will ask for
    confirmation: :message:`Before you can edit this template we must
    create a local copy on the server.  This will exclude the template
    from future updates.`

           
Build methods
-------------

.. class:: BuildMethods

    The choicelist of build methods offered on this site.
    
.. class:: BuildMethod

    Base class for all build methods.  A build method encapsulates the
    process of generating a "printable document" that inserts data
    from the database into a template, using a given combination of a
    template parser and post-processor.

    .. attribute:: use_webdav
   
        Whether this build method results is an editable file.  For
        example, `.odt` files are considered editable while `.pdf` files
        aren't.

        In that case the target will be in a webdav folder and the print
        action will respond `open_davlink_url` instead of the usual
        `open_url`, which extjs3 ui will implement by calling
        `Lino.davlink_open()` instead of the usual `window.open()`.

        When :mod:`lino.modlib.davlink` is not installed, this setting
        still influences the target path of resulting files, but the
        clients will not automatically recognize them as webdav-editable
        URLs.

.. class:: TemplatedBuildMethod
           
    A :class:`BuildMethod` which uses a template.
    
.. class:: DjangoBuildMethod
           
    A :class:`TemplatedBuildMethod` which uses Django's templating engine.


.. class:: XmlBuildMethod    
    
    Generates .xml files from .xml templates.
    
.. class:: SimpleBuildMethod

    Base for build methods which use Lino's templating system
    (:meth:`find_config_file <lino.core.site.Site.find_config_file>`).

    TODO: check whether this extension to Django's templating system
    is still needed.


.. class:: CustomBuildMethod
           
    For example CourseToXls.

    Simple example::

        from lino.modlib.printing.utils import CustomBuildMethod

        class HelloWorld(CustomBuildMethod):
            target_ext = '.txt'
            name = 'hello'
            label = _("Hello")

            def custom_build(self, ar, obj, target):
                # this is your job
                file(target).write("Hello, world!")

        class MyModel(Model):
            say_hello = HelloWorld.create_action()


    

    .. method:: custom_build(self, ar, obj, target)

        Concrete subclasses must implement this.

        This is supposed to create a file named `target`.
        
           
.. class:: LatexBuildMethod    

    Not actively used.
    Generates `.pdf` files from `.tex` templates.
    
.. class:: RtfBuildMethod    

    Not actively used.
    Generates `.rtf` files from `.rtf` templates.
    
.. class:: PisaBuildMethod
           
    Deprecated.
    Generates .pdf files from .html templates.
    Requires `pisa <https://pypi.python.org/pypi/pisa>`_.
    Usage example see :mod:`lino_book.projects.pisa`.

