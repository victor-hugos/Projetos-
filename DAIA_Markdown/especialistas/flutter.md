# Flutter

## Introdução

O Flutter é um framework de desenvolvimento de aplicativos móveis que utiliza a linguagem de programação Dart. Ele permite a criação de aplicativos com interface de usuário rápida e responsiva em várias plataformas, incluindo Android e iOS. A arquitetura recomendada para o desenvolvimento de aplicativos Flutter é baseada no padrão de arquitetura MVC (Model-View-Controller), organizado em módulos.

## Visão geral

A arquitetura baseada em módulos é uma abordagem que visa dividir a aplicação em módulos independentes, cada um com sua própria responsabilidade e funcionalidades. Cada módulo contém seus próprios componentes, como modelos de dados, visualizações, controladores, serviços e repositórios.

Essa abordagem permite que a equipe de desenvolvimento trabalhe em diferentes partes da aplicação simultaneamente, o que pode acelerar o desenvolvimento e melhorar a manutenibilidade. Além disso, a separação de módulos pode ajudar a isolar e solucionar problemas com mais facilidade.

A arquitetura baseada em módulos também é uma forma de implementar a arquitetura MVC (Model-View-Controller), em que cada módulo representa uma parte do padrão MVC. Cada módulo tem seu próprio modelo de dados, que é gerenciado pelo repositório. A visualização é responsável por apresentar os dados ao usuário, enquanto o controlador gerencia a interação entre a visualização e o modelo de dados. Por fim, o serviço é responsável por realizar a comunicação com o servidor.

Ao adotar a arquitetura baseada em módulos, é importante ter em mente que a divisão dos módulos deve ser baseada em torno da funcionalidade da aplicação e da forma como os usuários a utilizam. Uma boa estratégia é pensar nos diferentes casos de uso da aplicação e identificar as funcionalidades que correspondem a cada caso de uso. Cada caso de uso pode então ser convertido em um módulo separado, com seus próprios componentes.

## Vantagens

### Desenvolvimento rápido

Flutter permite o desenvolvimento rápido de aplicativos, pois é possível escrever e testar o código em tempo real, sem a necessidade de recompilar a aplicação a cada pequena mudança.

### Interface do usuário atraente

Flutter oferece widgets personalizados, que são fáceis de estilizar e adaptar para diferentes dispositivos e tamanhos de tela, resultando em uma interface do usuário atraente e responsiva.

### Alta performance

Flutter é construído sobre o motor gráfico Skia, o que resulta em uma alta performance e fluidez na renderização de interface do usuário, especialmente quando comparado a outras tecnologias híbridas.

### Código compartilhado

Flutter permite que o código seja compartilhado entre as plataformas iOS e Android, o que resulta em menos trabalho e menos chances de erros no desenvolvimento.

### Boa documentação

O Flutter tem uma documentação bem completa, que facilita o aprendizado e a solução de problemas. Além disso, a comunidade Flutter é muito ativa e solidária, o que ajuda a encontrar soluções para problemas específicos.

### Ferramentas e integrações

Flutter possui um conjunto de ferramentas integradas, como o Hot Reload, que permite testar e implementar rapidamente alterações no código, além de ser compatível com várias IDEs, como Android Studio e VS Code.

### Multiplataforma

Com o Flutter, é possível criar aplicativos para diversas plataformas, incluindo Android, iOS, Windows, macOS, Linux e web, com um único conjunto de código.

## Estrutura de diretórios

Exemplo da estrutura de diretórios

