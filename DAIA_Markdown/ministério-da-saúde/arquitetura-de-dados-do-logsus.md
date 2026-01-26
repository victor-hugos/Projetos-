# Arquitetura de Dados do LogSUS

# Diagrama

 ![](/api/attachments.redirect?id=fe782d1b-5da8-4175-b430-c86f212f7dd0)

\
# Sobre a arquitetura

O LogSUS tem como objetivo reunir dados de diferentes fontes, entregar essas informações para outros sistemas e para alimentar Dashboards. Para que isso seja possível necessitamos de alguns passos:


1. Ingestão
2. Armazenamento
3. Transformação
4. Disponibilização
5. Visualização

## 1. Ingestão de Dados

Tendo em vista que o LogSUS deverá ingerir dados de sistemas internos (Ex: SISMAT) e externos (SEI, SIAFI, etc). Devemos pensar em uma maneira de gerenciar a busca desses dados. 

### Orquestrador

O ministério da Saúde já possui hoje uma instância do [Apache Airflow](https://airflow.apache.org/) que é uma plataforma open-source para criar, gerenciar, agendar e monitorar a execução de fluxos de trabalho. Em geral esses fluxos são escritos em Python ou Scala. 

Apesar de ser uma ferramenta genérica capaz de executar múltiplos tipos de “*workflows*", é muito utilizado para executar processos de Dados. Visto que disponibiliza uma série de [conectores](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/connections.html), que facilitam a conexão e execução de fluxos com diferentes fontes e destinos de dados.

Utilizando o conceito de DAGs (Directed Acyclic Graph) e Tasks, podemos criar fluxos completos, que incluam mas não se limitam a:

* Realizar a busca dos dados em uma fonte específica;
* Executar fluxos diferentes em caso de sucesso ou falha;
* Realizar novas tentativas em caso de falha;
* Observabilidade na execução das DAGs ou granular a nível de cada Task.

### Ingestão de dados via Python

De acordo com [pesquisa realizada pelo StackOverflow](https://survey.stackoverflow.co/2023/) Python é a 3a linguagem mais popular do mundo sendo também uma das principais linguagens para uso em ciência e engenharia de dados. A utilização do Python se apresenta como uma ótima alternativa por sua popularidade, manutenibilidade e integração com o Apache Airflow.

Ao utilizar Python é possível utilizar os conectores do airflow, desenvolver sistemas que buscam dados em bancos de dados, em APIs, via “web crawling" entre outras.

### Ingestão de dados via Airbyte (Opcional)

O [Airbyte](https://airbyte.com/) é uma ferramenta *no-code* para criação de Data Pipelines e processos de ETL. Possui uma variedade de [conectores](https://airbyte.com/connectors) que exigem apenas algumas configurações que podem ser realizadas através de sua interface gráfica. Uma desvantagem é a quantidade elevada de recursos necessários para funcionamento da ferramenta, quando comparado, por exemplo, a execução de scripts via Airflow. O Airbyte necessita de ao menos 11 containeres para o seu funcionamento básico, podendo ultrapassar esse número em momentos de execução de “*jobs*".

## 2. Armazenamento dos dados

Sabendo que os dados ingeridos variam entre “Dados estruturados" (Bancos de dados relacionais), “Dados Semi-estruturados" (Bancos de dados não-relacionais, arquivos JSON e CSV, respostas de APIs e etc) e “Dados não estruturados" (Arquivos em pdf, imagens entre outros). A criação de um ambiente de “*data lake*" se apresenta como alternativa Ideal.

Para a criação de tal ambiente, sugere-se a utilização da ferramenta [Min.io](https://min.io/), que é uma plataforma open-source de armazenamento de objetos compatível com o padrão S3. Outra vantagem está em sua integração com ferramentas de infraestrutura como o Kubernetes, permitindo a criação de buckets e armazenamento de objetos em ambientes de "*Cloud”(Aws, Azure, GCP e etc), on-premise (Rancher, Kubernetes,* VMs entre outros) e Híbridos. O minio oferece a possibilidade de distribuição, replicação e *tiering* dos dados em múltiplos ambientes, provedores ou locais diferentes.

A principal vantagem do Minio está no baixo custo de armazenamento, facilidade de integração com múltiplos sistemas por utilizar um protocolo comum, o armazenamento de objetos em diferentes formatos e a possibilidade de executar processos de "*particionamento on write*" utilizando uma estrutura de pastas para facilitar a busca de dados quando necessário. Por exemplo:

É possível criar um “*bucket*" para armazenar informações de fornecedores, utilizando como “chave primária" o CNPJ, e em um único local, manter armazenado informações relevantes, como dados de cadastro, certificados, certidões, contratos e etc.

 ![](/api/attachments.redirect?id=78fbdfb3-0801-41b3-af04-17c78af12c46)

Ainda é possivel aumentar o nível de particionamento de informações ao utilizar partições temporais como Ano, mês, dia, hora, minuto, segundo e etc em que o registro foi criado ou adicionado ao Data Lake.

## 3. Transformação dos dados

Ao realizar a ingestão de dados no Data Lake já é possível disponibilizar a consulta desses dados, conforme discutido a seguir, porém, em geral, realiza-se um processo de "Transformação" que envolve a limpeza, cruzamento e padronização dos dados.

O processo de transformação mostra-se essencial para o melhor funcionamento do LogSUS uma vez que evita que recursos sejam gastos para realizar essas transformações a cada nova consulta, sendo necessário executa-lo apenas uma vez para os novos conjuntos de dados.

O Processo de Transformação de dados pode ser executado utilizando Scripts Python orquestrados pelo Apache Airflow, através de outras ferramentas, como por exemplo o DBT (que permite realizar o processo utilizando a linguagem SQL) ou ao utilizar programas desenvolvidos com esse propósito.

> Importante notar, que as transformações em geral seguem requisitos negociais e técnicos, sendo necessário mapea-los para o correto funcionamento do processo.

## 4. Disponibilização dos dados

A disponibilização de dados pode ser realizada de diferentes maneiras que podem entregar dados em diferentes etapas dos processos sendo executados, por exemplo:


1. [Data warehouse](https://www.oracle.com/br/database/what-is-a-data-warehouse/)

   
   1. Um **data warehouse** é um tipo de sistema de [gerenciamento de dados](https://www.oracle.com/br/database/what-is-data-management/) projetado para ativar e fornecer suporte às atividades de business intelligence (BI), especialmente a análise avançada. Os data warehouses destinam-se exclusivamente a realizar consultas e análises avançadas e geralmente contêm grandes quantidades de dados históricos. Os dados em um data warehouse geralmente são derivados de uma ampla variedade de fontes, como arquivos de log de aplicativos e aplicativos de transações.
   2. Tem como principal vantagem a facilidade e liberdade para criação de novas análises.
   3. Uma desvantagem porém é um o custo elevado para funcionamento visto que exige processar todas as "*queries*" executando as buscas, transformações, uniões e outros processos definidos pelas mesmas.
2. **“Tabelas calculadas"**

   
   1. O uso de tabelas calculadas aproxima-se um pouco dos chamadas [OLAP Cubes](https://www.ibm.com/docs/en/spss-statistics/saas?topic=features-olap-cubes). Todavia a as tabelas calculadas não precisam, necessariamente, permitir ao usuário realizar processos de “Drill down" ou “Drill up" nos dados apresentados.
   2. O baixo custo para a consulta das informações apresenta-se como a principal vantagem desse formato.
   3. A dificuldade para gerar novas análises, ou permitir apenas análises mais limitadas sem permitir a exploração aprofundada porém é uma de suas desvantagens.
   4. E por depender de um processo de criação dessa tabela, análises em “*real-time*" tornam-se inviáveis.
3. [Query Engine](https://trino.io/)

   
   1. Uma query engine, tem como objetivo permitir buscas simultâneas em múltiplas fontes de dados.
   2. Pode ser vista como um complemento as formas apresentadas anteriormente, uma vez que a ferramenta permite realizar consultas no data warehouse, nas tabelas calculadas, no data lake e outras fontes de dados necessários.

### [Apache Hive](https://hive.apache.org/) (Data warehouse)

O serviço de data warehouse pode ser oferecido ao utilizar a ferramenta [Apache Hive](https://hive.apache.org/), que é open-source e criada para ser capaz de lidar com grandes quantidades de dados e dados distribuídos utilizando para isso a linguagem SQL.

### "Tabelas Calculadas”

A criação das tabelas calculadas depende de um levantamento de requisitos claro, para que a informação disponibilizada seja precisa e útil.

### [Trino (query engine)](https://trino.io/)

Trino é uma ferramenta criada com objetivo de conectar múltiplas fontes de dados como Bancos de dados, data lakes, arquivos locais e etc utilizando um ou mais dos seus [conectores](https://trino.io/ecosystem/index.html). O acesso a informação coletada pode ser feita através do [cliente JDBC](https://trino.io/docs/current/client/jdbc.html)  ou via [REST API](https://trino.io/docs/current/develop/client-protocol.html).

### [Reverse ETL](https://docs.getdbt.com/terms/reverse-etl)

O ETL reverso é o processo de transferir seus dados transformados armazenados no seu armazém de dados para plataformas de negócios finais, como CRMs de vendas e plataformas de anúncios. Uma vez em uma plataforma final, esses dados são frequentemente usados para impulsionar ações comerciais significativas, como a criação de públicos personalizados em plataformas de anúncios, personalização de campanhas de email ou complementação de dados em um CRM de vendas. Você também pode ouvir falar sobre ETL reverso sendo referido como análise operacional ou ativação de dados.

## 5. Visualização dos dados

Para visualização dos dados gerados, além do uso programático via Trino, podemos integrar diversas ferramentas de criação de dashboards como por exemplo: [Metabase](https://trino.io/episodes/44.html), [Power Bi](https://learn.microsoft.com/pt-br/power-query/connectors/azure-hdinsight-on-aks-trino), [Qlik](https://help.qlik.com/en-US/connectors/Subsystems/ODBC_connector_help/Content/Connectors_ODBC/Presto/Create-Presto-connection.htm) entre outros.