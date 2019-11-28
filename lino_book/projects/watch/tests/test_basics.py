# -*- coding: utf-8 -*-
# Copyright 2017-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Basic tests.

This module is part of the Lino test suite. You can test only this
module by issuing either::

  $ go watch
  $ python manage.py test tests.test_basics

or::

  $ go lino
  $ python setup.py test -s tests.ProjectsTests.test_watch


"""

from __future__ import unicode_literals
from __future__ import print_function

import six
from django.conf import settings

from lino.utils.djangotest import RemoteAuthTestCase

from lino.core.callbacks import popCallBack, applyCallbackChoice
class QuickTest(RemoteAuthTestCase):

    # fixtures = ['demo', 'demo2']
    maxDiff = None

    def test_this(self):

        from lino.api import rt
        from lino.core.renderer import TestRenderer
        
        UserTypes = rt.models.users.UserTypes        
        rt.models.users.User(
            username="robin", user_type=UserTypes.admin).save()
        
        ses = rt.login('robin', renderer=TestRenderer(settings.SITE.kernel.default_ui))

        s = ses.show('changes.Changes')
        self.assertEqual(s, "No data to display")


        rr = rt.models.contacts.Companies.required_roles
        self.assertTrue(ses.user.user_type.role.satisfies_requirement(rr))

        # We create a new organization:

        url = '/api/contacts/Companies'
        data = dict(an='submit_insert', name='My pub')
        res = self.post_json_dict('robin', url, data)
        self.assertEqual(
            res.message, 'Organization "My pub" has been created.')

        s = ses.show('changes.Changes',
                     column_names="id type master object diff")
        # print(s)
        expected = """\
==== ============= ========== ========================================== ===============================================
 ID   Change Type   Master     Object                                     Changes
---- ------------- ---------- ------------------------------------------ -----------------------------------------------
 1    Create        *My pub*   `My pub </api/contacts/Companies/100>`__   Company(id=100,name='My pub',partner_ptr=100)
==== ============= ========== ========================================== ===============================================
"""
        
        self.assertEqual(s, expected)
        
        url = '/api/contacts/Companies/100'
        data = "an=submit_detail&name=Our%20pub"
        res = self.put_json_dict('robin', url, data)
        self.assertEqual(
            res.message, 'Organization "Our pub" has been updated.')

        output = ses.show('changes.Changes', column_names="id type master object diff")
        # print(output)
        expected = """\
==== ============= =========== =========================================== ===============================================
 ID   Change Type   Master      Object                                      Changes
---- ------------- ----------- ------------------------------------------- -----------------------------------------------
 2    Update        *Our pub*   `Our pub </api/contacts/Companies/100>`__   name : 'My pub' --> 'Our pub'
 1    Create        *Our pub*   `Our pub </api/contacts/Companies/100>`__   Company(id=100,name='My pub',partner_ptr=100)
==== ============= =========== =========================================== ===============================================
"""
        self.assertEqual(output, expected)

        # We add an entry:

        url = '/api/entries/Entries'
        data = dict(an='submit_insert', subject='test', companyHidden=100)
        res = self.post_json_dict('robin', url, data)
        if six.PY2:
            self.assertEqual(
                res.message, 'Entry "Entry object" has been created.')
        else:
            self.assertEqual(
                res.message, 'Entry "Entry object (1)" has been created.')

        expected = """\
==== ============= =========== =============================================== ===============================================
 ID   Change Type   Master      Object                                          Changes
---- ------------- ----------- ----------------------------------------------- -----------------------------------------------
 3    Create        *Our pub*   `Entry object (1) </api/entries/Entries/1>`__   Entry(id=1,user=1,subject='test',company=100)
 2    Update        *Our pub*   `Our pub </api/contacts/Companies/100>`__       name : 'My pub' --> 'Our pub'
 1    Create        *Our pub*   `Our pub </api/contacts/Companies/100>`__       Company(id=100,name='My pub',partner_ptr=100)
==== ============= =========== =============================================== ===============================================
"""

        output = ses.show('changes.Changes',
                     column_names="id type master object diff")
        # print(output)
        self.assertEqual(output, expected)
        
        
        # Now we delete the entry:

        url = '/api/entries/Entries/1'
        data = dict(an='delete_selected', sr=1)
        res = self.get_json_dict('robin', url, data)
        if six.PY2:
            self.assertEqual(
            res.message, """\
You are about to delete 1 Entry:
Entry object
Are you sure ?""")
        else:
            self.assertEqual(
                res.message, """\
You are about to delete 1 Entry:
Entry object (1)
Are you sure ?""")

        
        
        # We answer "yes":
        applyCallbackChoice(res, data, "yes")
        # url = "/callbacks/{0}/yes".format(res['xcallback']['id'])
        # print(data)
        res = self.get_json_dict('robin', url, data)
        # print(res)
        # r = test_client.get(url)
        self.assertEqual(res.success, True)
        self.assertEqual(res.record_deleted, True)
        

        expected = """\
==== ============= =========== =========================================== ===============================================
 ID   Change Type   Master      Object                                      Changes
