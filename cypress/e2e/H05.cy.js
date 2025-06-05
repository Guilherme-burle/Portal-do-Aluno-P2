// cypress/e2e/login.cy.js
Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delect.py', { failOnNonZeroExit: false });
});

Cypress.Commands.add('login', (username, password) => {
    cy.visit('');
    cy.get('.container').within(() => {
    cy.visit('');
    cy.get('[type="text"]').type(username);
    cy.get('[type="password"]').type(password);
    cy.wait(2000);
    cy.get('[type="submit"]').click();
    });
});

Cypress.Commands.add('createUser', (username, email, password) => {
    cy.visit('cadastro');
    cy.switchToRegister();
    cy.get('.container').within(() => {
    cy.visit('cadastro');
    cy.get('[type="text"]').type(username);
    cy.get('[type="email"]').type(email);
    cy.get('[name="senha"]').type(password);
    cy.get('[name="confirmarSenha"]').type(password);
    cy.wait(2000);
    cy.get('[type="submit"]').click();
    });
});

Cypress.Commands.add('switchToRegister', () => {
    cy.get('p > a').click();
});

describe('Como aluno eu gostaria de acessar o calendário acadêmico e gerenciar', () => {
  it('Exibi os eventos do Calendário (cenário favorável 1)', () => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get(':nth-child(1) > a').click();
    cy.get('.evento-nome').click();
  });
  it('Exibi os eventos do Calendário e edita um evento (cenário favorável 2)', () => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get(':nth-child(1) > a').click();
    cy.get('.evento-nome').click();
    cy.get('#nome').type('Atividade de IHC');
    cy.get('[type="time"]').type('01:30');
    cy.get('.btn-cadastro').click();
  });
  it('Deleta um evento do Calendário (cenário favorável 3)', () => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get(':nth-child(1) > a').click();
    cy.get('form > button').click();
  });

});
