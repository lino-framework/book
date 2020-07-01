describe('Connecting ...', function () {
    beforeEach(() => {

        // Logging in

        cy.visit('/');
        cy.get('ul > :nth-child(4) > a').click().log("Sign in as robin"); // sign
        cy.get('.l-ActionFormPanel .l-ok').click().log('Submit log-in');
        cy.wait(1000);
        // cy.get('#ext-gen26').click();
        // cy.type("robin");

    });
    it('Create First client', function () {
        cy.server();
        cy.route('/api/**').as('getData');

        cy.get('.l-mainmenu button:first').click(); //Contacts
        cy.get("a[class='x-menu-item']").eq(2).click().wait("@getData"); //People
        cy.get("button[class=' x-btn-text x-tbar-add']").click({force: true}).log("Insert").wait("@getData");
        cy.get('.l-InsertFormPanel input[name="first_name"]').type("Alfred", {delay:300}).wait(20);
        cy.get('.l-InsertFormPanel input[name="last_name"]').type("BarBar", {delay:300}).wait(20);
        cy.get('.l-InsertFormPanel input[name="email"]').type("FooBar@Foobar.com", {delay:300}).wait(20);
        cy.get('.l-InsertFormPanel input[name="gender"]+img').click();
        cy.get(".x-combo-list-item:nth-child(2)").click();  //male
        cy.get(".l-InsertFormPanel button").click().wait("@getData"); //submit
        cy.get(".l-DetailFormPanel").log("Confirm creation of person by geting detail window")
        cy.get(".l-DetailFormPanel .x-panel.x-box-item").contains("A")
        //cy.get('div:contains("Yes")').click().wait(1000); //submit
        // if (cy.get('body').find(".l-confirmation").length) {
        //     cy.get(".l-confirmation button:nth(1)").click({force:true});
        // }
    });
    it('Create second client with same name', function () {
        cy.server();
        cy.get('.l-mainmenu button:first').click(); //Contacts
        cy.get("a[class='x-menu-item']").eq(2).click().wait(20); //People
        cy.get("button[class=' x-btn-text x-tbar-add']").click({force: true}).log("Insert").wait(100);
        cy.get('.l-InsertFormPanel input[name="first_name"]').type("Alfred", {delay:300}).wait(20);
        cy.get('.l-InsertFormPanel input[name="last_name"]').type("BarBar", {delay:300}).wait(20);
        cy.get('.l-InsertFormPanel input[name="email"]').type("FooBar@Foobar.com", {delay:300}).wait(20);
        cy.get('.l-InsertFormPanel input[name="gender"]+img').click();
        cy.get(".x-combo-list-item:nth-child(2)").click();  //male
        cy.get(".l-InsertFormPanel button").click().wait(1000); //submit
        cy.get(".l-confirmation button:nth(1)").click();


    });


    it('Delete a person using the hotkey DEL', function () {
        cy.server();
        // cy.route("GET", '/api/*/*').as('getData');
        cy.get('.l-mainmenu button:first').click(); //Contacts
        cy.get("a[class='x-menu-item']:first").click(); //People

        // cy.get('.x-tbar-add').click({force: true}).log("Insert").wait(20);
        //
        // cy.get('.l-InsertFormPanel input[name="first_name"]').type("A");
        // cy.get('.l-InsertFormPanel input[name="last_name"]').type("BarBar");
        // cy.get('.l-InsertFormPanel input[name="email"]').type("FooBar@Foobar.com");
        // cy.get('.l-InsertFormPanel input[name="gender"]+img').click();// open
        // cy.get(".x-combo-list-item:nth-child(2)").click(); // male
        // cy.get(".l-InsertFormPanel button").click().wait(1000); //submit
        cy.get(".x-toolbar-cell input[type='text']:first").type("BarBar",{delay:300}).wait(1000); //submit

        // const text_initial_record_count = cy.get("div[class='xtb-text']").text();
        // const initial_record_count = parseInt(text_initial_record_count.split(" ")[text_initial_record_count.length - 1]);
        cy.wait(100).get("div[class='x-grid3-row    x-grid3-row-first']:first").click();
        cy.wait(100).get("div[class='x-grid3-row    x-grid3-row-first']:first").get("td[tabindex='0']:first").type("{del}").log("Selecting a record ...");
        // cy.wait(100).get("x-grid3-scroller")
        cy.get(".l-confirmation button:nth(1)", ).click({force:true}).wait(3000); // nth(0) created a bad callback which erros, use 1 for yes 3 for no*

        // delete second row
        cy.wait(100).get("div[class='x-grid3-row    x-grid3-row-first']:first").click();
        cy.wait(100).get("div[class='x-grid3-row    x-grid3-row-first']:first").get("td[tabindex='0']:first").type("{del}").log("Selecting a record ...");
        // cy.wait(100).get("x-grid3-scroller")
        cy.get(".l-confirmation button:nth(1)", ).click({force:true}); // nth(0) created a bad callback which erros, use 1 for yes 3 for no*
        // const text_new_record_count = cy.get("div[class='xtb-text']").text();
        // const new_record_count = parseInt(text_new_record_count.split(" ")[text_new_record_count.length - 1]);
        // expect(initial_record_count - new_record_count ).to.include(1);


    })
});
