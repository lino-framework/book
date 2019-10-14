.. _dev.request_pull:

============================
How to submit a pull request
============================

.. _dev.patch:

Send a patch
============

The easiest and most basic way of contributing a code change is to send a patch.
Here is how to do that.

- Go to the project root directory and type::

    $ git diff > mypatch.txt

- Send the file :file:`mypatch.txt` or its content via e-mail to
  `lino-developers@lino-framework.org` or directly to a committer (somebody who
  has write permission to the public code repositories).

One disadvantage of this method is that your contribution is not visible in the
history of the repository.

Using GitHub
============

You use the GitHub web interface as explained
in `Creating a pull request
<https://help.github.com/articles/creating-a-pull-request/>`_.
We accept this way of communication.



Using :cmd:`git request-pull`
=============================

Here are some thoughts about this:

- `How to make pull requests *without* a github account?
  <http://stackoverflow.com/questions/9630774/how-to-make-pull-requests-without-a-github-account>`__
  (2012-03-09)

- `Why Linus Thorvalds doesn't do github pull requests.
  <https://github.com/torvalds/linux/pull/17#issuecomment-5654674>`__
  (2012-05-11)

- The `git request-pull <https://git-scm.com/docs/git-request-pull>`__
  command.

The following would be our recommended way of making pull requests.

Preparation:

- Make sure that you have no local changes in your project
  repositories.

- Create a fork (on GitHub or somewhere else) of the repositories you
  are going to work on.

- Change the `remote` of your local copy so that it points to your
  fork. Add an *upstram* remote. Setup your git credentials.  (TODO:
  explain more details)


For each request:

- Work in your local clone of that repository.

- Publish the changes in your working copy to your public repository
  using :cmd:`inv ci` or :cmd:`git commit` and :cmd:`git push`.

- run :cmd:`git request-pull`



Pushing directly to master branch?
==================================

Hell is when people push directly to master branch.
That's at least what  `this
thread on Reddit
<https://www.reddit.com/r/ProgrammerHumor/comments/dh87ae/dante_would_be_proud/>`__
suggests. The resulting discussion is interesting.
Obviously there are
different religious schools about the topic.

Some quotes of the comments:

- Who lets people push to master without a pull request and code review?

  It depends on what the workflow for git is. If you CI/CD deploys to production
  on a push to master, well you shouldn't push to master obviously. If "master"
  is the bleeding edge branch that may be broken from time to time, then it's
  not that big of a big deal. For example, Google does it that way in Flutter.
  Master is only "Usually functional, though sometimes we accidentally break
  things.". After testing, master gets merged into "dev", then "beta", then
  "stable".

  We push to master in my current role and I have in all my jobs for the last
  10+ years. We do ci/cd, feature toggles and automated testing. Pairing is how
  we do code reviews. Honestly nothing wrong with it 🙂
