.. _dev.request_pull:

============================
How to submit a pull request
============================

The simple way would be to use the GitHub web interface as explained
in `Creating a pull request
<https://help.github.com/articles/creating-a-pull-request/>`_.

But life is not simple. Here are some thoughts about this:

- `How to make pull requests *without* a github account?
  <http://stackoverflow.com/questions/9630774/how-to-make-pull-requests-without-a-github-account>`__
  (2012-03-09)

- `Why Linus Thorvalds doesn't do github pull requests.
  <https://github.com/torvalds/linux/pull/17#issuecomment-5654674>`__
  (2012-05-11)

- The `git request-pull <https://git-scm.com/docs/git-request-pull>`__
  command.

So here is our recommended way of making pull requests.

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


  
