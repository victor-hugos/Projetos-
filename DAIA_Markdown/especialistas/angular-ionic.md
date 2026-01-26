# Angular + Ionic

## Introdução

Este documento tem como objetivo descrever as melhores práticas e padrões recomendados para a arquitetura de projetos em Angular + Ionic, utilizando uma abordagem modular. A adoção desses padrões ajudará a garantir que os projetos sejam estruturados de maneira consistente, fáceis de manter e escaláveis.

\
## Vantagens

Um projeto em Angular + Ionic + Capacitor tem várias vantagens. O Angular é um framework poderoso para o desenvolvimento de aplicações web, o Ionic fornece uma biblioteca de componentes visuais e ferramentas para o desenvolvimento de aplicações móveis, enquanto o Capacitor permite que essas aplicações sejam compiladas para plataformas móveis nativas. Aqui estão algumas razões pelas quais criar um projeto nessa combinação é importante:

\
### Flexibilidade de desenvolvimento

O Angular fornece uma grande variedade de recursos para desenvolvedores web, enquanto o Ionic fornece recursos para o desenvolvimento de aplicativos móveis. O Capacitor, por sua vez, permite que aplicativos baseados em web sejam compilados para plataformas móveis nativas, o que significa que os desenvolvedores podem criar aplicativos com uma única base de código e implantá-los em várias plataformas.

### Design responsivo

O Ionic é projetado para fornecer uma experiência de usuário consistente em todas as plataformas, o que significa que os aplicativos podem ser desenvolvidos com um design responsivo que se adapta a diferentes tamanhos de tela. Isso ajuda a garantir que os aplicativos pareçam e funcionem bem em diferentes dispositivos.

### Acesso a recursos nativos

O Capacitor fornece acesso a recursos nativos, como a câmera, a localização e o armazenamento do dispositivo. Isso significa que os aplicativos podem ser desenvolvidos com recursos que normalmente só estão disponíveis em aplicativos nativos.

### Desenvolvimento mais rápido

O Angular e o Ionic possuem ferramentas poderosas para acelerar o desenvolvimento de aplicativos. A CLI do Angular e a CLI do Ionic permitem que os desenvolvedores gerem rapidamente artefatos de código, como componentes, serviços e módulos. Isso economiza tempo e permite que os desenvolvedores se concentrem em implementar as funcionalidades do aplicativo.

### Escalabilidade

O Angular é projetado para desenvolvimento em grande escala e fornece recursos para modularizar o código. O Capacitor e o Ionic também fornecem recursos para modularizar o código e componentizar a interface do usuário. Isso significa que os aplicativos podem ser desenvolvidos de forma escalável, tornando mais fácil a manutenção do código à medida que o projeto cresce.

Em resumo, criar um projeto em Angular + Ionic + Capacitor permite que os desenvolvedores criem aplicativos web e móveis com uma única base de código, acesso a recursos nativos e uma experiência de usuário consistente em várias plataformas. Além disso, o uso dessas ferramentas ajuda a acelerar o desenvolvimento e a garantir que o código seja modular e escalável.

## Visão geral

A arquitetura modular divide o projeto em módulos que podem ser desenvolvidos e testados independentemente uns dos outros. Cada módulo contém seus próprios componentes, serviços, diretivas, pipes e outros recursos, e pode ser importado por outros módulos conforme necessário.

## Trabalhando com componentes

Os componentes são pequenos quebra-cabeças que usamos para criar um aplicativo. Com componentes:

* Não nos repetimos. Um componente pode ser usado em vários lugares no aplicativo.
* Temos um código sustentável. Podemos detectar rapidamente o que está acontecendo e onde está dando errado.
* Podemos criar aplicativos rapidamente.
* É por isso que hoje em dia todos os frameworks e bibliotecas frontend usam componentes ou funções para construir o frontend como um quebra-cabeça.

### Quando criar um componente?

O objetivo principal de um componente é encapsular a funcionalidade. Se o uso da funcionalidade se repetir no aplicativo, você deverá criar um componente. Se for simples e não tiver muito código, você pode não considerar a criação de um componente.

### Prefixando seletores de componentes

Por padrão, a CLI Angular gera o componente com o prefixo app-. Personalizar seletores de componentes é uma boa prática, especialmente em aplicativos grandes. Isso ajuda a evitar conflitos com outros módulos importados e a ver explicitamente o módulo do componente de onde vem (princípio de localizar o código rapidamente).

