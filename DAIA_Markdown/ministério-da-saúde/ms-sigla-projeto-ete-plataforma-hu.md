# MS Sigla Projeto ETE Plataforma HU

Esse artefato se trata de um arquivo .DOCX, portanto estará disponível para download no link a seguir:

\
<https://gitlab.zello.services/clientes/ms/documentacao/templates/-/blob/main/Sprint%20Design/SIGLAPROJETO_SIGLAMODULO_ETE_Web_NomeHU.docx>

\
\
**Especificação Técnica**

*\[Nome da História do Usuário\]*

|    |
|----|
| **Instruções de preenchimento do documento** |
| Este documento deverá seguir as seguintes considerações de preenchimento:\n\n-   **Nomenclatura:** Abreviar a sigla do módulo caso seja grande/ Web: Adequar de acordo com a HU\n\nExemplo: MS_ConectaSUS_ETE_Android_ExportarCertificadoVacinacaoCovid\n\n-   **Fonte:** Arial\n-   **Tamanho:** 10\n-   **Cor:** Preta\n-   **Sigla e nome do Projeto:** Caixa Alta\n-   **\[ ... \]:** Retirar os *colchetes* ao transcrever o texto\n-   Quando algum item não for aplicado a este documento informar a sigla “N/A”\n-   Pendente:\n\n- Verificar com MS possibilidade de evoluir a HU das funcionalidades, a cada necessidade de alterar a mesma transação, alterar a HU existente da transação para que seja possível ter uma única HU com todas as informações da transação. Após a primeira versão aprovada, as demais seriam enviadas com controle de alteração do Word para que seja possível visualizar os pontos de alteração relacionados a OS, podemos colocar como padrão as inclusões marcadas em azul e exclusões marcadas em ~~vermelho tachado~~.\n\n- Verificar como tratar transação em manutenção: especificar somente o que irá afetar a transação em manutenção e referenciar caso exista os documentos existentes no item Informações Complementares desse documento.\n\n-   *Após o preenchimento do documento, este quadro deverá ser excluído.* |

\

|    |
|----|
| **\[SIGLA\] – \[NOME DO PROJETO\]** |
| **Gestor do Projeto** |
| *\[Nome\]* |
| *[\[E-mail\]](mailto:jessica.costa@saude.gov.br)* |
| *\[Telefone\]* |

\

