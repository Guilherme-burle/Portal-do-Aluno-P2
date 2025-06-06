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

describe('Administrador se Cadastrando', () => {
  it('administrador fazendo o login', () => {
    // Visita a página de login
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('a').click();
    cy.get('[type="text"]').type("testeuser");
    cy.get('[type="email"]').type('testeuser@cesar.school')
    cy.get('[name="senha"]').type('test123')
    cy.get('#is_admin').click()
    cy.get('.btn-cadastrar').click()
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('testeuser@cesar.school')
    cy.get('[type="password"]').type('test123')
    cy.get('.btn-login').click()


  });

  describe('Cadastro de Aluno (cenário favorável 1)', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('testeuser@cesar.school')
    cy.get('[type="password"]').type('test123')
    cy.get('.btn-login').click()
  });

  it('deve permitir cadastrar aluno com dados válidos', () => {
    cy.get("[onclick=\"location.href='/add/'\"]").click();
    cy.visit('http://127.0.0.1:8000/add/')
    cy.get('[name="usuario_id"]').type('testeuser@cesar.school')
    cy.get('[name="nome"]').type('João da Silva');
    cy.get('[type="date"]').invoke('val', '2005-06-04').trigger('change');
    cy.get('[name="escolaridade"]').select('Ensino médio incompleto');
    cy.get('[name="turno"]').type('Manhã');
    cy.get('[name="escola"]').type('Colegio');
    cy.get('[name="endereco"]').type('ibura');
    cy.get('[name="bairro"]').type('Várzea');
    cy.get('[type="tel"]').type('81 987654321');
    cy.get('[name="curso"]').select('Programação');
    cy.get('.btn-cadastro').click();

    // Valida a presença de mensagem de sucesso ou redirecionamento

  });
  describe('Cadastro de Aluno com falta de informação (cenário desfavorável 1)', () => {
  beforeEach(() => {
    // Login como administrador
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('testeuser@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('[type="submit"]').click();
  });

  it('não deve permitir cadastro do aluno', () => {
    // Clica no botão para ir para a página de cadastro de alunos
    cy.get("[onclick=\"location.href='/add/'\"]").click();
    cy.visit('http://127.0.0.1:8000/add/');

    // Preenche o formulário com dados válidos, exceto a idade com letras
    cy.get('[name="nome"]').type('João da Silva');
    cy.get('[type="date"]').invoke('val', '2025-06-04').trigger('change'); 
    cy.get('[name="escolaridade"]').select('Ensino médio incompleto');
    cy.get('[name="turno"]').select('Manhã');
    cy.get('[name="escola"]').type('Colegio');
    cy.get('[name="endereco"]').type('ibura');
    cy.get('[name="bairro"]').select('Várzea');// falta de informação

    // Envia o formulário
    cy.get('.btn-cadastro').click();

  });
});

 describe('Cadastro de Aluno com data de nascimento mal inserida (cenário desfavorável 2)', () => {
  beforeEach(() => {
    // Login como administrador
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('[type="email"]').type('testeuser@cesar.school');
    cy.get('[type="password"]').type('test123');
    cy.get('[type="submit"]').click();
  });

  it('não deve permitir cadastro do aluno', () => {
    // Clica no botão para ir para a página de cadastro de alunos
    cy.get("[onclick=\"location.href='/add/'\"]").click();
    cy.visit('http://127.0.0.1:8000/add/');

    // Preenche o formulário com dados válidos, exceto a idade com letras
    cy.get('[name="nome"]').type('João da Silva');
    cy.get('[type="date"]').invoke('val', '2025-06-  ').trigger('change'); 
    cy.get('[name="escolaridade"]').select('Ensino médio incompleto');
    cy.get('[name="turno"]').select('Manhã');
    cy.get('[name="escola"]').type('Colegio');
    cy.get('[name="endereco"]').type('ibura');
    cy.get('[name="bairro"]').select('Várzea');
    cy.get('[type="tel"]').type('81 987654321');
    cy.get('[name="curso"]').select('Programação');// falta de informação

    // Envia o formulário
    cy.get('.btn-cadastro').click();

  });
});
});
});