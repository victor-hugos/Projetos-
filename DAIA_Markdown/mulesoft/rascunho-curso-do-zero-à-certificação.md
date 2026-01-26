# RASCUNHO Curso - Do Zero à certificação

* O que é C4A (Center for Enablement)?
  * É um time cross-funcional
  * Garante que os ativos são:
    * Produzidos e Publicados
    * Consumidos
    * Ampla e largamente utilizados na organização
    * Bem alavancados
  * O sucesso do C4E é medido pelo uso dos ativos
  * É composto por: Time de TI, Time de Inovação e Times de LOB (line of business)

\
* Conectividade liderada por API 
  * a

\
* Alcançando uma rede de aplicativos
  * a

\
* Desconstruindo APIs e APIs RESTful
  * <https://www.mulesoft.com/api-university/what-are-apis-and-how-do-they-work>
  * API ou Application Programming Interface (ou interface de programação de aplicativos) é um conjunto de abstrações das funcionalidades de um sistema, que são expostas para serem utilizadas por outros atores externos aos processos internos do sistema.
    * Exemplos de Abstrações:
      * O pedal do acelerador de um carro
      * A torneira da sua casa
  * Ela fornece informações sobre como se comunicar com um componente de software, definindo:
    * Operações (o que chamar)
    * Entradas (o que detectar com uma chamada)
    * Saídas (O que retorna de uma chamada)
    * Tipos de dados Subjacente
  * É uma abstração por que oferece a funcionalidade independente da implementação. 
    * O que permite que você altere a implementação sem afetar os usuários da API
  * \

\
* O que é um Web service?
  * É um método de comunicação que permite dois sistemas de software trocarem informações através da internet
  * Os dois tipos mais comuns de Web service são:
    * SOAP
    * REST

\
* RESTful web services
  * REST (REpresentational State Transfer ou transferência de estado representacional)
    * É um estilo de arquitetura onde clientes e servidores trocam representações de recursos usando o Protocolo HTTP
    * Por ser uma arquitetura (Stateless) o servidor não armazena o estado do cliente, sendo assim, todas as requisições devem conter todas as informações necessárias como por exemplo:
      * O Estado do cliente
      * A operação a ser realizada
      * Os dados a serem processados
      * etc…
    * \

\
# Começando de verdade


:::info
Assets: <https://anypoint.mulesoft.com/exchange/portals/muletraining/>

:::

\
## Ciclo de vida de uma API


 1. Design da API
 2. Simulação
 3. Feedback
 4. Validação
 5. Construção
 6. Teste
 7. Versionamento
 8. Segurança
 9. Deploy e Registro
10. Monitoramento
11. Analyze
12. Troubleshoot
13. Escala

\
O que é Mule

* É o motor de tempo de execução da Anypoint Platform
* Um Barramento de Serviço Empresarial (ESB) leve baseado em Java
* E uma plataforma de integração que permite aos desenvolvedores conectar aplicativos de maneira rápida e fácil
* Age como um sistema de trânsito para transporte de dados entre apps
* Pode conectar todos os sistemas, incluindo serviços web, JMS, JDBC, HTTP e muito mais
* Desacopla integrações ponto a ponto fazendo com que todos os aplicativos (não-Mule) conversem com o barramento em vez de diretamente entre si
* Pode ser implantado em qualquer lugar, pode integrar e orquestrar eventos em tempo real ou em lote
* Aplica políticas para governança de API

\
* Os aplicativos Mule recebem eventos, os processam e os roteiam para outros terminais;
* O Aplicativo Mule aceita e processa um evento Mule por meio de uma série de processadores de eventos Mule concetados em um Fluxo
* A aplicação pode consistir em:
  * Um único fluxo
  * Vários fluxos
  * Vários fluxos conectados 

\
Um fluxo típico do Mule

* Uma origem de eventos Mule que inicia a execução do Fluxo
  * Pode ser acionado por um evento como:
    * Uma solicitação do consumidor de um dispositivo móvel
    * Uma alteração nos dados em um banco de dados
    * A criação de um novo ID de cliente em um aplicativo SaaS
    * entre outors
* Processadores de eventos Mule que transformam, filtram, enriquecem e processam o evento e sua mensagem
* \

\
Criando aplicativo de integração com o Flow Designer

\
> Runtime Worker - CloudHub

\
Worker do CloudHub

* Um worker é uma instância dedicada do Mule que executa um aplicativo
* Cada Worker:
  * É executado em um contêiner separado de todos os outros aplicativos
  * É implantado e monitorado de forma independente
  * Executa em uma nuvem de trabalho específica em uma região do Mundo
* Os workers podem ter uma capacidade de memória e poder de processamento diferentes
  * Os aplicativos podem ser dimensionados verticalmente alterando o tamanho do worker
  * Os aplicativos podem ser dimensionados horizontalmente adicionando vários workers
* Há workers em diferentes ambientes
  * Design (apenas para aplicativos Flow Designer), Sandbox, Produção, …
  * Os aplicativos podem ser promovidos de um ambiente para o outro.
  * \

\
Estrutura do Evento Mule

* Um evento no Mule é composto por:
  * Mule Message são os dados que passam pelos fluxos no aplicativo e inclui:
    * Attributes - Metadados contidos no cabeçalho da mensagem
    * Payload - As informações principais da mensagem - os dados que o aplicativo processa
  * Variables - São Metadados para o evento Mule - podem ser definidos e referenciados no aplicativo que está processando o envento

\
Datawave

> <https://dataweave.mulesoft.com/learn/dataweave>

* É uma linguagem de expressão para o Mule acessar, consultar e transformar dados de eventos do Mule
* É uma linguagem semelhante a Json criada apenas para casos de uso de consulta e transformação de dados
  * Framework completo e totalmente nativo
* Totalmente integrado com o Flow Designer (e Anypoint studio)
  * Interface gráfica com desenvolvimento com reconhecimento de carga útil (Payload)
  * \

\
