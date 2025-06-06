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
 // cypress/e2e/adicionar_desempenho.cy.js

// cypress/e2e/adicionar_desempenho.cy.js

describe('Adicionar desempenho', () => {
  it('Exibi o desempenho do aluno (cenário favorável 1)', () => {
     cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('teste_user@cesar.school'); // ajuste conforme seu app
    cy.get('[type="password"]').type('test123'); // ajuste conforme seu app
    cy.get('.btn-login').click();
    // Visita a tela de adicionar desempenho
    cy.get('ul > :nth-child(3) > a').click();


  });
   it('Administrador edita o desempenho do aluno (cenário favorável 2)', () => {

    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('testeuser@cesar.school'); // ajuste conforme seu app
    cy.get('[type="password"]').type('test123'); // ajuste conforme seu app
    cy.get('.btn-login').click();
    cy.get("[onclick=\"location.href='/listDF/'\"]").click();
    cy.get('[href="/editDF/8/"]').click();
    cy.get('[type="number"]').clear()
    cy.get('[type="number"]').type('16');
    cy.get(':nth-child(1) > input').click();
    cy.get('textarea').clear();
    cy.get('textarea').type('Pessimo desempenho')
    cy.get('.btn-cadastro').click();


    // Agora você deve estar logado e redirecionado para alguma tela inicial
  });
  it('Exibe mensagem quando não há dados cadastrados (cenário desfavorável 1)', () => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('testeuser@cesar.school');  // Use um aluno SEM dados cadastrados
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
    cy.get("[onclick=\"location.href='/listDF/'\"]").click();
    cy.get('[href="/deleteDF/8/"]').click();
});
});