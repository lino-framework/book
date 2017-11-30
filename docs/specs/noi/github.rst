.. doctest docs/specs/noi/github.rst
.. _specs.noi.github:

=================
The github module
=================

..  doctest init:
    >>> import lino
    >>> import datetime
    >>> import requests_mock
    >>> lino.startup('lino_book.projects.team.settings.demo')
    >>> from lino.api.doctest import *


Requirements
============
If requests raises::

    SSLError
    ('bad handshake: SysCallError(0, None)',)

You might need the pyOpenssl package. install it with::

    pip install pyopenssl

How it works
============

The :mod:`lino_xl.lib.github` module is a plugin to help with tracking what was
committed by who on what ticket.

It uses git-hub's v3 api to request all commits on the Master branch of any repository.
It is recommended to create a o-auth token for larger repositories beacuse without it there is a limit
of 60 requests per hour.

After the plugin has requested the list of commits it matches the commits to users and tickets by the following logic.

If the commit has a github username associated with it it will try to match the name to a user user
via their Github Username that is set in their My Settings page.
Failing that it will try to match the First name of the Commiter name and User name.
That might change in the future for larger teams.

To match to a ticket it first looks at the description of the ticket,
if there is a ticket number listed in the format of::

    #[0-9]

The commit will be matched to the ticket with that number.

Otherwise it will try to match to a ticket via the associated user's working time by looking for
sessions that were active during the time of committing.

