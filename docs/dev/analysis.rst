==============
About analysis
==============


The "technical specification" of an application is a document which
describes what an application is expected to do.

Such a description is an important document when doing software
development in a team.  Writing this document is the job of the
**analyst**.  The analyst communicates directly with the customer and
formulates their needs. The salesman uses this document when
discussing with the customer about the price.  The developer uses this
document in order to understand what he is being asked to implement.
The salesman, the analyst and the developer can be a single person in
a small team. But even then it is a good habit to write a technical
specification.

For a Lino application, the technical specification should include the
following elements.

- A textual description of your **database structure**, i.e. the list
  of **models** (tables) to be used.  Each model has a list of
  **fields** (properties).  Each field should have a meaningful name.
  
  It is good to agree with your customer on the meaning of certain
  words.
  makes certain things clear between the customer and the
  developer.

- Another thing to discuss with your customer during analysis is the
  **menu structure** and the content of the **main page** (dashboard).

- the **layout** of detail forms

- a description of the different **user types**



It is important to get some fictive data which corresponds more or
less to the reality of your customer.

As soon as you have written such a fixture, you can start writing
"specs", i.e. :doc:`tested documents <doctests>` which use that demo
data.

Specs are both a **visualisation of your demo data** (which you might
show to your customer) and a **part of the test suite** of your
application.


