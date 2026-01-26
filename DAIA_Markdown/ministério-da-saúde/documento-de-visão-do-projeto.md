# Documento de visão do projeto

# Por que?

O DLOG adquire todos os anos bilhões de reais em IES (Insumos Estratégicos de Saúde) para abastecimento aos estados e posterior entrega dos insumos na ponta para serem utilizadas no atendimento de pacientes do SUS. Por

Os registros de entrada e saída de insumos não ocorrem em tempo real, ou seja, concomitantemente com a movimentação física dos estoques nos almoxarifados, o que gera retrabalho com diversas conferências e grande possibilidade de erro, já que os inputs de dados são manuais. Observa-se ainda que não há rastreio das ações realizadas, logo não há como indicar os autores das ações. Fora as questões de controle, a parte operacional não é registrada, como as informações sobre tamanho e peso de embalagem, cubagem, endereço de lotes nas prateleiras, entre outros. 

Assim o sistema não permite a criação de novas ferramentas que atendam todas as Coordenações-Gerais deste DLOG. Nesse contexto, a solução tecnológica precisa abranger todas as Coordenações-Gerais, em módulos próprios e integrados. 

> Outro motivador está na exigência feita pelo TCU, pela criação de sistema automatizado que reúna todas essas características e evite a necessidade de ações manuais dos usuários.

\
# Como ?

Implementando uma solução de integração capaz de conectar com os sistemas de origem, e a integração com os sistemas da ponta, permitindo ao usuário acompanhar toda a movimentação do insumo sem sair do sistema.\n

# O que?

Criar uma solução tecnológica de logística e uma infraestrutura para integração de dados (barramento), como a da Rede Nacional de Dados em Saúde - RNDS, de modo a prover: 

* um fluxo de automação dos processos de gestão da logística relacionados ao planejamento, 
* à aquisição, 
* à armazenagem, 
* ao transporte, 
* à distribuição e 
* ao pagamento dos Insumos Estratégicos para Saúde - IES, 
* visando a otimização administrativa, 
* melhoria das ferramentas de gestão,
*  aumento da publicidade e da transparência dos atos públicos, 
* além da integração com outros subsistemas do Governo Federal e o ambiente do Departamento de Informática do Sistema Único de Saúde - DATASUS.
* Tornar viável uma infraestrutura capaz de promover a interoperabilidade e integração entre sistemas do MS, sistemas estruturantes do Governo Federal, de prestadores de serviços (operadores logísticos de armazenagem e de transporte) e de saúde de estados e municípios.

O Sistema LogSUS será criado com o objetivo de atender as demandas levantadas incluindo, mas não limitadas a:

* A implementação de uma solução tecnológica de logística integrada;
* Gestão física dos estoques; 
* Movimentação e controle das cargas até a dispensação dos IES sob a gestão e a responsabilidade do DLOG. 
* eficiência no acompanhamento dos fluxos, 
* redução de erros, 
* automatização de processos, 
* melhoria do índice de satisfação, 
* padronização de procedimentos, 
* Racionalização de gastos e 
* melhoria gerencial.

\
# Anexos

## **Do Projeto**

O projeto é a criação de uma estrutura transversal que permita ao Ministério da Saúde realizar monitoramento de aquisições de medicamentos e insumos para saúde, bem como planejar o desembaraço, armazenamento e distribuição de tais produtos.

Diante deste cenário, o projeto tem algumas vertentes, que já seguem os apontamentos do Acórdão 313/2023 do TCU que solicita a implementação de um novo SISMAT.

O **SISMAT(Sistema Integrado de Administração de Material)** é uma ferramenta utilizada no âmbito da administração direta do **Ministério da Saúde** para gerenciar o pedido de material de consumo, gestão de almoxarifado e o catálogo único de material de consumo. Alguns pontos relevantes sobre o SISMAT incluem:

**Regulamentação**: A **Portaria Nº 2069 de 30 de outubro de 2003** estabelece as regras para o funcionamento e os procedimentos relacionados ao uso do SISMAT.[ ](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2003/prt2069_30_10_2003.html)__[Essa regulamentação visa otimizar a aquisição e o controle de materiais necessários para a saúde pública](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2003/prt2069_30_10_2003.html)*[1](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2003/prt2069_30_10_2003.html)*__.

