.. _lino.datamig:

=========================
Data migrations à la Lino
=========================

Overview
========

Data migration is a complex topic. Django needed until version 1.7
before they dared to suggest a default method to automating these
tasks (see `Migrations
<https://docs.djangoproject.com/en/1.11/topics/migrations/>`_).

Lino suggests a radically different approach for doing database
migrations using :doc:`Python dumps <dump2py>`.

Advantages of Lino migrations:

- They make the process of deploying applications and upgrading
  production sites simpler and more transparent.

- They work also when you use Lino's :doc:`inject_field
  <inject_field>` or :ref:`BabelField <mldbc>` features.

You might still want to use the Django approach because Lino
migrations have one inevitable **disadvantage**: they are slower than
:manage:`migrate`. Users must stop working in your application during
that time.  There are systems where half an hour downtime for an
upgrade is not acceptable.

Rule of thumb: If your application uses either the :doc:`inject_field
<inject_field>` or :ref:`BabelField <mldbc>` features (or if it uses a
plugin which uses them), then Django migrations won't work.  If your
site *does* need to use Django migrations, then you cannot use
:doc:`inject_field <inject_field>` and :ref:`BabelField <mldbc>`.


How to use data migrations à la Lino
====================================

As the responsible adminstrator of a Lino production site, you will
simply :doc:`write a Python dump </dev/dump2py>` with the old version
(*before* upgrading), and then load that dump with the new version
(*after* upgrading).

See :doc:`/admin/upgrade`


General strategy for managing data migrations
=============================================

As the maintainer of a Lino application that is being used on one or
several production sites you care about how these production sites
will migrate their data.

There are two ways for managing data migrations: either by locally
modifying the :xfile:`restore.py` script or by writing a migrator.


Modifying :xfile:`restore.py` script
====================================

Locally modifying a :xfile:`restore.py` script is the natural way when
there is only one production site who needs to be migrated and when
the application maintainer is also the site administrator. It is a
common situation when a new customer project has gone into production
but is being used only on that customer's site.

Certain schema changes will migrate automatically: new models, new
fields (when they have a default value), `unique` constraints, ...

If there were unhandled schema changes, you will get error messages
during the restore.  And then you can just change the
:xfile:`restore.py` script and try again.  You can run the
:xfile:`restore.py` script as often as needed until there are no more
errors.

The code of the :xfile:`restore.py` script is optimized for applying
most database schema changes.  For example if a model or field has
been removed, you can just comment out one line in that script.


Manually repairing data
=======================

There are situations where you want to be a magician. For example your
users (or yourself) accidentally deleted a bunch of data from their
database and you don't have a recent backup.

In such situations you can inject data by writing a :manage:`run`
script which uses Python dumps.  Here is an example of such a script::


    from os.path import join
    from django.db.models import Count
    from django.core.exceptions import ValidationError
    
    REALLY = False  # set to True when you are sure

    p = "20150824a"  # the snapshot from where to restore

    # don't execute main(), just load create_aaa_bbb functions
    __name__ = ""
    execfile(join(p, "restore.py"))
    
    class PartnerLoader:

        def __init__(self):
            self.ignored = 0
            self.restored = 0
            self.errors = 0
            self.pklist = (85229, 84047)

        def flush_deferred_objects(self):
            pass

        def save(self, obj):
            if obj.id in self.pklist:
                if obj.__class__.objects.filter(pk=obj.pk).count() == 0:
                    try:
                        obj.full_clean()
                    except ValidationError as e:
                        self.errors += 1
                        logger.info("20150826 %s : %s", obj, e)
                        return

                    if REALLY: obj.save()
                    self.restored += 1
                    return
                else:
                    self.ignored += 1
                    return

        def report(self):
            msg = "Partners: {0} errors, {1} restored, {2} ignored"
            print msg.format(self.errors, self.restored, self.ignored)


    class MyLoader:

        def __init__(self):
            self.ignored = 0
            self.restored = 0
            self.errors = 0
            qs = debts_Budget.objects.annotate(num=Count('entry')).filter(num=0)
            self.pklist = qs.values_list('id', flat=True)
            print "Restore entries for", len(self.pklist), "budgets", [int(i) for i in self.pklist]

        def flush_deferred_objects(self):
            pass

        def save(self, obj):
            if obj.budget_id in self.pklist:
                if obj.__class__.objects.filter(pk=obj.pk).count() == 0:
                    try:
                        obj.full_clean()
                    except ValidationError as e:
                        self.errors += 1
                        print "20150826.py", obj, e
                        return

                    if REALLY: obj.save()
                    self.restored += 1
                    return
                else:
                    self.ignored += 1
                    return

        def report(self):
            msg = "Entries: {0} errors, {1} restored, {2} ignored"
            print msg.format(self.errors, self.restored, self.ignored)

    loader = PartnerLoader()
    execfile(join(p, "contacts_partner.py"))
    #execfile(join(p, "households_household.py"))
    #execfile(join(p, "contacts_company.py"))
    #execfile(join(p, "pcsw_client.py"))
    loader.report()

    loader = MyLoader()
    #execfile(join(p, "debts_actor.py"))
    #loader.report()
    execfile(join(p, "debts_entry.py"))
    loader.report()



Writing a migrator
==================

(Not finished)

- Increase your version number
- 

