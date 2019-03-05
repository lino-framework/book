describe('My First Test', function () {
    beforeEach(() => {

        // Logging in

        cy.visit('/');
        cy.get('ul > :nth-child(1) > a').click().log("Sign in as robin"); // sign
        cy.get('#ext-comp-1018 > .x-btn-small > :nth-child(2) > .x-btn-mc').click().log('Submit log-in');
        cy.wait(500);
        // cy.get('#ext-gen26').click();
        // cy.type("robin");

    });
    it('Can Add a new person', function () {
        cy.get('#ext-gen20').click(); //Contacts
        cy.get('#ext-gen37').click(); //People

        cy.get('.x-tbar-add').click({force: true}).log("Insert");

        cy.get('.l-InsertFormPanel input[name="first_name"]').type("FooFoo");
        cy.get('.l-InsertFormPanel input[name="last_name"]').type("BarBar");
        cy.get('.l-InsertFormPanel input[name="email"]').type("FooBar@Foobar.com");
        cy.get('.l-InsertFormPanel input[name="gender"]+img').click();// open
        cy.get(".x-combo-list-item:nth-child(2)").click(); // male
        cy.get(".l-InsertFormPanel button").click() //submit
    })
});
