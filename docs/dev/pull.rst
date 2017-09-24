.. _dev.git_pull:
.. _pull.sh:

===========================================
How to update your copy of the repositories
===========================================

Lino is in constant development, so you will probably often need to
update your copy of these repositories.  Because Lino is a *series of
repositories* maintained by the same team, it is recommended to always
update all related repositories at the same time.

To update your copy of the Lino sources, you do::

  $ pp git pull

See the documentation of `git pull
<https://git-scm.com/docs/git-pull>`_ for more information.

After running :cmd:`git pull` it is a good idea to run::

  $ pp inv clean -b

This removes all :file:`.pyc` (compiled Python) files.  See e.g. `here
<http://stackoverflow.com/questions/785519/how-do-i-remove-all-pyc-files-from-a-project>`_
for other methods.  This is not necessary most of the time because
Python automatically recompiles them when needed, but there are
situations where you get problems caused by dangling :file:`.pyc`
files.

Note that you **don't need** to re-run ``pip install`` on these
updated repositories since you used the ``-e`` command line option of
``pip install`` (as instructed in :ref:`lino.dev.install`).

Keep in mind the **difference between repositories and virtual
environments**. Cloning a local copy of the Lino repositories from
GitHub is a relatively time-consuming operation (it takes a few
minutes).  Once you have cloned the repositories, you probably won't
need to do this operation again. You just update them using :cmd:`git
pull`. You can also switch them to specific versions using :cmd:`git
checkout`.  But *virtual environments* are cheap. You can easily
create new ones, install Lino into them, throw them away.

It can happen that Lino's **dependencies** change.  And simply pulling
new sources won't update these. One possibility is to find out what's
missing (by reading the error message or the blog or by asking) and
installing the missing packages.  Another (not yet well tested)
possibility can be to create a new virtualenv (as explained in
:ref:`lino.dev.env`).

