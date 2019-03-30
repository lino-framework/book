.. doctest docs/specs/voga/invoicing.rst
.. _voga.specs.invoicing:

========================================================
Invoicing in Lino Voga (:mod:`lino_voga.lib.invoicing`)
========================================================

This document explains how Lino Voga generates invoices.

General functionality for automatically generating invoices is defined
in :mod:`lino_xl.lib.invoicing`.


.. contents:: 
   :local:
   :depth: 2

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.roger.settings.doctests')
>>> from lino.api.doctest import *


Overview
========

In Lino Voga, enrolments are the things that generate invoices.  This
is implemented by extending :class:`Enrolment
<lino_xl.lib.courses.Enrolment>` so that it inherits from
:class:`Invoiceable <lino_xl.lib.invoicing.InvoiceGenerator>`.

Another invoiceable thing in Lino Voga is when they rent a room to a
third-party organisation.  This is called a :class:`Booking
<lino_voga.lib.rooms.models.Booking>`.

IOW, in Lino Voga both :class:`Enrolment
<lino_xl.lib.courses.models.Enrolment>` and :class:`Booking
<lino_voga.lib.rooms.models.Booking>` are :class:`InvoiceGenerator
<lino_xl.lib.invoicing.InvoiceGenerator>`:

>>> rt.models_by_base(rt.models.invoicing.InvoiceGenerator)
[<class 'lino_voga.lib.roger.courses.models.Enrolment'>, <class 'lino_voga.lib.rooms.models.Booking'>]


User interface
==============

On the user-visible level this plugin adds

- a menu entry :menuselection:`Journals --> Create invoices`,

and a :class:`StartInvoicing <lino_xl.lib.invoicing.StartInvoicing>`
action (with a basket as icon, referring to a shopping basket) at four
places:

- as a menu command :menuselection:`Accounting --> Create invoices`
- on every *partner* (generate invoices for this partner)
- on every *course* (generate invoices for all enrolments of this
  course)
- on every *journal* which supports automatic invoice generation. 

>>> rt.models.contacts.Partner.start_invoicing
<lino_xl.lib.invoicing.actions.StartInvoicingForPartner start_invoicing ('Create invoices')>

>>> rt.models.courses.Course.start_invoicing
<lino_voga.lib.invoicing.models.StartInvoicingForCourse start_invoicing ('Create invoices')>

Enrolments are invoice generators
=================================

:attr:`Enrolment.invoicing_info` is a summary of what has been
invoiced by a given enrolment.