\
```typescript
- lib/
  - main.dart
  - modules/
    - authentication/
      - model/
        - user.dart
      - view/
        - login_screen.dart
        - registration_screen.dart
      - controller/
        - authentication_controller.dart
      - repository/
        - authentication_repository.dart
      - service/
        - authentication_service.dart
    - post/
      - model/
        - post.dart
      - view/
        - post_list_screen.dart
        - post_detail_screen.dart
        - post_create_screen.dart
      - controller/
        - post_controller.dart
      - repository/
        - post_repository.dart
      - service/
        - post_service.dart
    - user/
      - model/
        - user_profile.dart
      - view/
        - profile_screen.dart
      - controller/
        - user_controller.dart
      - repository/
        - user_repository.dart
      - service/
        - user_service.dart
  - shared/
    - widget/
      - custom_button.dart
      - custom_text_field.dart
    - utils/
      - constants.dart
      - routes.dart
      - themes.dart
- test/
    - module_test/
      - authentication_test/
        - authentication_controller_test.dart
        - authentication_repository_test.dart
        - authentication_service_test.dart
      - post_test/
        - post_controller_test.dart
        - post_repository_test.dart
        - post_service_test.dart
      - user_test/
        - user_controller_test.dart
        - user_repository_test.dart
        - user_service_test.dart
    - widget_test/
      - custom_button_test.dart
      - custom_text_field_test.dart
```

