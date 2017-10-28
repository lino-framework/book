.. _voga.specs.invoicing:

================================
How Lino Voga generates invoices
================================

.. to test only this doc:

    $ doctest docs/specs/invoicing.rst

    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *


.. contents:: 
   :local:
   :depth: 2

Overview
========

The general functionality for automatically generating invoices is
defined in :mod:`lino_cosi.lib.invoicing`.

Lino Voga uses this functionality by extending :class:`Enrolment
<lino_xl.lib.courses.models.Enrolment>` so that it inherits from
:class:`Invoiceable <lino_cosi.lib.invoicing.mixins.Invoiceable>`. In
Lino Voga, enrolments are the things for which they write invoices.

Another invoiceable thing in Lino Voga is when they rent a room to a
third-party organisation.  This is called a :class:`Booking
<lino_voga.lib.rooms.models.Booking>`.

IOW, in Lino Voga both :class:`Enrolment
<lino_xl.lib.courses.models.Enrolment>` and :class:`Booking
<lino_voga.lib.rooms.models.Booking>` are :class:`Invoiceable
<lino_cosi.lib.invoicing.mixins.Invoiceable>`:

>>> rt.models_by_base(rt.modules.invoicing.Invoiceable)
[<class 'lino_voga.lib.roger.courses.models.Enrolment'>, <class 'lino_voga.lib.rooms.models.Booking'>]


User interface
==============

On the user-visible level this plugin adds

- a menu entry :menuselection:`Journals --> Create invoices`,

and a :class:`StartInvoicing
<lino_cosi.lib.invoicing.actions.StartInvoicing>` 
action (with a basket as icon, referring to a shopping basket) 
at four places: 

- as a menu command :menuselection:`Accounting --> Create invoices`
- on every *partner* (generate invoices for this partner)
- on every *course* (generate invoices for all enrolments of this
  course)
- on every *journal* which supports automatic invoice generation. 

>>> rt.models.contacts.Partner.start_invoicing
<lino_xl.lib.invoicing.actions.StartInvoicingForPartner start_invoicing ('Create invoices')>

>>> rt.models.courses.Course.start_invoicing
<lino_voga.lib.invoicing.models.StartInvoicingForCourse start_invoicing ('Create invoices')>

API
===

On the API level it defines the :class:`Invoiceable
<lino_xl.lib.invoicing.mixins.Invoiceable>` mixin.

The *invoices journal* which supports automatic generation is
indirectly defined by the :attr:`voucher_model
<lino_xl.lib.invoicing.Plugin.voucher_model>` setting.

>>> vt = dd.plugins.invoicing.get_voucher_type()
>>> vt.table_class.start_invoicing
<lino_xl.lib.invoicing.actions.StartInvoicingForJournal start_invoicing ('Create invoices')>

>>> rt.models.invoicing.Plan.start_invoicing
<lino_xl.lib.invoicing.actions.StartInvoicing start_invoicing ('Create invoices')>


Enrolments as invoiceables
==========================

