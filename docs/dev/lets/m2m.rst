Note about many-to-many relationships
=====================================

There are two `many-to-many relationships
<https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/>`_
between *Member* and *Product*:

- A given member can *offer* multiple products, and a given product
  can *be offered* by multiple members. We can call this the
  **providers** of a product.

- A given member can *want* multiple products, and a given product can
  *be wanted* by multiple members. We can call this the **customers** of
  a product.

Using Django's interface for `many-to-many relationships
<https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/>`_, we
might express this as follows::

    providers = models.ManyToManyField(
        'lets.Member', through='lets.Offer', related_name='offered_products')
    customers = models.ManyToManyField(
        'lets.Member', through='lets.Demand', related_name='wanted_products')


Which you can read as follows:

- *Offer* is the "intermediate model" used "to govern the m2m relation
  *Product.providers* / *Member.offered_products*.

- *Demand* is the intermediate model used to govern the m2m relation
  *Product.customers* / *Member.wanted_products*.

A *ManyToManyField* is originally a shortcut for telling Django to
create an automatic, "invisible", additional model, with two
ForeignKey fields.  But in most real-life situations you anyway want
to define what Django calls "`extra fields on many-to-many
relationships
<https://docs.djangoproject.com/en/3.1/topics/db/models/#intermediary-manytomany>`_",
and thus you must explicitly name that "intermediate model" of your
ManyToManyField.  That's why we
prefer to define an explicit intermediate model for
each m2m relation instead of using ManyToManyField.  Less magic, easier to extend.
