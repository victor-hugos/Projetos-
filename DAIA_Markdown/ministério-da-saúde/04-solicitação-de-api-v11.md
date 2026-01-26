# 04-Solicitação de API-v1.1

**SUMÁRIO**

[1 Quais são os sistemas e tecnologias específicas que serão fornecidos pela Contratada além do WMS e TMS? 2](#_Toc140147480)

[1.1 Tecnologia Web (Navegabilidade): 2](#_Toc140147481)

[1.2 Padrões de desenvolvimento (Interface – Web) 3](#_Toc140147482)

[1.3 Linguagem de programação 3](#_Toc140147483)

[1.4 Arquitetura de Desenvolvimento/implementação 4](#_Toc140147484)

[1.5 Aplication Program Interface 4](#_Toc140147485)

[2 Quais são os principais requisitos de segurança de dados que devem ser atendidos? 4](#_Toc140147486)

[3 Existem regulamentos específicos que devem ser seguidos em relação ao armazenamento e processamento de dados? 5](#_Toc140147487)

[4 Como será garantida a confidencialidade dos dados do MS? 6](#_Toc140147488)

[5 Haverá a necessidade de integração com sistemas ou plataformas existentes do MS? 6](#_Toc140147489)

[6 Requisitos de disponibilidade e tempo de resposta para os sistemas fornecidos? 6](#_Toc140147490)

[7 É necessário fornecer treinamento e suporte técnico para o uso adequado dos sistemas? 6](#_Toc140147491)

[8 Como serão realizadas as atualizações de software e manutenção dos sistemas? 6](#_Toc140147492)

[9 Existe a necessidade de implementar medidas de backup e recuperação de dados? 7](#_Toc140147493)

[10 Diretrizes de acesso e controle de privilégios de usuário para os sistemas fornecidos? 7](#_Toc140147494)

[12 Há alguma exigência específica em relação à infraestrutura tecnológica, como servidores, redes, dispositivos móveis, etc.? 7](#_Toc140147495)

[13 Quais são as garantias e prazos para atualização, manutenção e suporte técnico dos sistemas e softwares utilizados? 7](#_Toc140147496)

[14 É necessário que a contratada possua certificações ou comprovações de qualificação técnica na área de tecnologia? 7](#_Toc140147497)

[15 Como será feito o acompanhamento e controle da qualidade dos serviços tecnológicos prestados pela contratada? 8](#_Toc140147498)

**Considerações Gerais**

**Cenário 1**

\- Aquisição de solução com a perspectiva de atendimento ao máximo dos requisitos;

Nota:

-   Vai entregar o código fonte (Entrega da solução);
    -   Existe a possibilidade internalização (DATASUS);
-   Em caso de finalização do contrato (Entregar banco de dados – populado “Com todos os dados da operação);
-   Quem será o guarda do Storage (Armazenamento + hospedagem );
-   A solução estará em Cloud ( Nuvem ) ?

**SOLICITAÇÃO DE API**

## 1 Quais são os sistemas e tecnologias específicas que serão fornecidos pela Contratada além do WMS e TMS?

-   Possui integração com ERP (Gestão Financeira)
-   Pode ser solicitado módulo financeiro para gestão de dados

Informações básicas de controle da ERP:

-   Informações relacionadas ao pedido;
-   Informações de registro do ingresso da mercadoria, na maioria das vezes nesta fase são gerados os registros os códigos do SKU e a atualização do inventário;
-   Recebimento do pedido, faturamento e registro;
-   Registro da saída da mercadoria e atualização do inventário;

Para o caso da inexistência da integração com ERP, o processo WMS e TMS deve ser considerado módulo com características de ERP.

## 1.1 Tecnologia Web (Navegabilidade):

O Sistema a ser desenvolvida utilizando padrões que contenham recursos específicos da World Wide WEB compatíveis com as principais formas de acessibilidade disponibilizadas na infraestrutura, tais como:

-   Pluralidade de navegação, ou seja, compatível com os principais navegadores disponíveis no mercado:
    -   Microsoft EDGE;
    -   Google Chrome;
    -   Firefox (Monzila Firefox);
    -   Safari;
    -   Opera;
    -   Samsung Internet Browser.
    -   Dentre outros

\

**Nota técnica:**

-   Considerando aspectos de navegabilidade, os sistemas devem ser construídos prevendo a utilização em dispositivos móveis, obedecendo as regras de usabilidade, recursividade de forma responsíva.
-   Verificar a perspectiva de implementação dos requisitos funcionais para a acessibilidade web para portadores de deficiência visual.
    

## 1.2 Padrões de desenvolvimento (Interface – Web)

Os padrões de desenvolvimento podem adotar referências técnicas como as da [https://www.w3c.br/Padroes/](https://www.w3c.br/Padroes/), ou seja, desta forma as especificações que utilizarem Hypertext Markup Language – HTML e Cascading Style Sheets – CSS estarão aderentes as especificações relacionadas aos requisitos de implementação de solução;

**Nota:**

Caso não seja utilizado padrão w3c a empresa deve informar quais os padrões foram utilizados.

## 1.3 Linguagem de programação

Desde que utilizados padrões Web no desenvolvimento da solução, será considerada a infraestrutura e o potencial de internalização da tecnologia do Departamento de informática do Sistema Único de Saúde do Brasil – DATASUS.

**Nota:**

Verificar com o DATAUS recursos de infraestrutura para internalização de Sistemas;

**SUGESTÃO DE DESENVOLVIMENTO:**

\- Java;

\- JavaScript (Deve ser considerada a utilização de Frameworks como Angular, React, Vue JS;

\- TypeScript;

\- Asp.net;

\- PHP (Desde que atualizados os requisitos de segurança)

\- Python;

Definir linguagem / _Descobrir qual a linguagem de programação do Site VTC_

**Nota técnica:**

A ordem com que foi descrito as sugestões de desenvolvimento não espelham necessariamente os critérios de preferência.

## 1.4 Arquitetura de Desenvolvimento/implementação

Considerando que o Sistema seja construído para WEB deve-se comprovar no padrões de arquitetura do tipo Model, View e Controller – MVC, ou seja, Manipulação dos dados, interação com usuário e camada de controler.

Nota:

Caso não seja utilizada arquitetura MVC a contratada deve apresentar a arquitetura que foi utilizada para desenvolvimento do sistema.

## 1.5 Aplication Program Interface

Implementação dos padrões de programação visando a integração entre aplicações através do compartilhamento de informações.

Em relação a demanda de API segue a relação das principais API’s de mercado:

\- Swagger API;

\- Google Drive;

\- API Gateway;

\- Akita API;

\- Bugsnag;

\- Checly ( Deve ser considero os padrões de segurança da API);

\- Datadog;

\- Moesif;

\- New Relic API;

\- Postmam;

\- Rapid API;

\- SeNTRY API;

\- Swagger API;

\- Watson ( Usa inteligência artificial);

\- Dropbox;

\- Amatino (Fornece dados financeiros);

Nota:

Anexo I - Relação das principais APIS de acesso no Governo Federal

Observação: Devem ser definidos quais os dados de quais processos estarão na API

## 2 Quais são os principais requisitos de segurança de dados que devem ser atendidos?

Os critérios de segurança que deverão ser implementados leva em consideração os aspectos de Storage (Armazenamento), podendo este ser em ambiente do cliente ou interno.

Infraestrutura:

\- Direct Attached Storage ( DAS );

\- Network Attached Storage ( NAS);

\- Storage Érea Network ( SAN ).

**ASPECTOS DE ACESSO A APLICAÇÃO:**

\-Escalonamento de perfil de usuário;

\-Modelagem de banco de dados considerando criação e disponibilização das views em banco de dados;

\- Criptografia dos dados;

\- O modelo de banco de dados deve utilizar definições de procedures;

\- Análise funcional de caracteres especiais em formulários do FrontEnd;

\- Controle de acesso de aplicação;

\- Análise e criptografia dos dados de perfis e autenticação;

\- Protocolo HPPTS incluindo certificado de acesso;

\- Aplicação em Cloud (Nuvem) para o caso da definição onde será a hospedagem do Sistema;

\- Implementação de CAPTHCHA evitando a implementação de robôs;

\- Dados criptografados das strings de conexão com banco de dados;

\- Dados criptografados das configurações de Web.config se for o caso;

\- Segurança nos processos de indexação (Evitando sites de buscas e Crawler);

\- Infraestrutura de padronização de autenticação com padrões pré-definidos;

\- Níveis de validação e segurança de download de fontes e dados diversos;

\- Implementação dos termos de confidencialidade nos cadastros de usuários

Nota:

A relação acima é apenas uma demonstração dos aspectos utilizado em certificação digital, sejam eles através de certificado e/ou fluxo de processo

## 3 Existem regulamentos específicos que devem ser seguidos em relação ao armazenamento e processamento de dados?

\- Lei Nº 13.709, de 14 de agosto de 2018 ( [https://www.planalto.gov.br/ccivil\_03/\_ato2015-2018/2018/lei/l13709.htm](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) )

Além da LGPD os padrões podem ser considerados os seguintes padrões:

\- ISO 27001 – Gerenciamento da Segurança da Informação;

\- ISO 27033-3 – Segurança em Rede de Computadores;

\- ISO 27033-4 – Comunicação segura entre rede e Gateways;

\- ISO 27036 – Segurança da Informação no relacionamento com fornecedores

\- ISO 27039 – IDS (Intrusion Detection Systems) – IPS ( Instrusion Prevention SYSTEMS

-   IDS – Sistema de Detecção de intrusão;
-   IPS – Sistema de Prevenção de intrusão;

## 4 Como será garantida a confidencialidade dos dados do MS?

Termo de confidencialidade associado aos requisitos de adesão a LGPD

## 5 Haverá a necessidade de integração com sistemas ou plataformas existentes do MS?

DATASUS

# 6 Quais são os requisitos de disponibilidade e tempo de resposta para os sistemas fornecidos?

Poderão ser implementados indicadores de SLA e ou de KPIs. Os principais são:

Service Levei Agreement - SLA

-   Tempo Médio de Atendimento (TMA)
-   Tempo Médio de Espera (TME)
-   Tempo da Primeira Resposta
-   Desempenho do Colaborador
-   Taxa de Resolução no Primeiro Contato
-   Taxa de Abandono
-   Tickets de Suporte Resolvidos
-   Customers Satisfaction Score (CSAT)
-   Net Promoter Score (NPS)

\

# 7 É necessário fornecer treinamento e suporte técnico para o uso adequado dos sistemas?

\- Será necessário o fornecimento de treinamento;

\- Manual do usuário incluído as atualizações de Sistema;

\- Vídeos de treinamento incluindo todas funcionalidades do Sistema ( EAD );

# 8 Como serão realizadas as atualizações de software e manutenção dos sistemas?

Em caso da solução (Sistema) for desenvolvida com tecnologia WEB, será necessária a disponibilização de Ambiente de homologação, antes da entrada da versão em produção. Nesta fase deverão ser atualizadas toda e qualquer instrução técnica de utilização do Sistema

Atualização deve ser dinâmica com controle de versão

# 9 Existe a necessidade de implementar medidas de backup e recuperação de dados?

As rotinas de backup’s deversão ser criadas a partir da infraestrutura de armazenamento podendo ser nas dependências do cliente ou em infraestrutura interna do DataSUS;

# 10 Quais são as diretrizes de acesso e controle de privilégios de usuário para os sistemas fornecidos?

Conforme perfis de acesso do sistema levando em consideração os termos de confidencialidade; os perfis de administração deverão ser monitorados promovendo a geração de logs de _acesso de todos os perfis, sendo possível a exportação de dados para auditoria;_

11 Quais são as principais funcionalidades e recursos tecnológicos necessários para o cumprimento das atividades contratadas?

Explorar a partir das funcionalidades da VTC e dos usuários atualmente.

# 12 Há alguma exigência específica em relação à infraestrutura tecnológica, como servidores, redes, dispositivos móveis, etc.?

Depende de onde será instalado o Sistema.

# 13 Quais são as garantias e prazos para atualização, manutenção e suporte técnico dos sistemas e softwares utilizados?

Ver os itens de implementação das SLA’s conforme item 6

# 14 É necessário que a contratada possua certificações ou comprovações de qualificação técnica na área de tecnologia?

Cenário 1:

Em caso de aquisição de Software pode-se verificar se a empresa que desenvolveu o Sistema possui certificação que seja referência no processo de desenvolvimento de Software como por exemplo:

-   MPS.BR;
-   CMMI;
-   ISO 9001:2015;
-   ISO/IEC 12207 – Processo de Ciclo de vida de Software;
-   ISO/IEC 15504 – Software Process Improvement and Capability Determination;
-   ISSO/ 9126 – Qualidade de produto de Software;

Cenário 2: Em caso de desenvolvimento da solução pode-se verificar se os profissionais possuem certificações com as descritas abaixo:

-   Certificação ITIL;
-   Certificação CISSP;
-   Oracle Certified Professional Advanced PL/SQL;
-   Oracle Cloud;
-   Certificação DELL EMC;
-   VMware VCP-Cloud;
-   Certificações MCSD;
-   CCIE;
-   Certificação PMP;
-   AWS Certified Solutions Architect – Associate;
-   Certified in the Governance of Enterprise IT (CGEIT);
-   Certificações de Teste de Software
    -   CTFL Foundation Level;
    -   CTFL Agile Tester;
    -   CTFL Model Based Test. 
    -   CTAL-TTA (Technical Test Analyst);
    -   CTAL-TA (Test Analyst);
    -   CTAL-TM (Test Manager);
    -   CTEL-ST (Security Testing);
    -   CTEL-TA (Test Automation).

Nota:

As certificações que serão proposta devem estar alinhadas com os recurso de infraestrutura do DATASUS

# 15 Como será feito o acompanhamento e controle da qualidade dos serviços tecnológicos prestados pela contratada?

-   Poderá ser contratada auditoria de terceiros.
-   Ou fiscais de contrato;
-   Próprio Ministério;

ANEXO I

1.  **_Sistema Único de Saúde (SUS) API_** - A API do SUS permite acessar informações sobre pacientes, prontuários médicos, medicamentos e procedimentos médicos disponíveis no sistema de saúde público. Isso pode ser útil para verificar a disponibilidade de medicamentos, obter informações de prescrições médicas e atualizar registros de pacientes.
2.  **_Agência Nacional de Vigilância Sanitária (ANVISA) API_** \- A ANVISA disponibiliza APIs que permitem verificar informações sobre registros de medicamentos, normas e regulamentos relacionados à saúde. Isso pode ajudar a garantir a conformidade e a qualidade dos medicamentos e insumos utilizados no sistema de saúde.
3.  **_Sistema de Informação Hospitalar (SIH) API -_** A API do SIH pode ser utilizada para acessar dados relacionados aos serviços hospitalares, como informações sobre leitos disponíveis, procedimentos realizados, taxas de ocupação hospitalar e estatísticas sobre internações. Essas informações podem ser úteis para planejar a distribuição de suprimentos médicos e alocar recursos de forma mais eficiente.
4.  **_Sistema Nacional de Gerenciamento de Produtos Controlados (SNGPC) API -_** Se houver necessidade de controle de medicamentos controlados, a API do SNGPC pode ser útil para acessar informações sobre a movimentação, estoque e venda desses medicamentos. Isso pode auxiliar na gestão e rastreabilidade desses produtos no WMS.
5.  **_Receita Federal API: -_** A Receita Federal disponibiliza APIs que permitem acessar informações relacionadas a empresas, como dados cadastrais, situação fiscal, certidões negativas, consulta de CNPJ, entre outros. Essas informações podem ser úteis para verificar a validade de fornecedores e realizar processos de verificação e cadastro de empresas.
6.  **_Instituto Nacional do Seguro Social (INSS) API -_** A API do INSS pode ser usada para obter informações sobre benefícios previdenciários, como aposentadorias e pensões. Esses dados podem ser relevantes para verificar a elegibilidade de pacientes e obter informações sobre o histórico de atendimento médico.
7.  **_Ministério da Economia - Sistema Integrado de Administração Financeira (SIAFI) API -_** O SIAFI API possibilita o acesso a informações financeiras, como pagamentos, empenhos, despesas e receitas do governo federal. Integrar essa API pode ser útil para acompanhar os processos de pagamento, orçamento e controle financeiro relacionados aos suprimentos médicos.
8.  **_Sistema Único de Saúde (SUS) API_** - A API do SUS permite acessar informações sobre pacientes, prontuários médicos, medicamentos e procedimentos médicos disponíveis no sistema de saúde público. Isso pode ser útil para verificar a disponibilidade de medicamentos, obter informações de prescrições médicas e atualizar registros de pacientes.
9.  **_Agência Nacional de Vigilância Sanitária (ANVISA) API -_** A ANVISA disponibiliza APIs que permitem verificar informações sobre registros de medicamentos, normas e regulamentos relacionados à saúde. Isso pode ajudar a garantir a conformidade e a qualidade dos medicamentos e insumos utilizados no sistema de saúde.
10.  **_Instituto Brasileiro de Geografia e Estatística (IBGE) API -_** O IBGE disponibiliza APIs para acessar dados estatísticos sobre a população, como informações demográficas, indicadores socioeconômicos, dados do Censo, entre outros. Esses dados podem ser utilizados para análises e projeções de demanda, auxiliando no planejamento de estoque e distribuição de suprimentos.
11.  **_Caixa Econômica Federal API -_** A Caixa Econômica Federal oferece APIs para acesso a informações sobre benefícios sociais, programas de transferência de renda, como o Bolsa Família, FGTS, entre outros. Integrar essa API pode ajudar a verificar a elegibilidade dos pacientes e acessar informações relevantes para a gestão de serviços sociais.
12.  **_Portal Brasileiro de Dados Abertos (dados.gov.br) API -_** O dados.gov.br é um portal que reúne diversas bases de dados públicos, disponibilizando APIs para acessá-los. Essa plataforma oferece uma ampla gama de informações sobre diversos setores, incluindo saúde, economia, educação, entre outros. Integrar essa API pode fornecer acesso a dados relevantes para análises de planejamento e tomada de decisões.
13.  **_Instituto de Pesquisa Econômica Aplicada (IPEA) API -_** O IPEA oferece APIs para acesso a dados e estudos econômicos, sociais e ambientais. Essas informações podem ser úteis para análises de impacto econômico, projeções de demanda e avaliação de políticas públicas relacionadas à saúde.
14.  **_Sistema de Informações Gerenciais de Projetos (SIGProj) API -_** O SIGProj é um sistema utilizado para gestão de projetos do governo federal. Sua API permite acessar informações sobre projetos em andamento, como cronogramas, recursos alocados, metas e indicadores de desempenho. Integrar essa API pode ajudar no planejamento de projetos relacionados à logística de suprimentos médicos e otimização dos recursos.
15.  **_Sistema de Informações para o Controle da Administração Pública (SICAP) API -_** O SICAP API disponibiliza informações sobre contratos, licitações, convênios e outros processos de contratação do governo federal. Integrar essa API pode ser útil para acompanhar contratos de fornecedores, monitorar prazos e garantir a conformidade dos processos de aquisição.
16.  **_API dos Correios -_** A API dos Correios permite rastrear pacotes, calcular preços e prazos de entrega, obter informações sobre serviços postais, como Sedex e PAC, e gerar etiquetas de envio. Essa API é essencial para integração com o sistema de logística do WMS, garantindo a rastreabilidade e controle dos produtos durante o processo de transporte.
17.  **_API do Instituto Nacional de Metrologia, Qualidade e Tecnologia (INMETRO)_** \- A API do INMETRO pode ser utilizada para acessar informações sobre a certificação, conformidade e qualidade de produtos. Isso pode ser útil para garantir que os insumos e medicamentos atendam aos padrões de qualidade e segurança exigidos.
18.  **_API do Sistema de Informações de Movimentação de Produtos (SIMP) -_** O SIMP é um sistema que permite o controle e rastreamento de movimentação de produtos químicos no Brasil. Sua API pode ser útil para rastrear a movimentação de produtos químicos utilizados em insumos médicos e garantir a conformidade com as regulamentações e normas de segurança.
19.  **_API do Sistema Nacional de Informações Tóxico-Farmacológicas (SINITOX) -_** O SINITOX é um sistema que registra informações sobre intoxicações e envenenamentos. Sua API pode ser utilizada para acessar dados sobre produtos tóxicos e informações relevantes para a gestão de estoques, como precauções de manuseio e armazenamento.
20.  **_API do Ministério da Agricultura, Pecuária e Abastecimento (MAPA) -_** O MAPA disponibiliza APIs relacionadas à fiscalização agropecuária, como informações sobre registros de estabelecimentos de produtos de origem animal, certificados de produtos agrícolas e informações sobre inspeções sanitárias. Essas APIs podem ser úteis para a gestão de suprimentos médicos relacionados à saúde animal e produtos agrícolas utilizados na saúde pública.
21.  **_API do e-SIC (Sistema Eletrônico do Serviço de Informações ao Cidadão) -_** O e-SIC é um sistema utilizado para gerenciar as solicitações de acesso à informação. Sua API pode ser utilizada para integrar funcionalidades de acesso à informação, como envio e acompanhamento de solicitações, diretamente no WMS corporativo.
22.  **_API do e-CAC (Centro Virtual de Atendimento ao Contribuinte) -_** O e-CAC é um sistema utilizado pela Receita Federal para disponibilizar serviços e informações relacionadas à área fiscal. Sua API pode ser útil para acessar informações tributárias, validar informações de contribuintes e facilitar processos relacionados à fiscalização e impostos.
23.  **_API do Cadastro Nacional de Empresas Inidôneas e Suspensas (CEIS) -_** O CEIS é um cadastro que reúne informações sobre empresas declaradas inidôneas ou suspensas pela administração pública. Sua API pode ser útil para verificar a regularidade de fornecedores e evitar transações com empresas com histórico de irregularidades.
24.  **_API do Cadastro Nacional de Condenações Cíveis por Ato de Improbidade Administrativa (CNIA) -_** O CNIA é um cadastro que registra condenações cíveis por atos de improbidade administrativa. Sua API pode ser utilizada para verificar a idoneidade de empresas e pessoas físicas envolvidas em processos de contratação pública.
25.  **_API do Painel de Preços -_** O Painel de Preços é uma plataforma que permite consultar e comparar preços de referência de produtos e serviços contratados pelo governo federal. Sua API pode ser utilizada para obter informações sobre os preços praticados em compras públicas, auxiliando na avaliação de propostas e na negociação de contratos.
26.  **_API do Banco Nacional de Itens (BNI) -_** O BNI é uma base de dados que reúne informações sobre itens padronizados, utilizados em processos de aquisição pública. Sua API pode ser útil para obter informações sobre especificações técnicas de produtos, facilitando a pesquisa e seleção de itens a serem adquiridos.
27.  **_API do Sistema Eletrônico de Informações (SEI) -_** O SEI é um sistema utilizado para gerenciar documentos e processos administrativos no âmbito governamental. Sua API pode ser utilizada para integração com o WMS corporativo, permitindo o acesso e gerenciamento de documentos relacionados a processos de compras e contratações.
28.  **_API do Sistema de Cadastramento Unificado de Fornecedores (SICAF) -_** O SICAF é um sistema utilizado para cadastrar e habilitar fornecedores para participarem de processos de licitação no governo federal. Sua API pode ser utilizada para consultar informações sobre fornecedores cadastrados, verificar a regularidade fiscal e habilitação técnica.
29.  **_API do Portal de Compras Governamentais -_** O Portal de Compras Governamentais é uma plataforma que reúne informações sobre compras públicas realizadas por diferentes órgãos e entidades governamentais. Sua API pode ser utilizada para obter informações sobre editais de licitação, contratos, fornecedores e demais dados relacionados às compras governamentais.
30.  **_Outros_**

_Fonte: Boletim Informativo sobre Tecnologia – TechTips_

_Anderson Luis Oliveira e Silva_

[_anderson@iloca.com.br_](mailto:anderson@iloca.com.br)