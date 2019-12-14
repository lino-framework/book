.. _dev.cypress:
    
=======
Cypress
=======

`Cypress <https://www.cypress.io/>`_ is a JavaScript End to End Testing Framework. 
We use this tool to test web interface interraction with users usage.
To start using it, you need to intall cypress.

If nodejs and npm are not installed yet, we need to install them::
  
    $ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

If you need to install another version, for example 13.x, just change setup_12.x with setup_13.x::

    $ sudo apt install nodejs

The nodejs package contains both the node and npm binaries.
Cypress be installed locally on the book project.

    $ go book
    $ npm init -y
    $ npm install cypress

Once installed we run test of the min1 project which include a include a cypress tests::

    $ cd book_lino/projects/min1
    $ inv test


