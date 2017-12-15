.. _lino.socialauth:

=====================
Social Authentication
=====================

In a Lino application you can easily enable third-party authentication
thanks to `Python Social Auth
<https://github.com/python-social-auth>`__ (PSA).


Specifying the backends
=======================

You must chose which authentication providers you want to offer to
your users.  For each provider you will activate the corresponding
"backend". Available backends are listed `in the PSA documentation
<http://python-social-auth.readthedocs.io/en/latest/backends/>`__.

In your local :xfile:`settings.py` you must set
:attr:`social_auth_backends
<lino.core.site.Site.social_auth_backends>` to a list of the backends
you want to offer on your site.  If you want GitHub, the you will
write::

      class Site(Site):
          ...
          social_auth_backends = [
             'social_core.backends.github.GithubOAuth2']


We got the name of that backend
(``social_core.backends.github.GithubOAuth2``) from the detailed
instructions page for `GitHub
<http://python-social-auth.readthedocs.io/en/latest/backends/github.html>`__.

Note that with Lino, unlike plain Django applications, you do not need
to set :setting:`AUTHENTICATION_BACKENDS` yourself, Lino will do that
for you, based on miscellaneous criteria (and
:attr:`social_auth_backends
<lino.core.site.Site.social_auth_backends>` is only one of them).

Most backends require additional parameters, and you must define them
in your :xfile:`settings.py`. For example::

    SOCIAL_AUTH_GITHUB_KEY = '...'
    SOCIAL_AUTH_GITHUB_SECRET = '...'
  
These codes come from the provider's website where you must create an
"application", and the provider will then give you a "key" and a
"secret".

Setting up your third-party authentication provider
===================================================

Using your account on GitHub, Google, Facebook or any other backend,
you must create an "oauth application" on their website.

with the following parameters:

- Application name: Social Auth Tester
- Homepage URL: http://127.0.0.1:8000/
- Authorization callback URL: http://127.0.0.1:8000/oauth/complete/github

The client secrets of these applications is not really secret
anymore since it is stored in the :xfile:`settings.py` of the team
demo project (more exactly `here
<https://github.com/lino-framework/book/blob/master/lino_book/projects/team/settings/demo.py>`__). But
that's for educational purposes.  In a real setup you will of course
give the public URL of your website, and you will write that secret
only to the :xfile:`settings.py` on your website.


In Facebook you must go to :menuselection:`Products --> Facebook Login
--> Settings` and enabled the following:

    | **Embedded Browser OAuth Login**
    | Enables browser control redirect uri for OAuth client login.



.. figure:: 20171215b.png
    :scale: 50 %
            
    Facebook asking your permission to authenticate you at the "Lino
    authentication" app



A working example
=================

A working example is in the :mod:`lino_book.projects.team` demo
project.  If you have the :doc:`Lino developer environment </dev/install>`
installed, you can test the social auth functionality on your machine
by doing::

    $ go team
    $ python manage.py prep
    $ runserver

Now point your browser to http://127.0.0.1:8000/ and you should see
something like this:

.. figure:: socialauth1.png
    :scale: 80 %

    The Lino Team main page for anonymous users.
            

Note the message **Or sign in using github, googleplus or facebook**.
This works out of the box because we did the work of creating
applications on GitHub, Google+ and Facebook (details about how to do
that see below).


Click on **github**. This will lead you to the GitHub website:

.. figure:: socialauth2.png
    :scale: 80 %
            
    Github asking your permission to authenticate you at the "Lino
    auth tester" app

There you must click on the big green button to tell GitHub that they
may communicate your contact data to the **Social Auth Tester**
application at http://127.0.0.1:8000/ (IOW on you own computer).

.. image:: socialauth3.png

Voilà. You you are now logged in into the Lino Noi running on your
machine, authentified via your GitHub account. You can now edit your
user profile by clicking on **[My settings]**:

.. image:: socialauth4.png

Exercises
=========

- Note that your user type is "user" and that you cannot change this.
  Only administrators can change the user type.
  
- Sign out. Note that your user name is now listed below **This demo
  site has 7 users:**. This list does not show on a real site, it is
  there because :attr:`is_demo_site
  <lino.core.site.Site.is_demo_site>` is `True`.

- Note that you exist as a user, but you can sign in only through
  GitHub. You can not sign in using the
  :class:`lino.modlib.users.SignIn` dialog window because you have no
  password set.
  
- and then sign in as robin (an administrator)