**Objetivos**:

**Pedido de Material de Consumo**: O SISMAT permite solicitar materiais de consumo, como medicamentos e dispositivos médicos, de forma padronizada e eficiente.

**Gestão de Almoxarifado**: Facilita o controle do estoque, movimentação e distribuição dos materiais nos almoxarifados.

**__[Catálogo Único](https://www.gov.br/saude/pt-br/composicao/sectics/desid/catmat)__**__[: Mantém uma linguagem única e padronizada de codificação e descrição dos itens a serem adquiridos pelo Governo Federal, atendendo às normas de licitação e contratação](https://www.gov.br/saude/pt-br/composicao/sectics/desid/catmat)*[2](https://www.gov.br/saude/pt-br/composicao/sectics/desid/catmat)*__

**Integração**: O SISMAT deve se integrar com outros sistemas utilizados pelo Ministério da Saúde, garantindo a sincronização de dados e a eficiência operacional.

Em resumo, o SISMAT é uma ferramenta essencial para a gestão eficaz dos materiais necessários à saúde pública, contribuindo para a otimização dos processos logísticos e a transparência nas aquisições.

Outra vertente importante que deve ser atendido no LOGSUS, é a criação de uma rede estruturada de dados de insumos e medicamentos para possibilitar que seja realizada a  logística transversalmente e com interoperabilidade entre os sistemas que compõem o ecossistema, desde a aquisição, desembaraço, armazenamento e distribuição de.

\
## Justificativa

Anualmente, o DLOG adquire em torno dezenas de bilhões de reais em IES e abastece todos os estados da federação, que, por sua vez, entregam os insumos à ponta, em que ocorre a dispensação aos pacientes do Sistema Único de Saúde - SUS. O MS está se preparando para uma mudança significativa de cenário na contratação de IES: de R$ 18.400.787.340,98 (318 contratações, 320 Documentos de Formalização de Demanda - DFDs e 488 itens), em 2023, para R$ 39.640.924.663,36 (461 contratações, 447 DFDs e 795 itens), em 2024. 

Diante desse cenário, urge a implementação de um sistema integrado de logística a partir de 2024. Além do Sistema Eletrônico de Informações - SEI e do Sistema Integrado de Administração Financeira - SIAFI, este Departamento se utiliza do Sistema Integrado de Administração de Material - SISMAT. No entanto, o SISMAT tem arquitetura obsoleta e que não comporta mais atualizações. 

Os registros de entrada e saída de insumos não ocorrem em tempo real, ou seja, concomitantemente com a movimentação física dos estoques nos almoxarifados, o que gera retrabalho com diversas conferências e grande possibilidade de erro, já que os inputs de dados são manuais. Observa-se ainda que não há rastreio das ações realizadas, logo não há como indicar os autores das ações. Fora as questões de controle, a parte operacional não é registrada, como as informações sobre tamanho e peso de embalagem, cubagem, endereço de lotes nas prateleiras, entre outros. 

Assim o sistema não permite a criação de novas ferramentas que atendam todas as Coordenações-Gerais deste DLOG. Nesse contexto, a solução tecnológica precisa abranger todas as Coordenações-Gerais, em módulos próprios e integrados. Por exemplo: 

\
* a Coordenação-Geral de Logística de Insumos Estratégicos para Saúde - CGLOG precisa de um módulo/ferramenta que faça um acompanhamento apurado dos materiais do recebimento até o retorno da expedição ao destinatário final, com todos os documentos que precisam acompanhar os bens entregues; 
* a Coordenação-Geral de Planejamento, Monitoramento e Controle Logístico - CGPLAM, de uma solução que se integre ao módulo da CGLOG e que realize o planejamento das contratações, considerando, inclusive, o que está estocado e o que ainda será recebido, de acordo com os contratos firmados pela CoordenaçãoGeral de Aquisição de Insumos Estratégicos para Saúde - CGIES. 
* A CGIES precisa de uma ferramenta que controle prazos, padronize procedimentos e apresente informações gerenciais sobre as compras. 
* Por fim, a Coordenação-Geral de Execução Orçamentária e Financeira - CGOF, ao realizar pagamentos advindos das execuções contratuais, precisa ter a certeza de que a entrega foi feita e atestada, e que as notas fiscais não serão pagas em duplicidade, entre outros. 

  \

Ademais, a proposta visa atender igualmente às determinações e recomendações emanadas pela Egrégia Corte de Contas, por meio do Acórdão 313/2023-Plenário, tratadas no bojo do processo SEI nº 25000.146573/2021-42, relacionado, conforme transcrito abaixo:

* No prazo de 90 (noventa) dias: 9.3.5. utilização de sistema automatizado de informação em logística, tal como o Silos, eventual sistema desenvolvido de forma específica para as necessidades do MS ou sistemas WMS existentes no mercado, promovendo e documentando a análise de custo-benefício das alternativas possíveis. 
* No prazo de 180 (cento e oitenta) dias: 9.4 (...) que apresente:
  *  plano de ação no prazo de 180 (cento e oitenta) dias, identificando as ações a serem adotadas, 
  * os responsáveis por cada uma delas e prazos para a implementação, com vistas à substituição do Sistema Integrado de Administração de Material – Sismat, seja iniciando processo de aquisição de sistema de gestão de estoque disponível no mercado – WMS (Warehouse Management Systems), ou solicitando ao Datasus o desenvolvimento de novo sistema informatizado, promovendo e documentando a análise de custo-benefício das alternativas possíveis, a fim de corrigir as vulnerabilidades constatadas e permitir funcionalidades que garantam o controle pleno do estoque de maneira independente da empresa de operação logística contratada, a exemplo de: 
    * 9.4.1. integração com os sistemas de WMS das empresas contratadas para operação logística e com os demais sistemas informatizados do MS, inclusive o sistema contábil e o sistema de nota fiscal eletrônica; 
    * 9.4.2. manutenção de registro (log) de todas as inserções e alterações realizadas em informações do sistema; 
    * 9.4.3. controle da regra FEFO (first to expire, first out) com alerta e bloqueio da operação em caso de não atendimento do princípio, a ser analisado pela instância máxima competente; 
    * 9.4.4. controle da proximidade da validade dos IES com envio de alerta regular às áreas demandantes; 
    * 9.4.5. gestão de insumos para descarte, com informações de peso e tamanho das embalagens para permitir a definição quanto ao melhor momento de encaminhar para incineração; 
    * 9.4.6. identificação dos lotes dos insumos com a correspondente localização nas prateleiras do estoque; 
    * 9.4.7. extração de relatórios gerenciais não apenas em formato PDF, que permitam auxiliar no planejamento e otimização das compras e na logística do estoque, tais como relatórios de entrada, saída, consumo médio mensal, medicamentos e insumos próximos do vencimento etc.; 
    * 9.4.8. demais funcionalidades necessárias à gestão de estoque e prevenção de perdas de insumos sem utilização, permitindo que o Ministério da Saúde exerça o controle automatizado dos seus insumos sem depender de sistemas de empresas contratadas.

## Proposta de Solução

Implementando uma solução de integração por uso gerenciado de APIs, conforme as regras de negócios do DLOG e regras técnicas do DATASUS, que sejam capazes de monitorar ou fluxos dos processos, que possam subsidiar atividades de coleta de informações em ambiente interno, bem como de ambientes externos, utilizados pelo Departamento de Logística. Em outros termos, este projeto está relacionado à gestão transversal de vários processos, do planejamento das aquisições à execução orçamentaria e financeira dos contratos firmados pelo MS, incluindo a gestão física dos estoques, bem como a movimentação e controle das cargas até a dispensação dos IES sob a gestão e a responsabilidade do DLOG. A implementação de uma solução tecnológica de logística integrada, no âmbito do DLOG, proporcionará eficiência no acompanhamento dos fluxos, redução de erros, automatização de processos, melhoria do índice de satisfação, padronização de procedimentos, ou seja, um controle mais eficiente e qualificado das atividades desenvolvidas, além de racionalização de gastos e melhoria gerencial. Logo, é de grande urgência e de suma importância, considerando que será possível a emissão de relatórios gerenciais com informações extraídas do banco de dados seguros, que embasarão a tomada de decisões das autoridades competentes do MS, aumentando a eficiência e a economicidade do ciclo logístico dos IES.