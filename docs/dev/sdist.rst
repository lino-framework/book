.. _dev.sdist:

================================
Publishing a new version of Lino
================================


Generate Lino packages
======================
We can use atelier to generate for us the installable packages for lino, but the need the be sure that sdist_dir is
correctly set in your invoke.py. It should be some value like ::

        sdist_dir = '/home/khchine5/PycharmProjects/lino/book/docs/dl/{prj}'

Atelier will replace the {prj} variable with the name of the current projet.

To generate lino packages for all lino projects, we use the command ::

        $ pp inv sdist

Test Lino packages
======================
Lino use his own repository to host the generated packages for testing before publishing officially on the Pypi. To
publish the docs and Lino packages to use the usual commands ::

        $ go book
        $ inv bd pd

Once it is done, we can use https://lino-framework.org/dl/ as our main repository to install Lino using the following
 command with a fresh virtualenv ::

        pip install --index-url http://lino-framework.org/dl lino --trusted-host lino-framework.org --extra-index-url
        https://pypi.org/simple

