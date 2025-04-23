# 📘 Portal do Aluno - P2

Um portal educacional desenvolvido para atender às necessidades do cliente, como parte da disciplina Projetos 2 na CESAR School.  
Projeto realizado sob a supervisão da professora Ana Carolina Candido de Melo.

----

## 👥 Integrantes

1. [Guilherme Burle Medeiros](https://github.com/Guilherme-burle)  
2. [Pedro Valença Ferraz](https://github.com/PedroFerraz87)  
3. [Rafael de Lima Cavalcanti Loyo](https://github.com/rafaelcf29)  
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

## Histórias de Usuário

<details>
<summary><strong>História 1:</strong> Como administrador da plataforma, eu gostaria de adicionar alunos ao sistema.</summary>

- **Cenário favorável 1:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” e posteriormente “Cadastrar alunos”  
  Então o sistema exibe uma mensagem indicando que é preciso preencher todas as informações.

- **Cenário favorável 2:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” e posteriormente “Cadastrar alunos”  
  Então o sistema exibe campos como “Nome”, “Idade”, “Situação”, entre outros.

- **Cenário desfavorável 1:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” e posteriormente “Cadastrar alunos”  
  Então o sistema não responde adequadamente à tentativa de cadastro.

</details>

<details>
<summary><strong>História 2:</strong> Como administrador da plataforma, eu gostaria de visualizar, atualizar e excluir alunos do sistema.</summary>

- **Cenário favorável 1:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” e seleciona “Visualizar”, “Atualizar” ou “Excluir alunos”  
  Então o sistema exibe os alunos cadastrados ou permite as ações desejadas.

- **Cenário favorável 2:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Atualizar alunos”  
  Então os dados dos alunos são exibidos para edição.

- **Cenário desfavorável 1:**  
  Dado que o administrador está logado  
  Quando acessa a aba “Atualizar alunos”  
  Então nenhum aluno aparece pois ainda não há dados cadastrados.

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
  Então são exibidas datas de provas, entregas, feriados e comemorações.

- **Cenário favorável 2:**  
  Dado que o aluno está logado  
  Quando acessa a aba “Calendário”  
  Então as informações acadêmicas são mostradas corretamente.

- **Cenário desfavorável 1:**  
  Dado que o aluno está logado  
  Quando acessa a aba “Calendário”  
  Então as datas aparecem em branco pois não foram cadastradas.

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

## Issue / Bugtracker:
![image](https://github.com/user-attachments/assets/e03b057d-c2e3-4e69-a69d-b92a905d175d)

---
## Screencasts
- [Sreencast protótipo Lo-Fi]()
- [Screencast Portal do Aluno]()

## Links Úteis

- [Jira](https://projeto2grupo10.atlassian.net/jira/software/projects/KAN/boards/1/backlog?assignee=712020%3A5102e8eb-4036-4150-8d35-bdcf805d24b4%2Cunassigned&atlOrigin=eyJpIjoiNTRhZjVmMDFjZjEwNDhkMmI5NGJkYzUxNjRmZjI5MzUiLCJwIjoiaiJ9)  
- [Docs](https://docs.google.com/document/d/1Kb8RnBP_5Gz-eml2weoGkFe5UCOAMaLPehDUtYEnm3E/edit?tab=t.0)
- [Site](https://sites.google.com/d/1QneHjgrhPjpQ_i9iDOVrf8Ivn7McXcIN/p/1fAGUYkQG2JxVmydQqaz1o78MrP8PPQCt/edit)
- [Figma](https://www.figma.com/design/fahGccQiZEC5xWfqc5brNX/Untitled?m=auto&t=6C6LfIGmLXlI1Yj5-6)


