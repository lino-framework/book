.. doctest docs/specs/voga/vat.rst
.. _voga.specs.vat:

============================
VAT declaration in Lino Voga
============================

..  doctest init:
   
    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *


Test cases
==========

The following covers a bug that was was fixed :blogref:`20170905`


>>> rt.show(vat.IntracomSales)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
==================== ================== ======== =================== ================= ===== =================
 Invoice              Partner            VAT id   VAT regime          Total excl. VAT   VAT   Total incl. VAT
-------------------- ------------------ -------- ------------------- ----------------- ----- -----------------
 *SLS 17*             Jeanémart Jérôme            Intracom supplies   20,00                   20,00
 *SLS 35*             Brecht Bernd                Intracom services   295,00                  295,00
 **Total (2 rows)**                                                   **315,00**              **315,00**
==================== ================== ======== =================== ================= ===== =================
<BLANKLINE>

>>> rt.show(vat.IntracomPurchases)
===================== =============== ======== =================== ================= ===== =================
 Invoice               Partner         VAT id   VAT regime          Total excl. VAT   VAT   Total incl. VAT
--------------------- --------------- -------- ------------------- ----------------- ----- -----------------
 *PRC 7*               Donderweer BV            Intracom services   199,90                  199,90
 *PRC 14*              Donderweer BV            Intracom services   200,50                  200,50
 *PRC 21*              Donderweer BV            Intracom services   201,00                  201,00
 *PRC 28*              Donderweer BV            Intracom services   201,20                  201,20
 *PRC 35*              Donderweer BV            Intracom services   202,40                  202,40
 *PRC 42*              Donderweer BV            Intracom services   199,90                  199,90
 *PRC 49*              Donderweer BV            Intracom services   200,50                  200,50
 *PRC 56*              Donderweer BV            Intracom services   201,00                  201,00
 *PRC 63*              Donderweer BV            Intracom services   201,20                  201,20
 *PRC 70*              Donderweer BV            Intracom services   202,40                  202,40
 *PRC 77*              Donderweer BV            Intracom services   199,90                  199,90
 *PRC 84*              Donderweer BV            Intracom services   200,50                  200,50
 *PRC 91*              Donderweer BV            Intracom services   203,00                  203,00
 *PRC 98*              Donderweer BV            Intracom services   203,20                  203,20
 *PRC 105*             Donderweer BV            Intracom services   204,40                  204,40
 *PRC 112*             Donderweer BV            Intracom services   201,90                  201,90
 *PRC 119*             Donderweer BV            Intracom services   202,50                  202,50
 **Total (17 rows)**                                                **3 425,40**            **3 425,40**
===================== =============== ======== =================== ================= ===== =================
<BLANKLINE>

>>> url = "/api/vat/IntracomPurchases?fmt=json&rp=ext-comp-1224&limit=17&start=0"
>>> # test_client.get(url)
>>> json_fields = 'count rows title success no_data_text param_values'
>>> kwargs = dict(fmt='json', limit=5, start=0)
>>> demo_get('robin', "api/vat/IntracomPurchases", json_fields, 17, **kwargs)
