# 📘 Portal do Aluno - P2

Um portal educacional desenvolvido para atender às necessidades do cliente, o Instituto Solidare, como parte da disciplina Projetos 2 na CESAR School.  
Projeto realizado sob a supervisão da professora Ana Carolina Candido de Melo.

----

## 👥 Integrantes:

1. [Guilherme Burle Medeiros](https://github.com/Guilherme-burle)  
2. [Pedro Valença Ferraz](https://github.com/PedroFerraz87)  
3. [Rafael de Lima Cavalcanti Loyo Fernandes](https://github.com/rafaelcf29)  
4. [Gabriel França de Albuquerque Pernambuco](https://github.com/gabrielfranca10)  
5. [Caio Cabral da Mata Buonora](https://github.com/caiobuonora)  
6. [Victor de Matos Vilela](https://github.com/VI170105)  
7. [Fernando Soares da Silva](https://github.com/Nando101210)  
8. [Eduardo Henrique de Sá Nogueira Lemos](https://github.com/EduardoHenrique15)  
9. [Luca Ribeiro Albuquerque](https://github.com/LucaAlbuquerque)  
10. Helena Maia Jordão  
11. Raul Pedro Soares de Lima  
12. Maria Eduarda Leal  

---

## Histórias de Usuário:

<details>
<summary><strong>História 1:</strong> Como administrador da plataforma, eu gostaria de adicionar alunos ao sistema.</summary>

- **Cenário favorável 1:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Cadastrar alunos”  
  Então o sistema indica que é preciso preencher todas as informações, feito isso, salva tudo que foi pedido no banco de dados.

- **Cenário desfavorável 1:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Cadastrar alunos”  
  Então o sistema não responde adequadamente à tentativa de cadastro, pois no lugar de números foram inseridas letras na idade.

- **Cenário desfavorável 2:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Cadastrar alunos”  
  Então o sistema não responde adequadamente à tentativa de cadastro, pois um número foi inserido no lugar do nome.

</details>

<details>
<summary><strong>História 2:</strong> Como administrador da plataforma, eu gostaria de Gerenciar alunos, ou seja: visualizar, atualizar e excluir alunos do sistema.</summary>

- **Cenário favorável 1:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” e seleciona “Visualizar” <br>
  Então o sistema exibe todos os alunos cadastrados no banco de dados.

- **Cenário favorável 2:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” e seleciona “Editar” <br>
  Então os dados do aluno escolhido são exibidos para edição.

- **Cenário favorável 3:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” e seleciona “Excluir” <br>
  Então os alunos são exibidos e há a opção de deletá-los do sistema.

- **Cenário desfavorável 1:**  
  Dado que o administrador está logado  
  Quando acessa a aba “Gerenciar alunos”  
  Então nenhum aluno aparece pois ainda não há alunos cadastrados.

</details>

<details>
<summary><strong>História 3:</strong> Como aluno eu gostaria de avaliar a instituição com sugestões de melhorias.</summary>

- **Cenário favorável 1:**  
  Dado que o aluno está matriculado e logado  
  Quando acessa a aba “Avalie a Solidare”  
  Então perguntas são exibidas para resposta.

- **Cenário favorável 2:**  
  Dado que o aluno está matriculado e logado  
  Quando acessa a aba “Avalie a Solidare”  
  Então um formulário é exibido para registrar sugestões e opiniões.

- **Cenário desfavorável 1:**  
  Dado que o aluno está logado  
  Quando acessa a aba “Avalie a Solidare”  
  Então uma falha no carregamento impede o acesso à aba.

</details>

<details>
<summary><strong>História 4:</strong> Como aluno eu gostaria de acessar o calendário acadêmico da instituição para saber precisamente as datas do calendário.</summary>

- **Cenário favorável 1:**  
  Dado que o aluno está matriculado e logado  
  Quando acessa a aba “Calendário”  
  Então são exibidas as informações acadêmicas, como: datas de provas, entregas, feriados e comemorações.

- **Cenário desfavorável 1:**  
  Dado que o aluno está logado  
  Quando acessa a aba “Calendário”  
  Então as informações não aparecem pois a letra dos eventos está da mesma cor do caléndario.

- **Cenário desfavorável 2:**  
  Dado que o aluno está logado  
  Quando acessa a aba “Calendário”  
  Então as datas aparecem em branco, ou seja, sem eventos, pois não foram cadastradas.

</details>

<details>
<summary><strong>História 5:</strong> Como aluno eu gostaria de acompanhar meu desempenho acadêmico e frequência.</summary>

> Obs: Avaliação será feita com "carinhas" (feliz/triste) e comentário do avaliador.

- **Cenário favorável 1:**  
  Dado que o aluno está matriculado e logado  
  Quando acessa a aba “Desempenho e Frequência”  
  Então são exibidas faltas e desempenho.

- **Cenário favorável 2:**  
  Dado que o aluno está logado  
  Quando acessa a aba “Desempenho e Frequência”  
  Então são exibidas “carinhas” e comentários do avaliador.

- **Cenário desfavorável 1:**  
  Dado que o aluno está logado  
  Quando acessa a aba “Desempenho e Frequência”  
  Então os campos aparecem em branco pois não foram preenchidos ainda.

</details>

### OBS:
  As histórias 1 e 2 foram as implementadas para o Status Report 1

---

## Relato Pair Programming:
  Trabalhamos em duplas e utilizamos o recurso de compartilhamento de tela durante as reuniões para atender a todos os requisitos do projeto. Essa abordagem permitiu uma melhor gestão do tempo, garantindo que as entregas fossem realizadas de maneira eficiente e dentro dos prazos estabelecidos. 

  **Divisao de Tarefas:** Durante cada reunião, organizávamos a divisão de tarefas formando duplas e definindo as responsabilidades de cada uma, o que ajudava a agilizar o andamento das entregas. As decisões eram registradas em um grupo no WhatsApp, garantindo que todos estivessem cientes das atividades e prazos, evitando atrasos. Rafael e Caio se reuniram no Google Meet para fazer os códigos de front-end em HTML e CSS, e Pedro e Luca se reuniram para criar o banco de dados e funções do projeto, por exemplo.

  **Metodologia de Trabalho:** Realizávamos nossas reuniões, tanto em grupo quanto em duplas, por meio do Google Meet, o que facilitava a participação ativa de todos os integrantes. O compartilhamento de tela foi essencial para promover a colaboração de todos durante a execução das tarefas, permitindo que todas as atividades fossem desenvolvidas de forma conjunta e com o conhecimento coletivo do grupo.

---

## Issue / Bugtracker:
![image](https://github.com/user-attachments/assets/a20ce089-9de6-47ab-a92e-c4399ea83196)


---
## Screencasts
- [Sreencast Figma Lo-Fi](https://youtu.be/hD8LePoT_Wk)
- [Screencast site portal do aluno](https://youtu.be/MeUWsWJPRtE?feature=shared)

---

## Links Úteis

- [Jira](https://projeto2grupo10.atlassian.net/jira/software/projects/KAN/boards/1/backlog?assignee=712020%3A5102e8eb-4036-4150-8d35-bdcf805d24b4%2Cunassigned&atlOrigin=eyJpIjoiNTRhZjVmMDFjZjEwNDhkMmI5NGJkYzUxNjRmZjI5MzUiLCJwIjoiaiJ9)  
- [Docs](https://docs.google.com/document/d/1Kb8RnBP_5Gz-eml2weoGkFe5UCOAMaLPehDUtYEnm3E/edit?tab=t.0)
- [Site](https://sites.google.com/d/1QneHjgrhPjpQ_i9iDOVrf8Ivn7McXcIN/p/1fAGUYkQG2JxVmydQqaz1o78MrP8PPQCt/edit)
- [Figma](https://www.figma.com/design/fahGccQiZEC5xWfqc5brNX/Untitled?m=auto&t=6C6LfIGmLXlI1Yj5-6)
- [Diagrama](https://miro.com/app/board/uXjVI-xQymA=/)
- [Slides apresentação SR1](https://www.canva.com/design/DAGlk-OyK3U/sfz8-SnF07B0pNAjbGoarA/edit)
