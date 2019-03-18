describe('My First Test', function () {
    beforeEach(() => {

        // Logging in

        cy.visit('/');
        cy.get('ul > :nth-child(1) > a').click().log("Sign in as robin"); // sign
        cy.get('.l-ActionFormPanel .l-ok').click().log('Submit log-in');
        cy.wait(1000);
        // cy.get('#ext-gen26').click();
        // cy.type("robin");

    });
    it('Can Add a new person then delete them', function () {
        cy.server();
        cy.route("GET", '/api/*/*').as('getData');


        cy.get('.l-mainmenu button:first').click(); //Contacts
        cy.get('.x-menu[style*="visibility: visible;"] .x-menu-item:first').click(); //People

        cy.get('.x-tbar-add').click({force: true}).log("Insert").wait(20);

        cy.get('.l-InsertFormPanel input[name="first_name"]').type("FooFoo");
        cy.get('.l-InsertFormPanel input[name="last_name"]').type("BarBar");
        cy.get('.l-InsertFormPanel input[name="email"]').type("FooBar@Foobar.com");
        cy.get('.l-InsertFormPanel input[name="gender"]+img').click();// open
        cy.get(".x-combo-list-item:nth-child(2)").click(); // male
        cy.get(".l-InsertFormPanel button").click().wait(1000); //submit

        cy.wait(100).get('.l-DetailFormPanel .x-tbar-delete').click({force: true}).log("delete");
        cy.get(".l-confirmation button:nth(1)", ).click({force:true}); // nth(0) created a bad callback which erros, use 1 for yes 3 for no


    })
});
