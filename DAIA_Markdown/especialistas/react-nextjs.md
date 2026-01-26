# React + NextJS

## Introdução

O objetivo deste documento é descrever a arquitetura baseada em NextJS para o desenvolvimento de um frontend de alta qualidade. O NextJS é um framework React que fornece funcionalidades de renderização do lado do servidor e um sistema de roteamento poderoso para a criação de aplicativos modernos e escaláveis.

## Vantagens

O NextJS é um framework React para criação de aplicações frontend. Ele fornece uma série de recursos que tornam o desenvolvimento mais rápido, eficiente e escalável. Aqui estão algumas das principais vantagens de se usar o NextJS:

### Renderização do lado do servidor

O NextJS permite a renderização do lado do servidor (SSR), que gera o HTML do lado do servidor antes de ser enviado para o navegador do usuário. Isso melhora significativamente o tempo de carregamento da página, aumentando a velocidade da aplicação.

### Roteamento dinâmico

O NextJS possui um sistema de roteamento dinâmico baseado em arquivos, que permite a criação de rotas com base em arquivos JavaScript, sem a necessidade de configurações adicionais. Isso torna o roteamento de páginas mais fácil e intuitivo.

### Código dividido

O NextJS usa o conceito de código dividido, que divide o código em pedaços menores e os carrega sob demanda, de acordo com a necessidade do usuário. Isso reduz o tamanho do arquivo inicial, tornando a aplicação mais rápida e reduzindo o tempo de carregamento.

### Suporte a CSS Modules

O NextJS suporta CSS Modules, que permite encapsular os estilos em cada componente, evitando conflitos e tornando a estilização mais fácil e organizada.

### Integração com APIs

O NextJS tem uma integração nativa com APIs, permitindo o uso de dados de API em tempo de compilação e tempo de execução. Isso permite a criação de páginas dinâmicas que podem se atualizar automaticamente com os dados da API.

### SEO amigável

O NextJS é SEO amigável, permitindo a inclusão de meta tags personalizadas e o uso de URLs amigáveis, o que ajuda a melhorar a visibilidade do aplicativo nos mecanismos de busca.

Em resumo, o NextJS é uma escolha sólida para o desenvolvimento de aplicativos frontend escaláveis e eficientes, com recursos avançados, como renderização do lado do servidor, roteamento dinâmico, código dividido, integração com APIs e suporte a CSS Modules, tornando o desenvolvimento mais fácil e eficiente.

## Visão geral

A arquitetura modular divide o projeto em módulos que podem ser desenvolvidos e testados independentemente uns dos outros. Cada módulo contém seus próprios componentes, serviços, diretivas, pipes e outros recursos, e pode ser importado por outros módulos conforme necessário.

## SDK Ionic[​](https://portal.api.zello.services/docs/arquitetura/react-arq#sdk-ionic "Direct link to SDK Ionic")

A SDK Ionic é uma ferramenta que permite o desenvolvimento de aplicativos móveis híbridos para iOS, Android e web usando tecnologias web, como HTML, CSS e JavaScript. A SDK Ionic é baseada no popular framework Angular e é construída em cima do Cordova e do Capacitor para fornecer recursos nativos aos aplicativos. A SDK Ionic fornece uma ampla variedade de componentes e recursos que permitem que os desenvolvedores criem aplicativos móveis modernos, responsivos e personalizados.

