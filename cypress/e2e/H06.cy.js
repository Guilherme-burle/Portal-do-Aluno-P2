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
  beforeEach(() => {
    // Limpa o banco antes de cada teste
    cy.deleteAllUsers();

    // Faz o login
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('testeuser@cesar.school'); // ajuste conforme seu app
    cy.get('[type="password"]').type('test123'); // ajuste conforme seu app
    cy.get('.btn-login').click();

    // Agora você deve estar logado e redirecionado para alguma tela inicial
  });

  it('Deve adicionar desempenho de um aluno (cenário favorável 1)', () => {
    // Visita a tela de adicionar desempenho
    cy.visit('http://127.0.0.1:8000/addDF');

    // Seleciona o alun
    cy.get('select').select('João da Silva')

    // Preenche o número de faltas
    cy.get('input[name="faltas"]').type('4');

    // Seleciona desempenho - aqui usando o radio button "Satisfeito"
    cy.get('input[type="radio"]').eq(2).check();

    // Preenche o comentário
    cy.get('textarea').type('Bom desempenho');
    cy.get('.btn-cadastro').click();
  });
   it('Erro ao preeencher o número de faltas com letras (cenário desfavorável 1)', () => {
    // Visita a tela de adicionar desempenho
    cy.visit('http://127.0.0.1:8000/addDF');

    // Seleciona o aluno
    cy.get('select').select('João da Silva')

    // Seleciona desempenho - aqui usando o radio button "Satisfeito"
    cy.get('input[type="radio"]').eq(2).check();

    // Preenche o comentário
    cy.get('textarea').type('Bom desempenho');
    cy.get('.btn-cadastro').click();
  });
   it('Erro ao não preencher o nome do aluno (cenário desfavorável 2)', () => {
    // Visita a tela de adicionar desempenho
    cy.visit('http://127.0.0.1:8000/addDF');

    cy.get('input[name="faltas"]').type('4');

    // Seleciona desempenho - aqui usando o radio button "Satisfeito"
    cy.get('input[type="radio"]').eq(1).check();

    // Preenche o comentário
    cy.get('textarea').type('Mal desempenho');
    cy.get('.btn-cadastro').click();
  });
});