>>> from textwrap import wrap
>>> for obj in courses.Enrolment.objects.order_by("id"):
...     ii = '\n'.join(wrap(to_rst(obj.invoicing_info), 80))
...     print(u"{} : {} {}\n{}".format(obj.id, obj.course, obj.pupil, ii))
...     #doctest: +REPORT_UDIFF +NORMALIZE_WHITESPACE
1 : 001 Greece 2014 Hans Altenberg (MEL)
Invoiced : 14.08.
2 : 002 London 2014 Laurent Bastiaensen (ME)
Invoiced : 14.07.
3 : Five Weekends 2015 Laurent Bastiaensen (ME)
No invoiced events
4 : 004 comp (First Steps) Laurent Bastiaensen (ME)
Invoiced : (...) 23.04., 30.04., 07.05.
5 : 007C WWW (Internet for beginners) Ulrike Charlier (ME)
Invoiced : (...) 29.04., 06.05., 13.05. Not invoiced : 12.11., 19.11., 03.12.,
10.12., 17.12., 24.12., 31.12., 07.01., 14.01., 28.01., 04.02., 11.02., 25.02.,
04.03., 11.03., 18.03.
6 : 009C BT (Belly dancing) Ulrike Charlier (ME)
Not invoiced : 02.04., 09.04., 16.04.
7 : 009C BT (Belly dancing) Ulrike Charlier (ME)
Not invoiced : 21.05., 28.05., 04.06., 11.06., 18.06., 02.07., 09.07., 16.07.,
23.07., 30.07., 06.08., 13.08., 27.08., 03.09., 10.09., 17.09., 24.09., 01.10.,
08.10., 22.10., 29.10., 05.11., 12.11., 19.11., 26.11., 03.12., 17.12., 24.12.,
31.12., 07.01., 14.01., 21.01., 28.01., 11.02., 25.02., 04.03., 11.03., 18.03.,
25.03., 01.04., 15.04., 22.04., 29.04., 06.05., 13.05., 20.05.
8 : 010C FG (Functional gymnastics) Ulrike Charlier (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 06.10., 20.10., 27.10.,
03.11., 10.11., 17.11., 24.11., 01.12., 15.12., 22.12., 29.12., 05.01., 12.01.,
19.01., 26.01., 09.02., 23.02., 02.03., 09.03., 16.03.
9 : 011C FG (Functional gymnastics) Ulrike Charlier (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 06.10., 13.10., 27.10.,
03.11., 10.11., 17.11., 24.11., 01.12., 08.12., 22.12., 29.12., 05.01., 12.01.,
19.01., 26.01., 02.02., 23.02., 02.03., 09.03., 16.03.
10 : 012 Rücken (Swimming) Ulrike Charlier (ME)
No invoiced events
11 : 013 Rücken (Swimming) Daniel Dericum (ME)
No invoiced events
12 : 018 SV (Self-defence) Dorothée Demeulenaere (ME)
Invoiced : 20.03., 10.04., 17.04.
13 : 019 SV (Self-defence) Dorothée Demeulenaere (ME)
Invoiced : 06.03., 13.03., 20.03.
14 : 019 SV (Self-defence) Dorothée Demeulenaere (ME)
No invoiced events
15 : 020C GLQ (GuoLin-Qigong) Dorothée Dobbelstein-Demeulenaere (ME)
Invoiced : (...) 27.04., 04.05., 18.05. Not invoiced : 28.07., 04.08., 11.08.,
18.08., 25.08., 01.09., 08.09., 22.09., 29.09., 06.10., 13.10., 20.10., 27.10.,
03.11., 17.11., 24.11., 01.12., 08.12., 15.12., 22.12., 29.12., 12.01., 19.01.,
26.01., 02.02., 09.02., 23.02., 02.03., 16.03., 23.03., 30.03., 13.04.
16 : 021C GLQ (GuoLin-Qigong) Dorothée Dobbelstein-Demeulenaere (ME)
Not invoiced : 18.07., 25.07., 01.08., 08.08., 22.08., 29.08., 12.09., 19.09.,
26.09., 03.10., 10.10., 17.10., 24.10., 14.11., 21.11., 28.11., 05.12., 12.12.,
19.12., 26.12., 09.01., 16.01., 23.01., 30.01., 06.02., 13.02., 20.02., 24.04.,
08.05., 15.05.
17 : 005 comp (First Steps) Dorothée Dobbelstein-Demeulenaere (ME)
Invoiced : 28.03., 04.04., 11.04.
18 : 008C WWW (Internet for beginners) Eberhart Evers (ME)
Not invoiced : 24.10., 07.11., 14.11., 21.11., 28.11., 05.12., 12.12., 26.12.,
02.01., 09.01., 16.01., 23.01., 30.01., 06.02., 20.02., 27.02., 06.03., 13.03.,
20.03., 27.03., 10.04., 24.04., 08.05., 15.05.
19 : 016 Rücken (Swimming) Daniel Emonts (MES)
No invoiced events
20 : 017 Rücken (Swimming) Daniel Emonts (MES)
No invoiced events
21 : 017 Rücken (Swimming) Daniel Emonts (MES)
No invoiced events
22 : 003 comp (First Steps) Edgar Engels (ME)
Invoiced : (...) 05.05., 12.05., 19.05.
23 : 006C WWW (Internet for beginners) Edgar Engels (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 03.11., 10.11., 17.11.,
24.11., 01.12., 08.12., 15.12., 29.12., 05.01., 12.01., 19.01., 26.01., 02.02.,
09.02., 02.03., 09.03.
24 : 022C MED (Finding your inner peace) Edgar Engels (ME)
Not invoiced : 23.09., 30.09., 07.10., 14.10.
25 : 023C MED (Finding your inner peace) Luc Faymonville (MEL)
Not invoiced : 06.02., 13.02., 20.02., 27.02., 13.03., 20.03., 27.03., 10.04.,
17.04., 24.04., 08.05.
26 : 024C Yoga Luc Faymonville (MEL)
Invoiced : 04.05., 11.05. Not invoiced : 23.03., 30.03., 13.04., 20.04., 27.04.
27 : 025C Yoga Luc Faymonville (MEL)
Not invoiced : 08.11., 15.11., 22.11., 29.11.
28 : 025C Yoga Luc Faymonville (MEL)
Not invoiced : 03.01., 10.01., 17.01., 24.01., 31.01., 07.02., 14.02., 28.02.,
07.03., 14.03., 21.03., 28.03., 04.04., 11.04., 02.05., 09.05., 16.05., 23.05.,
30.05., 06.06., 13.06., 27.06., 04.07., 11.07., 18.07., 25.07., 01.08., 08.08.,
29.08., 05.09., 12.09., 19.09., 26.09., 03.10., 10.10., 24.10., 07.11., 14.11.,
21.11., 28.11., 05.12., 12.12., 26.12., 02.01., 09.01., 16.01., 23.01., 30.01.
29 : 014 Rücken (Swimming) Luc Faymonville (MEL)
No invoiced events
30 : 015 Rücken (Swimming) Hildegard Hilgers (ME)
No invoiced events
31 : 001 Greece 2014 Jacqueline Jacobs (ME)
Invoiced : 14.08.
32 : 002 London 2014 Jacqueline Jacobs (ME)
Invoiced : 14.07.
33 : Five Weekends 2015 Jacqueline Jacobs (ME)
No invoiced events
34 : 004 comp (First Steps) Jacqueline Jacobs (ME)
Invoiced : 26.03., 02.04.
35 : 004 comp (First Steps) Jacqueline Jacobs (ME)
Invoiced : 07.05.
36 : 007C WWW (Internet for beginners) Jacqueline Jacobs (ME)
Invoiced : 13.05. Not invoiced : 29.10., 05.11., 12.11., 19.11., 03.12., 10.12.,
17.12., 24.12., 31.12., 07.01., 14.01., 28.01., 04.02., 11.02., 25.02., 04.03.,
11.03., 18.03., 01.04., 08.04., 15.04., 22.04., 29.04., 06.05.
37 : 009C BT (Belly dancing) Josef Jonas (ME)
Invoiced : (...) 06.05., 13.05., 20.05. Not invoiced : 02.04., 09.04., 16.04.,
23.04., 07.05., 14.05., 21.05., 28.05., 04.06., 11.06., 18.06., 02.07., 09.07.,
16.07., 23.07., 30.07., 06.08., 13.08., 27.08., 03.09., 10.09., 17.09., 24.09.,
01.10., 08.10., 22.10., 29.10., 05.11., 12.11., 19.11., 26.11., 03.12., 17.12.,
24.12., 31.12., 07.01., 14.01., 21.01., 28.01., 11.02., 25.02., 04.03., 11.03.,
18.03., 25.03., 01.04., 15.04., 22.04.
38 : 010C FG (Functional gymnastics) Karl Kaivers (ME)
Not invoiced : 06.10., 20.10., 27.10., 03.11.
39 : 011C FG (Functional gymnastics) Karl Kaivers (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 06.10., 13.10., 27.10.,
03.11., 10.11., 17.11., 24.11., 01.12., 08.12., 22.12., 29.12., 05.01., 12.01.,
19.01., 26.01., 02.02., 23.02., 02.03., 09.03., 16.03.
40 : 012 Rücken (Swimming) Karl Kaivers (ME)
No invoiced events
41 : 013 Rücken (Swimming) Laura Laschet (ME)
No invoiced events
42 : 013 Rücken (Swimming) Laura Laschet (ME)
No invoiced events
43 : 018 SV (Self-defence) Laura Laschet (ME)
Invoiced : (...) 20.03., 10.04., 17.04.
44 : 019 SV (Self-defence) Laura Laschet (ME)
Invoiced : (...) 20.03., 27.03., 10.04.
45 : 020C GLQ (GuoLin-Qigong) Laura Laschet (ME)
Not invoiced : 28.07., 04.08., 11.08., 18.08.
46 : 021C GLQ (GuoLin-Qigong) Laura Laschet (ME)
Not invoiced : 18.07., 25.07., 01.08., 08.08., 22.08., 29.08., 12.09., 19.09.,
26.09., 03.10., 10.10., 17.10., 24.10., 14.11., 21.11., 28.11., 05.12., 12.12.,
19.12., 26.12., 09.01., 16.01., 23.01., 30.01., 06.02., 13.02., 20.02., 24.04.,
08.05., 15.05.
47 : 005 comp (First Steps) Josefine Leffin (MEL)
Invoiced : (...) 02.05., 09.05., 16.05.
48 : 008C WWW (Internet for beginners) Marie-Louise Meier (ME)
Not invoiced : 24.10., 07.11., 14.11.
49 : 008C WWW (Internet for beginners) Marie-Louise Meier (ME)
Invoiced : 08.05., 15.05. Not invoiced : 12.12., 26.12., 02.01., 09.01., 16.01.,
23.01., 30.01., 06.02., 20.02., 27.02., 06.03., 13.03., 20.03., 27.03., 10.04.,
24.04.
50 : 016 Rücken (Swimming) Marie-Louise Meier (ME)
No invoiced events
51 : 017 Rücken (Swimming) Marie-Louise Meier (ME)
No invoiced events
52 : 003 comp (First Steps) Marie-Louise Meier (ME)
Invoiced : 31.03., 07.04., 14.04.
53 : 006C WWW (Internet for beginners) Marie-Louise Meier (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 03.11., 10.11., 17.11.,
24.11., 01.12., 08.12., 15.12., 29.12., 05.01., 12.01., 19.01., 26.01., 02.02.,
09.02., 02.03., 09.03.
54 : 022C MED (Finding your inner peace) Erna Emonts-Gast (MS)
Not invoiced : 07.10., 14.10., 28.10., 04.11., 18.11., 25.11., 02.12., 09.12.,
16.12., 30.12., 06.01., 13.01., 20.01., 27.01., 03.02., 10.02., 24.02., 10.03.,
17.03., 24.03., 31.03., 07.04., 14.04., 05.05., 12.05., 19.05., 26.05., 02.06.,
16.06., 23.06., 07.07., 14.07., 28.07., 04.08., 11.08., 18.08., 25.08., 08.09.,
15.09., 22.09., 29.09., 06.10., 13.10., 20.10., 03.11., 10.11., 17.11., 24.11.,
01.12., 08.12., 15.12., 29.12., 05.01., 12.01., 19.01., 26.01., 02.02., 09.02.,
02.03., 09.03., 16.03.
55 : 023C MED (Finding your inner peace) Erna Emonts-Gast (MS)
Not invoiced : 06.02., 13.02., 20.02.
56 : 023C MED (Finding your inner peace) Erna Emonts-Gast (MS)
Not invoiced : 27.03., 10.04., 17.04., 24.04., 08.05.
57 : 024C Yoga Alfons Radermacher (ME)
Invoiced : 04.05., 11.05. Not invoiced : 23.03., 30.03., 13.04., 20.04., 27.04.
58 : 025C Yoga Alfons Radermacher (ME)
Not invoiced : 08.11., 15.11., 22.11., 29.11., 06.12., 13.12., 20.12., 03.01.,
10.01., 17.01., 24.01., 31.01., 07.02., 14.02., 28.02., 07.03., 14.03., 21.03.,
28.03., 04.04., 11.04., 02.05., 09.05., 16.05., 23.05., 30.05., 06.06., 13.06.,
27.06., 04.07., 11.07., 18.07., 25.07., 01.08., 08.08., 29.08., 05.09., 12.09.,
19.09., 26.09., 03.10., 10.10., 24.10., 07.11., 14.11., 21.11., 28.11., 05.12.,
12.12., 26.12., 02.01., 09.01., 16.01., 23.01., 30.01.
59 : 014 Rücken (Swimming) Alfons Radermacher (ME)
No invoiced events
60 : 015 Rücken (Swimming) Christian Radermacher (MEL)
No invoiced events
61 : 001 Greece 2014 Christian Radermacher (MEL)
No invoiced events
62 : 002 London 2014 Christian Radermacher (MEL)
Invoiced : 14.07.
63 : 002 London 2014 Christian Radermacher (MEL)
No invoiced events
64 : Five Weekends 2015 Christian Radermacher (MEL)
No invoiced events
65 : 004 comp (First Steps) Christian Radermacher (MEL)
Invoiced : (...) 23.04., 30.04., 07.05.
66 : 007C WWW (Internet for beginners) Edgard Radermacher (ME)
Not invoiced : 29.10., 05.11., 12.11., 19.11.
67 : 009C BT (Belly dancing) Guido Radermacher (ME)
Invoiced : (...) 06.05., 13.05., 20.05. Not invoiced : 02.04., 09.04., 16.04.,
23.04., 07.05., 14.05., 21.05., 28.05., 04.06., 11.06., 18.06., 02.07., 09.07.,
16.07., 23.07., 30.07., 06.08., 13.08., 27.08., 03.09., 10.09., 17.09., 24.09.,
01.10., 08.10., 22.10., 29.10., 05.11., 12.11., 19.11., 26.11., 03.12., 17.12.,
24.12., 31.12., 07.01., 14.01., 21.01., 28.01., 11.02., 25.02., 04.03., 11.03.,
18.03., 25.03., 01.04., 15.04., 22.04.
68 : 010C FG (Functional gymnastics) Guido Radermacher (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 20.10., 27.10., 03.11.,
10.11., 17.11., 24.11., 01.12., 15.12., 22.12., 29.12., 05.01., 12.01., 19.01.,
26.01., 09.02., 23.02., 02.03., 09.03., 16.03., 23.03.
69 : 011C FG (Functional gymnastics) Guido Radermacher (ME)
Not invoiced : 06.10., 13.10.
70 : 011C FG (Functional gymnastics) Guido Radermacher (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 24.11., 01.12., 08.12.,
22.12., 29.12., 05.01., 12.01., 19.01., 26.01., 02.02., 23.02., 02.03., 09.03.,
16.03., 23.03.
71 : 012 Rücken (Swimming) Hedi Radermacher (ME)
No invoiced events
72 : 013 Rücken (Swimming) Hedi Radermacher (ME)
No invoiced events
73 : 018 SV (Self-defence) Hedi Radermacher (ME)
Invoiced : 06.03., 13.03., 20.03.
74 : 019 SV (Self-defence) Hedi Radermacher (ME)
Invoiced : (...) 20.03., 27.03., 10.04.
75 : 020C GLQ (GuoLin-Qigong) Hedi Radermacher (ME)
Invoiced : 27.04., 04.05., 18.05. Not invoiced : 04.08., 11.08., 18.08., 25.08.,
01.09., 08.09., 22.09., 29.09., 06.10., 13.10., 20.10., 27.10., 03.11., 17.11.,
24.11., 01.12., 08.12., 15.12., 22.12., 29.12., 12.01., 19.01., 26.01., 02.02.,
09.02., 23.02., 02.03., 16.03., 23.03., 30.03., 13.04., 20.04.
76 : 021C GLQ (GuoLin-Qigong) Jean Radermacher (ME)
Not invoiced : 18.07., 25.07., 01.08.
77 : 021C GLQ (GuoLin-Qigong) Jean Radermacher (ME)
Not invoiced : 12.09., 19.09., 26.09., 03.10., 10.10., 17.10., 24.10., 14.11.,
21.11., 28.11., 05.12., 12.12., 19.12., 26.12., 09.01., 16.01., 23.01., 30.01.,
06.02., 13.02., 20.02., 24.04., 08.05., 15.05.
78 : 005 comp (First Steps) Didier di Rupo (MS)
Invoiced : (...) 02.05., 09.05., 16.05.
79 : 008C WWW (Internet for beginners) Didier di Rupo (MS)
Not invoiced : 24.10., 07.11., 14.11., 21.11., 28.11., 05.12., 12.12., 26.12.,
02.01., 09.01., 16.01., 23.01., 30.01., 06.02., 20.02., 27.02., 06.03., 13.03.,
20.03., 27.03., 10.04., 24.04., 08.05., 15.05.
80 : 016 Rücken (Swimming) Erna Ärgerlich (ME)
No invoiced events
81 : 017 Rücken (Swimming) Jean Dupont (ME)
No invoiced events
82 : 003 comp (First Steps) Jean Dupont (ME)
Invoiced : (...) 05.05., 12.05., 19.05.
83 : 006C WWW (Internet for beginners) Jean Dupont (ME)
Not invoiced : 03.11., 10.11.
84 : 006C WWW (Internet for beginners) Jean Dupont (ME)
Invoiced : (...) 04.05., 11.05., 18.05. Not invoiced : 15.12., 29.12., 05.01.,
12.01., 19.01., 26.01., 02.02., 09.02., 02.03., 09.03.
85 : 022C MED (Finding your inner peace) Mark Martelaer (MS)
Not invoiced : 23.09., 30.09., 07.10., 14.10., 28.10., 04.11., 18.11., 25.11.,
02.12., 09.12., 16.12., 30.12., 06.01., 13.01., 20.01., 27.01., 03.02., 10.02.,
24.02., 10.03., 17.03., 24.03., 31.03., 07.04., 14.04., 05.05., 12.05., 19.05.,
26.05., 02.06., 16.06., 23.06., 07.07., 14.07., 28.07., 04.08., 11.08., 18.08.,
25.08., 08.09., 15.09., 22.09., 29.09., 06.10., 13.10., 20.10., 03.11., 10.11.,
17.11., 24.11., 01.12., 08.12., 15.12., 29.12., 05.01., 12.01., 19.01., 26.01.,
02.02., 09.02., 02.03., 09.03., 16.03.
86 : 023C MED (Finding your inner peace) Mark Martelaer (MS)
Not invoiced : 06.02., 13.02., 20.02., 27.02., 13.03., 20.03., 27.03., 10.04.,
17.04., 24.04., 08.05.
87 : 024C Yoga Mark Martelaer (MS)
No invoiced events
88 : 025C Yoga Mark Martelaer (MS)
Not invoiced : 08.11., 15.11., 22.11., 29.11., 06.12., 13.12., 20.12., 03.01.,
10.01., 17.01., 24.01., 31.01., 07.02., 14.02., 28.02., 07.03., 14.03., 21.03.,
28.03., 04.04., 11.04., 02.05., 09.05., 16.05., 23.05., 30.05., 06.06., 13.06.,
27.06., 04.07., 11.07., 18.07., 25.07., 01.08., 08.08., 29.08., 05.09., 12.09.,
19.09., 26.09., 03.10., 10.10., 24.10., 07.11., 14.11., 21.11., 28.11., 05.12.,
12.12., 26.12., 02.01., 09.01., 16.01., 23.01., 30.01.
89 : 014 Rücken (Swimming) Lisa Lahm (MS)
No invoiced events
90 : 015 Rücken (Swimming) Lisa Lahm (MS)
No invoiced events
91 : 015 Rücken (Swimming) Lisa Lahm (MS)
No invoiced events
92 : 001 Greece 2014 Bernd Brecht (ME)
Invoiced : 14.08.
93 : 002 London 2014 Bernd Brecht (ME)
Invoiced : 14.07.
94 : Five Weekends 2015 Bernd Brecht (ME)
No invoiced events
95 : 004 comp (First Steps) Jérôme Jeanémart (ME)
Invoiced : (...) 23.04., 30.04., 07.05.

Here is a list of all enrolments:

>>> rt.show(rt.models.courses.Enrolments)
...     #doctest: +REPORT_UDIFF +ELLIPSIS
================= ===================================== ========= ======================================== =============== =================
 Date of request   Activity                              State     Participant                              Workflow        Author
----------------- ------------------------------------- --------- ---------------------------------------- --------------- -----------------
 30/08/2013        022C MED (Finding your inner peace)   Started   Mark Martelaer (MS)                      **Confirmed**   Tom Thess
 14/09/2013        022C MED (Finding your inner peace)   Started   Edgar Engels (ME)                        **Confirmed**   Monique Mommer
 04/10/2013        022C MED (Finding your inner peace)   Started   Erna Emonts-Gast (MS)                    **Confirmed**   Rolf Rompen
 19/10/2013        024C Yoga                             Started   Alfons Radermacher (ME)                  **Confirmed**   Tom Thess
 03/11/2013        025C Yoga                             Started   Alfons Radermacher (ME)                  **Requested**   Marianne Martin
 03/11/2013        024C Yoga                             Started   Mark Martelaer (MS)                      **Confirmed**   Monique Mommer
 08/11/2013        025C Yoga                             Started   Luc Faymonville (MEL)                    **Confirmed**   Robin Rood
 08/11/2013        025C Yoga                             Started   Luc Faymonville (MEL)                    **Confirmed**   Robin Rood
 08/11/2013        025C Yoga                             Started   Mark Martelaer (MS)                      **Confirmed**   Romain Raffault
 23/11/2013        024C Yoga                             Started   Luc Faymonville (MEL)                    **Confirmed**   Rolf Rompen
 26/02/2014        003 comp (First Steps)                Started   Edgar Engels (ME)                        **Confirmed**   Tom Thess
 26/02/2014        005 comp (First Steps)                Started   Didier di Rupo (MS)                      **Confirmed**   Tom Thess
 ...
 11/07/2015        017 Rücken (Swimming)                 Started   Daniel Emonts (MES)                      **Confirmed**   Robin Rood
 11/07/2015        017 Rücken (Swimming)                 Started   Daniel Emonts (MES)                      **Confirmed**   Robin Rood
 11/07/2015        013 Rücken (Swimming)                 Started   Laura Laschet (ME)                       **Confirmed**   Robin Rood
 11/07/2015        013 Rücken (Swimming)                 Started   Laura Laschet (ME)                       **Confirmed**   Robin Rood
 11/07/2015        017 Rücken (Swimming)                 Started   Jean Dupont (ME)                         **Requested**   Romain Raffault
 26/07/2015        016 Rücken (Swimming)                 Started   Daniel Emonts (MES)                      **Confirmed**   Rolf Rompen
 26/07/2015        012 Rücken (Swimming)                 Started   Karl Kaivers (ME)                        **Confirmed**   Rolf Rompen
 26/07/2015        014 Rücken (Swimming)                 Started   Lisa Lahm (MS)                           **Confirmed**   Rolf Rompen
================= ===================================== ========= ======================================== =============== =================
<BLANKLINE>



Invoicings
==========

The :class:`lino_xl.lib.invoicing.InvoicingsByGenerator` table in the
detail window of an enrolment shows all invoicings of that enrolment:

>>> obj = courses.Enrolment.objects.get(pk=67)
>>> rt.show('invoicing.InvoicingsByGenerator', obj)
... #doctest: +REPORT_UDIFF
==================== ================================================== ========== ============== ============ ==================
 Sales invoice        Heading                                            Quantity   Voucher date   State        Number of events
-------------------- -------------------------------------------------- ---------- -------------- ------------ ------------------
 SLS 20/2014          [1] Enrolment to 009C BT (Belly dancing)           1          31/12/2013     Registered   12
 SLS 44/2014          [2] Renewal Enrolment to 009C BT (Belly dancing)   1          30/06/2014     Registered   12
 SLS 56/2014          [3] Renewal Enrolment to 009C BT (Belly dancing)   1          30/09/2014     Registered   12
 SLS 9/2015           [4] Renewal Enrolment to 009C BT (Belly dancing)   1          31/12/2014     Registered   12
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
>>> qs = qs.filter(fee__tariff__number_of_events__isnull=True)
>>> qs = qs.order_by('request_date')
>>> qs.count()
12

We want only those for which an invoice has been generated. Above
number shrinks to 10:

>>> from django.db.models import Count
>>> qs = qs.annotate(invoicings_count=Count('invoicings'))
>>> qs = qs.filter(invoicings_count__gt=0)
>>> qs.count()
10

Let's select the corresponding invoice items:

>>> InvoiceItem = dd.plugins.invoicing.item_model
>>> qs2 = InvoiceItem.objects.filter(
...     invoiceable_id__in=qs.values_list('id', flat=True))
>>> qs2.count()
10

Now we define a utility function which prints out what we want to see
for each of these items:

>>> def fmt(obj):
...     enr = obj.invoiceable
...     # avoid initdb_demo after change in item_description.html:
...     enr.setup_invoice_item(obj) 
...     print(u"--- Invoice #{0} for enrolment #{1} ({2}):".format(
...         obj.voucher.number, enr.id, enr))
...     print(u"Title: {0}".format(obj.title))
...     print("Start date: " + dd.fds(obj.invoiceable.start_date))
...     if enr.start_date:
...       missed_events = enr.course.events_by_course().filter(
...         start_date__lte=enr.start_date)
...       # if missed_events.count() == 0: return
...       missed_events = ', '.join([dd.fds(o.start_date) for o in missed_events])
...       print("Missed events: {0}".format(missed_events))
...     print("Description:")
...     print(noblanklines(obj.description))


And run it:

>>> for o in qs2: fmt(o)  #doctest: +REPORT_UDIFF
--- Invoice #5 for enrolment #12 (018 SV (Self-defence) / Dorothée Demeulenaere (ME)):
Title: Enrolment to 018 SV (Self-defence)
Start date: 18/03/2015
Missed events: 06/03/2015, 13/03/2015
Description:
Time: Every Friday 18:00-19:00.
Fee: 20€.
Scheduled dates:
20/03/2015, 27/03/2015, 10/04/2015, 17/04/2015, 
--- Invoice #5 for enrolment #14 (019 SV (Self-defence) / Dorothée Demeulenaere (ME)):
Title: Enrolment to 019 SV (Self-defence)
Start date: 21/04/2015
Missed events: 06/03/2015, 13/03/2015, 20/03/2015, 27/03/2015, 10/04/2015, 17/04/2015
Description:
Time: Every Friday 19:00-20:00.
Fee: 20€.
Scheduled dates:
--- Invoice #8 for enrolment #19 (016 Rücken (Swimming) / Daniel Emonts (MES)):
Title: Enrolment to 016 Rücken (Swimming)
Start date: 26/07/2015
Missed events: 16/07/2015, 23/07/2015
Description:
Time: Every Thursday 11:00-12:00.
Fee: 80€.
Scheduled dates:
30/07/2015, 06/08/2015, 13/08/2015, 20/08/2015, 27/08/2015, 03/09/2015, 10/09/2015, 17/09/2015, 
--- Invoice #8 for enrolment #21 (017 Rücken (Swimming) / Daniel Emonts (MES)):
Title: Enrolment to 017 Rücken (Swimming)
Start date: 29/08/2015
Missed events: 16/07/2015, 23/07/2015, 30/07/2015, 06/08/2015, 13/08/2015, 20/08/2015, 27/08/2015
Description:
Time: Every Thursday 13:30-14:30.
Fee: 80€.
Scheduled dates:
03/09/2015, 10/09/2015, 17/09/2015, 
--- Invoice #13 for enrolment #40 (012 Rücken (Swimming) / Karl Kaivers (ME)):
Title: Enrolment to 012 Rücken (Swimming)
Start date: 26/07/2015
Missed events: 
Description:
Time: Every Monday 11:00-12:00.
Fee: 80€.
Scheduled dates:
21/03/2016, 04/04/2016, 11/04/2016, 18/04/2016, 25/04/2016, 02/05/2016, 09/05/2016, 23/05/2016, 30/05/2016, 06/06/2016, 
--- Invoice #14 for enrolment #42 (013 Rücken (Swimming) / Laura Laschet (ME)):
Title: Enrolment to 013 Rücken (Swimming)
Start date: 29/08/2015
Missed events: 
Description:
Time: Every Monday 13:30-14:30.
Fee: 80€.
Scheduled dates:
21/03/2016, 04/04/2016, 11/04/2016, 18/04/2016, 25/04/2016, 02/05/2016, 09/05/2016, 23/05/2016, 30/05/2016, 06/06/2016, 
--- Invoice #15 for enrolment #47 (005 comp (First Steps) / Josefine Leffin (MEL)):
Title: Enrolment to 005 comp (First Steps)
Start date: 02/04/2014
Missed events: 21/03/2014, 28/03/2014
Description:
Time: Every Friday 13:30-15:00.
Fee: 20€.
Scheduled dates:
04/04/2014, 11/04/2014, 25/04/2014, 02/05/2014, 09/05/2014, 16/05/2014, 
--- Invoice #18 for enrolment #61 (001 Greece 2014 / Christian Radermacher (MEL)):
Title: Enrolment to 001 Greece 2014
Start date: 29/08/2014
Missed events: 14/08/2014
Description:
Date: 14/08/2014-20/08/2014.
Fee: Journeys.
--- Invoice #25 for enrolment #82 (003 comp (First Steps) / Jean Dupont (ME)):
Title: Enrolment to 003 comp (First Steps)
Start date: 02/04/2014
Missed events: 24/03/2014, 31/03/2014
Description:
Time: Every Monday 13:30-15:00.
Fee: 20€.
Scheduled dates:
07/04/2014, 14/04/2014, 28/04/2014, 05/05/2014, 12/05/2014, 19/05/2014, 
--- Invoice #26 for enrolment #89 (014 Rücken (Swimming) / Lisa Lahm (MS)):
Title: Enrolment to 014 Rücken (Swimming)
Start date: 26/07/2015
Missed events: 14/07/2015
Description:
Time: Every Tuesday 11:00-12:00.
Fee: 80€.
Scheduled dates:
28/07/2015, 04/08/2015, 11/08/2015, 18/08/2015, 25/08/2015, 01/09/2015, 08/09/2015, 15/09/2015, 22/09/2015, 

Let's have a closer look at one of above invoicings.

>>> enr = rt.models.courses.Enrolment.objects.get(pk=82)

These are the scheduled events for the course:

>>> qs = enr.course.events_by_course().order_by('start_date')
>>> print(', '.join([dd.fds(e.start_date) for e in qs]))
24/03/2014, 31/03/2014, 07/04/2014, 14/04/2014, 28/04/2014, 05/05/2014, 12/05/2014, 19/05/2014

But our enrolment starts later:

>>> print(dd.fds(enr.start_date))
02/04/2014
>>> enr.end_date

So it missed the first three events and covers only the following
events:

>>> qs = rt.models.system.PeriodEvents.started.add_filter(qs, enr)
>>> print(', '.join([dd.fds(e.start_date) for e in qs]))
07/04/2014, 14/04/2014, 28/04/2014, 05/05/2014, 12/05/2014, 19/05/2014


Invoicing plan
==============

The demo database contains exactly one plan, which still holds
information about the last invoicing run.

>>> obj = rt.models.invoicing.Plan.objects.all()[0]
>>> rt.show('invoicing.ItemsByPlan', obj)  #doctest: +REPORT_UDIFF
==================== =================== ======================================================================== ============ ===============
 Selected             Partner             Preview                                                                  Amount       Invoice
-------------------- ------------------- ------------------------------------------------------------------------ ------------ ---------------
 Yes                  Evers Eberhart      [3] Renewal Enrolment to 008C WWW (Internet for beginners) (48.00 €)     48,00        *SLS 22/2015*
 Yes                  Jacobs Jacqueline   [3] Renewal Enrolment to 007C WWW (Internet for beginners) (48.00 €)     48,00        *SLS 23/2015*
 Yes                  Emonts-Gast Erna    [6] Renewal Enrolment to 022C MED (Finding your inner peace) (64.00 €)   64,00        *SLS 24/2015*
 Yes                  Radermacher Guido   [3] Renewal Enrolment to 011C FG (Functional gymnastics) (50.00 €)       50,00        *SLS 25/2015*
 Yes                  di Rupo Didier      [3] Renewal Enrolment to 008C WWW (Internet for beginners) (48.00 €)     48,00        *SLS 26/2015*
 **Total (5 rows)**                                                                                                **258,00**
==================== =================== ======================================================================== ============ ===============
<BLANKLINE>



Item descriptions
=================

The template :xfile:`courses/Enrolment/item_description.html` defines
the text to use as the description of an invoice item
when generating invoices.

Here is an overview of the different cases of item descriptions.

>>> qs = InvoiceItem.objects.filter(invoiceable_id__isnull=False)
>>> qs.count()
174
>>> cases = set()
>>> for i in qs:
...     e = i.invoiceable
...     k = (e.places == 1, e.start_date is None, 
...         e.course.start_time is None,
...         e.start_date is None,
...         e.option_id is None,
...         e.fee.tariff is None or e.fee.tariff.number_of_events is None,
...         e.course.every_unit)
...     if k in cases: continue
...     print("=== {} ===".format(k))
...     fmt(i)
...     cases.add(k)
...  #doctest: +REPORT_UDIFF
=== (True, True, True, True, True, True, <Recurrencies.once:O>) ===
--- Invoice #1 for enrolment #1 (001 Greece 2014 / Hans Altenberg (MEL)):
Title: Enrolment to 001 Greece 2014
Start date: 
Description:
Date: 14/08/2014-20/08/2014.
Fee: Journeys.
=== (True, True, False, True, True, True, <Recurrencies.weekly:W>) ===
--- Invoice #2 for enrolment #4 (004 comp (First Steps) / Laurent Bastiaensen (ME)):
Title: Enrolment to 004 comp (First Steps)
Start date: 
Description:
Time: Every Wednesday 17:30-19:00.
Fee: 20€.
Scheduled dates:
19/03/2014, 26/03/2014, 02/04/2014, 09/04/2014, 16/04/2014, 23/04/2014, 30/04/2014, 07/05/2014, 
=== (True, False, False, False, True, False, <Recurrencies.weekly:W>) ===
--- Invoice #3 for enrolment #5 (007C WWW (Internet for beginners) / Ulrike Charlier (ME)):
Title: [1] Enrolment to 007C WWW (Internet for beginners)
Start date: 08/11/2014
Missed events: 29/10/2014, 05/11/2014
Description:
Time: Every Wednesday 17:30-19:00.
Fee: 48€/8 hours.
Your start date: 08/11/2014.
=== (True, True, False, True, True, False, <Recurrencies.weekly:W>) ===
--- Invoice #3 for enrolment #6 (009C BT (Belly dancing) / Ulrike Charlier (ME)):
Title: [1] Enrolment to 009C BT (Belly dancing)
Start date: 
Description:
Time: Every Wednesday 19:00-20:00.
Fee: 64€/12 hours.
=== (True, False, False, False, True, True, <Recurrencies.weekly:W>) ===
--- Invoice #5 for enrolment #12 (018 SV (Self-defence) / Dorothée Demeulenaere (ME)):
Title: Enrolment to 018 SV (Self-defence)
Start date: 18/03/2015
Missed events: 06/03/2015, 13/03/2015
Description:
Time: Every Friday 18:00-19:00.
Fee: 20€.
Scheduled dates:
20/03/2015, 27/03/2015, 10/04/2015, 17/04/2015, 
=== (False, True, True, True, True, True, <Recurrencies.once:O>) ===
--- Invoice #11 for enrolment #31 (001 Greece 2014 / Jacqueline Jacobs (ME)):
Title: Enrolment to 001 Greece 2014
Start date: 
Description:
Places used: 2.
Date: 14/08/2014-20/08/2014.
Fee: Journeys.
=== (True, False, True, False, True, True, <Recurrencies.once:O>) ===
--- Invoice #18 for enrolment #61 (001 Greece 2014 / Christian Radermacher (MEL)):
Title: Enrolment to 001 Greece 2014
Start date: 29/08/2014
Missed events: 14/08/2014
Description:
Date: 14/08/2014-20/08/2014.
Fee: Journeys.


Invoice recipient
=================

>>> show_fields(rt.models.contacts.Partners, 'salesrule__invoice_recipient', True)
============================== =================== =================================================================
 Internal name                  Verbose name        Help text
------------------------------ ------------------- -----------------------------------------------------------------
 salesrule__invoice_recipient   Invoicing address   The partner who should get the invoices caused by this partner.
============================== =================== =================================================================

List of pupils who have an invoice_recipient:

>>> for p in rt.models.contacts.Partner.objects.filter(salesrule__invoice_recipient__isnull=False):
...     print("{} --> {}".format(p, p.salesrule.invoice_recipient))
Faymonville Luc --> Engels Edgar
Radermacher Alfons --> Emonts-Gast Erna
Martelaer Mark --> Dupont Jean

We take one of the recipients and verify that
PartnersByInvoiceRecipient shows as expected:

>>> recipient = rt.models.courses.Pupil.objects.get(last_name="Engels")
>>> rt.show(rt.models.invoicing.PartnersByInvoiceRecipient, recipient)
================= ===== ===========================
 Partner           ID    Address
----------------- ----- ---------------------------
 Faymonville Luc   130   Brabantstraße, 4700 Eupen
================= ===== ===========================
<BLANKLINE>

Here are the enrolments of the pupil:

>>> pupil = rt.models.courses.Pupil.objects.get(last_name="Faymonville")
>>> pupil
Pupil #130 ('Luc Faymonville (MEL)')
>>> rt.show('courses.EnrolmentsByPupil', pupil, column_names="id request_date course amount workflow_buttons")
==== ================= ===================================== ============ ===============
 ID   Date of request   Activity                              Amount       Workflow
---- ----------------- ------------------------------------- ------------ ---------------
 27   08/11/2013        025C Yoga                             50,00        **Confirmed**
 28   08/11/2013        025C Yoga                             50,00        **Confirmed**
 26   23/11/2013        024C Yoga                             50,00        **Confirmed**
 25   01/02/2015        023C MED (Finding your inner peace)   64,00        **Confirmed**
 29   21/06/2015        014 Rücken (Swimming)                 80,00        **Confirmed**
                                                              **294,00**
==== ================= ===================================== ============ ===============
<BLANKLINE>

We pick one of them and look at the issued invoices:

>>> e = rt.models.courses.Enrolment.objects.get(id=28)
>>> rt.show('invoicing.InvoicingsByGenerator', e)
===================== ===================================== ========== ============== ============ ==================
 Sales invoice         Heading                               Quantity   Voucher date   State        Number of events
--------------------- ------------------------------------- ---------- -------------- ------------ ------------------
 SLS 9/2014            [1] Enrolment to 025C Yoga            1          31/12/2013     Registered   5
 SLS 29/2014           [2] Renewal Enrolment to 025C Yoga    1          31/01/2014     Registered   5
 SLS 34/2014           [3] Renewal Enrolment to 025C Yoga    1          31/03/2014     Registered   5
 SLS 39/2014           [4] Renewal Enrolment to 025C Yoga    1          31/05/2014     Registered   5
 SLS 42/2014           [5] Renewal Enrolment to 025C Yoga    1          30/06/2014     Registered   5
 SLS 46/2014           [6] Renewal Enrolment to 025C Yoga    1          31/07/2014     Registered   5
 SLS 52/2014           [7] Renewal Enrolment to 025C Yoga    1          30/09/2014     Registered   5
 SLS 60/2014           [8] Renewal Enrolment to 025C Yoga    1          31/10/2014     Registered   5
 SLS 65/2014           [9] Renewal Enrolment to 025C Yoga    1          30/11/2014     Registered   5
 SLS 14/2015           [10] Renewal Enrolment to 025C Yoga   1          31/01/2015     Registered   5
 **Total (10 rows)**                                         **10**                                 **50**
===================== ===================================== ========== ============== ============ ==================
<BLANKLINE>

These invoices are not issued to the pupil but to the recipient:

>>> rt.show('sales.InvoicesByPartner', pupil)
No data to display

>>> rt.show('sales.InvoicesByPartner', recipient)
===================== =========== ========= ================= ================
 Entry date            Reference   No.       Total incl. VAT   Workflow
--------------------- ----------- --------- ----------------- ----------------
 01/02/2015            SLS         14        50,00             **Registered**
 01/01/2015            SLS         3         48,00             **Registered**
 01/12/2014            SLS         65        50,00             **Registered**
 01/11/2014            SLS         60        50,00             **Registered**
 01/10/2014            SLS         52        50,00             **Registered**
 01/08/2014            SLS         46        50,00             **Registered**
 01/07/2014            SLS         42        50,00             **Registered**
 01/06/2014            SLS         39        50,00             **Registered**
 01/04/2014            SLS         34        50,00             **Registered**
 01/02/2014            SLS         29        50,00             **Registered**
 01/01/2014            SLS         9         426,00            **Registered**
 **Total (11 rows)**               **393**   **924,00**
===================== =========== ========= ================= ================
<BLANKLINE>

