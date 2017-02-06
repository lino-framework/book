.. _lino.dev.demo_projects:

===================
About demo projects
===================

Every code repository can come with a series of demo projects.

A demo project is a project in the Django meaning of the word: a
directory where you can go and run django-admin commands.

Demo projects are used for testing, documentation and demonstration
purposes.

They are defined with the :envvar:`demo_projects` in the repository's
:xfile:`tasks.py` file.

They contain fictive data generated using Python fixtures.

:cmd:`inv prep` initializes all demo projects of a repository.

You can manually initialiae a single demo project by going to it's
directory and running :manage:`prep`.
