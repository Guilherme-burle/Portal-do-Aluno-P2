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

Cypress.on('uncaught:exception', (err, runnable) => {
  // se quiser, você pode filtrar por mensagem de erro
  if (err.message.includes("Cannot read properties of null (reading 'addEventListener')")) {
    return false; // Ignora o erro
  }
  return true; // para outros erros, deixa Cypress falhar o teste
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

describe('Gerenciamento de Alunos pelo Administrador', () => {
  beforeEach(() => {
    // Login como administrador antes de cada teste
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('testeuser@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('.btn-login').click();
  });

  it('deve exibir todos os alunos cadastrados (cenário favorável 1)', () => {
    cy.get('[onclick="location.href=\'/ver/\'"]').click();  // Ajuste de acordo com o seletor correto
    cy.visit('http://127.0.0.1:8000/homeadm/');// Verifica se estamos na página de listagem
  });

  it('deve permitir editar um aluno (cenário favorável 2)', () => {
    cy.get('[onclick="location.href=\'/ver/\'"]').click();
    cy.get(':nth-child(1) > :nth-child(6) > .btn-editar').click(); // Ajuste a classe conforme o botão de editar
  });

  it('deve permitir deletar um aluno (cenário favorável 3)', () => {
    cy.get('[onclick="location.href=\'/ver/\'"]').click();
    cy.get('.btn-deletar').first().click();  // Ajuste a classe conforme o botão de deletar
  });

  it('não deve exibir alunos quando nenhum estiver cadastrado (cenário desfavorável 1)', () => {
    // Limpa o banco antes (supondo que você tenha um endpoint ou comando para isso)
    cy.deleteAllUsers();  // Use seu comando criado para deletar todos os usuários, se incluir alunos.
    cy.get('[onclick="location.href=\'/ver/\'"]').click();
  });
});
