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

describe('Como aluno eu gostaria de acessar o calendário acadêmico', () => {
  it('Adiociona um evento no Calendário (cenário favorável 1)', () => {
    // Visita a página de login
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get(':nth-child(1) > a').click();
    cy.get(':nth-child(2) > :nth-child(1) > [style="color: rgb(0, 160, 228); font-weight: bold; font-size: 18px; text-align: left; margin-top: 5px; cursor: pointer;"]').click();
    cy.get('#nome').type('Atividade de PIF');
    cy.get('[type="time"]').type('00:40');
    cy.get('.btn-cadastro').click();
    });
  it('Tenta adicionar um evento e não preenche o título  (cenário desfavorável 1)', () => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get(':nth-child(1) > a').click();
    cy.get(':nth-child(2) > :nth-child(1) > [style="color: rgb(0, 160, 228); font-weight: bold; font-size: 18px; text-align: left; margin-top: 5px; cursor: pointer;"]').click();
    cy.get('[type="time"]').type('00:40');
    cy.get('.btn-cadastro').click();
  });
  it('Tenta adicionar um evento e não preenche o horário corretamente (cenário desfavorável 2)', () => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get(':nth-child(1) > a').click();
    cy.get(':nth-child(2) > :nth-child(1) > [style="color: rgb(0, 160, 228); font-weight: bold; font-size: 18px; text-align: left; margin-top: 5px; cursor: pointer;"]').click();
    cy.get('#nome').type('Atividade de PIF');
    cy.get('.btn-cadastro').click();
  });
});
