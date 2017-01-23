==============================
Structure overview cheat sheet
==============================


.. graphviz::

   digraph foo {
    lino -> atelier;
      lino_xl -> lino;
        lino_book -> lino_xl; 
      lino_noi -> lino_xl; 
      lino_cosi -> lino_xl; 
        lino_welfare -> lino_cosi;
        lino_voga -> lino_cosi;
        lino_presto -> lino_cosi;
      lino_avanti -> lino_noi;

  }   

- Atelier : :mod:`projects <atelier.projects>`, , :mod:`invlib <atelier.invlib>`, :mod:`rstgen <atelier.rstgen>`
- Lino : users, notify, comments, changes, about, ...
- XL : Extension library (contacts, countries, cal, ...) 
- Book (no PyPI package)
- Noi (tickets, projects, work, votes)
- Così:   Accounting