Em pequenos aplicativos, personalizar um prefixo de componente não é interessante.

### Separando classe de componente, CSS e template

O guia de estilo angular recomenda que, se o CSS ou modelo tiver mais de três linhas, mova o CSS para um arquivo de estilo e o HTML para um arquivo de modelo. Isso ajuda a manter o código limpo e fácil de ler.

 ![Example banner](https://portal.api.zello.services/assets/images/separando-components-6b09d3ab78b20f6af039223f90c0efaf.webp " =1714x710")

### Entrada e Saída de Decoração[​](https://portal.api.zello.services/docs/arquitetura/angular-arq#entrada-e-sa%C3%ADda-de-decora%C3%A7%C3%A3o "Direct link to Entrada e Saída de Decoração")

Use entradas e saídas com seus decoradores correspondentes: @Input(), @Output() em vez de usar atributos dentro do @Component

 ![Example banner](https://portal.api.zello.services/assets/images/entrada-saida-e09d87458f02ebc55b179759945e1721.webp " =1714x674")

### Delegar lógica complexa

Se a lógica for simples, mantenha-a no componente. Caso contrário, mova-o para um serviço (princípio de responsabilidade única).

## SDK Ionic

A SDK Ionic é uma ferramenta que permite o desenvolvimento de aplicativos móveis híbridos para iOS, Android e web usando tecnologias web, como HTML, CSS e JavaScript. A SDK Ionic é baseada no popular framework Angular e é construída em cima do Cordova e do Capacitor para fornecer recursos nativos aos aplicativos. A SDK Ionic fornece uma ampla variedade de componentes e recursos que permitem que os desenvolvedores criem aplicativos móveis modernos, responsivos e personalizados.

[Click aqui para ver a documentação](https://ionicframework.com/docs/components)

## Estrutura de diretórios[​](https://portal.api.zello.services/docs/arquitetura/angular-arq#estrutura-de-diret%C3%B3rios "Direct link to Estrutura de diretórios")

A seguir, está a estrutura de diretórios para projetos em Angular + Ionic com uma arquitetura modular:

**Exemplo da estrutura de diretórios**

```javascript
my-app/
├── /node_modules
├── /src
│   ├── /app
│   │   ├── app.component.ts
│   │   ├── app.module.ts
│   │   ├── app-routing.module.ts
│   │   ├── /core
│   │   │   ├── /pages
│   │   ├── /shared
│   │   │   ├── /components
│   │   │   ├── /services
│   │   │   ├── /models
│   │   │   ├── /pipes
│   │   │   ├── /directives
│   │   ├── /modules
│   │   │   ├── /feature1
│   │   │   │   ├── feature1.module.ts
│   │   │   │   ├── /models
│   │   │   │   ├── /services
│   │   │   │   ├── /components
│   │   │   │   │   ├── component1
│   │   │   │   │   │   ├── component1.component.html
│   │   │   │   │   │   ├── component1.component.scss
│   │   │   │   │   │   ├── component1.component.ts
│   │   │   │   │   ├── component2
│   │   │   │   │   │   ├── component2.component.html
│   │   │   │   │   │   ├── component2.component.scss
│   │   │   │   │   │   ├── component2.component.ts
│   │   │   │   ├── /pages
│   │   │   │   │   ├── /page1
│   │   │   │   │   │   ├── page1.component.html
│   │   │   │   │   │   ├── page1.component.scss
│   │   │   │   │   │   ├── page1.component.ts
│   │   │   │   ├── /page2
│   │   │   │   │   ├── page2.component.html
│   │   │   │   │   ├── page2.component.scss
│   │   │   │   │   ├── page2.component.ts
│   ├── /assets
│   ├── /environments
│   ├── index.html
│   ├── main.ts
│   ├── styles.scss
│   ├── /theme
│   │   ├── variables.scss
│   │   ├── typography.scss
├── /platforms
├── /plugins
├── /www
├── config.xml
├── package.json
├── tsconfig.json
├── tslint.json


```

#### /node_modules

Pasta que contém todas as dependências do projeto.

#### /src[​](https://portal.api.zello.services/docs/arquitetura/angular-arq#src "Direct link to /src")

Pasta que contém todo o código-fonte da aplicação.

#### /app

Pasta que contém os arquivos relacionados à configuração do módulo raiz da aplicação.

* app.component.ts: arquivo que contém o componente principal da aplicação.
* app.module.ts: arquivo que define o módulo raiz da aplicação.
* app-routing.module.ts: arquivo que contém as rotas da aplicação.

#### /core

Pasta que contém os arquivos relacionados ao núcleo da aplicação.

* /pages: pasta que contém os componentes que são compartilhados por diferentes partes da aplicação.

#### /shared

Pasta que contém os arquivos compartilhados entre os diferentes módulos da aplicação.

* /components: pasta que contém os componentes que são usados em diferentes partes da aplicação.
* /services: pasta que contém os serviços que são usados em diferentes partes da aplicação.
* /models: pasta que contém os modelos de dados que são usados em diferentes partes da aplicação.
* /pipes: pasta que contém os pipes que são usados em diferentes partes da aplicação.
* /directives: pasta que contém as diretivas que são usadas em diferentes partes da aplicação.

#### /modules

Pasta que contém os diferentes módulos da aplicação.

* /feature1: pasta que contém o módulo da feature1.
  * feature1.module.ts: arquivo que define o módulo da feature1.
  * /models: pasta que contém os modelos de dados específicos da feature1.
  * /services: pasta que contém os serviços específicos da feature1.
  * /components: pasta que contém os componentes específicos da feature1.
    * /component1: pasta que contém o componente1 específico da feature1.
      * component1.component.html: arquivo que contém o template do componente1 específico da feature1.
      * component1.component.scss: arquivo que contém os estilos do componente1 específico da feature1.
      * component1.component.ts: arquivo que contém a lógica do componente1 específico da feature1.
    * /component2: pasta que contém o componente2 específico da feature1.
      * component2.component.html: arquivo que contém o template do componente2 específico da feature1.
      * component2.component.scss: arquivo que contém os estilos do componente2 específico da feature1.
      * component2.component.ts: arquivo que contém a lógica do componente2 específico da feature1.
  * /pages: pasta que contém os componentes de página específicos da feature1.
    * /page1: pasta que contém o componente de página 1 específico da feature1.
      * page1.component.html: arquivo que contém o template do componente de página 1 específico da feature1.
      * page1.component.scss: arquivo que contém os estilos do componente de página 1 específico da feature1.
      * page1.component.ts: arquivo que contém a lógica do componente de página 1 específico da feature1.

#### /assets

Pasta que contém os arquivos estáticos da aplicação, como imagens e fontes.

#### /environments

Pasta que contém os arquivos de configuração para os diferentes ambientes da aplicação, como desenvolvimento e produção.

#### index.html

Arquivo HTML que é a página principal da aplicação.

#### main.ts

Arquivo que é o ponto de entrada da aplicação.

#### styles.scss

Arquivo que contém os estilos globais da aplicação.

#### /theme

Pasta que contém os arquivos relacionados ao tema da aplicação, como as variáveis de estilo e as definições de tipografia.

#### /platforms

Pasta que contém as plataformas de destino da aplicação, como iOS e Android, no caso de um projeto Ionic.

#### /plugins

Pasta que contém os plugins adicionais para a aplicação, no caso de um projeto Ionic.

#### /www

Pasta que contém o código compilado da aplicação, pronta para ser implantada em um servidor ou em uma loja de aplicativos.

#### config.xml

Arquivo que contém a configuração da aplicação para um projeto Ionic.

#### package.json

Arquivo que contém as informações sobre as dependências do projeto e outras configurações do projeto.

#### tsconfig.json

Arquivo que contém as configurações do compilador TypeScript.

#### tslint.json

Arquivo que contém as regras do linter de código.

#### Conclusão

A estrutura de diretórios proposta organiza o código de forma eficiente, tornando-o mais fácil de entender e manter. Os recursos compartilhados são armazenados no diretório shared, enquanto as funcionalidades específicas da feature são armazenadas no diretório modules. As páginas principais da aplicação são armazenadas no diretório core, permitindo que elas sejam gerenciadas de forma independente. Os componentes específicos da feature são armazenados dentro dos subdiretórios das páginas específicas da feature. Esperamos que essa estrutura ajude a manter a aplicação organizada e fácil de manter.

## Convenções

### Componentes

* Use nomes descritivos para componentes, por exemplo, product-list ao invés de list.
* Use kebab-case para nomes de componentes, por exemplo, product-list ao invés de ProductList ou productList.
* Use um prefixo para componentes que pertencem a um módulo específico, por exemplo, cart-product-list para um componente que pertence ao módulo de carrinho de compras.

### Módulos

* Use nomes descritivos para módulos, por exemplo, product-catalog ao invés de catalog.
* Use kebab-case para nomes de módulos, por exemplo, product-catalog ao invés de ProductCatalog ou productCatalog.
* Use um sufixo Module para nomes de módulos, por exemplo, product-catalog.module.ts.

### Serviços

* Use nomes descritivos para serviços, por exemplo, product-service ao invés de service.
* Use kebab-case para nomes de serviços, por exemplo, product-service ao invés de ProductService ou productService.
* Use um sufixo Service para nomes de serviços, por exemplo, product-service.ts.

### Variáveis[​](https://portal.api.zello.services/docs/arquitetura/angular-arq#vari%C3%A1veis "Direct link to Variáveis")

* Use camelCase para nomes de variáveis, por exemplo, productList ao invés de product_list ou ProductList.
* Use nomes descritivos para variáveis.

### Métodos

* Use camelCase para nomes de métodos, por exemplo, getProductList ao invés de get_product_list ou GetProductList.
* Use nomes descritivos para métodos.

## Padrões

### Estrutura de Diretórios

* Use uma arquitetura modular para organizar a aplicação em módulos específicos da feature.
* Armazene os recursos compartilhados em um diretório shared, como modelos, serviços, pipes e diretivas.
* Armazene os componentes compartilhados em um diretório shared/components.
* Use a estrutura padrão do Angular para componentes, que inclui um arquivo HTML, um arquivo CSS e um arquivo TypeScript.
* Armazene as páginas principais da aplicação em um diretório core/pages.
* Armazene os componentes específicos da feature dentro dos subdiretórios das páginas específicas da feature.
* Evite aninhamento excessivo de diretórios para evitar problemas de legibilidade e manutenção.

### Organização de Código

* Use injeção de dependência para gerenciar dependências entre componentes, serviços e outros recursos.
* Separe o HTML, CSS e TypeScript em arquivos separados para cada componente.
* Use um arquivo .module.ts para cada módulo e um arquivo .service.ts para cada serviço.
* Use interfaces para definir a forma dos objetos complexos, como modelos de dados.
* Use tipos TypeScript fortemente tipados sempre que possível para melhorar a legibilidade e evitar erros.
* Mantenha as funções e métodos o mais curtos possível, preferencialmente abaixo de 30 linhas.

## Bibliotecas

### dependencies

* "@angular/common": "^15.0.0",
* "@angular/core": "^15.0.0",
* "@angular/forms": "^15.0.0",
* "@angular/platform-browser": "^15.0.0",
* "@angular/platform-browser-dynamic": "^15.0.0",
* "@angular/router": "^15.0.0",
* "@capacitor/app": "4.1.1",
* "@capacitor/core": "4.6.3",
* "@capacitor/haptics": "4.1.0",
* "@capacitor/keyboard": "4.1.1",
* "@capacitor/status-bar": "4.1.1",
* "@ionic/angular": "^6.1.9",
* "ionicons": "^6.0.3",
* "rxjs": "\~7.5.0",
* "tslib": "^2.3.0",
* "zone.js": "\~0.11.4"

### devDependencies

* "@angular-devkit/build-angular": "^15.0.0",
* "@angular-eslint/builder": "^14.0.0",
* "@angular-eslint/eslint-plugin": "^14.0.0",
* "@angular-eslint/eslint-plugin-template": "^14.0.0",
* "@angular-eslint/template-parser": "^14.0.0",
* "@angular/cli": "^15.0.0",
* "@angular/compiler": "^15.0.0",
* "@angular/compiler-cli": "^15.0.0",
* "@angular/language-service": "^15.0.0",
* "@capacitor/cli": "4.6.3",
* "@ionic/angular-toolkit": "^6.0.0",
* "@types/jasmine": "\~4.0.0",
* "@types/node": "^12.11.1",
* "@typescript-eslint/eslint-plugin": "5.3.0",
* "@typescript-eslint/parser": "5.3.0",
* "eslint": "^7.6.0",
* "eslint-plugin-import": "2.22.1",
* "eslint-plugin-jsdoc": "30.7.6",
* "eslint-plugin-prefer-arrow": "1.2.2",
* "jasmine-core": "\~4.3.0",
* "jasmine-spec-reporter": "\~5.0.0",
* "karma": "\~6.4.0",
* "karma-chrome-launcher": "\~3.1.0",
* "karma-coverage": "\~2.2.0",
* "karma-coverage-istanbul-reporter": "\~3.0.2",
* "karma-jasmine": "\~5.1.0",
* "karma-jasmine-html-reporter": "\~2.0.0",
* "ts-node": "\~8.3.0",
* "typescript": "\~4.8.4"

## Capacitor

O Capacitor é um dos principais frameworks para o desenvolvimento de aplicativos móveis híbridos em conjunto com o Ionic. Ele é uma biblioteca de código aberto que permite acessar recursos nativos dos dispositivos móveis, como câmera, geolocalização, sensores, notificações, entre outros. O Capacitor é uma escolha popular para projetos em conjunto com o Ionic por várias razões:

Compatibilidade com o Angular: O Capacitor foi desenvolvido com o Angular em mente, o que o torna uma opção natural para desenvolvedores que trabalham com o Ionic.

Acesso a recursos nativos: O Capacitor fornece uma API fácil de usar para acessar recursos nativos do dispositivo móvel, permitindo que os aplicativos desenvolvidos com o Ionic tenham uma experiência de usuário mais rica e personalizada.

Desenvolvimento de aplicativos híbridos: O Capacitor permite o desenvolvimento de aplicativos híbridos, que podem ser implantados tanto no iOS quanto no Android.

Compatibilidade com outras bibliotecas: O Capacitor é compatível com outras bibliotecas e frameworks populares, como o Cordova, o qual já foi amplamente utilizado na comunidade Ionic.

Usando o Capacitor em conjunto com o Ionic, os desenvolvedores podem criar aplicativos móveis híbridos poderosos e personalizados que funcionam em várias plataformas. Além disso, o Capacitor permite que os aplicativos tenham acesso a recursos nativos dos dispositivos móveis, como a câmera e a geolocalização, sem ter que escrever código nativo para cada plataforma. Isso pode economizar muito tempo e esforço de desenvolvimento e tornar o processo de desenvolvimento mais eficiente.

Para incluir o Capacitor em um projeto Ionic, você pode seguir os seguintes passos:


1. Instalar o Capacitor: execute o seguinte comando no terminal para instalar o Capacitor na sua aplicação Ionic:

**Exemplo**

```javascript
npm install @capacitor/core @capacitor/cli --save-exact
```


2. Inicializar o Capacitor: execute o seguinte comando para inicializar o Capacitor na sua aplicação Ionic:

**Exemplo**

```javascript
npx cap init
```


3. Adicionar plataformas: execute o seguinte comando para adicionar as plataformas que deseja suportar:

**Exemplo**

```javascript
npx cap add android
npx cap add ios
```


4. Adicionar plugins: adicione os plugins que deseja usar em sua aplicação com o Capacitor. Por exemplo, para usar a câmera, execute o seguinte comando:

**Exemplo**

```javascript
npm install @capacitor/camera
npx cap sync
```

## Melhores Práticas

### Utilize o Angular CLI

O Angular CLI (Command Line Interface) é uma ferramenta poderosa e essencial para desenvolvedores que trabalham com Angular. A principal importância do uso do Angular CLI é que ele automatiza tarefas tediosas e repetitivas que precisam ser executadas para criar um novo projeto Angular ou adicionar recursos à um projeto existente.

Algumas das tarefas que a CLI realiza automaticamente incluem:

* Criar a estrutura de diretórios do projeto com as configurações iniciais, como o arquivo package.json.
* Configurar as dependências necessárias para o projeto, como o Angular e outros pacotes de terceiros.
* Gerar componentes, diretivas, serviços e outros artefatos de código para o projeto, usando comandos simples.
* Criar módulos para organizar o código do projeto.
* Configurar o sistema de build e testes do projeto.
* Iniciar um servidor de desenvolvimento para executar e testar a aplicação em tempo real.

Com a CLI, os desenvolvedores podem criar projetos Angular rapidamente e facilmente, sem precisar se preocupar com a configuração inicial e as tarefas de build e deploy. Isso permite que os desenvolvedores possam se concentrar na implementação das funcionalidades da aplicação e na lógica de negócios.

Além disso, a CLI do Angular segue as melhores práticas e padrões recomendados pela equipe de desenvolvimento do Angular, o que garante que o projeto esteja seguindo uma arquitetura sólida e bem estruturada. Isso significa que os projetos criados com a CLI do Angular são mais fáceis de manter, testar e escalar.

Portanto, se você deseja instalar o CLI usando pacotes NPM, deve usar npm install -g @angular/cli

* Agora, se você deseja criar um novo aplicativo, pode usar ng new e iniciar um aplicativo totalmente funcional imediatamente.
* Se você deseja usar shells de teste para o desenvolvimento de componentes, rotas, serviços e canais com um único comando, pode usar “ ng create ”
* Para um aplicativo que é desenvolvido localmente e precisa ser testado na fase de desenvolvimento, você pode usar “ng serve” para testar e encontrar erros.
* Para executar testes de unidade local ou testes de ponta a ponta, o comando mais comum usado é o comando “ng test” .
* Para criar um brilho de código, você pode usar ng lint .
* E quando você quiser configurar um service worker Angular, digite ng add @angular/pwa.

### Use Lazy Loading

Lazy loading é uma técnica de otimização em aplicações web que consiste em carregar apenas o código necessário para a visualização inicial da página, atrasando o carregamento do restante do código até que ele seja necessário. Em aplicações Angular + Ionic, o lazy loading é comumente usado para dividir o aplicativo em módulos menores, que podem ser carregados de forma independente.

Quando o aplicativo é carregado, o código para a página inicial é carregado primeiro. Em seguida, o código para cada módulo é carregado à medida que o usuário navega pelo aplicativo. Isso melhora significativamente o tempo de carregamento inicial e ajuda a reduzir o tamanho do pacote de código do aplicativo, o que pode melhorar o desempenho em dispositivos móveis e em redes lentas.

Para implementar o lazy loading em um aplicativo Angular + Ionic, é necessário definir os módulos de forma que sejam carregados apenas quando necessários. Isso é feito usando o método loadChildren do Angular Router para carregar o módulo quando a rota correspondente for acessada. O módulo é então carregado sob demanda e adicionado ao aplicativo, sem a necessidade de carregar todo o aplicativo de uma só vez.

**Exemplo**

```javascript
const routes: Routes = [
  {
    path: 'profile',
    loadChildren: () => import('./modules/profile/profile.module').then(m => m.ProfileModule)
  }
];
```

### Use interfaces

As interfaces permitem definir contratos que especificam a estrutura e o comportamento de objetos em um programa, sem precisar implementar a funcionalidade completa.

Ao definir uma interface, é possível especificar um conjunto de propriedades e métodos que devem ser implementados por qualquer classe que implemente essa interface. Isso permite que outras partes do código possam interagir com a classe por meio da interface, em vez de se vincular diretamente à implementação da classe. Isso facilita a manutenção do código, pois permite que as implementações das classes sejam alteradas sem afetar outras partes do código.

As interfaces também são úteis para garantir que as classes implementem um conjunto consistente de propriedades e métodos, tornando o código mais seguro e confiável. Isso pode ajudar a prevenir erros comuns, como acessar uma propriedade que não existe ou chamar um método que não foi implementado corretamente.

Em projetos Angular, as interfaces são amplamente utilizadas para definir modelos de dados, bem como para especificar contratos para serviços e diretivas. Por exemplo, é comum usar interfaces para definir o formato de objetos que são retornados por serviços RESTful ou para especificar a estrutura de dados que é usada em um formulário.

Em resumo, usar interfaces é uma boa prática em programação porque ajuda a tornar o código mais modular, seguro e fácil de manter. As interfaces permitem especificar contratos claros entre as partes do código, facilitando a colaboração e a interoperabilidade.

**Exemplo**

```javascript
export interface BookState {
  books: Book[];
  loaded: boolean;
  error?: string | null;
}
```

### Evite vazamentos de memória

Quando navegamos de um componente para outro componente, o primeiro componente é destruído e o outro inicializa. O primeiro componente foi inscrito no Observable e agora o componente foi destruído. Isso pode causar vazamentos de memória.

Segue dicas de como previnir:


1. Usando takeUntil

   O operador takeUntil permite cancelar a assinatura de um observável quando um segundo observável emite um valor.

   Em muitos casos, em aplicações Angular, observáveis são usados para monitorar eventos do usuário, como cliques em botões, rolagem de página ou outras interações. Esses observáveis podem continuar emitindo valores, mesmo após a destruição do componente ou serviço que os criou, o que pode causar vazamento de memória e outros problemas.

   O takeUntil resolve esse problema, permitindo que o desenvolvedor cancele a assinatura do observável quando o componente ou serviço é destruído. O operador takeUntil cria um segundo observável que emite um valor quando um evento específico ocorre, como a destruição de um componente ou serviço. Quando esse segundo observável emite um valor, o operador takeUntil cancela a assinatura do primeiro observável, evitando que ele continue emitindo valores.

   Por exemplo, o código abaixo mostra um exemplo de uso do operador takeUntil para gerenciar a assinatura de um observável de eventos do usuário:

**Exemplo**

```javascript
import { Component, OnDestroy } from '@angular/core';
import { fromEvent, Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';

@Component({
  selector: 'app-example',
  template: '<button (click)="onClick()">Click me</button>',
})
export class ExampleComponent implements OnDestroy {
  private unsubscribe$ = new Subject<void>();

  constructor() {
    fromEvent(document, 'click')
      .pipe(takeUntil(this.unsubscribe$))
      .subscribe(() => console.log('Document clicked'));
  }

  onClick() {
    console.log('Button clicked');
  }

  ngOnDestroy() {
    this.unsubscribe$.next();
    this.unsubscribe$.complete();
  }
}
```

Neste exemplo, o operador takeUntil é usado para cancelar a assinatura do observável fromEvent quando o componente é destruído. O takeUntil recebe um segundo observável, this.unsubscribe$, que emite um valor quando o componente é destruído. O método ngOnDestroy é usado para completar o unsubscribe$, o que garante que o observável fromEvent seja cancelado quando o componente é destruído.

Em resumo, o operador takeUntil é uma técnica útil para gerenciar a assinatura de observáveis em aplicações Angular, permitindo que os desenvolvedores evitem vazamentos de memória e outros problemas relacionados à assinatura de observáveis.


2. Usando Async pipe

   O AsyncPipe é uma diretiva do Angular que simplifica o gerenciamento de observáveis no template. Ele é usado para obter valores de um observável e atualizar automaticamente o template sempre que o valor é atualizado. O AsyncPipe é uma forma fácil de exibir dados assíncronos em um template sem ter que gerenciar manualmente as assinaturas e desassinaturas de observáveis.

   A diretiva AsyncPipe é muito útil quando se trabalha com observáveis que emitem valores de forma assíncrona, como em chamadas de API assíncronas ou em atualizações em tempo real de banco de dados. Quando um observável é passado para o AsyncPipe, ele se inscreve automaticamente no observável e atualiza o template sempre que o valor do observável é atualizado.

   Para usar o AsyncPipe, basta passar o observável para a diretiva no template usando a sintaxe observavel | async. O AsyncPipe cuida da assinatura e desassinatura do observável automaticamente. O exemplo abaixo mostra como usar o AsyncPipe para exibir dados de um serviço assíncrono em um template:

**Exemplo**

```javascript
<div *ngIf="servicoDados.dados$ | async as dados">
  <p>Nome: {{ dados.nome }}</p>
  <p>Idade: {{ dados.idade }}</p>
</div>
```


3. Use take(1)

O operador take(1) é uma função do RxJS que é usada para limitar o número de valores emitidos por um observável. Ele é comumente usado em aplicações para obter o primeiro valor emitido por um observável e cancelar a assinatura após o recebimento desse valor.

O uso do take(1) é importante em muitos cenários, porque ajuda a evitar problemas comuns, como vazamento de memória e fluxos infinitos. O take(1) garante que o observável em questão emita apenas um valor, mesmo que continue a emitir valores indefinidamente. Isso é importante porque muitas vezes só precisamos do primeiro valor emitido, e não há necessidade de manter a assinatura do observável aberta.

Além disso, o uso do take(1) pode melhorar o desempenho de aplicativos que trabalham com fluxos de dados assíncronos. Ao limitar o número de valores emitidos pelo observável, o take(1) reduz a carga no sistema, garantindo que apenas o valor necessário seja processado.

O exemplo abaixo mostra como usar o take(1) para obter o primeiro valor emitido por um observável e cancelar a assinatura do observável após o recebimento desse valor:

**Exemplo**

```javascript
import { Observable } from 'rxjs';
import { take } from 'rxjs/operators';

const observable: Observable<number> = /* observable que emite valores */

observable.pipe(
  take(1)
).subscribe((value: number) => {
  console.log('Valor recebido:', value);
});
```

Neste exemplo, o take(1) é usado para obter o primeiro valor emitido pelo observável observable e cancelar a assinatura do observável após o recebimento desse valor. O subscribe recebe apenas um valor e imprime esse valor no console.

Em resumo, o uso do take(1) é importante em muitos cenários de desenvolvimento de aplicações Angular, porque ajuda a evitar problemas comuns, como vazamento de memória e fluxos infinitos. Ele é uma maneira simples e eficaz de obter apenas o valor necessário de um observável e cancelar a assinatura do observável após o recebimento desse valor.

### Cache API calls

Usar cache para as chamadas da API é uma técnica importante em aplicações, pois pode melhorar significativamente o desempenho e a experiência do usuário. A Cache API calls refere-se à prática de armazenar em cache os resultados de chamadas de API, para que possam ser reutilizados sem precisar fazer uma nova chamada à API.

A principal vantagem de usar a Cache API calls é que ela reduz a quantidade de chamadas de API necessárias para renderizar a página ou atualizar os dados, reduzindo assim o tempo de carregamento e a sobrecarga do servidor. Com a Cache API calls, as chamadas de API só precisam ser feitas quando os dados mudam, o que significa que as chamadas de API podem ser evitadas quando os dados não mudam.

Além disso, o uso da Cache API calls pode melhorar a experiência do usuário, pois os dados armazenados em cache são exibidos instantaneamente, sem atrasos devido a chamadas de API. Isso é especialmente útil em dispositivos móveis, onde as chamadas de API podem ser lentas e afetar negativamente a experiência do usuário.

Existem várias maneiras de implementar a Cache API calls em aplicações Angular, incluindo o uso de bibliotecas de cache, como o http-interceptor do Angular. Com o http-interceptor, é possível interceptar as chamadas de API e armazenar em cache os resultados em uma memória local ou em um armazenamento persistente. Dessa forma, as próximas solicitações para os mesmos dados podem ser atendidas a partir do cache, em vez de fazer uma nova chamada à API.

Em resumo, usar Cache API calls é uma técnica importante em aplicações Angular porque pode melhorar significativamente o desempenho e a experiência do usuário, além de reduzir a sobrecarga do servidor. Com a Cache API calls, as chamadas de API só precisam ser feitas quando os dados mudam, o que significa que as chamadas de API podem ser evitadas quando os dados não mudam. Existem várias maneiras de implementar a Cache API calls em aplicações Angular, incluindo o uso de bibliotecas de cache, como o http-interceptor do Angular.

segue abaixo um exemplo simples de como usar o HttpInterceptor do Angular:

**Exemplo**

```javascript
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpEvent, HttpHandler, HttpRequest, HttpResponse } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()
export class CacheInterceptor implements HttpInterceptor {

  private cache: Map<string, any> = new Map();

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

    if (request.method !== 'GET') {
      return next.handle(request);
    }

    const cachedResponse = this.cache.get(request.url);

    if (cachedResponse) {
      return of(new HttpResponse({ body: cachedResponse }));
    }

    return next.handle(request).pipe(
      tap(event => {
        if (event instanceof HttpResponse) {
          this.cache.set(request.url, event.body);
        }
      })
    );
  }
}
```

Neste exemplo, o HttpInterceptor é usado para armazenar em cache os resultados de chamadas de API GET. Quando uma solicitação GET é feita, o interceptor verifica se a resposta está armazenada em cache. Se estiver, ele retorna a resposta em cache em vez de fazer uma nova solicitação à API. Caso contrário, a solicitação é enviada à API e a resposta é armazenada em cache após o recebimento.

Para usar o HttpInterceptor, é necessário fornecê-lo no módulo que será usado. Por exemplo:

**Exemplo**

```javascript
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { CacheInterceptor } from './cache-interceptor';

@NgModule({
imports: [ HttpClientModule ],
providers: [
{ provide: HTTP_INTERCEPTORS, useClass: CacheInterceptor, multi: true }
]
})
export class AppModule { }
```

Neste exemplo, o CacheInterceptor é fornecido como um interceptor HTTP. O multi: true é usado para permitir que vários interceptores sejam fornecidos simultaneamente.

### Práticas consistentes de codificação

Aqui estão algumas práticas recomendadas a serem seguidas para garantir que seu projeto de desenvolvimento angular siga os padrões de código corretos.

* Os arquivos devem ser limitados a 400 linhas de código.
* Crie funções curtas com no máximo 75 linhas de código.
* Declare-o com 'const' se os valores das variáveis ​​não estiverem mudando.
* Obdeça a convenção de nomenclatura de variáveis ​​camelCase.
* Obdeça a estrutura de diretórios defina na arquitetura.

\
\