:attr:`Enrolment.invoicing_info` is a summary of what has been
invoiced (and what hasn't) for a given enrolment.

>>> from textwrap import wrap
>>> for obj in courses.Enrolment.objects.all():
...     ii = '\n'.join(wrap(E.to_rst(obj.invoicing_info), 80))
...     print(u"{} : {} {}\n{}".format(obj.id, obj.course, obj.pupil, ii))
...     #doctest: +REPORT_UDIFF +NORMALIZE_WHITESPACE
1 : 001 Greece 2014 Hans Altenberg (MEL)
<BLANKLINE>
2 : 002 London 2014 Laurent Bastiaensen (ME)
<BLANKLINE>
3 : 004 comp (First Steps) Laurent Bastiaensen (ME)
<BLANKLINE>
4 : 007C WWW (Internet for beginners) Laurent Bastiaensen (ME)
Invoiced : 13.05., 20.05. Not invoiced : 29.10., 05.11., 12.11., 19.11., 26.11.,
03.12., 17.12., 24.12., 31.12., 07.01., 14.01., 21.01., 28.01., 11.02., 25.02.,
04.03., 11.03., 18.03., 25.03., 01.04., 15.04., 22.04., 29.04., 06.05.
5 : 009C BT (Belly dancing) Ulrike Charlier (ME)
Invoiced : 13.05., 20.05. Not invoiced : 16.04., 23.04., 30.04., 07.05., 21.05.,
28.05., 04.06., 11.06., 18.06., 25.06., 02.07., 16.07., 23.07., 30.07., 06.08.,
13.08., 20.08., 27.08., 10.09., 17.09., 24.09., 01.10., 08.10., 15.10., 22.10.,
05.11., 12.11., 19.11., 26.11., 03.12., 10.12., 17.12., 31.12., 07.01., 14.01.,
21.01., 28.01., 04.02., 11.02., 04.03., 11.03., 18.03., 25.03., 01.04., 08.04.,
15.04., 29.04., 06.05.
6 : 010C FG (Functional gymnastics) Ulrike Charlier (ME)
Not invoiced : 06.10., 13.10., 20.10.
7 : 010C FG (Functional gymnastics) Ulrike Charlier (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 24.11., 01.12., 08.12.,
15.12., 29.12., 05.01., 12.01., 19.01., 26.01., 02.02., 09.02., 02.03., 09.03.,
16.03., 23.03.
8 : 011C FG (Functional gymnastics) Ulrike Charlier (ME)
Invoiced : (...) 27.04., 11.05., 18.05. Not invoiced : 06.10., 13.10., 20.10.,
27.10., 10.11., 17.11., 24.11., 01.12., 08.12., 15.12., 22.12., 05.01., 12.01.,
19.01., 26.01., 02.02., 09.02., 23.02., 09.03., 16.03.
9 : 012 Rücken (Swimming) Ulrike Charlier (ME)
<BLANKLINE>
10 : 013 Rücken (Swimming) Ulrike Charlier (ME)
<BLANKLINE>
11 : 018 SV (Self-defence) Daniel Dericum (ME)
<BLANKLINE>
12 : 019 SV (Self-defence) Dorothée Demeulenaere (ME)
<BLANKLINE>
13 : 020C GLQ (GuoLin-Qigong) Dorothée Demeulenaere (ME)
Not invoiced : 28.07.
14 : 020C GLQ (GuoLin-Qigong) Dorothée Demeulenaere (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 08.09., 15.09., 22.09.,
06.10., 13.10., 20.10., 27.10., 03.11., 10.11., 17.11., 01.12., 08.12., 15.12.,
22.12., 29.12., 05.01., 12.01., 26.01., 02.02., 09.02., 23.02., 02.03., 09.03.,
16.03.
15 : 021C GLQ (GuoLin-Qigong) Dorothée Dobbelstein-Demeulenaere (ME)
Invoiced : (...) 27.02., 24.04., 15.05.
16 : 005 comp (First Steps) Dorothée Dobbelstein-Demeulenaere (ME)
<BLANKLINE>
17 : 008C WWW (Internet for beginners) Dorothée Dobbelstein-Demeulenaere (ME)
Not invoiced : 24.10., 14.11., 21.11., 28.11.
18 : 016 Rücken (Swimming) Eberhart Evers (ME)
<BLANKLINE>
19 : 017 Rücken (Swimming) Daniel Emonts (MES)
<BLANKLINE>
20 : 003 comp (First Steps) Daniel Emonts (MES)
<BLANKLINE>
21 : 003 comp (First Steps) Daniel Emonts (MES)
<BLANKLINE>
22 : 006C WWW (Internet for beginners) Edgar Engels (ME)
Not invoiced : 27.10., 03.11., 17.11., 24.11., 01.12., 08.12., 15.12., 22.12.,
29.12., 12.01., 19.01., 26.01., 02.02., 09.02., 23.02., 02.03., 16.03., 23.03.,
30.03., 13.04., 20.04., 27.04., 04.05., 18.05.
23 : 022C MED (Finding your inner peace) Edgar Engels (ME)
Invoiced : (...) 23.02., 02.03., 16.03.
24 : 023C MED (Finding your inner peace) Edgar Engels (ME)
Not invoiced : 06.02., 13.02., 20.02., 27.02., 06.03.
25 : 024C Yoga Luc Faymonville (MEL)
Invoiced : 11.05., 18.05. Not invoiced : 23.03., 13.04., 20.04., 27.04., 04.05.
26 : 025C Yoga Luc Faymonville (MEL)
Not invoiced : 29.11., 06.12., 13.12., 20.12., 27.12., 03.01., 17.01., 24.01.,
31.01., 07.02., 14.02., 21.02., 28.02., 14.03., 21.03., 28.03., 04.04., 11.04.,
25.04., 02.05., 16.05., 23.05., 30.05., 06.06., 13.06., 20.06., 27.06., 11.07.,
18.07., 25.07., 01.08., 08.08., 22.08., 29.08., 12.09., 19.09., 26.09., 03.10.,
10.10., 17.10., 24.10., 14.11., 21.11., 28.11., 05.12., 12.12., 19.12., 26.12.,
09.01., 16.01., 23.01., 30.01.
27 : 014 Rücken (Swimming) Luc Faymonville (MEL)
<BLANKLINE>
28 : 014 Rücken (Swimming) Luc Faymonville (MEL)
<BLANKLINE>
29 : 015 Rücken (Swimming) Luc Faymonville (MEL)
<BLANKLINE>
30 : 001 Greece 2014 Hildegard Hilgers (ME)
<BLANKLINE>
31 : 002 London 2014 Jacqueline Jacobs (ME)
<BLANKLINE>
32 : 004 comp (First Steps) Jacqueline Jacobs (ME)
<BLANKLINE>
33 : 007C WWW (Internet for beginners) Jacqueline Jacobs (ME)
Invoiced : (...) 06.05., 13.05., 20.05. Not invoiced : 12.11., 19.11., 26.11.,
03.12., 17.12., 24.12., 31.12., 07.01., 14.01., 21.01., 28.01., 11.02., 25.02.,
04.03., 11.03., 18.03.
34 : 009C BT (Belly dancing) Jacqueline Jacobs (ME)
Invoiced : 02.04., 09.04., 16.04.
35 : 009C BT (Belly dancing) Jacqueline Jacobs (ME)
Invoiced : (...) 06.05., 13.05., 20.05.
36 : 010C FG (Functional gymnastics) Jacqueline Jacobs (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 06.10., 13.10., 20.10.,
03.11., 10.11., 17.11., 24.11., 01.12., 08.12., 15.12., 29.12., 05.01., 12.01.,
19.01., 26.01., 02.02., 09.02., 02.03., 09.03., 16.03.
37 : 011C FG (Functional gymnastics) Josef Jonas (ME)
Invoiced : (...) 27.04., 11.05., 18.05. Not invoiced : 06.10., 13.10., 20.10.,
27.10., 10.11., 17.11., 24.11., 01.12., 08.12., 15.12., 22.12., 05.01., 12.01.,
19.01., 26.01., 02.02., 09.02., 23.02., 09.03., 16.03.
38 : 012 Rücken (Swimming) Karl Kaivers (ME)
<BLANKLINE>
39 : 013 Rücken (Swimming) Karl Kaivers (ME)
<BLANKLINE>
40 : 018 SV (Self-defence) Karl Kaivers (ME)
<BLANKLINE>
41 : 019 SV (Self-defence) Laura Laschet (ME)
<BLANKLINE>
42 : 019 SV (Self-defence) Laura Laschet (ME)
<BLANKLINE>
43 : 020C GLQ (GuoLin-Qigong) Laura Laschet (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 28.07., 11.08., 18.08.,
25.08., 01.09., 08.09., 15.09., 22.09., 06.10., 13.10., 20.10., 27.10., 03.11.,
10.11., 17.11., 01.12., 08.12., 15.12., 22.12., 29.12., 05.01., 12.01., 26.01.,
02.02., 09.02., 23.02., 02.03., 09.03., 16.03., 30.03., 13.04., 20.04.
44 : 021C GLQ (GuoLin-Qigong) Laura Laschet (ME)
Not invoiced : 25.07., 01.08., 08.08., 22.08., 29.08., 05.09., 12.09., 26.09.,
03.10., 10.10., 17.10., 24.10., 07.11., 14.11., 28.11., 05.12., 12.12., 19.12.,
26.12., 02.01., 09.01., 23.01., 30.01., 06.02., 13.02., 20.02., 27.02., 24.04.,
15.05.
45 : 005 comp (First Steps) Laura Laschet (ME)
<BLANKLINE>
46 : 008C WWW (Internet for beginners) Laura Laschet (ME)
Invoiced : (...) 17.04., 24.04., 15.05.
47 : 016 Rücken (Swimming) Josefine Leffin (MEL)
<BLANKLINE>
48 : 017 Rücken (Swimming) Marie-Louise Meier (ME)
<BLANKLINE>
49 : 017 Rücken (Swimming) Marie-Louise Meier (ME)
<BLANKLINE>
50 : 003 comp (First Steps) Marie-Louise Meier (ME)
<BLANKLINE>
51 : 006C WWW (Internet for beginners) Marie-Louise Meier (ME)
Not invoiced : 27.10., 03.11., 17.11., 24.11., 01.12., 08.12., 15.12., 22.12.,
29.12., 12.01., 19.01., 26.01., 02.02., 09.02., 23.02., 02.03., 16.03., 23.03.,
30.03., 13.04., 20.04., 27.04., 04.05., 18.05.
52 : 022C MED (Finding your inner peace) Marie-Louise Meier (ME)
Not invoiced : 23.09., 30.09., 07.10., 14.10., 21.10.
53 : 023C MED (Finding your inner peace) Marie-Louise Meier (ME)
Not invoiced : 06.02., 13.02., 20.02., 27.02., 06.03., 13.03., 27.03., 10.04.,
17.04., 24.04., 08.05., 15.05.
54 : 024C Yoga Erna Emonts-Gast (MS)
Invoiced : 11.05., 18.05. Not invoiced : 23.03., 13.04., 20.04., 27.04., 04.05.
55 : 025C Yoga Erna Emonts-Gast (MS)
Not invoiced : 08.11., 22.11., 29.11.
56 : 025C Yoga Erna Emonts-Gast (MS)
Not invoiced : 27.12., 03.01., 17.01., 24.01., 31.01., 07.02., 14.02., 21.02.,
28.02., 14.03., 21.03., 28.03., 04.04., 11.04., 25.04., 02.05., 16.05., 23.05.,
30.05., 06.06., 13.06., 20.06., 27.06., 11.07., 18.07., 25.07., 01.08., 08.08.,
22.08., 29.08., 12.09., 19.09., 26.09., 03.10., 10.10., 17.10., 24.10., 14.11.,
21.11., 28.11., 05.12., 12.12., 19.12., 26.12., 09.01., 16.01., 23.01., 30.01.
57 : 014 Rücken (Swimming) Alfons Radermacher (ME)
<BLANKLINE>
58 : 015 Rücken (Swimming) Alfons Radermacher (ME)
<BLANKLINE>
59 : 001 Greece 2014 Alfons Radermacher (ME)
<BLANKLINE>
60 : 002 London 2014 Christian Radermacher (MEL)
<BLANKLINE>
61 : 004 comp (First Steps) Christian Radermacher (MEL)
<BLANKLINE>
62 : 007C WWW (Internet for beginners) Christian Radermacher (MEL)
Not invoiced : 29.10., 05.11., 12.11.
63 : 007C WWW (Internet for beginners) Christian Radermacher (MEL)
Invoiced : (...) 06.05., 13.05., 20.05. Not invoiced : 17.12., 24.12., 31.12.,
07.01., 14.01., 21.01., 28.01., 11.02., 25.02., 04.03., 11.03., 18.03., 25.03.
64 : 009C BT (Belly dancing) Christian Radermacher (MEL)
Invoiced : (...) 06.05., 13.05., 20.05. Not invoiced : 02.04., 09.04., 16.04.,
23.04., 30.04., 07.05., 21.05., 28.05., 04.06., 11.06., 18.06., 25.06., 02.07.,
16.07., 23.07., 30.07., 06.08., 13.08., 20.08., 27.08., 10.09., 17.09., 24.09.,
01.10., 08.10., 15.10., 22.10., 05.11., 12.11., 19.11., 26.11., 03.12., 10.12.,
17.12., 31.12., 07.01., 14.01., 21.01., 28.01., 04.02., 11.02., 04.03., 11.03.,
18.03., 25.03., 01.04., 08.04., 15.04.
65 : 010C FG (Functional gymnastics) Christian Radermacher (MEL)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 06.10., 13.10., 20.10.,
03.11., 10.11., 17.11., 24.11., 01.12., 08.12., 15.12., 29.12., 05.01., 12.01.,
19.01., 26.01., 02.02., 09.02., 02.03., 09.03., 16.03.
66 : 011C FG (Functional gymnastics) Edgard Radermacher (ME)
Not invoiced : 06.10., 13.10., 20.10., 27.10.
67 : 012 Rücken (Swimming) Guido Radermacher (ME)
<BLANKLINE>
68 : 013 Rücken (Swimming) Guido Radermacher (ME)
<BLANKLINE>
69 : 018 SV (Self-defence) Guido Radermacher (ME)
<BLANKLINE>
70 : 018 SV (Self-defence) Guido Radermacher (ME)
<BLANKLINE>
71 : 019 SV (Self-defence) Hedi Radermacher (ME)
<BLANKLINE>
72 : 020C GLQ (GuoLin-Qigong) Hedi Radermacher (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 28.07., 11.08., 18.08.,
25.08., 01.09., 08.09., 15.09., 22.09., 06.10., 13.10., 20.10., 27.10., 03.11.,
10.11., 17.11., 01.12., 08.12., 15.12., 22.12., 29.12., 05.01., 12.01., 26.01.,
02.02., 09.02., 23.02., 02.03., 09.03., 16.03., 30.03., 13.04., 20.04.
73 : 021C GLQ (GuoLin-Qigong) Hedi Radermacher (ME)
Not invoiced : 25.07., 01.08., 08.08.
74 : 005 comp (First Steps) Hedi Radermacher (ME)
<BLANKLINE>
75 : 008C WWW (Internet for beginners) Hedi Radermacher (ME)
Invoiced : (...) 17.04., 24.04., 15.05.
76 : 016 Rücken (Swimming) Jean Radermacher (ME)
<BLANKLINE>
77 : 016 Rücken (Swimming) Jean Radermacher (ME)
<BLANKLINE>
78 : 017 Rücken (Swimming) Didier di Rupo (MS)
<BLANKLINE>
79 : 003 comp (First Steps) Didier di Rupo (MS)
<BLANKLINE>
80 : 006C WWW (Internet for beginners) Erna Ärgerlich (ME)
Not invoiced : 27.10., 03.11., 17.11., 24.11.
81 : 022C MED (Finding your inner peace) Jean Dupont (ME)
Invoiced : (...) 23.02., 02.03., 16.03.
82 : 023C MED (Finding your inner peace) Jean Dupont (ME)
Not invoiced : 20.02., 27.02., 06.03., 13.03., 27.03., 10.04., 17.04., 24.04.,
08.05., 15.05.
83 : 024C Yoga Jean Dupont (ME)
<BLANKLINE>
84 : 024C Yoga Jean Dupont (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 23.03., 13.04.
85 : 025C Yoga Mark Martelaer (MS)
Not invoiced : 08.11., 22.11., 29.11., 06.12., 13.12., 20.12., 27.12., 03.01.,
17.01., 24.01., 31.01., 07.02., 14.02., 21.02., 28.02., 14.03., 21.03., 28.03.,
04.04., 11.04., 25.04., 02.05., 16.05., 23.05., 30.05., 06.06., 13.06., 20.06.,
27.06., 11.07., 18.07., 25.07., 01.08., 08.08., 22.08., 29.08., 12.09., 19.09.,
26.09., 03.10., 10.10., 17.10., 24.10., 14.11., 21.11., 28.11., 05.12., 12.12.,
19.12., 26.12., 09.01., 16.01., 23.01., 30.01.
86 : 014 Rücken (Swimming) Mark Martelaer (MS)
<BLANKLINE>
87 : 015 Rücken (Swimming) Mark Martelaer (MS)
<BLANKLINE>
88 : 001 Greece 2014 Mark Martelaer (MS)
<BLANKLINE>
89 : 002 London 2014 Lisa Lahm (MS)
<BLANKLINE>
90 : 004 comp (First Steps) Lisa Lahm (MS)
<BLANKLINE>
91 : 004 comp (First Steps) Lisa Lahm (MS)
<BLANKLINE>
92 : 007C WWW (Internet for beginners) Bernd Brecht (ME)
Invoiced : 13.05., 20.05. Not invoiced : 29.10., 05.11., 12.11., 19.11., 26.11.,
03.12., 17.12., 24.12., 31.12., 07.01., 14.01., 21.01., 28.01., 11.02., 25.02.,
04.03., 11.03., 18.03., 25.03., 01.04., 15.04., 22.04., 29.04., 06.05.
93 : 009C BT (Belly dancing) Bernd Brecht (ME)
Invoiced : (...) 06.05., 13.05., 20.05.
94 : 010C FG (Functional gymnastics) Bernd Brecht (ME)
Not invoiced : 06.10., 13.10., 20.10., 03.11.
95 : 011C FG (Functional gymnastics) Jérôme Jeanémart (ME)
Invoiced : (...) 27.04., 11.05., 18.05. Not invoiced : 06.10., 13.10., 20.10.,
27.10., 10.11., 17.11., 24.11., 01.12., 08.12., 15.12., 22.12., 05.01., 12.01.,
19.01., 26.01., 02.02., 09.02., 23.02., 09.03., 16.03.

Here is a list of all enrolments:

>>> rt.show(rt.actors.courses.Enrolments)
...     #doctest: +REPORT_UDIFF +ELLIPSIS
================= ===================================== ========= ======================================== =============== =================
 Date of request   Activity                              State     Participant                              Workflow        Author
----------------- ------------------------------------- --------- ---------------------------------------- --------------- -----------------
 14/09/2013        022C MED (Finding your inner peace)   Started   Edgar Engels (ME)                        **Requested**   Tom Thess
 14/09/2013        022C MED (Finding your inner peace)   Started   Marie-Louise Meier (ME)                  **Confirmed**   Marianne Martin
 19/09/2013        022C MED (Finding your inner peace)   Started   Jean Dupont (ME)                         **Requested**   Monique Mommer
 19/10/2013        025C Yoga                             Started   Mark Martelaer (MS)                      **Confirmed**   Robin Rood
 08/11/2013        024C Yoga                             Started   Luc Faymonville (MEL)                    **Confirmed**   Monique Mommer
 08/11/2013        025C Yoga                             Started   Erna Emonts-Gast (MS)                    **Confirmed**   Rolf Rompen
 08/11/2013        025C Yoga                             Started   Erna Emonts-Gast (MS)                    **Confirmed**   Rolf Rompen
 08/11/2013        024C Yoga                             Started   Jean Dupont (ME)                         **Confirmed**   Rolf Rompen
 08/11/2013        024C Yoga                             Started   Jean Dupont (ME)                         **Confirmed**   Rolf Rompen
 23/11/2013        025C Yoga                             Started   Luc Faymonville (MEL)                    **Confirmed**   Romain Raffault
 23/11/2013        024C Yoga                             Started   Erna Emonts-Gast (MS)                    **Confirmed**   Romain Raffault
 26/02/2014        003 comp (First Steps)                Started   Marie-Louise Meier (ME)                  **Confirmed**   Robin Rood
 ...
 11/07/2015        016 Rücken (Swimming)                 Started   Jean Radermacher (ME)                    **Confirmed**   Rolf Rompen
 11/07/2015        016 Rücken (Swimming)                 Started   Jean Radermacher (ME)                    **Confirmed**   Rolf Rompen
 26/07/2015        017 Rücken (Swimming)                 Started   Daniel Emonts (MES)                      **Confirmed**   Romain Raffault
 26/07/2015        016 Rücken (Swimming)                 Started   Josefine Leffin (MEL)                    **Confirmed**   Romain Raffault
 26/07/2015        013 Rücken (Swimming)                 Started   Guido Radermacher (ME)                   **Confirmed**   Romain Raffault
================= ===================================== ========= ======================================== =============== =================
<BLANKLINE>


Invoicings
==========

The detail window of an enrolment shows all invoicings of that
enrolment:

>>> obj = courses.Enrolment.objects.get(pk=64)
>>> rt.show('invoicing.InvoicingsByInvoiceable', obj)
... #doctest: +REPORT_UDIFF
==================== ================================================== ========== ============== ============ ==================
 Product invoice      Heading                                            Quantity   Voucher date   State        Number of events
-------------------- -------------------------------------------------- ---------- -------------- ------------ ------------------
 SLS 14               [1] Enrolment to 009C BT (Belly dancing)           1          01/04/2014     Registered   12
 SLS 29               [2] Renewal Enrolment to 009C BT (Belly dancing)   1          01/07/2014     Registered   12
 SLS 42               [3] Renewal Enrolment to 009C BT (Belly dancing)   1          01/10/2014     Registered   12
 SLS 72               [4] Renewal Enrolment to 009C BT (Belly dancing)   1          01/01/2015     Registered   12
 **Total (4 rows)**                                                      **4**                                  **48**
==================== ================================================== ========== ============== ============ ==================
<BLANKLINE>


Subscription courses
====================

Subscription courses are courses for which the customer pays *a given
number of events*, not simply all events of that course. This means
that the presences for these courses must have been entered.

A subscription course does not end and start at a given date, the
course itself is continously being given. Participants can start on
any time of the year. They usually pay for 12 sessions in advance (the
first invoice for that enrolment), and Lino must write a new invoice
every 12 weeks.


Descriptions
============

The items of automatically generated invoices have a
:attr:`description` field whose context is defined by the
:xfile:`courses/Enrolment/item_description.html` template and can be
complex and application specific.

See the :xfile:`config/courses/Enrolment/item_description.html` file 
in :mod:`lino_voga.lib.voga`.


Scheduled dates
===============

For enrolments in non-continuous courses (i.e. with a fee whose
:attr:`number_of_events` is empty), the description on the invoice
includes a list of "Scheduled dates". This is basically an enumeration
of the planned events of that course.

It can happen that a participant joins a started course afterwards and
pays less, in function of the events he didn't attend. The amount to
be invoiced in such cases is subject to individual discussion, and the
user simply enters that amount in the enrolment.

The following code snippets tests whether above is true.

There are 12 enrolments matching this condition:

>>> Enrolment = rt.models.courses.Enrolment
>>> EnrolmentStates = rt.models.courses.EnrolmentStates
>>> qs = Enrolment.objects.filter(start_date__isnull=False)
>>> qs = qs.filter(state=EnrolmentStates.confirmed)
>>> qs = qs.filter(fee__number_of_events__isnull=True)
>>> qs = qs.order_by('request_date')
>>> qs.count()
12

We want only those for which an invoice has been generated. Above
number shrinks to 2:

>>> from django.db.models import Count
>>> qs = qs.annotate(invoicings_count=Count('invoicings'))
>>> qs = qs.filter(invoicings_count__gt=0)
>>> qs.count()
2

Let's select the corresponding invoice items:

>>> InvoiceItem = dd.plugins.invoicing.item_model
>>> qs2 = InvoiceItem.objects.filter(
...     invoiceable_id__in=qs.values_list('id', flat=True))
>>> qs2.count()
2

Now we define a utility function which prints out what we want to see
for each of these items:

>>> def fmt(obj):
...     enr = obj.invoiceable
...     # avoid initdb_demo after change in item_description.html:
...     enr.setup_invoice_item(obj) 
...     print(u"--- Invoice #{0} for enrolment #{1} ({2}):".format(
...         obj.voucher.number, enr.id, enr))
...     print("Title: {0}".format(obj.title))
...     print("Start date: " + dd.fds(obj.invoiceable.start_date))
...     if enr.start_date:
...       missed_events = enr.course.events_by_course.filter(
...         start_date__lte=enr.start_date)
...       # if missed_events.count() == 0: return
...       missed_events = ', '.join([dd.fds(o.start_date) for o in missed_events])
...       print("Missed events: {0}".format(missed_events))
...     print("Description:")
...     print(noblanklines(obj.description))


And run it:

>>> for o in qs2: fmt(o)  #doctest: +REPORT_UDIFF
--- Invoice #18 for enrolment #21 (003 comp (First Steps) / Daniel Emonts (MES)):
Title: Enrolment to 003 comp (First Steps)
Start date: 06/05/2014
Missed events: 24/03/2014, 31/03/2014, 07/04/2014, 14/04/2014, 28/04/2014, 05/05/2014
Description:
Time: Every Monday 13:30-15:00.
Tariff: 20€.
Scheduled dates:
12/05/2014, 19/05/2014, 
--- Invoice #23 for enrolment #61 (004 comp (First Steps) / Christian Radermacher (MEL)):
Title: Enrolment to 004 comp (First Steps)
Start date: 02/04/2014
Missed events: 19/03/2014, 26/03/2014, 02/04/2014
Description:
Time: Every Wednesday 17:30-19:00.
Tariff: 20€.
Scheduled dates:
02/04/2014, 09/04/2014, 16/04/2014, 23/04/2014, 30/04/2014, 07/05/2014, 

Let's have a closer look at the first of above invoicings.

>>> course = rt.models.courses.Course.objects.get(pk=4)

These are the scheduled events for the course:

>>> qs = course.events_by_course.order_by('start_date')
>>> print(', '.join([dd.fds(e.start_date) for e in qs]))
19/03/2014, 26/03/2014, 02/04/2014, 09/04/2014, 16/04/2014, 23/04/2014, 30/04/2014, 07/05/2014

But our enrolment starts later:

>>> enr = rt.models.courses.Enrolment.objects.get(pk=61)
>>> print(dd.fds(enr.start_date))
02/04/2014
>>> enr.end_date

So it missed the first three events and covers only the following
events:

>>> qs = rt.models.system.PeriodEvents.started.add_filter(qs, enr)
>>> print(', '.join([dd.fds(e.start_date) for e in qs]))
02/04/2014, 09/04/2014, 16/04/2014, 23/04/2014, 30/04/2014, 07/05/2014


Invoicing plan
==============

The demo database contains exactly one plan, which still holds
information about the last invoicing run.

>>> obj = rt.models.invoicing.Plan.objects.all()[0]
>>> rt.show('invoicing.ItemsByPlan', obj)  #doctest: +REPORT_UDIFF
==================== ===================== ====================================================================== ============ ========= ==========
 Selected             Partner               Preview                                                                Amount       Invoice   Workflow
-------------------- --------------------- ---------------------------------------------------------------------- ------------ --------- ----------
 Yes                  Charlier Ulrike       [3] Renewal Enrolment to 010C FG (Functional gymnastics) (50.00 €)     50,00        SLS 91
 Yes                  Engels Edgar          [3] Renewal Enrolment to 006C WWW (Internet for beginners) (48.00 €)   48,00        SLS 92
 Yes                  Brecht Bernd          [3] Renewal Enrolment to 007C WWW (Internet for beginners) (48.00 €)   48,00        SLS 93
 Yes                  Meier Marie-Louise    [3] Renewal Enrolment to 006C WWW (Internet for beginners) (48.00 €)   48,00        SLS 94
 Yes                  Bastiaensen Laurent   [3] Renewal Enrolment to 007C WWW (Internet for beginners) (48.00 €)   48,00        SLS 95
 Yes                  Radermacher Hedi      Enrolment to 019 SV (Self-defence) (20.00 €)                           20,00        SLS 96
 Yes                  Dupont Jean           [1] Enrolment to 023C MED (Finding your inner peace) (64.00 €)         64,00        SLS 97
 **Total (7 rows)**                                                                                                **326,00**
==================== ===================== ====================================================================== ============ ========= ==========
<BLANKLINE>


Item descriptions
=================

The template :xfile:`courses/Enrolment/item_description.html` defines
the text to use as the description of an invoice item
when generating invoices.

Here is an overview of the different cases of item descriptions.

>>> qs = InvoiceItem.objects.filter(invoiceable_id__isnull=False)
>>> qs.count()
120
>>> cases = set()
>>> for i in qs:
...     e = i.invoiceable
...     k = (e.places == 1, e.start_date is None, 
...         e.course.start_time is None,
...         e.start_date is None,
...         e.option_id is None,
...         e.fee.number_of_events is None,
...         e.course.every_unit)
...     if k in cases: continue
...     print "=== {} ===".format(k)
...     fmt(i)
...     cases.add(k)
...  #doctest: +REPORT_UDIFF
=== (True, True, False, True, True, False, <Recurrencies.weekly:W>) ===
--- Invoice #1 for enrolment #52 (022C MED (Finding your inner peace) / Marie-Louise Meier (ME)):
Title: [1] Enrolment to 022C MED (Finding your inner peace)
Start date: 
Description:
Time: Every Monday 18:00-19:30.
Tariff: 64€/12 hours.
=== (True, False, False, False, True, False, <Recurrencies.weekly:W>) ===
--- Invoice #3 for enrolment #26 (025C Yoga / Luc Faymonville (MEL)):
Title: [1] Enrolment to 025C Yoga
Start date: 23/11/2013
Missed events: 08/11/2013, 15/11/2013, 22/11/2013
Description:
Participant: Luc Faymonville (MEL).
Time: Every Friday 19:00-20:30.
Tariff: 50€/5 hours.
Your start date: 23/11/2013.
=== (True, True, False, True, True, True, <Recurrencies.weekly:W>) ===
--- Invoice #10 for enrolment #50 (003 comp (First Steps) / Marie-Louise Meier (ME)):
Title: Enrolment to 003 comp (First Steps)
Start date: 
Description:
Time: Every Monday 13:30-15:00.
Tariff: 20€.
Scheduled dates:
24/03/2014, 31/03/2014, 07/04/2014, 14/04/2014, 28/04/2014, 05/05/2014, 12/05/2014, 19/05/2014, 
=== (True, False, False, False, True, True, <Recurrencies.weekly:W>) ===
--- Invoice #18 for enrolment #21 (003 comp (First Steps) / Daniel Emonts (MES)):
Title: Enrolment to 003 comp (First Steps)
Start date: 06/05/2014
Missed events: 24/03/2014, 31/03/2014, 07/04/2014, 14/04/2014, 28/04/2014, 05/05/2014
Description:
Time: Every Monday 13:30-15:00.
Tariff: 20€.
Scheduled dates:
12/05/2014, 19/05/2014, 
=== (True, True, True, True, True, True, <Recurrencies.once:O>) ===
--- Invoice #38 for enrolment #1 (001 Greece 2014 / Hans Altenberg (MEL)):
Title: Enrolment to 001 Greece 2014
Start date: 
Description:
Date: 14/08/2014-20/08/2014.
Tariff: Journeys.
=== (False, True, True, True, True, True, <Recurrencies.once:O>) ===
--- Invoice #40 for enrolment #59 (001 Greece 2014 / Alfons Radermacher (ME)):
Title: Enrolment to 001 Greece 2014
Start date: 
Description:
Participant: Alfons Radermacher (ME).
Places used: 2.
Date: 14/08/2014-20/08/2014.
Tariff: Journeys.


Invoice recipient
=================

TODO: write explanations between the examples.

>>> show_fields(rt.models.contacts.Partner, 'invoice_recipient')
=================== =================== ===========================================================================
 Internal name       Verbose name        Help text
------------------- ------------------- ---------------------------------------------------------------------------
 invoice_recipient   Invoicing address   Redirect to another partner all invoices which should go to this partner.
=================== =================== ===========================================================================

>>> for p in rt.models.contacts.Partner.objects.filter(invoice_recipient__isnull=False):
...     print("{} --> {}".format(p, p.invoice_recipient))
Faymonville Luc --> Engels Edgar
Radermacher Alfons --> Emonts-Gast Erna
Martelaer Mark --> Dupont Jean

>>> p = rt.models.courses.Pupil.objects.get(last_name="Engels")
>>> rt.show(rt.models.sales.PartnersByInvoiceRecipient, p)
================= ===== ===========================
 Name              ID    Address
----------------- ----- ---------------------------
 Faymonville Luc   130   Brabantstraße, 4700 Eupen
================= ===== ===========================
<BLANKLINE>

>>> p = rt.models.courses.Pupil.objects.get(last_name="Faymonville")
>>> p
Pupil #130 ('Luc Faymonville (MEL)')

>>> rt.show('courses.EnrolmentsByPupil', p)
==================== ======================= ============ ============ ============= ======== ============ ===============
 Date of request      Activity                Start date   End date     Places used   Remark   Amount       Workflow
-------------------- ----------------------- ------------ ------------ ------------- -------- ------------ ---------------
 08/11/2013           024C Yoga                                         1                      50,00        **Confirmed**
 23/11/2013           025C Yoga               23/11/2013                1                      50,00        **Confirmed**
 21/06/2015           015 Rücken (Swimming)                             1                      80,00        **Confirmed**
 11/07/2015           014 Rücken (Swimming)                01/08/2015   1                      80,00        **Confirmed**
 11/07/2015           014 Rücken (Swimming)   29/08/2015                1                      80,00        **Confirmed**
 **Total (5 rows)**                                                     **5**                  **340,00**
==================== ======================= ============ ============ ============= ======== ============ ===============
<BLANKLINE>

>>> e = rt.models.courses.Enrolment.objects.get(id=22)
>>> e
Enrolment #22 ('006C WWW (Internet for beginners) / Edgar Engels (ME)')

>>> rt.show('invoicing.InvoicingsByInvoiceable', e)
==================== ============================================================ ========== ============== ============ ==================
 Product invoice      Heading                                                      Quantity   Voucher date   State        Number of events
-------------------- ------------------------------------------------------------ ---------- -------------- ------------ ------------------
 SLS 51               [1] Enrolment to 006C WWW (Internet for beginners)           1          01/11/2014     Registered   8
 SLS 71               [2] Renewal Enrolment to 006C WWW (Internet for beginners)   1          01/01/2015     Registered   8
 SLS 92               [3] Renewal Enrolment to 006C WWW (Internet for beginners)   1          01/03/2015     Registered   8
 **Total (3 rows)**                                                                **3**                                  **24**
==================== ============================================================ ========== ============== ============ ==================
<BLANKLINE>

>>> rt.show('sales.InvoicesByPartner', p)
No data to display

>>> p = rt.models.courses.Pupil.objects.get(last_name="Engels")
>>> p
Pupil #129 ('Edgar Engels (ME)')

>>> rt.show('sales.InvoicesByPartner', p)
===================== =========== ========= ================= ================
 Entry date            Reference   No.       Total incl. VAT   Workflow
--------------------- ----------- --------- ----------------- ----------------
 01/03/2015            SLS         92        48,00             **Registered**
 01/02/2015            SLS         82        114,00            **Registered**
 01/01/2015            SLS         71        98,00             **Registered**
 01/11/2014            SLS         51        98,00             **Registered**
 01/10/2014            SLS         41        50,00             **Registered**
 01/08/2014            SLS         34        50,00             **Registered**
 01/07/2014            SLS         28        50,00             **Registered**
 01/06/2014            SLS         26        50,00             **Registered**
 01/04/2014            SLS         13        50,00             **Registered**
 01/03/2014            SLS         9         50,00             **Registered**
 01/02/2014            SLS         7         50,00             **Registered**
 01/01/2014            SLS         3         100,00            **Registered**
 **Total (12 rows)**               **457**   **808,00**
===================== =========== ========= ================= ================
<BLANKLINE>