>>> # Mock API response.
>>> json = """[{"sha":"8bac51399644261ce1a216a299a1dd3aa5c63632","commit":{"author":{"name":"Luc Saffre","email":"luc.saffre@gmail.com","date":"2014-07-26T05:02:49Z"},"committer":{"name":"Luc Saffre","email":"luc.saffre@gmail.com","date":"2014-07-26T05:02:49Z"},"message":"http://docs.lino-framework.org/blog/2014/0726.html","tree":{"sha":"c393f1e1401d53c3004d00f3fc7d88200b1ecebf","url":"https://api.github.com/repos/lino-framework/noi/git/trees/c393f1e1401d53c3004d00f3fc7d88200b1ecebf"},"url":"https://api.github.com/repos/lino-framework/noi/git/commits/8bac51399644261ce1a216a299a1dd3aa5c63632","comment_count":0,"verification":{"verified":false,"reason":"unsigned","signature":null,"payload":null}},"url":"https://api.github.com/repos/lino-framework/noi/commits/8bac51399644261ce1a216a299a1dd3aa5c63632","html_url":"https://github.com/lino-framework/noi/commit/8bac51399644261ce1a216a299a1dd3aa5c63632","comments_url":"https://api.github.com/repos/lino-framework/noi/commits/8bac51399644261ce1a216a299a1dd3aa5c63632/comments","author":{"login":"lsaffre","id":4406823,"avatar_url":"https://avatars0.githubusercontent.com/u/4406823?v=4","gravatar_id":"","url":"https://api.github.com/users/lsaffre","html_url":"https://github.com/lsaffre","followers_url":"https://api.github.com/users/lsaffre/followers","following_url":"https://api.github.com/users/lsaffre/following{/other_user}","gists_url":"https://api.github.com/users/lsaffre/gists{/gist_id}","starred_url":"https://api.github.com/users/lsaffre/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lsaffre/subscriptions","organizations_url":"https://api.github.com/users/lsaffre/orgs","repos_url":"https://api.github.com/users/lsaffre/repos","events_url":"https://api.github.com/users/lsaffre/events{/privacy}","received_events_url":"https://api.github.com/users/lsaffre/received_events","type":"User","site_admin":false},"committer":{"login":"lsaffre","id":4406823,"avatar_url":"https://avatars0.githubusercontent.com/u/4406823?v=4","gravatar_id":"","url":"https://api.github.com/users/lsaffre","html_url":"https://github.com/lsaffre","followers_url":"https://api.github.com/users/lsaffre/followers","following_url":"https://api.github.com/users/lsaffre/following{/other_user}","gists_url":"https://api.github.com/users/lsaffre/gists{/gist_id}","starred_url":"https://api.github.com/users/lsaffre/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lsaffre/subscriptions","organizations_url":"https://api.github.com/users/lsaffre/orgs","repos_url":"https://api.github.com/users/lsaffre/repos","events_url":"https://api.github.com/users/lsaffre/events{/privacy}","received_events_url":"https://api.github.com/users/lsaffre/received_events","type":"User","site_admin":false},"parents":[{"sha":"54d694931acc7c66c93deebd6a1377e9480360df","url":"https://api.github.com/repos/lino-framework/noi/commits/54d694931acc7c66c93deebd6a1377e9480360df","html_url":"https://github.com/lino-framework/noi/commit/54d694931acc7c66c93deebd6a1377e9480360df"}]},{"sha":"54d694931acc7c66c93deebd6a1377e9480360df","commit":{"author":{"name":"Luc Saffre","email":"luc.saffre@gmail.com","date":"2014-07-08T20:11:05Z"},"committer":{"name":"Luc Saffre","email":"luc.saffre@gmail.com","date":"2014-07-08T20:11:05Z"},"message":"http://docs.lino-framework.org/blog/2014/0708.html","tree":{"sha":"6faf8947e41f6af957aeeffc728931decbc29c9b","url":"https://api.github.com/repos/lino-framework/noi/git/trees/6faf8947e41f6af957aeeffc728931decbc29c9b"},"url":"https://api.github.com/repos/lino-framework/noi/git/commits/54d694931acc7c66c93deebd6a1377e9480360df","comment_count":0,"verification":{"verified":false,"reason":"unsigned","signature":null,"payload":null}},"url":"https://api.github.com/repos/lino-framework/noi/commits/54d694931acc7c66c93deebd6a1377e9480360df","html_url":"https://github.com/lino-framework/noi/commit/54d694931acc7c66c93deebd6a1377e9480360df","comments_url":"https://api.github.com/repos/lino-framework/noi/commits/54d694931acc7c66c93deebd6a1377e9480360df/comments","author":{"login":"lsaffre","id":4406823,"avatar_url":"https://avatars0.githubusercontent.com/u/4406823?v=4","gravatar_id":"","url":"https://api.github.com/users/lsaffre","html_url":"https://github.com/lsaffre","followers_url":"https://api.github.com/users/lsaffre/followers","following_url":"https://api.github.com/users/lsaffre/following{/other_user}","gists_url":"https://api.github.com/users/lsaffre/gists{/gist_id}","starred_url":"https://api.github.com/users/lsaffre/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lsaffre/subscriptions","organizations_url":"https://api.github.com/users/lsaffre/orgs","repos_url":"https://api.github.com/users/lsaffre/repos","events_url":"https://api.github.com/users/lsaffre/events{/privacy}","received_events_url":"https://api.github.com/users/lsaffre/received_events","type":"User","site_admin":false},"committer":{"login":"lsaffre","id":4406823,"avatar_url":"https://avatars0.githubusercontent.com/u/4406823?v=4","gravatar_id":"","url":"https://api.github.com/users/lsaffre","html_url":"https://github.com/lsaffre","followers_url":"https://api.github.com/users/lsaffre/followers","following_url":"https://api.github.com/users/lsaffre/following{/other_user}","gists_url":"https://api.github.com/users/lsaffre/gists{/gist_id}","starred_url":"https://api.github.com/users/lsaffre/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lsaffre/subscriptions","organizations_url":"https://api.github.com/users/lsaffre/orgs","repos_url":"https://api.github.com/users/lsaffre/repos","events_url":"https://api.github.com/users/lsaffre/events{/privacy}","received_events_url":"https://api.github.com/users/lsaffre/received_events","type":"User","site_admin":false},"parents":[{"sha":"e2ac08a8031fecd19c96117a787b5c932bf223a8","url":"https://api.github.com/repos/lino-framework/noi/commits/e2ac08a8031fecd19c96117a787b5c932bf223a8","html_url":"https://github.com/lino-framework/noi/commit/e2ac08a8031fecd19c96117a787b5c932bf223a8"}]},{"sha":"e2ac08a8031fecd19c96117a787b5c932bf223a8","commit":{"author":{"name":"Luc Saffre","email":"luc.saffre@gmail.com","date":"2014-07-07T06:28:30Z"},"committer":{"name":"Luc Saffre","email":"luc.saffre@gmail.com","date":"2014-07-07T06:28:30Z"},"message":"http://docs.lino-framework.org/blog/2014/0707.html","tree":{"sha":"3830629468f25ed5f81f67fe38bad49e03627648","url":"https://api.github.com/repos/lino-framework/noi/git/trees/3830629468f25ed5f81f67fe38bad49e03627648"},"url":"https://api.github.com/repos/lino-framework/noi/git/commits/e2ac08a8031fecd19c96117a787b5c932bf223a8","comment_count":0,"verification":{"verified":false,"reason":"unsigned","signature":null,"payload":null}},"url":"https://api.github.com/repos/lino-framework/noi/commits/e2ac08a8031fecd19c96117a787b5c932bf223a8","html_url":"https://github.com/lino-framework/noi/commit/e2ac08a8031fecd19c96117a787b5c932bf223a8","comments_url":"https://api.github.com/repos/lino-framework/noi/commits/e2ac08a8031fecd19c96117a787b5c932bf223a8/comments","author":{"login":"lsaffre","id":4406823,"avatar_url":"https://avatars0.githubusercontent.com/u/4406823?v=4","gravatar_id":"","url":"https://api.github.com/users/lsaffre","html_url":"https://github.com/lsaffre","followers_url":"https://api.github.com/users/lsaffre/followers","following_url":"https://api.github.com/users/lsaffre/following{/other_user}","gists_url":"https://api.github.com/users/lsaffre/gists{/gist_id}","starred_url":"https://api.github.com/users/lsaffre/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lsaffre/subscriptions","organizations_url":"https://api.github.com/users/lsaffre/orgs","repos_url":"https://api.github.com/users/lsaffre/repos","events_url":"https://api.github.com/users/lsaffre/events{/privacy}","received_events_url":"https://api.github.com/users/lsaffre/received_events","type":"User","site_admin":false},"committer":{"login":"lsaffre","id":4406823,"avatar_url":"https://avatars0.githubusercontent.com/u/4406823?v=4","gravatar_id":"","url":"https://api.github.com/users/lsaffre","html_url":"https://github.com/lsaffre","followers_url":"https://api.github.com/users/lsaffre/followers","following_url":"https://api.github.com/users/lsaffre/following{/other_user}","gists_url":"https://api.github.com/users/lsaffre/gists{/gist_id}","starred_url":"https://api.github.com/users/lsaffre/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lsaffre/subscriptions","organizations_url":"https://api.github.com/users/lsaffre/orgs","repos_url":"https://api.github.com/users/lsaffre/repos","events_url":"https://api.github.com/users/lsaffre/events{/privacy}","received_events_url":"https://api.github.com/users/lsaffre/received_events","type":"User","site_admin":false},"parents":[{"sha":"742de256c933f2beba0a03d64acf788c1d4f4c16","url":"https://api.github.com/repos/lino-framework/noi/commits/742de256c933f2beba0a03d64acf788c1d4f4c16","html_url":"https://github.com/lino-framework/noi/commit/742de256c933f2beba0a03d64acf788c1d4f4c16"}]},{"sha":"742de256c933f2beba0a03d64acf788c1d4f4c16","commit":{"author":{"name":"Luc Saffre","email":"luc.saffre@gmail.com","date":"2014-07-07T06:22:58Z"},"committer":{"name":"Luc Saffre","email":"luc.saffre@gmail.com","date":"2014-07-07T06:22:58Z"},"message":"first commit","tree":{"sha":"ec3c6a89dfbc0253837721e257245658b01894da","url":"https://api.github.com/repos/lino-framework/noi/git/trees/ec3c6a89dfbc0253837721e257245658b01894da"},"url":"https://api.github.com/repos/lino-framework/noi/git/commits/742de256c933f2beba0a03d64acf788c1d4f4c16","comment_count":0,"verification":{"verified":false,"reason":"unsigned","signature":null,"payload":null}},"url":"https://api.github.com/repos/lino-framework/noi/commits/742de256c933f2beba0a03d64acf788c1d4f4c16","html_url":"https://github.com/lino-framework/noi/commit/742de256c933f2beba0a03d64acf788c1d4f4c16","comments_url":"https://api.github.com/repos/lino-framework/noi/commits/742de256c933f2beba0a03d64acf788c1d4f4c16/comments","author":{"login":"lsaffre","id":4406823,"avatar_url":"https://avatars0.githubusercontent.com/u/4406823?v=4","gravatar_id":"","url":"https://api.github.com/users/lsaffre","html_url":"https://github.com/lsaffre","followers_url":"https://api.github.com/users/lsaffre/followers","following_url":"https://api.github.com/users/lsaffre/following{/other_user}","gists_url":"https://api.github.com/users/lsaffre/gists{/gist_id}","starred_url":"https://api.github.com/users/lsaffre/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lsaffre/subscriptions","organizations_url":"https://api.github.com/users/lsaffre/orgs","repos_url":"https://api.github.com/users/lsaffre/repos","events_url":"https://api.github.com/users/lsaffre/events{/privacy}","received_events_url":"https://api.github.com/users/lsaffre/received_events","type":"User","site_admin":false},"committer":{"login":"lsaffre","id":4406823,"avatar_url":"https://avatars0.githubusercontent.com/u/4406823?v=4","gravatar_id":"","url":"https://api.github.com/users/lsaffre","html_url":"https://github.com/lsaffre","followers_url":"https://api.github.com/users/lsaffre/followers","following_url":"https://api.github.com/users/lsaffre/following{/other_user}","gists_url":"https://api.github.com/users/lsaffre/gists{/gist_id}","starred_url":"https://api.github.com/users/lsaffre/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lsaffre/subscriptions","organizations_url":"https://api.github.com/users/lsaffre/orgs","repos_url":"https://api.github.com/users/lsaffre/repos","events_url":"https://api.github.com/users/lsaffre/events{/privacy}","received_events_url":"https://api.github.com/users/lsaffre/received_events","type":"User","site_admin":false},"parents":[]}]"""
>>> repo = rt.models.github.Repository(user_name='lino-framework',repo_name='noi')
>>> repo.save()
>>> #Unknown Create base request?
>>> ses=rt.login('robin')
>>> with requests_mock.mock() as m:
...     m.get('https://api.github.com/repos/lino-framework/noi/commits?per_page=100&page=1&sha=8bac51399644261ce1a216a299a1dd3aa5c63632', text=json)
...     repo.import_all_commits(ses, sha='8bac51399644261ce1a216a299a1dd3aa5c63632')
>>> rt.show(github.Commit)
==================== ========================================== ======== ======== ================== ==================================================== =========================== =========
 Repository           Sha Hash                                   Ticket   Author   Github User Name   Summary                                              Created                     Comment