\
* **lib/**: diretório raiz do projeto, que contém o arquivo main.dart, bem como os módulos e a pasta compartilhada. 
* **modules/**: diretório que contém os módulos da aplicação, como autenticação, postagem e perfil do usuário.
* **shared/**: diretório que contém componentes compartilhados em todos os módulos, como widgets e utilitários.
* **test/**: diretório que contém os testes do projeto, organizados em subdiretórios para cada módulo e para os testes de widgets. Nessa estrutura, a pasta principal é lib/, que contém o arquivo main.dart, os módulos authentication, post e user, além da pasta shared e a pasta de testes test/. Cada módulo contém pastas para model, view, controller, repository e service. A pasta shared contém subpastas para widget e utils. A pasta de testes possui subpastas para os testes de cada módulo e para os testes de widget.

\
## Trabalhando com widgets

Trabalhar com widgets é uma parte fundamental do desenvolvimento de aplicativos Flutter. Os widgets são os blocos de construção básicos da interface do usuário em Flutter, e são utilizados para construir desde componentes simples, como botões e textos, até telas mais complexas, como listas e gráficos.

Existem existem dois tipos principais de widgets no Flutter: os StatelessWidgets e os StatefulWidgets. Os StatelessWidgets são widgets que não armazenam estado interno, enquanto os StatefulWidgets armazenam estado interno. Ambos os tipos de widgets têm um método build() que retorna uma hierarquia de widgets, que representa a interface do usuário.

O Flutter possui uma vasta coleção de widgets pré-construídos, que permitem aos desenvolvedores criar rapidamente uma interface do usuário atraente e responsiva. Os widgets pré-construídos incluem widgets básicos, como Text, Image e Icon, e widgets mais complexos, como ListView, GridView e AppBar. Esses widgets pré-construídos são altamente personalizáveis e podem ser facilmente adaptados para atender às necessidades específicas da aplicação.

Além dos widgets pré-construídos, é possível criar widgets personalizados. Para criar um widget personalizado, basta estender a classe StatelessWidget ou StatefulWidget e implementar o método build(). O widget personalizado pode ser estilizado e personalizado com propriedades e eventos específicos do componente.

O Flutter também fornece recursos para trabalhar com a hierarquia de widgets, incluindo o uso de layouts, como o Row e o Column, para organizar e posicionar widgets na tela. O Flutter também oferece a possibilidade de construir telas com várias camadas de widgets, por exemplo, adicionando um Container ou um Scaffold como pai de outros widgets.

Em resumo, trabalhar com widgets é fundamental para o desenvolvimento de aplicativos Flutter, uma vez que os widgets são os blocos de construção básicos da interface do usuário. O Flutter oferece uma vasta coleção de widgets pré-construídos e também permite a criação de widgets personalizados. Além disso, o Flutter fornece recursos para trabalhar com a hierarquia de widgets, como o uso de layouts para posicionar os widgets na tela e a possibilidade de construir telas com várias camadas de widgets.

## Convenções

Convenção de nomenclatura É importante adotar uma convenção de nomenclatura consistente para classes, variáveis, funções e widgets. Algumas das convenções mais comuns incluem o uso de camelCase para nomes de variáveis e funções, PascalCase para nomes de classes e snake_case para nomes de arquivos.

Exemplo de convenção de nomenclatura

```typescript
import 'package:flutter/material.dart';

// Definindo as constantes de cores e tamanhos
const kPrimaryColor = Colors.blue;
const kSecondaryColor = Colors.white;

// Widget principal do aplicativo
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My App',
      // Define o tema do aplicativo
      theme: ThemeData(
        primaryColor: kPrimaryColor,
        scaffoldBackgroundColor: kSecondaryColor,
      ),
      // Define a página inicial do aplicativo
      home: HomePage(title: 'Home Page'),
    );
  }
}

// Widget da página inicial do aplicativo
class HomePage extends StatelessWidget {
  HomePage({Key key, this.title}) : super(key: key);

  final String title;

  // Método para exibir uma caixa de diálogo ao pressionar o botão
  void _showDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Olá'),
          content: Text('Este é um exemplo de caixa de diálogo!'),
          actions: <Widget>[
            TextButton(
              child: Text('Fechar'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  // Widget da página inicial do aplicativo
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'Bem-vindo ao meu aplicativo!',
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => _showDialog(context),
              child: Text('Clique aqui para abrir uma caixa de diálogo'),
            ),
          ],
        ),
      ),
    );
  }
}
```

Neste exemplo, as convenções de nomenclatura são seguidas para nomear variáveis, classes e métodos de acordo com as práticas comuns do Flutter. Por exemplo, a classe MyApp é renomeada para MyApp, enquanto a classe MyHomePage é renomeada para HomePage. As variáveis são nomeadas usando camelCase, com a primeira letra minúscula, como kPrimaryColor e kSecondaryColor. Os métodos são nomeados usando camelCase, com a primeira letra minúscula, como _showDialog.

Ao seguir as convenções de nomenclatura do Flutter, o código do aplicativo é mais legível e mais fácil de dar manutenção, pois os nomes das classes, variáveis e métodos seguem uma convenção padrão. Além disso, o uso de convenções de nomenclatura ajuda a garantir que a aparência do aplicativo seja consistente em toda a interface do usuário.

\
## Organização do projeto

É recomendável organizar o projeto em pastas e subpastas de acordo com a funcionalidade dos diferentes módulos. Isso ajuda a manter o projeto organizado e fácil de entender.

### Documentação

É importante documentar o código de forma clara e concisa, incluindo comentários no código e a criação de um arquivo README para explicar a estrutura do projeto, as dependências e outras informações importantes.

### Uso de widgets personalizados

É importante criar widgets personalizados para funcionalidades repetitivas em diferentes partes da aplicação, como cabeçalhos, rodapés e botões. Isso ajuda a manter a consistência visual e a reutilização de código.

### Uso de classes para gerenciamento de estado

É recomendável usar classes para gerenciar o estado do aplicativo, em vez de armazenar o estado em widgets individuais. Isso ajuda a simplificar o código e torná-lo mais fácil de entender.

### Uso de testes automatizados

É importante escrever testes automatizados para garantir que a aplicação funcione conforme o esperado. Isso ajuda a identificar e corrigir problemas antes que a aplicação seja lançada.

### Uso de boas práticas de programação

É importante seguir as boas práticas de programação, como evitar código duplicado, manter o código simples e legível, e escrever código modular e reutilizável.

## Padrões

### Widgets

* Reutilize widgets sempre que possível: uma das principais vantagens dos widgets é que eles podem ser reutilizados em diferentes partes da aplicação. Sempre que possível, é recomendável reutilizar widgets em vez de criar novos widgets para tarefas semelhantes. Isso ajuda a economizar tempo e esforço no desenvolvimento, além de garantir uma consistência visual em toda a aplicação.
* Separe o layout da lógica: para tornar o código mais legível e fácil de manter, é importante separar o layout da lógica do widget. O layout deve ser responsável por definir a aparência do widget, enquanto a lógica deve ser separada em classes separadas.
* Use o máximo de widgets pré-construídos: o Flutter fornece uma vasta coleção de widgets pré-construídos, que podem ser facilmente personalizados para atender às necessidades específicas da aplicação. Ao utilizar esses widgets pré-construídos, é possível economizar tempo e esforço no desenvolvimento, além de garantir a consistência visual em toda a aplicação.
* Evite criar widgets complexos: ao criar um widget, é importante mantê-lo o mais simples possível. Widgets complexos são mais difíceis de entender, testar e manter. Além disso, widgets complexos podem afetar negativamente o desempenho da aplicação.
* Mantenha a hierarquia de widgets simples: a hierarquia de widgets é a estrutura que define a relação entre os diferentes widgets na interface do usuário. Para garantir um desempenho ideal, é importante manter a hierarquia de widgets o mais simples possível. Hierarquias complexas podem afetar negativamente o desempenho da aplicação.
* Use layouts para organizar widgets: o Flutter fornece layouts, como o Row, o Column e o Stack, para organizar e posicionar widgets na tela. Ao usar layouts, é possível criar interfaces do usuário bem organizadas e responsivas.
* Personalize os widgets com propriedades: os widgets pré-construídos podem ser personalizados com propriedades específicas, como cor, tamanho e estilo. Ao personalizar widgets, é possível adaptá-los para atender às necessidades específicas da aplicação.
* Teste os widgets: é importante testar os widgets para garantir que eles funcionem conforme o esperado. O Flutter fornece recursos para testar widgets, incluindo o WidgetTester e o WidgetInspector.

## Gerenciamento de estado

O gerenciamento de estado é um aspecto crítico do desenvolvimento de aplicativos Flutter, pois permite que o aplicativo mantenha e atualize dinamicamente os dados do usuário. Existem várias abordagens para gerenciamento de estado em aplicativos Flutter, cada uma com suas próprias vantagens e desvantagens.

A seguir, estão algumas das abordagens mais comuns para gerenciamento de estado em aplicativos Flutter:

Gerenciamento de estado local: o gerenciamento de estado local envolve o uso de variáveis locais para armazenar e atualizar dados de estado em um widget específico. Isso é adequado para aplicativos simples, mas pode se tornar difícil de gerenciar à medida que a complexidade do aplicativo aumenta.

Gerenciamento de estado com passagem de parâmetros: essa abordagem envolve a passagem de dados de estado entre widgets por meio de parâmetros. Isso é adequado para aplicativos pequenos e simples, mas pode se tornar difícil de gerenciar à medida que a complexidade do aplicativo aumenta.

Gerenciamento de estado com streams e blocos: essa abordagem envolve o uso de streams e blocos para gerenciar o estado do aplicativo. É adequado para aplicativos mais complexos e permite a separação da lógica de negócios da interface do usuário.

Gerenciamento de estado com Provider: essa abordagem envolve o uso da biblioteca Provider para gerenciar o estado do aplicativo. É adequado para aplicativos de qualquer tamanho e ajuda a simplificar o código do aplicativo.

Independentemente da abordagem escolhida, é importante manter o estado do aplicativo consistente e escalável. Isso pode ser feito seguindo boas práticas de programação, como evitar a duplicação de código, manter o código modular e reutilizável e documentar o código de forma clara e concisa. Além disso, é importante escrever testes automatizados para garantir que o aplicativo funcione conforme o esperado. Com um gerenciamento de estado cuidadoso, o aplicativo Flutter pode oferecer uma experiência do usuário mais fluida e agradável.

## Bibliotecas

==flutter_bloc:== uma biblioteca para gerenciamento de estado que ajuda a separar a lógica do negócio da interface do usuário.

==http:== uma biblioteca para fazer solicitações HTTP, permitindo que o aplicativo se comunique com APIs externas.

==cached_network_image:== uma biblioteca para fazer cache de imagens baixadas da web.

==shared_preferences:== uma biblioteca para armazenar dados simples como chaves e valores no dispositivo.

==provider:== uma biblioteca que ajuda a gerenciar o estado do aplicativo de maneira eficiente.

==intl:== uma biblioteca que fornece recursos de localização, como formatação de datas, números e moedas.

==flutter_localizations:== um pacote que fornece recursos de localização para idiomas diferentes.

==google_maps_flutter:== uma biblioteca que permite a criação de mapas e integração com o Google Maps.

==flutter_svg:== uma biblioteca que permite a exibição de imagens vetoriais SVG em vez de imagens rasterizadas.