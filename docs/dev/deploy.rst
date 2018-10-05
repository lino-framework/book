.. _team.deploy:

======================
The deployment process
======================


.. toctree::
   :maxdepth: 1


   runtests
   versioning
   sdist
   release

Deployment checklist
====================


- Check you have a clean working copy of all projects maintained by
  the Lino Team.

- Check that all test suites are passing and all doc trees are
  building.

- For every demo project that has a
  :xfile:`test_restore.py` file in its test suite,
  run :manage:`makemigdump`
  and add the new version to the :attr:`tested_versions
  <lino.utils.djangotest.RestoreTestCase.tested_versions>` in the
  :xfile:`test_restore.py` file.
  See :doc:`migtests` for details.
         

- Update the `version` and `install_requires` in the
  :xfile:`setup_info.py` files of each project.

- Run :cmd:`pp inv ci` to commit and push these changes.
  
- Run :cmd:`pp inv sdist` to create a source tarball
  
- Run :cmd:`pp inv release`         

- Update the release notes.