-------------------- ------------------------------------------ -------- -------- ------------------ ---------------------------------------------------- --------------------------- ---------
 lino-framework:noi   8bac51399644261ce1a216a299a1dd3aa5c63632            Luc      lsaffre            http://docs.lino-framework.org/blog/2014/0726.html   2014-07-26 05:02:49+00:00
 lino-framework:noi   54d694931acc7c66c93deebd6a1377e9480360df            Luc      lsaffre            http://docs.lino-framework.org/blog/2014/0708.html   2014-07-08 20:11:05+00:00
 lino-framework:noi   e2ac08a8031fecd19c96117a787b5c932bf223a8            Luc      lsaffre            http://docs.lino-framework.org/blog/2014/0707.html   2014-07-07 06:28:30+00:00
 lino-framework:noi   742de256c933f2beba0a03d64acf788c1d4f4c16            Luc      lsaffre            first commit                                         2014-07-07 06:22:58+00:00
==================== ========================================== ======== ======== ================== ==================================================== =========================== =========
<BLANKLINE>
>>> s = rt.models.clocking.Session(ticket = rt.models.tickets.Ticket.objects.get(pk = 1), user = rt.models.users.User.objects.get(first_name="Luc"))
>>> s.start_date, s.end_time = rt.models.github.Commit.objects.all()[0].created.date(), rt.models.github.Commit.objects.all()[0].created.time()
>>> s.start_time = datetime.datetime.combine(datetime.datetime.today(), s.end_time ) - datetime.timedelta(seconds = 60)
>>> s.start_time = s.start_time.time()
>>> s.end_date = s.start_date
>>> s.full_clean()
>>> s.save()
>>> with requests_mock.mock() as m:
...     m.get('https://api.github.com/repos/lino-framework/noi/commits?per_page=100&page=1&sha=8bac51399644261ce1a216a299a1dd3aa5c63632', text=json)
...     repo.import_all_commits(ses, sha='8bac51399644261ce1a216a299a1dd3aa5c63632')
>>> rt.show(github.Commit)
==================== ========================================== ================================== ======== ================== ==================================================== =========================== =========
 Repository           Sha Hash                                   Ticket                             Author   Github User Name   Summary                                              Created                     Comment
