describe('My First Test', function() {
  it('Does Pass!', function() {
    expect(true).to.equal(true);
  })
  it('Does Fail!', function() {
    expect(true).to.equal(false);
  })
  it('Visits the Kitchen Sink', function() {
    cy.visit('/');
  })
})