---- ------------- ----------- ------------------------------------------- -----------------------------------------------
 4    Delete        *Our pub*                                               Entry(id=1,user=1,subject='test',company=100)
 3    Create        *Our pub*                                               Entry(id=1,user=1,subject='test',company=100)
 2    Update        *Our pub*   `Our pub </api/contacts/Companies/100>`__   name : 'My pub' --> 'Our pub'
 1    Create        *Our pub*   `Our pub </api/contacts/Companies/100>`__   Company(id=100,name='My pub',partner_ptr=100)
==== ============= =========== =========================================== ===============================================
"""
        output = ses.show('changes.Changes',
                     column_names="id type master object diff")
        # print(output)
        self.assertEqual(output, expected)

        # Note how the `object` column of the first two rows in above
        # table is empty. That's because the entry object has been
        # deleted, so it does no longer exist in the database and Lino
        # cannot point to it. But note also that `object` is a
        # "nullable Generic ForeignKey", the underlying fields
        # `object_id` and `object_type` still contain their
        # values. Here is the same table with "Object" split into its
        # components:

        expected = """\
==== ============= =========== ============== =========== ===============================================
 ID   Change Type   Master      Object type    object id   Changes
---- ------------- ----------- -------------- ----------- -----------------------------------------------
 4    Delete        *Our pub*   Entry          1           Entry(id=1,user=1,subject='test',company=100)
 3    Create        *Our pub*   Entry          1           Entry(id=1,user=1,subject='test',company=100)
 2    Update        *Our pub*   Organization   100         name : 'My pub' --> 'Our pub'
 1    Create        *Our pub*   Organization   100         Company(id=100,name='My pub',partner_ptr=100)
==== ============= =========== ============== =========== ===============================================
"""
        output = ses.show('changes.Changes',
                     column_names="id type master object_type object_id diff")
        # print(output)
        self.assertEqual(output, expected)


# Until 20150626 only the
# :attr:`object<lino.modlib.changes.models.Change.object>` was nullable,
# not the :attr:`master<lino.modlib.changes.models.Change.master>`.  But
# now you can also delete the master, and all change records will still
# remain:

        url = '/api/contacts/Companies/100'
        data = dict(an='delete_selected', sr=100)
        res = self.get_json_dict('robin', url, data)
        applyCallbackChoice(res, data, "yes")
        # url = "/callbacks/{0}/yes".format(res.xcallback['id'])
        self.get_json_dict('robin', url, data)
        
        expected = """\
==== ============= ======== ======== ================================================
 ID   Change Type   Master   Object   Changes
---- ------------- -------- -------- ------------------------------------------------
 5    Delete                          Company(id=100,name='Our pub',partner_ptr=100)
 4    Delete                          Entry(id=1,user=1,subject='test',company=100)
 3    Create                          Entry(id=1,user=1,subject='test',company=100)
 2    Update                          name : 'My pub' --> 'Our pub'
 1    Create                          Company(id=100,name='My pub',partner_ptr=100)
==== ============= ======== ======== ================================================
"""
        output = ses.show('changes.Changes',
                     column_names="id type master object diff")
        # print(output)
        self.assertEqual(output, expected)
        

        # Of course these change records are now considered broken GFKs:

        expected = """\
================================================ ================================= ============================================================= ========
 Database model                                   Database object                   Message                                                       Action
------------------------------------------------ --------------------------------- ------------------------------------------------------------- --------
 `Change </api/contenttypes/ContentTypes/14>`__   `#1 </api/changes/Changes/1>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
 `Change </api/contenttypes/ContentTypes/14>`__   `#2 </api/changes/Changes/2>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
 `Change </api/contenttypes/ContentTypes/14>`__   `#3 </api/changes/Changes/3>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
 `Change </api/contenttypes/ContentTypes/14>`__   `#4 </api/changes/Changes/4>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
 `Change </api/contenttypes/ContentTypes/14>`__   `#5 </api/changes/Changes/5>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
 `Change </api/contenttypes/ContentTypes/14>`__   `#1 </api/changes/Changes/1>`__   Invalid primary key 100 for contacts.Company in `object_id`   clear
 `Change </api/contenttypes/ContentTypes/14>`__   `#2 </api/changes/Changes/2>`__   Invalid primary key 100 for contacts.Company in `object_id`   clear
 `Change </api/contenttypes/ContentTypes/14>`__   `#3 </api/changes/Changes/3>`__   Invalid primary key 1 for entries.Entry in `object_id`        clear
 `Change </api/contenttypes/ContentTypes/14>`__   `#4 </api/changes/Changes/4>`__   Invalid primary key 1 for entries.Entry in `object_id`        clear
 `Change </api/contenttypes/ContentTypes/14>`__   `#5 </api/changes/Changes/5>`__   Invalid primary key 100 for contacts.Company in `object_id`   clear
================================================ ================================= ============================================================= ========
"""
        output = ses.show('gfks.BrokenGFKs')
        # print(output)
        self.assertEqual(output, expected)
        
        # There open questions regarding these change records:

        # - Do we really never want to remove them? Do we really want a nullable
        #   master field? Should this option be configurable?
        # - How to tell :class:`lino.modlib.gfks.models.BrokenGFKs` to
        #   differentiate them from ?
        # - Should :meth:`get_broken_generic_related
        #   <lino.core.kernel.Kernel.get_broken_generic_related>` suggest to
        #   "clear" nullable GFK fields?

