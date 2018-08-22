.. _dev.release:

================================
Publishing to the official PyPI
================================

When :doc:`sdist` is done, here we go for releasing a new version of
Lino to the world.

Of course you need maintainer's permission on PyPI for all projects.

You also need to configure your :xfile:`~/.pypirc` file::

    [distutils]
    index-servers =
        pypi

    [pypi]
    username:joe.doe
    password:My password


Run :cmd:`inv release` on every project::

  $ pp inv release

It will automatically create a git tag and then call twine.


  
