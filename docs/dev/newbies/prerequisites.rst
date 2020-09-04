============================
Before starting a mentorship
============================

Before reading this guide, you should have (or acquire) basic experience with
certain topics.  This page gives an overview of what a qualified mentee should
know. The next page will give concrete learning resources.

Linux
=====

When you want to become a Lino developer, there is a first requirement that
might sound hard for those who never tried it: you need to say goodbye to
Windows and move on to Linux.  We don't discuss about this question, but we will
help you with the move.

Lino itself has no specific OS requirements, but on proprietary operating
systems you are likely to encounter problems that are not our business.  For
example some dependencies are more difficult to install on these systems.  If
you are using Windows as your primary OS, we recommend to switch to Ubuntu
before going on.


Python
======

Lino is mostly written in the Python programming language. You need to know for
example

- what's an object, a string, a list, a dict, a float
- the difference between a class method and an instance method
- what's a generator
- what's a decorator
- when and how to use subprocesses and threads
- what are the following standard modules used for:
  `datetime`,  `sys`,  `os`, `re`,  `decimal`,  `logging`, ...
- the major differences between Python 2 and 3

Django
======

Lino applications are Django projects.

- You need to know how to get a Django project up and running.
  (You should have followed the `Tutorial <https://docs.djangoproject.com/en/3.1/>`_)
  You need to know what a :xfile:`settings.py` file is.
- You need to know most about Django's model layer : the ``Model`` class,
  the field types, executing database queries, ...


Git
===

Lino is hosted on Github. You need to know how to use this collaboration
platform.

- You have read the `GitHub Help <https://help.github.com>`_ pages,
  especially the "Bootcamp" and "Setup" sections.
- You have created a free account on GitHub and made a fork of Lino.
- You are able to make some change in your working copy, commit your
  branch and send a pull request.


The UNIX shell
==============

Lino is a web application framework.  You are going to install it on web
servers.  Free people use free operating systems.

- You know the meaning of shell commands like ``ls``, ``cp``, ``rm``,
  ``cd``, ``ls``
- You have written your own bash scripts. You know how to use shell
  variables and functions.
- You know what is a pipe, what is redirection
- You can configure your bash and know about the files :xfile:`.bashrc`
  and :xfile:`.bash_aliases`.


HTML, CSS and Javascript
========================

- You need to understand the meaning of tags like
  ``<body>``, ``<ul>``, ``<li>`` ...
- You should know what an AJAX request is.

Databases
=========

Lino is a part of Django and therefore uses relational databases (SQL). You
don't usually need to write SQL yourself when using Lino, but it is of course
important to understand the concepts behind a database. And on a production
server you will have to deal with database servers like MySQL or PostgreSQL
when doing database snapshots or running migrations.
