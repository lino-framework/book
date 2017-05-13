=========================================
Customer to Bank communication using SEPA
=========================================

The first and currently only C2B application implemented in Lino are
**payment orders**. A payment order is when you ask your bank to
perform a payment from one of your accounts to the account of one of
your business partners. One payment order may contain more than one
such instructions.

There is a DirectPrintAction

A payment order is called "Customer Credit Transfer Initiation" in
SEPA and described by `pain.001.VAR.VER` where VAR is always 001 and
VER is 01, 02 or 03.

Lino uses simple Jinja templates files for generating this PAIN XML
file.

If I look at code like
https://github.com/totaler/sepa/blob/master/sepa/sepa19.py then I feel
that no, we are not going to generate the XML file by Python code
(using an etree approach) because that would be overkill. We must
write test cases which validate the generated XML using lxml and the
XSD (code currently in :mod:`lino.utils.xmlgen.sepa`) but we don't
need to do this validity check for each generated document.

.. xfile:: pain.001.xml

The template for generating a CCTI is called :xfile:`pain.001.xml` and
lives in :file:`lino_xl/lib/finan/config/finan/PaymentOrder`.
It
currently uses version 02 though 03 seems to be most used nowadays. 


   
