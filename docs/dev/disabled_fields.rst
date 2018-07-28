.. _disabled_fields:

===========================
Disabling individual fields
===========================

Sometimes you want to disable (make non-editable) individual fields of
a form based on certain conditions.  The conditions for disabling
individual fields can be application specific and based e.g. on user
permissions or the values of certain other fields of the object being
displayed.

For example, in :ref:`cosi` an invoice disables most fields when it
has been registered.  Here are two screenshots of a same invoice, once
when the invoice's state is "draft" and once when it is "registered":

.. image:: /specs/cosi/sales.Invoice.detail.draft.png
    :scale: 20
            
.. image:: /specs/cosi/sales.Invoice.detail.registered.png
    :scale: 20

In Lino you define this behaviour by writing a :meth:`disabled_fields
<lino.core.model.Model.disabled_fields>` instance method on your
model.  This method must return a :class:`set` of names of the fields
that should be disabled for this record::


    class MyModel(dd.Model):
        ...
        def disabled_fields(self, ar):
            s = super(MyModel, self).disabled_fields(ar)
            ...
            return set()

The :class:`Invoice` model used in above screenshots does something
like this::

    class Invoice(dd.Model):
      ...
      def disabled_fields(self, ar):
          df = super(Invoice, self).disabled_fields(ar)
          if self.state == InvoiceStates.registered:
              df.add('subject')
              df.add('payment_term')
              ...
          return df

The decision which fields to disable may depend an the current
user. Here is a fictive example of a model :class:`Case` where only
the author may change first and last name::

    class Case(dd.Model):      
      ...
      def disabled_fields(self, ar):
          df = super(Case, self).disabled_fields(ar)
          if self.author == ar.user:
              return df
          df.add('first_name')
          df.add('last_name')
          return df


You may also disable actions simply by adding their name to the set of
disabled fields. (The method name is actually misleading, one day we
might rename it to :meth:`disabled_elements`).

You may want to define this method on the actor instead of per model.
In that case it must be a class method that accepts two arguments `obj`
and `ar` (an `ActionRequest`)::

  @classmethod
  def disabled_fields(cls, obj, ar):
      s = super(MyActor, cls).disabled_fields(obj, ar)
      ...
      return set()

Note that Lino calls the :meth:`disabled_fields
<lino.core.model.disabled_fields>` method only once per model instance
and request.  The returned set is cached in memory.


