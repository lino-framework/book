.. _disabled_fields:

===========================
Disabling individual fields
===========================

Sometimes you want to disable (make non-editable) individual fields of
a form based on certain conditions like user permissions or values of
certain other fields.

In Lino you do this by writing a :meth:`disabled_fields
<lino.core.model.disabled_fields>` method on your model.
  
This method must return a set of names of fields or actions that
should be disabled for this record.  Despite its name, you may also
disable actions simply by adding their name to the set of disabled
fields.

Fictive usage examples::

    class Invoice(dd.Model):

      def disabled_fields(self, ar):
          df = super(MyModel, self).disabled_fields(ar)
          if not self.has_vat:
              df.add('total_vat')
              df.add('total_incl')
          return df

    class Case(dd.Model):      

      def disabled_fields(self, ar):
          df = super(MyModel, self).disabled_fields(ar)
          if self.author == ar.user:
              return df
          df.add('first_name')
          df.add('last_name')
          return df

If defined in the Actor, this must be a class method that accepts two
arguments `obj` and `ar` (an `ActionRequest`)::

  @classmethod
  def disabled_fields(cls, obj, ar):
      s = super(MyActor, cls).disabled_fields(obj, ar)
      ...
      return set()

If not defined in the Table, Lino will look whether the Table's model
has a `disabled_fields` method and install a wrapper to this model
method.  When defined on the model, is must be an *instance* method::

  def disabled_fields(self, ar):
      s = super(MyModel, self).disabled_fields(ar)
      ...
      return set()


Note that Lino calls the :meth:`disabled_fields
<lino.core.model.disabled_fields>` method only once per model instance
and request.  The returned set is cached in memory.


