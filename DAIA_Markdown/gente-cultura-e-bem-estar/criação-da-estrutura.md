# Criação da Estrutura 

Como estratégia para o suporte ao planejamento e execução dos projetos na Zello, foi implantado no ALM Jira o Advanced Roadmaps (Roteiros Avançados). Esse aplicativo permite que o trabalho seja planejado e rastreado entre várias equipes e projetos, permitindo o planejamento com base na capacidade, rastreamento de dependências e prioridades concorrentes, além da possibilidade de explorar cenários alternativos antes de atualizar os dados originais de um determinado projeto ou sprint.

## Responsável pela Estrutura

Gerente de Projetos

## Premissa

Clareza sobre o **Planejamento de Execução** (Plano de Trabalho). É desejável que o plano de trabalho tenha sido validado previamente pelo cliente para que os objetivos do **Plano de Ação** estejam alinhados com o valor a ser entregue. 

## Criando uma estrutura


:::info
Nos passos a seguir, estão ilustrados exemplos de um projeto já existente (Ministério da Saúde), caso o seu projeto seja diferente, por favor entre em contato com seu Administrador do Jira para criação do Projeto e Roteiro Avançado.

:::

### Acesso ao ALM

Ao acessar o Jira (<https://zellounit.atlassian.net/jira>), você será redirecionado para uma página padrão denominada “Seu Trabalho“:

 ![Figura 1: Página padrão: "Seu Trabalho"](/api/attachments.redirect?id=bba89c69-79aa-49a4-aa83-77f4d7b0d443)

\
Para acessar o Roteiro Avançado, acione a opção “Planos“ e em seguida a opção “Ver todos os planos“:

 ![Figura 2: Planos: acesso aos roteiros avançados](/api/attachments.redirect?id=01ef7e59-2d3b-4c27-bed3-2798dfe94be1)

\
Na lista, deverão aparecer todos os planos existentes.

 ![Figura 3: Lista de roteiros existentes](/api/attachments.redirect?id=23a76398-9313-4bd4-887e-d99c07e0e9d6)


:::info
Lembrando que os planos são criados a partir de projetos, quadros ou até mesmo de filtros específicos, portanto se o seu projeto não tem ainda um roteiro criado, entre em contato com seu Administrador do Jira para criação do Projeto ou Filtro e em seguida do Roteiro Avançado.

:::

Selecione o Roteiro na lista. Para tanto basta clicar sobre o nome do Roteiro na coluna “Título“:


:::tip
Clicando sobre a estrela, o roteiro será favoritado, permanecendo fixo no menu “Planos“. Desta maneira não será necessário acessar todos os planos para voltar a acessá-lo :wink:.

:::

\
A visão do roteiro se apresentará conforme a imagem a seguir:

 ![Figura 4: Visão do Roteiro Avançado](/api/attachments.redirect?id=3baeda64-2d0a-4129-9f5c-9c511cf92c36)

O roteiro dispõe de uma série de funcionalidades que possibilitam customizar a visão para facilitar a gestão visual, a saber:

* Campos customizáveis;
* Filtros;
* Gráfico de Gant customizável (possibilita selecionar parâmetros temporais distintintos: semana, meses, trimestres, anos)


:::tip
No exemplo acima, os “Campos” estão contraídos para melhor visualização do diagrama de Gantt, para expandi-los basta clicar sobre o campo. 

:::

Observados os aspectos apresentados, vamos então à criação dos itens de trabalho.

Considerando a hierarquia dos itens de trabalho, **o primeiro item a ser criado é o Épico**, que representa em nosso contexto de trabalho, as ordens de serviço (Sprints no caso do Ministério da Saúde), ou seja, um pacote de trabalho cujos itens abaixo de sua estrutura deverão entregar o valor contratado.

Para criar um épico, acione a opção “Criar item“ disponível no cabeçalho da coluna “Item”:

 ![Figura 5: Como criar um Épico ](/api/attachments.redirect?id=1821fa29-bec6-4e15-acd1-9ebec5ba9ff0)

No menu apresentado, selecione a opção “Epic“:

 ![Figura 6: Menu de criação de itens no roteiro](/api/attachments.redirect?id=30f3f989-4289-4b02-9371-ba3af4eab4df)

O épico será adicionado na lista da coluna “Item“. Para concluir a criação, o Resumo (título) do item deverá ser preenchido. 


:::warning
Por convenção, o Resumo (título) do épico **deverá** ser preenchido com o identificador numérico da ordem de serviço ou sprint, de acordo com o número gerado na ferramenta de gestão de demandas do cliente (Redmine, OTRS, Citsmart…).

:::

 ![Figura 7: Nomeando o Épico](/api/attachments.redirect?id=a613151c-6d3a-412b-bd08-92fbeaca69ac)

Isso feito o item estará disponível na lista definitivamente, no entanto, ainda sem as demais informações que são relevantes para o contexto. 


:::tip
Para que uma estrutura básica fique disponível, certifique-se que esteja selecionada a visualização “Basic“.

:::

Na visualização básica, os campos a direita do item podem ser preenchidos diretamente, clicando sobre o campo. 

Os campos básicos necessários são:

* **Versão:** Identifica o projeto cujo Épico será trabalhado;
* **Status:** Situação atual do Épico (É preenchido automaticamente quando criado);
* **Início Planejado:** Data planejada para o início do trabalho (pode ser preenchido também com o cursor do mouse no diagrama de Gantt);
* **Término Planejado:** Data planejada para o término do trabalho (pode ser preenchido também com o cursor do mouse no diagrama de Gantt);
* **Responsável:** Identifica quem é o Gerente de Projeto escalado para condução do trabalho;

 ![Figura 8: Campos mínimos](/api/attachments.redirect?id=f0709b7b-0c89-4813-a06b-2c4e7f954841)

Preenchidos os campos básicos, observando-se a premissa para criação dos itens de trabalho, deve-se então passar à criação dos itens de trabalho. Os próximos itens deverão ser criados a partir do Épico.

Para tanto, com o cursor sobre o item, selecione o menu representado por três pontos e em seguida a opção “Criar Story“:

 ![Figura 9: Criando itens de trabalho: História ](/api/attachments.redirect?id=ca299fe2-1d17-4c91-b069-c77d28d79006)

Serão apresentadas quatro opções distintas para itens de trabalho, que deverão ser selecionadas de acordo com as características da demanda:

* **Bug:** caracterizam erros, defeitos em funcionalidades existentes ou em construção;
* **Story:** caracterizam funcionalidades. Uma história de usuário deve ser observada como um processo elementar, ou seja, **menor unidade de atividade significativa para o usuário**. Deve constituir uma transação completa, e é autocontida. Ao final de sua execução, deixa o negócio da aplicação em um estado consistente.
* **Ofensor:** caracteriza impedimentos em relação a tarefas existentes;
* **Tarefa:** caracteriza uma parte do trabalho que pode entregar resultado a partir de si mesma ou através de subtarefas.

Nos exemplos subsequentes será considerada uma **demanda de construção** para ilustrar.

 ![Figura 10: Opções de itens de trabalho](/api/attachments.redirect?id=2371f637-7c6b-4370-b3da-ed3612cff34d)

No exemplo abaixo, foram criadas macroatividades, que segundo a visão negocial do Gerente de Projetos entregariam o valor contratado na Sprint.

 ![Figura 11: Itens de trabalho (macro)](/api/attachments.redirect?id=06c73011-8bed-4264-bbde-94857d279d74)

Para continuar com a criação da estrutura no detalhe, é necessário agora a participação de outros atores. A continuidade agora é com o Líder Técnico, que após empoderar-se da demanda, deverá avaliar a estrutura básica, podendo incluir outros itens que julgar necessário para o alcance dos objetivos.