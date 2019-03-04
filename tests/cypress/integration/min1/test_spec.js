describe('My First Test', function () {
    it('can log in', function () {
        cy.visit('/');
        cy.get('ul > :nth-child(1) > a').click().log("Sign in as robin"); // sign
        cy.get('#ext-comp-1018 > .x-btn-small > :nth-child(2) > .x-btn-mc').click().log('Submit log-in');
        cy.wait(1000);
        // cy.get('#ext-gen26').click();
        // cy.type("robin");
        cy.get('#ext-gen20').click(); //Contacts
        cy.get('#ext-gen37').click(); //People

        cy.get('.x-tbar-add').click({force: true}).log("Insert");

        cy.get('div:not(.x-body-masked) input[name="first_name"]').type("FooFoo");
        cy.get('input[name="last_name"]').type("BarBar");
        cy.get('input[name="email"]').type("FooBar@Foobar.com");
        cy.get('input[name="gender"]+img').click();

    })
});