|    |    |    |    |    |
|----|----|----|----|----|
| **Histórico de Revisão** |    |    |    |    |
| **Data** | **Versão** | **Nº Ordem de Serviço** | **Descrição** | **Autor** |
| *\[dd/mm/aaaa\]* | *\[x.x\]* | *\[#0000000\]* | *\[Descrição do motivo da atualização\]* | *\[Nome do autor\]* |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |
|    |    |    |    |    |

**Especificação Técnica**


1. História de Usuário

*\[Descreva aqui o resumo da história do usuário: Quem?/ O que?/ Por quê?\]*

\

1. Perfil/ Persona

   
   1. \[Nome do perfil que executa a transação\]
   2. \[Regra de perfil da transação em anexo\]
2. Protótipo

Como demonstrar: \[Passo a passo para acesso da transação. Exemplo: Autenticar-se na plataforma

> Balcão de Oportunidades no menu à esquerda\]

\[P1\] – *\[Nome da tela\]*

*\[Adicionar a imagem do protótipo equivalente a HU\]*

*\[Adicionar todas as telas da HU identificando como P1, P2 e etc\]*

* \
  
  1. Descrição do Protótipo

|    |    |    |    |    |    |    |    |    |    |
|----|----|----|----|----|----|----|----|----|----|
| **Nome** | **Descrição** | **Preenc.** | **Tipo** | **Tam.** | **Domínio** | **Obrig.** | **Edit.** | **C.A.** | **Máscara** |
| ***\[P1\] – Nome Protótipo*** |    |    |    |    |    |    |    |    |    |
| *\[Data\]* | *\[descrição do campo\]* | *\[AFN\]* | *\[TXT\]* | *\[9\]* | *\[ - X*\n\n_- y \]_ | *\[S\]* | *\[S\]* | *\[C.1\]* | *DD/MM/AAAA*\n*HH:MM:SS*\n*(99) 9 9999-9999*\n\n_9XXXX_ |
| *\[Idade\]* | *\[idade\]* | *\[NUM\]* | *\[TXT\]* | *\[9\]* | *\[9\]* | *\[N\]* | *\[N\]* | *\[C.1\]* | *N/A* |
| *\[Cidade\]* | *\[cidade\]* | *\[AFN\]* | *\[TXT\]* | *\[9\]* | *N/A* | *\[N\]* | *\[N\]* | *\[C.1\]* | *N/A* |
| ***\[P2\] – Nome Protótipo*** |    |    |    |    |    |    |    |    |    |
| *\[Data\]* | *\[descrição do campo\]* | *\[AFN\]* | *\[TXT\]* | *\[9\]* | *\[9\]* | *\[S\]* | *\[S\]* | *\[C.1\]* | *(99) 9 9999-9999* |
|    |    |    |    |    |    |    |    |    |    |

Legenda

Tipo: TXT=Text, TXA=Text Área, CKB=Check Box, CBB=Combobox, SLM=Seleção Múltipla, RBT=Radiobutton, BT=Botão, TBL=Tabela, LNK=Link, URL=URL, M=Imagem, AC=Autocomplete N/A=Não se aplica.

Preenchimento: ALF=Alfa, AFN=Alfanumérico, ASC=Alfanumérico sem caracteres especiais, NUM=Numérico, N/A=Não se aplica.

\
* \
  
  1. Regras de Interface

     
     1. \[RI001: Regras de Interface da transação. Ex.: Os botões X, Y e Z devem estar desabilitados ao carregar a tela.\]


1. Critérios de Aceite

*\[Adicione aqui o(s) critério(s) de aceitação da especificação técnica e as referências às regras de negócio/ mensagens utilizando o processo BDD (Desenvolvimento Guiado por Comportamento):*

**Dado:** *Define quais são as pré-condições verdadeiras para executar o teste*

**Quando:** *Define a ação que será executada no sistema*

**Então:** *Seguindo a ação descrita no* QUANDO *define o resultado esperado*

*A palavra chave E pode ser usada para adicionar sentenças positivas no Dado, no Quando ou no Então*

*Utilizar sempre verbo nas ações “Ex: acionar, selecionar deverá”*

*Descrever cenários da transação de sucesso, alternativos e exceções\]*

*Exemplo:*

* \
  
  1. \[C.1\] Consultar Programas: Específicos do Concedente e de Emendas Parlamentares direcionados para minha instituição

***Dado*** *que desejo consultar os programas Específicos do Concedente e de Emendas Parlamentares direcionados para minha instituição*

***Quando*** *acionar a opção “Balcão de Oportunidades”*

***Então*** *o sistema deverá apresentar o total de programas direcionados para minha instituição* ***RN001***

* \
  
  1. \[C.2\] Consultar total de programas/chamamentos direcionados para minha instituição

***Dado*** *que desejo consultar os programas/chamamentos direcionados para minha instituição*

***Quando*** *acionar a opção “Balcão de Oportunidades”*

***Então*** *o sistema deverá apresentar o total de programas/chamamentos direcionados* ***RN002***

* \
  
  1. \[C.3\] Filtrar resultados

***Dado*** *que desejo consultar os programas e chamamentos direcionados para minha instituição*

***Quando*** *acionar a opção “Balcão de Oportunidades”*

***E*** *aplicar os filtros existentes*

***Então*** *o sistema deverá apresentar a lista de resultados conforme os filtros aplicados* ***RI001***


1. Mensagens específicas

   
   1. \[MSG001\] - XXXX
   2. \[MSG002\] - XXXX
2. Regras de negócio

   
   1. \[RN001\] - XXXX
   2. \[RN002\] - XXXX
3. Informações Complementares

   
   1. \[Informações da transação que não se aplicam aos itens acima.\]
4. Anexos

   
   1. \[Anexos. Ex.: Comunicação, Protótipo\]

\