[Click aqui para ver a documentação](https://ionicframework.com/docs/components)

## Estrutura de diretórios

A seguir, está a estrutura de diretórios para projetos com uma arquitetura modular:

**Exemplo da estrutura de diretórios**

```javascript
├── public ==> Diretório de arquivos publicos da aplicação (exemplo: imagens estáticas, fonts, svgs...)
│
├── src 
│ └─ pages      ==> Diretório de páginas da aplicação
│   ├── _app.tsx
│   ├── _document.tsx
│   ├── index.tsx
│   └── home-exemplo
│       └── index.tsx
├── shared      ====> Geralmente definimos nesse diretórios o que é comum a aplicação
│   ├── components
│   │   └── Exemplo
│   │       └── Exemplo.tsx
│   ├── constants
│   │   └── index.ts
│   ├── contexts
│   │   └── Exemplo
│   │       └── ExemploContext.tsx
│   ├── enums
│   │   └── routes.enum.ts
│   ├── guards
│   │   └── ExemploGuard.jsx
│   ├── hooks
│   │   └── useExemplo.jsx
│   ├── models
│   │   ├── global.ts
│   │   └── index.ts
│   ├── services
│   │   └── index.ts
│   └── utils
│       └── index.ts
├── modules      ====> Segue mesma estrutura da pasta shared, porém com módulos funcionalidades/responsábilidade isolada
│   ├── components
│   ├── constants
│   ├── contexts
│   ├── enums
│   ├── guards
│   ├── hooks
│   ├── models
│   └─ services
├── store.ts
└── styles
    └── globals.css
```

## Convenções

### Pages

O nome deve ter referencia ao objetivo do pagina e sua rota (URL). Como utilizados Next.js devemos seguir a referencia aqui descrita para padronização de correto funcionamento do projeto.

A página deve ser criada no diretorio referente ao projeto(.src/pages), utilizando a lingua portuguesa no padrão de kebab-case.

**Exemplo**

```javascript
// Ex. Quero criar uma página para a rota /quero-folga
// é necessário criar um arquivo "index.tsx" no diretório "quero-folga"
export const QueroFolga = () => {
    
    return (
        <>
            <h1>Chefe me dá folga?</>
            <p>Olha só que doc lindo!</p>
        </>
    )
}
export default QueroFolga
```

### Components

O nome deve ter referencia ao objetivo do componet que deseja criar, utilizando a lingua portuguesa no padrão de UpperCamelCase.

**Exemplo**

```javascript
// Ex. Quero criar um component de padrão de codigo, o nome dele ficaria PenseNumExemploLindo.tsx
export type ExemploProps = {
    titulo: string
    handleCancel?: any
    handleOk?: any
}
export const Exemplo = (props: ExemploProps) => {
    return (
        <>
            <div>
                <h1>{props.titulo}</h1>
                <button onClick={handleOk} >
                    <button onClick={handleCancel} >
            </div>
        </>
    )
}
export default Exemplo
```

### Enums

* Todos Enums da aplicação devem ficar no diretorio "enums".
* Todo enum deve conter o sufixo ".enum.ts"
* Caso seja de feature de um modulo deverá fica em: "src/modules/module-exemplo/enums"
* Caso seja de compartilhado na aplicação deverá fica em: "src/shared/enums"

**Exemplo**

```javascript
//Ex. Para criar um enum compartilhado de nome bora-tomar-uma
// "src/shared/enums/bora-tomar-uma.enum.ts"

export enum BoraTomarUmaEnum {
    NoHappyDaZello = 'no-happy-da-zello',
    NossoGerentePaga = 'nosso-gerente-paga'
}
```

**Exemplo**

```javascript
// Ex. Para criar um enum no módulo "bora-codar" de nome xama-bb
// "src/modules/bora-codar/enums/xama-bb.enum.ts"
export enum XamaBbEnum {
    XamaUm = 'xama-um',
    XamaDois = 'xama-dois',
    IhXamaBb = 'xama-bb',
}
```

### Guards

O nome deve ter referencia ao objetivo do guard que deseja criar, utilizando a lingua portuguesa no padrão de UpperCamelCase. O guard deve ser criado no diretorio referente ao projeto(.src/guards/components ou .src/meu-modulo/guards) e deve ter responsabilidade isolada.

**Exemplo**

```javascript
// Ex. Quero criar um guard de padrão de codigo, o nome dele ficaria OlhaMeuGuard.tsx
const ExemploGuard = ({ children }) => {
    useEffect(() => {
        // seu código
    }, [])
    function authCheck(url) {
        // seu código
    }
    return (authorized && children)
}
export default ExemploGuard
```

### Models

As representam todo comportamento da camada de modelo que utilizaremos no react. Todo tipo de comportamento de objetos deverá ser feito nessa camada, de chamadas asyncronas a atualização de estado de objetos compartilhados.

Nessa arquitetura utizamos o [rematch](https://rematchjs.org/) para abstrair e simplicar o uso do redux. Consulte a [documentação oficial](https://rematchjs.org/docs/) para mais informações.

**Exemplo**

```javascript
// Ex. Quero criar um model padrão, o nome dele ficaria exemplo.tsx
// Arquivos model devem conter SEMPRE nome minúsculo

import { createModel } from "@rematch/core"
import { RootModel } from './index'

export interface IExemplo {
    id: string
    nome: string
}

export const exemplo = createModel<RootModel>()({
    state: {} as ExemploState,
    reducers: {
        setNome: (state, nome) => {
            return { ...state, nome }
        },
        setId: (state, id) => {
            return { ...state, ...id }
        }
    },
    effects: (dispatch) => ({
        async metodoRetornaExemplo(id: string) {
            // Seu código
        },
        async metodoAtualizaExemplo(payload: IExemplo, rootState) {
            // Seu código
        },
    }),
})

interface ExemploState {
    _id?: string
    email?: string
    nome?: string
}
```

### Modules

* Use nomes descritivos para módulos, por exemplo, product-catalog ao invés de catalog.
* Use kebab-case para nomes de módulos, por exemplo, product-catalog ao invés de ProductCatalog ou productCatalog.
* Use um sufixo Module para nomes de módulos, por exemplo, product-catalog.module.ts.

### Services

* Use nomes descritivos para serviços, por exemplo, produro.service ao invés de service.
* Use kebab-case para nomes de serviços, por exemplo, product-service ao invés de ProductService ou productService.
* Use um sufixo Service para nomes de serviços, por exemplo, product.service.ts.

### Variáveis

* Use camelCase para nomes de variáveis, por exemplo, produtoLita ao invés de produto_lista.
* Use nomes descritivos para variáveis.

### Métodos

* Use camelCase para nomes de métodos, por exemplo, pegarProdutoLista ao invés de pegar_produto_lista.
* Use nomes descritivos para métodos.

## Padrões

### Estrutura de Diretórios[​](https://portal.api.zello.services/docs/arquitetura/react-arq#estrutura-de-diret%C3%B3rios-1 "Direct link to Estrutura de Diretórios")

* Use uma arquitetura modular para organizar a aplicação em módulos específicos.
* Armazene os recursos compartilhados em um diretório shared, como models, services, utils, enums, etc.
* Armazene os componentes compartilhados em um diretório shared/components.
* Armazene as páginas principais da aplicação em um diretório src/pages.
* Armazene os componentes específicos da feature dentro dos subdiretórios das páginas específicas da feature.
* Evite aninhamento excessivo de diretórios para evitar problemas de legibilidade e manutenção.
* \

### Organização de Código

* Use injeção de dependência para gerenciar dependências entre componentes, serviços e outros recursos.
* Use um arquivo .service.ts para cada serviço.
* Use interfaces para definir a forma dos objetos complexos, como modelos de dados.
* Use tipos TypeScript fortemente tipados sempre que possível para melhorar a legibilidade e evitar erros.
* Mantenha as funções e métodos o mais curtos possível, preferencialmente abaixo de 30 linhas.

## Bibliotecas

### dependencies

* "@next/font": "13.1.5",
* "@rematch/core": "^2.2.0",
* "@unform/core": "^2.1.6",
* "@unform/web": "^2.1.6",
* "axios": "^1.3.0",
* "iconsax-react": "^0.0.8",
* "moment": "^2.29.4",
* "next": "13.1.5",
* "nookies": "^2.5.2",
* "react": "18.2.0",
* "react-dom": "18.2.0",
* "quill": "1.3.7",
* "react-quilljs": "1.2.11",
* "react-redux": "^8.0.5",
* "react-toastify": "^9.1.1",
* "redux": "^4.2.1"

### devDependencies

* "@types/node": "18.11.18",
* "@types/react": "18.0.27",
* "@types/react-dom": "18.0.10",
* "@tailwindcss/forms": "^0.5.3",
* "autoprefixer": "^10.4.13",
* "typescript": "4.9.4",
* "postcss": "^8.4.21",
* "tailwindcss": "^3.2.4",
* "eslint": "8.32.0",
* "eslint-config-next": "13.1.5"

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

\
