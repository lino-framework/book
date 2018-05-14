.. _devblog:

=============================
Start your own developer blog
=============================

This section explains what a **developer blog** is, why you need it,
why *we* need it, and how you do it.



Documenting what you do
=======================

The basic idea of a developer blog is that you **leave a trace** about
what you have been doing, and that this trace is accessible in a
**public place** to everybody, including future contributors who might
want to explore **why you have been doing** things the way you did
them.  When you work on a free software project, documenting what you
do is more important than actually doing it.

The daily work of a software developer includes things like modifying
source code, pushing changes to public repositories, writing comments
in forums, surfing around, reading books, discovering new
technologies, contributing to other projects... 

In your developer blog you simply describe what you are doing. You
report about your daily work in order to share your experiences, your
know-how, your successes, your failures and your stumblings.  Day by
day. Using plain English language. It is your diary.



How to document what you do
===========================

You should begin privately without going public.  My first developer
blog was a simple plain text file (one per month) where I simply noted
every code change for myself.  

That's because in the beginning

If you don't dare going public right now, then do it locally and keep
it like a private notebook for yourself.

A developer blog **does not need** to be cool, exciting, popular or
easy to follow.  It **should rather be**:

- **complete** (e.g. not forget to mention any important code
  change you did)
- **concise** (e.g. avoid re-explaining things that are explained somewhere
  else)
- **understandable** (e.g. use references to point to these other
  places so that anybody with enough time and motivation has a chance
  to follow).

Note that these qulities are listed in order of difficulty.  Being
complete is rather easy and just a question of motivation.  It takes
some exercise to stay concise without becoming incomplete.  And being
understandable takes even more time.  I often just try to be
understandable at least to myself.  It happens quite often that I want
to know why I did some change one year ago, and that I am amazed about
how much I forgot during this year.

Your blog is a diary, but keep in mind that it is **public**. The
usual rules apply:

- Don't disclose any passwords or private data.
- Respect other people's privacy.
- Don't quote other author's words without naming them.
- Reference your sources of information.

A public developer blog can be the easiest way to ask for help in
complex cases which need screenshots, links, sections etc.


Luc's blogging system
=====================

You probably know already one example of a public developer blog,
namely `Luc's developer blog <http://luc.lino-framework.org>`_.  The
remaining sections describe how you can use Luc's system for your own
blog.

You may of course use another blogging system (blogger.com,
wordpress.com etc,), especially if you have been blogging before.

Luc's developer blog is free, simple and extensible.  
It answers well to certain requirements which we perceive as
important:

- A developer uses some editor for writing code, and wants to use that
  same editor for writing his blog.

- A developer usually works on more than one software projects at a
  time.

- A developer should not be locked just because there is no internet
  connection available for a few hours.

It is based on `Sphinx <http://sphinx-doc.org/>`_ which is the
established standard for Python projects. This has the advantage that
your blog has the same syntax as your docstrings.

Followers can subscribe to it using an RSS reader.


"Blog" versus "Documentation tree"
==================================

Luc's blogging system uses *daily* entries (maximum one blog entry per
day), and is part of some Sphinx documentation tree.

But don't mix up "a blog" with "a documentation tree".  You will
probably maintain only one *developer blog*, but you will maintain
many different *documentation trees*.  Not every documentation tree
contains a blog.

You probably will soon have other documentation trees than the one
which contains your blog. For example your first Lino application
might have a local project name "hello", and it might have two
documentation trees, one in English (`hello/docs`) and another in
Spanish (`hello/docs_es`). `fab pd` would upload them to
`public_html/hello_docs` and `public_html/hello_docs_es` respectively.
See :attr:`env.docs_rsync_dest <atelier.fablib.env.docs_rsync_dest>`.


.. _dblog:

The `dblog` project template
============================

To help you get started with blogging in your own developer blog,
there is a project template at https://github.com/lsaffre/dblog


.. You may find inspiration from the Lino website for configuring your
   developer blog.

    - Interesting files are:
      :file:`/docs/conf.py`
      :file:`/docs/.templates/layout.html`
      :file:`/docs/.templates/links.html`
