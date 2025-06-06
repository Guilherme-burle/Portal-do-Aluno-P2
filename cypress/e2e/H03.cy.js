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

describe('Como aluno eu gostaria de avaliar a instituição com sugestões de melhorias.', () => {
  it('Exibi a tela de avaliação do instituto e seleciona uma das opções (cenário favorável 1)', () => {
    // Visita a página de login
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('a').click();
    cy.get('[type="text"]').type('teste_user');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[name="senha"]').type('test123');
    cy.get('.btn-cadastrar').click();
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get('ul > :nth-child(2) > a').click();
    cy.get(':nth-child(2) > [value="sim"]').click();
    cy.get(':nth-child(3) > [value="sim"]').click();
    cy.get(':nth-child(4) > [value="sim"]').click();
  });
    it('Exibi a tela de avaliação do instituto e adiciona um comentário (cenário favorável 2)', () => {
    // Visita a página de login
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get('ul > :nth-child(2) > a').click();
    cy.get(':nth-child(5) > .p').type('Eu recomendo o instituto!')
  });
  it('Exibi a tela de avaliação do instituto e da um erro por não responder todas as informações (cenário desfavorável 1)', () => {
    // Visita a página de login
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get('ul > :nth-child(2) > a').click();
    cy.get(':nth-child(5) > .p').type('Eu recomendo o instituto!')
  });

});
