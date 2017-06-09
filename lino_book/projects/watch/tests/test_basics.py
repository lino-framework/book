# -*- coding: utf-8 -*-
# Copyright 2017 Luc Saffre
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


from lino.utils.djangotest import RemoteAuthTestCase


class QuickTest(RemoteAuthTestCase):

    # fixtures = ['demo', 'demo2']

    def test_this(self):

        from lino.api import rt
        from lino.core.renderer import TestRenderer
        # from lino.core.renderer import JsRenderer as TestRenderer
        
        UserTypes = rt.actors.auth.UserTypes        
        rt.models.auth.User(
            username="robin", user_type=UserTypes.admin).save()
        
        ses = rt.login('robin', renderer=TestRenderer())

        s = ses.show('changes.Changes')
        self.assertEqual(s, "No data to display")


        rr = rt.actors.contacts.Companies.required_roles
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
==== ============= ===================== ===================== ===============================================
 ID   Change Type   Master                Object                Changes
---- ------------- --------------------- --------------------- -----------------------------------------------
 1    Create        `My pub <Detail>`__   `My pub <Detail>`__   Company(id=100,name='My pub',partner_ptr=100)
==== ============= ===================== ===================== ===============================================
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
==== ============= ====================== ====================== ===============================================
 ID   Change Type   Master                 Object                 Changes
---- ------------- ---------------------- ---------------------- -----------------------------------------------
 2    Update        `Our pub <Detail>`__   `Our pub <Detail>`__   name : 'My pub' --> 'Our pub'
 1    Create        `Our pub <Detail>`__   `Our pub <Detail>`__   Company(id=100,name='My pub',partner_ptr=100)
==== ============= ====================== ====================== ===============================================
"""
        self.assertEqual(output, expected)

        # We add an entry:

        url = '/api/entries/Entries'
        data = dict(an='submit_insert', subject='test', companyHidden=100)
        res = self.post_json_dict('robin', url, data)
        self.assertEqual(
            res.message, 'Entry "Entry object" has been created.')
        
        expected = """\
==== ============= ====================== =========================== ===============================================
 ID   Change Type   Master                 Object                      Changes
---- ------------- ---------------------- --------------------------- -----------------------------------------------
 3    Create        `Our pub <Detail>`__   `Entry object <Detail>`__   Entry(id=1,user=1,subject='test',company=100)
 2    Update        `Our pub <Detail>`__   `Our pub <Detail>`__        name : 'My pub' --> 'Our pub'
 1    Create        `Our pub <Detail>`__   `Our pub <Detail>`__        Company(id=100,name='My pub',partner_ptr=100)
==== ============= ====================== =========================== ===============================================
"""
        output = ses.show('changes.Changes',
                     column_names="id type master object diff")
        # print(output)
        self.assertEqual(output, expected)
        
        
        # Now we delete the entry:

        url = '/api/entries/Entries/1'
        data = dict(an='delete_selected', sr=1)
        res = self.get_json_dict('robin', url, data)
        self.assertEqual(
            res.message, """\
You are about to delete 1 Entry:
Entry object
Are you sure ?""")

        
        
        # We answer "yes":

        url = "/callbacks/{0}/yes".format(res['xcallback']['id'])
        res = self.get_json_dict('robin', url, {})
        # r = test_client.get(url)
        self.assertEqual(res.success, True)
        self.assertEqual(res.record_deleted, True)
        

        expected = """\
==== ============= ====================== ====================== ===============================================
 ID   Change Type   Master                 Object                 Changes
---- ------------- ---------------------- ---------------------- -----------------------------------------------
 4    Delete        `Our pub <Detail>`__                          Entry(id=1,user=1,subject='test',company=100)
 3    Create        `Our pub <Detail>`__                          Entry(id=1,user=1,subject='test',company=100)
 2    Update        `Our pub <Detail>`__   `Our pub <Detail>`__   name : 'My pub' --> 'Our pub'
 1    Create        `Our pub <Detail>`__   `Our pub <Detail>`__   Company(id=100,name='My pub',partner_ptr=100)
==== ============= ====================== ====================== ===============================================
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
==== ============= ====================== ============== =========== ===============================================
 ID   Change Type   Master                 Object type    object id   Changes
---- ------------- ---------------------- -------------- ----------- -----------------------------------------------
 4    Delete        `Our pub <Detail>`__   Entry          1           Entry(id=1,user=1,subject='test',company=100)
 3    Create        `Our pub <Detail>`__   Entry          1           Entry(id=1,user=1,subject='test',company=100)
 2    Update        `Our pub <Detail>`__   Organization   100         name : 'My pub' --> 'Our pub'
 1    Create        `Our pub <Detail>`__   Organization   100         Company(id=100,name='My pub',partner_ptr=100)
==== ============= ====================== ============== =========== ===============================================
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
        
        url = "/callbacks/{0}/yes".format(res.xcallback['id'])
        self.get_json_dict('robin', url, {})
        
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
===================== ================= ============================================================= ========
 Database model        Database object   Message                                                       Action
--------------------- ----------------- ------------------------------------------------------------- --------
 `Change <Detail>`__   `#1 <Detail>`__   Invalid primary key 100 for contacts.Company in `object_id`   clear
 `Change <Detail>`__   `#2 <Detail>`__   Invalid primary key 100 for contacts.Company in `object_id`   clear
 `Change <Detail>`__   `#3 <Detail>`__   Invalid primary key 1 for entries.Entry in `object_id`        clear
 `Change <Detail>`__   `#4 <Detail>`__   Invalid primary key 1 for entries.Entry in `object_id`        clear
 `Change <Detail>`__   `#5 <Detail>`__   Invalid primary key 100 for contacts.Company in `object_id`   clear
 `Change <Detail>`__   `#1 <Detail>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
 `Change <Detail>`__   `#2 <Detail>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
 `Change <Detail>`__   `#3 <Detail>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
 `Change <Detail>`__   `#4 <Detail>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
 `Change <Detail>`__   `#5 <Detail>`__   Invalid primary key 100 for contacts.Partner in `master_id`   clear
===================== ================= ============================================================= ========
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

