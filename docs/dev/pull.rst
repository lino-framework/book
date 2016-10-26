.. _dev.git_pull:
.. _pull.sh:

===========================================
How to update your copy of the repositories
===========================================

Since Lino is in constant development, you will probably often do the
following::

  $ cd ~/repositories
  $ cd atelier ; git pull ; cd ..
  $ cd lino ; git pull ; cd ..
  $ cd xl ; git pull ; cd ..
  $ cd noi ; git pull ; cd ..
  $ cd cosi ; git pull ; cd ..
  $ cd welfare ; git pull ; cd ..
  $ cd voga ; git pull ; cd ..
  ...
  $ find ~/repositories -name '*.pyc' -delete

This means that you update your copy ("clone") of these repositories.
Because Lino is a *series of repos* maintained by the same team, it is
recommended to always update all related repos at the same time.

The last line runs :cmd:`find` in order to remove all :file:`.pyc`
(compiled Python) files. See e.g. `here
<http://stackoverflow.com/questions/785519/how-do-i-remove-all-pyc-files-from-a-project>`_
for other methods.  This is not necessary most of the time because
Python automatically recompiles them when needed, but there are
situations where you get problems caused by dangling :file:`.pyc`
files.

Note that you **don't need** to re-run ``pip install`` on these
updated repos since you used the ``-e`` command line option of ``pip
install`` (as instructed in :ref:`lino.dev.install`).

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

