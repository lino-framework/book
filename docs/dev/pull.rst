.. _dev.git_pull:
.. _pull.sh:

===========================================
How to update your copy of the repositories
===========================================

Lino is in constant development, so you will probably often need to
update your copy of these repositories.  Because Lino is a *series of
repositories* maintained by the same team, it is recommended to always
update all related repositories at the same time.

To update your copy of the Lino sources, you do the following (the
exact list of repositories might differ in your case)::

  $ cd ~/repositories
  $ cd atelier ; git pull ; cd ..
  $ cd lino ; git pull ; cd ..
  $ cd xl ; git pull ; cd ..
  $ cd noi ; git pull ; cd ..
  $ cd cosi ; git pull ; cd ..
  $ cd welfare ; git pull ; cd ..
  $ cd avanti ; git pull ; cd ..
  $ cd voga ; git pull ; cd ..
  ...
  $ find ~/repositories -name '*.pyc' -delete

See the documentation of `git pull
<https://git-scm.com/docs/git-pull>`_ for more information.

The last line runs :cmd:`find` in order to remove all :file:`.pyc`
(compiled Python) files.  See e.g. `here
<http://stackoverflow.com/questions/785519/how-do-i-remove-all-pyc-files-from-a-project>`_
for other methods.  This is not necessary most of the time because
Python automatically recompiles them when needed, but there are
situations where you get problems caused by dangling :file:`.pyc`
files.

To automate this task, you should create a bash script named
:xfile:`pull.sh` with the following content::

    for i in atelier lino xl noi cosi voga presto ; do
        echo $i
        cd repositories/$i
        git pull
        find -name '*.pyc' -delete
        cd ..
    done

Note that you **don't need** to re-run ``pip install`` on these
updated repositories since you used the ``-e`` command line option of
``pip install`` (as instructed in :ref:`lino.dev.install`).

But note also that it can happen that Lino's *dependencies* change.
And simply pulling new sources won't update these. To prevent problems
caused by obsolete or missing dependencies, the easiest way can be to
create a new virtualenv (as explained in :ref:`lino.dev.env`).

Keep in mind the **difference between repositories and virtual
environments***.  Cloning a local copy of the Lino repositories from
GitHub is a relatively time-consuming operation (it takes a few
minutes).  Once you have cloned the repositories, you probably won't
need to do this operation again. You just update them using `git
pull`. You can also switch them to specific versions using `git
checkout`.  But *virtual environments* are cheap. You can easily
create new ones, install Lino into them, throw them away.
