# Readme

\
# Nome do Projeto

\[Descrição breve do projeto\]

## Contato[​](https://portal.api.zello.services/docs/arquitetura/readme-default#contato "Direct link to Contato")

\[Inserir aqui informações de contato (TL, DEV, Analista e Gerente de Projeto), como e-mail ou link para o perfil no GitHub, caso alguém queira contribuir, reportar um problema ou tirar dúvidas.\]

## Pré-requisitos[​](https://portal.api.zello.services/docs/arquitetura/readme-default#pr%C3%A9-requisitos "Direct link to Pré-requisitos")

* Node.js (versão)
* Ionic CLI (versão)
* Angular CLI (versão)

## Instalação[​](https://portal.api.zello.services/docs/arquitetura/readme-default#instala%C3%A7%C3%A3o "Direct link to Instalação")


1. Clone o repositório:

   ```javascript
   git clone [URL do repositório]
   ```
2. Instale as dependências:

   ```javascript
   npm install
   ```
3. Inicie o servidor de desenvolvimento:

   ```javascript
   ionic serve
   ```

## Como usar[​](https://portal.api.zello.services/docs/arquitetura/readme-default#como-usar "Direct link to Como usar")


1. Inicie o servidor de desenvolvimento:

   ```javascript
   ionic serve
   ```
2. Abra o aplicativo em um navegador da web.
3. Use o aplicativo de acordo com as instruções fornecidas.

O aplicativo é composto por várias páginas e recursos, incluindo:

### Página inicial[​](https://portal.api.zello.services/docs/arquitetura/readme-default#p%C3%A1gina-inicial "Direct link to Página inicial")

A página inicial apresenta um resumo das principais características do aplicativo e um menu de navegação que permite acessar as diferentes seções do aplicativo.

### Seção 1[​](https://portal.api.zello.services/docs/arquitetura/readme-default#se%C3%A7%C3%A3o-1 "Direct link to Seção 1")

A seção 1 apresenta recursos relacionados à primeira funcionalidade do aplicativo. Inclui:

* Recurso 1: Descrição do recurso 1.
* Recurso 2: Descrição do recurso 2.
* Recurso 3: Descrição do recurso 3.

### Seção 2[​](https://portal.api.zello.services/docs/arquitetura/readme-default#se%C3%A7%C3%A3o-2 "Direct link to Seção 2")

A seção 2 apresenta recursos relacionados à segunda funcionalidade do aplicativo. Inclui:

* Recurso 1: Descrição do recurso 1.
* Recurso 2: Descrição do recurso 2.
* Recurso 3: Descrição do recurso 3.

### Seção 3[​](https://portal.api.zello.services/docs/arquitetura/readme-default#se%C3%A7%C3%A3o-3 "Direct link to Seção 3")

A seção 3 apresenta recursos relacionados à terceira funcionalidade do aplicativo. Inclui:

* Recurso 1: Descrição do recurso 1.
* Recurso 2: Descrição do recurso 2.
* Recurso 3: Descrição do recurso 3.

\[Adicione informações relevantes sobre como usar o aplicativo, incluindo instruções para navegação, funcionalidades específicas, telas e fluxos de trabalho. A ideia é que este readme possa ser usado como uma base de conhecimento para outros devs que precisem trabalhar no projeto ou queira reaproveitar código.\]

## Como trabalhar[​](https://portal.api.zello.services/docs/arquitetura/readme-default#como-trabalhar "Direct link to Como trabalhar")

Para trabalhar no projeto, siga as etapas abaixo:

### Passo 1: Clonar o repositório[​](https://portal.api.zello.services/docs/arquitetura/readme-default#passo-1-clonar-o-reposit%C3%B3rio "Direct link to Passo 1: Clonar o repositório")

Clone o repositório do projeto para o seu computador:

```javascript
git clone https://github.com/seu-usuario/nome-do-projeto.git
```

### Passo 2: Criar uma nova branch[​](https://portal.api.zello.services/docs/arquitetura/readme-default#passo-2-criar-uma-nova-branch "Direct link to Passo 2: Criar uma nova branch")

Crie uma nova branch a partir da branch develop para trabalhar na sua feature. Nomeie a branch de acordo com o padrão de nomenclatura do git-flow:

```javascript
git checkout develop
git pull origin develop
git checkout -b feature/nome-da-sua-feature
```

### Passo 3: Trabalhar na sua feature[​](https://portal.api.zello.services/docs/arquitetura/readme-default#passo-3-trabalhar-na-sua-feature "Direct link to Passo 3: Trabalhar na sua feature")

```javascript
git add .
git commit -m "Mensagem de commit"
git push origin feature/nome-da-sua-feature
```

### Passo 5: Criar um pull request[​](https://portal.api.zello.services/docs/arquitetura/readme-default#passo-5-criar-um-pull-request "Direct link to Passo 5: Criar um pull request")

Crie um pull request da sua branch para a branch develop e aguarde a revisão e aprovação do código.

### Passo 6: Atualizar a branch develop[​](https://portal.api.zello.services/docs/arquitetura/readme-default#passo-6-atualizar-a-branch-develop "Direct link to passo-6-atualizar-a-branch-develop")

Assim que seu pull request for aprovado, atualize a branch develop com as alterações:

```javascript
git checkout develop
git pull origin develop
```

### Passo 7: Remover a branch de feature[​](https://portal.api.zello.services/docs/arquitetura/readme-default#passo-7-remover-a-branch-de-feature "Direct link to Passo 7: Remover a branch de feature")

Remova a branch de feature que você criou para trabalhar na sua funcionalidade:

```javascript
git branch -d feature/nome-da-sua-feature
```

O git-flow é uma metodologia que auxilia no gerenciamento do fluxo de trabalho em projetos que usam o Git como ferramenta de versionamento. Com ele, é possível manter um histórico organizado das alterações, tornando o processo de colaboração mais eficiente e organizado.