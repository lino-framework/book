.. _dev.git_pull:
.. _pull.sh:

===========================================
How to update your copy of the repositories
===========================================

Lino is in constant development, so you will probably often do the
following::

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

This means that you update your copy of these repositories.  Because
Lino is a *series of repositories* maintained by the same team, it is
recommended to always update all related repositories at the same
time.

The last line runs :cmd:`find` in order to remove all :file:`.pyc`
(compiled Python) files. See e.g. `here
<http://stackoverflow.com/questions/785519/how-do-i-remove-all-pyc-files-from-a-project>`_
for other methods.  This is not necessary most of the time because
Python automatically recompiles them when needed, but there are
situations where you get problems caused by dangling :file:`.pyc`
files.

To automate this task, you can create a bash script `pull.sh` like the
following::

    for i in atelier lino xl noi voga presto
    do
        echo $i
        cd repositories/$i
        git pull
        find -name '*.pyc' -delete
        cd ..
    done

See the documentation of `git pull
<https://git-scm.com/docs/git-pull>`_ for more information.

Note that you **don't need** to re-run ``pip install`` on these
updated repositories since you used the ``-e`` command line option of
``pip install`` (as instructed in :ref:`lino.dev.install`).

But note also that it can happen that Lino's *dependencies* change.
And simply pulling new sources won't update these. To prevent problems
caused by obsolete or missing dependencies, the easiest way can be to
create a new virtualenv (as explained in :ref:`lino.dev.env`).