-------------------- ------------------------------------------ ---------------------------------- -------- ------------------ ---------------------------------------------------- --------------------------- ---------
 lino-framework:noi   8bac51399644261ce1a216a299a1dd3aa5c63632   #1 (⛶ Föö fails to bar when baz)   Luc      lsaffre            http://docs.lino-framework.org/blog/2014/0726.html   2014-07-26 05:02:49+00:00
 lino-framework:noi   54d694931acc7c66c93deebd6a1377e9480360df                                      Luc      lsaffre            http://docs.lino-framework.org/blog/2014/0708.html   2014-07-08 20:11:05+00:00
 lino-framework:noi   e2ac08a8031fecd19c96117a787b5c932bf223a8                                      Luc      lsaffre            http://docs.lino-framework.org/blog/2014/0707.html   2014-07-07 06:28:30+00:00
 lino-framework:noi   742de256c933f2beba0a03d64acf788c1d4f4c16                                      Luc      lsaffre            first commit                                         2014-07-07 06:22:58+00:00
==================== ========================================== ================================== ======== ================== ==================================================== =========================== =========
<BLANKLINE>

>>> s.ticket = rt.models.tickets.Ticket.objects.get(pk = 2)
>>> s.id, s1id = None, s.id
>>> s.save()
>>> with requests_mock.mock() as m:
...     m.get('https://api.github.com/repos/lino-framework/noi/commits?per_page=100&page=1&sha=8bac51399644261ce1a216a299a1dd3aa5c63632', text=json)
...     repo.import_all_commits(ses, sha='8bac51399644261ce1a216a299a1dd3aa5c63632')
>>> rt.show(github.Commit)
==================== ========================================== ================================== ======== ================== ==================================================== =========================== ================================================================
 Repository           Sha Hash                                   Ticket                             Author   Github User Name   Summary                                              Created                     Comment
