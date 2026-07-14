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
6. [Victor de Matos Vilela](https://github.com/VictorVilela0)  
8. [Fernando Soares da Silva](https://github.com/Nando101210)  
9. [Eduardo Henrique de Sá Nogueira Lemos](https://github.com/EduardoHenrique15)  
10. [Luca Ribeiro Albuquerque](https://github.com/LucaAlbuquerque)  
11. Helena Maia Jordão  
12. Raul Pedro Soares de Lima  
13. Maria Eduarda Leal  

---

## Histórias de Usuário:

<details>
<summary><strong>História 1:</strong> Como administrador da plataforma, eu gostaria de adicionar alunos ao sistema.</summary>

- **Cenário favorável 1:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Cadastrar alunos” e preenche os dados necessários <br>
  Então o sistema salva tudo que foi pedido no banco de dados.

- **Cenário desfavorável 1:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Cadastrar alunos” e esquece de colocar todas as informações devidas.
  Então o sistema não responde adequadamente à tentativa de cadastro, pois falta informação.

- **Cenário desfavorável 2:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Cadastrar alunos” e não insere corretamente sua "data de nascimento".
  Então o sistema não responde adequadamente à tentativa de cadastro, pois a data não foi adicionada.

</details>

<details>
<summary><strong>História 2:</strong> Como administrador da plataforma, eu gostaria de gerenciar os alunos, ou seja: visualizar, atualizar e excluir alunos do sistema.</summary>

- **Cenário favorável 1:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” <br>
  Então o sistema exibe todos os alunos cadastrados no banco de dados.

- **Cenário favorável 2:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” e seleciona “Editar” <br>
  Então os dados do aluno escolhido são exibidos para edição.

- **Cenário favorável 3:**  
  Dado que o administrador está logado no portal  
  Quando acessa a aba “Gerenciar alunos” e seleciona “Deletar” no aluno desejado <br>
  Então o aluno escolhido é excluído do sistema.

- **Cenário desfavorável 1:**  
  Dado que o administrador está logado no portal <br>
  Quando acessa a aba “Gerenciar alunos” <br>
  Então nenhum aluno aparece pois ainda não há alunos cadastrados.

</details>

<details>
<summary><strong>História 3:</strong> Como aluno eu gostaria de avaliar a instituição com sugestões de melhorias.</summary>

- **Cenário favorável 1:**  
  Dado que o aluno está matriculado e logado no portal <br>
  Quando acessa a aba “Avalie a Solidare” <br>
  Então perguntas são exibidas para resposta de "sim" e "não".

- **Cenário favorável 2:**  
  Dado que o aluno está matriculado e logado no portal <br>
  Quando acessa a aba “Avalie a Solidare”  <br>
  Então uma caixa é exibida para registrar sugestões e opiniões.

- **Cenário desfavorável 1:**  
  Dado que o aluno está matriculado e logado no portal <br>
  Quando acessa a aba “Avalie a Solidare” e não consegue responder todas as perguntas.<br>
  Então da erro na hora de concluir a sua avaliação.

</details>

<details>
<summary><strong>História 4:</strong> Como aluno, eu gostaria de acessar o calendário acadêmico para adicionar meus eventos para manter uma organização e rotina de estudos.</summary>

- **Cenário favorável 1:**  
  Dado que o aluno está matriculado e logado no portal <br>
  Quando acessa a aba “Calendário acadêmico", posteriormente "Adicionar evento" e preenche o evento desejado. <br>
  Então o sistema salva o evento no banco de dados.

- **Cenário desfavorável 1:**  
  Dado que o aluno está matriculado e logado no portal <br>
  Quando acessa a aba “Calendário acadêmico” e não preenche título do evento<br>
  Então o sistema exibe mensagem de erro e só salva o evento quando o aluno preencher o título.

- **Cenário desfavorável 2:**  
  Dado que o aluno está matriculado e logado <br>
  Quando acessa a aba “Calendário acadêmico”, posteriormente "Adicionar evento" e não preenhce o horário do evento.<br>
  Então o sistema exibe mensagem de erro e só salva o evento quando o aluno preencher corretamente.
  
</details>

<details>
<summary><strong>História 5:</strong> Como aluno, eu gostaria de acessar o calendário acadêmico para gerenciá-lo, ou seja: visualizar, editar e excluir eventos.</summary>

- **Cenário favorável 1:**  
  Dado que o aluno está matriculado e logado no portal <br>
  Quando acessa a aba “Calendário acadêmico” <br>
  Então são exibidos os eventos acadêmicos cadastrados no calendário, como: datas de provas, entregas, e estudos personalizados.

- **Cenário favorável 2:**  
  Dado que o aluno está matriculado e logado no portal <br>
  Quando acessa a aba “Calendário acadêmico” e posteriormente "Editar" no evento desejado e muda as informações desejadas, como mudança de nome e horário. <br>
  Então as novas informações são salvas no banco de dados, assim, substituindo as antigas.

- **Cenário favorável 3:**  
  Dado que o administrador está logado no portal <br>
  Quando acessa a aba “Calendário acadêmico” e posteriormente "Excluir" no evento desejado <br>
  Então o evento é excluído do banco de dados e desaparece do calendário.

</details>

<details>
<summary><strong>História 6:</strong> Como administrador, eu gostaria de adicionar o desempenho acadêmico e a frequência dos alunos.</summary>

- **Cenário favorável 1:**  
  Dado que o administrador está logado no portal <br>
  Quando acessa a aba “Desempenho e Frequência”, posteriormente "Adicionar informações" e preenche-as <br>
  Então o sistema salva as informações no banco de dados.

- **Cenário desfavorável 1:**  
  Dado que o administrador está logado no portal  <br>
  Quando acessa a aba “Desempenho e Frequência” e tenta preencher letras ao invés de números no número de faltas do aluno <br>
  Então o sistema não permite e só salva as informações quando forem postas corretamente.

- **Cenário desfavorável 2:**  
  Dado que o administrador está logado no portal <br>
  Quando acessa a aba “Desempenho e Frequência” e esquece de preencher o nome do aluno. <br>
  Então o sistema não permite e só salva as informações quando forem postas corretamente.

</details>

<details>
<summary><strong>História 7:</strong> Como administrador eu gostaria de gerenciar o desempenho acadêmico e a frequência dos alunos. Como aluno, apenas visualizá-los</summary>

- **Cenário favorável 1:**  
  Dado que o aluno está matriculado e logado no portal <br>
  Quando acessa a aba “Desempenho e Frequência” <br>
  Então o sistema exibe o número de faltas e o desempenho do aluno com "carinhas de satisfação" e comentário do avaliador.

- **Cenário favorável 2:**  
  Dado que o administrador está logado no portal
  Quando acessa a aba “Desempenho e frequência”, posteriormente "Editar" no aluno desejado e muda as informações desejadas <br>
  Então as novas informações são salvas no banco de dados, assim, substituindo as antigas. <br>

- **Cenário desfavorável 1:**  
  Dado que o aluno está logado no portal <br>
  Quando acessa a aba “Desempenho e Frequência” <br>
  Então uma mensagem avisa que não há dados cadastrados ainda.
</details>

### OBS:
  As histórias 1 e 2 foram as implementadas para o Status Report 1, já a 3, 4, 5, 6 e 7 são para o SR2.

---

## Relato Pair Programming:
  Trabalhamos em duplas e utilizamos o recurso de compartilhamento de tela durante as reuniões para atender a todos os requisitos do projeto. Essa abordagem permitiu uma melhor gestão do tempo, garantindo que as entregas fossem realizadas de maneira eficiente e dentro dos prazos estabelecidos. 

  **Divisao de Tarefas:** Durante cada reunião, organizávamos a divisão de tarefas formando duplas e definindo as responsabilidades de cada uma, o que ajudava a agilizar o andamento das entregas. As decisões eram registradas em um grupo no WhatsApp, garantindo que todos estivessem cientes das atividades e prazos, evitando atrasos. Rafael e Caio se reuniram no Google Meet para fazer os códigos de front-end em HTML e CSS, e Pedro e Luca se reuniram para criar o banco de dados e funções do projeto, por exemplo.

  **Metodologia de Trabalho:** Realizávamos nossas reuniões, tanto em grupo quanto em duplas, por meio do Google Meet, o que facilitava a participação ativa de todos os integrantes. O compartilhamento de tela foi essencial para promover a colaboração de todos durante a execução das tarefas, permitindo que todas as atividades fossem desenvolvidas de forma conjunta e com o conhecimento coletivo do grupo.

---

## Issue / Bugtracker:
![image](https://github.com/user-attachments/assets/a20ce089-9de6-47ab-a92e-c4399ea83196)

## Issue / Bugtracker parte 2:
![image](https://github.com/user-attachments/assets/e9d8314d-e93b-4949-bbaa-d33adb681def)


---
## Screencasts
- [Sreencast Figma Lo-Fi](https://youtu.be/hD8LePoT_Wk)
- [Screencast site portal do aluno](https://youtu.be/MeUWsWJPRtE?feature=shared)
- [Screencast CI/CD](https://youtu.be/0VAGMgBmHXM)
- [Screencast testes automatizados](https://youtu.be/P9t2NahtQ0A)
- [Screencast Figma média fidelidade](https://www.youtube.com/watch?v=oSP6ZIDnfQU)
- [Screencast site portal do aluno 2](https://youtu.be/R0ZSnatxuuI)
---

## Links Úteis

- [Docs](https://docs.google.com/document/d/1Kb8RnBP_5Gz-eml2weoGkFe5UCOAMaLPehDUtYEnm3E/edit?tab=t.0)
- [Site](https://sites.google.com/d/1QneHjgrhPjpQ_i9iDOVrf8Ivn7McXcIN/p/1fAGUYkQG2JxVmydQqaz1o78MrP8PPQCt/edit)
- [Figma](https://www.figma.com/design/fahGccQiZEC5xWfqc5brNX/Untitled?m=auto&t=6C6LfIGmLXlI1Yj5-6)
- [Diagrama](https://miro.com/app/board/uXjVI-xQymA=/)
- [Slides apresentação SR1](https://www.canva.com/design/DAGlk-OyK3U/sfz8-SnF07B0pNAjbGoarA/edit)
- [Slides apresentação SR2](https://www.canva.com/design/DAGpawfZ4vk/3-clsyfxyTdssPYi53kmEA/edit?utm_content=DAGpawfZ4vk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
