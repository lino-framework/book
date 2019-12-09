describe('Connecting ...', function () {
    beforeEach(() => {

        // Logging in

        cy.visit('/');
        cy.get('ul > :nth-child(1) > a').click().log("Sign in as robin"); // sign
        cy.get('.l-ActionFormPanel .l-ok').click().log('Submit log-in');
        cy.wait(1000);
        // cy.get('#ext-gen26').click();
        // cy.type("robin");

    });
    it('Delete a person using the hotkey DEL', function () {
        cy.server();
        cy.route("GET", '/api/*/*').as('getData');


        cy.get('.l-mainmenu button:first').click(); //Contacts
        cy.get("a[class='x-menu-item']:first").click(); //People

        // cy.get('.x-tbar-add').click({force: true}).log("Insert").wait(20);
        //
        // cy.get('.l-InsertFormPanel input[name="first_name"]').type("FooFoo");
        // cy.get('.l-InsertFormPanel input[name="last_name"]').type("BarBar");
        // cy.get('.l-InsertFormPanel input[name="email"]').type("FooBar@Foobar.com");
        // cy.get('.l-InsertFormPanel input[name="gender"]+img').click();// open
        // cy.get(".x-combo-list-item:nth-child(2)").click(); // male
        // cy.get(".l-InsertFormPanel button").click().wait(1000); //submit

        // const text_initial_record_count = cy.get("div[class='xtb-text']").text();
        // const initial_record_count = parseInt(text_initial_record_count.split(" ")[text_initial_record_count.length - 1]);
        cy.wait(100).get("div[class='x-grid3-row    x-grid3-row-first']:first").click();
        cy.wait(100).get("div[class='x-grid3-row    x-grid3-row-first']:first").get("td[tabindex='0']:first").type("{del}").log("Selecting a record ...");
        // cy.wait(100).get("x-grid3-scroller")
        cy.get(".l-confirmation button:nth(1)", ).click({force:true}); // nth(0) created a bad callback which erros, use 1 for yes 3 for no*

        // const text_new_record_count = cy.get("div[class='xtb-text']").text();
        // const new_record_count = parseInt(text_new_record_count.split(" ")[text_new_record_count.length - 1]);
        // expect(initial_record_count - new_record_count ).to.include(1);


    })
});