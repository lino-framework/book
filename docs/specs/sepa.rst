=================================================
``sepa`` : Communicating with the bank using SEPA
=================================================

.. currentmodule:: lino_xl.lib.sepa

The :mod:`lino_xl.lib.sepa` plugin functionality for managing bank accounts for
your partners.  When this plugin is installed, every partner can have one or
several bank accounts.

The name ``sepa`` is actually irritating because this plugin won't do
any SEPA transfer. Maybe rename it to ``iban``? OTOH it is needed by
the SEPA modules :mod:`lino_xl.lib.b2c` and
:mod:`lino_cosi.lib.c2b`.

It requires the :mod:`lino_xl.lib.ledger` plugin.



.. class:: Account

    A bank account related to a given partner.

    .. attribute:: partner


       :class:`Partner
       <lino.modlib.models.contacts.Partner>`


    .. attribute:: iban = IBANField(verbose_name=_("IBAN"))
    .. attribute:: bic = BICField(verbose_name=_("BIC"), blank=True)

    .. attribute:: remark = models.CharField(_("Remark"), max_length=200, blank=True)

    .. attribute:: primary = models.BooleanField(


    .. attribute:: statements

        A virtual field which displays the date of the last imported
        statement for this account. Clicking on this date will open
        the `B2C account <lino_xl.lib.b2c.models.Account>` with same
        IBAN number.

        This field is empty when no B2C Account exists.

        Available only when :mod:`lino_xl.lib.b2c` is installed as
        well.


.. class:: Accounts

.. class:: AccountsByPartner

    Show the bank account(s) defined for a given partner. To be
    included to a detail window on partner.


.. class:: BankAccount

    Defines a field :attr:`bank_account` and its chooser.

.. class:: Payable

    Mixin for models that represent *payable transactions*.  To be combined
    with some mixin which defines a field `partner`.

    A **payable transaction** is a transaction that is expected to cause a
    payment.

    .. attribute:: your_ref

    .. attribute:: due_date

    .. attribute:: payment_term

        See :attr:`lino_xl.lib.ledger.mixins.PartnerRelated.payment_term`

    .. attribute:: title

       A char field with a description for this transaction.

    .. method:: get_payable_sums_dict(self)

        To be implemented by subclasses.  Expected to return a dict which maps
        4-tuples `(acc_tuple, project, vat_class, vat_regime)` to the payable
        amount. `acc_tuple` is itself a tuple `(general_account,
        analytic_account)`, `vat_class` is a :class:`lino_xl.lib.vat.VatClasses`
        choice and `vat_regime` a :class:`lino_xl.lib.vat.VatRegimes` choice.

    .. method:: get_wanted_movements(self)

        Implements :meth:`lino_xl.lib.ledger.Voucher.get_wanted_movements`.
