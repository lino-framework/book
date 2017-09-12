=================================
The local configuration directory
=================================

The **local configuration directory** is a directory on your Lino
server which contains template files used by Lino when printing
invoices, contracts or any document.

At least one user of the site should be the **local template manager**
who is responsible for managing these files.

.. xfile:: config

The local configuration directory is always named :xfile:`config` and
is always a subdirectory of the :attr:`cache_dir
<lino.core.site.Site.cache_dir>`. Lino does not create this directory
automatically. If you want to use local templates, the system
administrator must create that directory and make sure that the Lino
web server process has write permission to it.

Creating a desktop link to the local configuration directory
============================================================

The template manager should have a **link on their desktop** so that
they can easily access the configuration directory using their GUI
file manager.

The directory to be shared is the :xfile:`config` subdirectory of your
*project directory*.

If the template manager has an **Ubuntu desktop** with the default
files manager, then it is easy:

- Open *Files* manager
- Select :menuselection:`File --> Connect to server`
- As the Server Address type something like::  

    sftp://admin@123.456.78.90/path/to/mysite/config
       
Otherwise poke around, consult the documentation of your file manager,
or search the Internet.  If apropriate you might write write
instructions and contribute them so that we can add them here.


Typical workflow
================

Here is a typical workflow for a local template optimization.

- Some user wants some change in a printed output.

- The template manager needs to know a database object that serves as
  example.

- Figure out how to clear the cache and rebuild the printable document
  without creating useless database content such as new excerpts.

- Find out which file is being used as template. Look at the
  :xfile:`lino.log` if you have no idea where to start.
  
- Create a backup copy of the template file.
  
- Make some change, save the template file, rebuild the printable.

- When you are satisfied, remove the backup file.  


Implementation details
======================

- :attr:`lino.core.site.Site.cache_dir`
- :mod:`lino.utils.config`