-------------------- ------------------------------------------ ---------------------------------- -------- ------------------ ---------------------------------------------------- --------------------------- ----------------------------------------------------------------
 lino-framework:noi   8bac51399644261ce1a216a299a1dd3aa5c63632   #1 (⛶ Föö fails to bar when baz)   Luc      lsaffre            http://docs.lino-framework.org/blog/2014/0726.html   2014-07-26 05:02:49+00:00   #1 (⛶ Föö fails to bar when baz), #2 (☎ Bar is not always baz)
 lino-framework:noi   54d694931acc7c66c93deebd6a1377e9480360df                                      Luc      lsaffre            http://docs.lino-framework.org/blog/2014/0708.html   2014-07-08 20:11:05+00:00
 lino-framework:noi   e2ac08a8031fecd19c96117a787b5c932bf223a8                                      Luc      lsaffre            http://docs.lino-framework.org/blog/2014/0707.html   2014-07-07 06:28:30+00:00
 lino-framework:noi   742de256c933f2beba0a03d64acf788c1d4f4c16                                      Luc      lsaffre            first commit                                         2014-07-07 06:22:58+00:00
==================== ========================================== ================================== ======== ================== ==================================================== =========================== ================================================================
<BLANKLINE>
>>> s.delete()
>>> s.id = s1id
>>> s.delete()
>>> repo.commits.all().delete()
(4, {u'github.Commit': 4})
>>> repo.delete()

#1081 (☉ Rename "kernel" to "environment"), #1108 (☑ RemovedInDjango110Warning: SubfieldBase has been deprecated), #1096 (☑ Paramètres par défaut dans [Bénéficiaires]), #1044 (⚒ Miscellaneous regular maintenance and support), #1130 (☎ Erik), #1071 (☉ Get
