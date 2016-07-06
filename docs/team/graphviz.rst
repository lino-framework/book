=======================
Diagrams using graphviz
=======================


Using the :rst:dir:`.. graphviz::` directive
============================================

.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }
   
   

Using the :rst:dir:`.. inheritance-diagram::` directive
=======================================================

::

  .. inheritance-diagram:: 
    lino_xl.lib.contacts.models.Contact  dsbe.models.Contact
    lino_xl.lib.contacts.models.Person   dsbe.models.Person
    lino_xl.lib.contacts.models.Company  dsbe.models.Company



