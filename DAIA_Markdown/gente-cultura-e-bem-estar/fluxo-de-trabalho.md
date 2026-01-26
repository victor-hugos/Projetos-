# Fluxo de Trabalho

O fluxo de trabalho elaborado atende as especificações mínimas de um processo simplificado de desenvolvimento de software.

Abaixo, estão representadas todas as situações possíveis para os itens de trabalho, bem como suas conexões e transições possíveis dentro do fluxo.

 ![Figura 1: diagrama de fluxo de trabalho](/api/attachments.redirect?id=01e88aaa-c130-4dbc-b533-35d3bc3eb63d)

As situações presentes no diagrama estão classificadas em três categorias distintas que visam representar de maneira macro as situações dos itens:


1. **Itens pendentes:** representados pela cor cinza;
2. **Itens em andamento:** representados pela cor azul;
3. **Itens concluídos:** representados pela cor verde.

Descrevemos de forma sucinta as situações para alinhamento dos conceitos:

* **Backlog:** itens que ainda estão por fazer, ou seja, ainda não tiveram o trabalho iniciado;
* **Em andamento:** itens que estejam sendo trabalhados, ou seja, o trabalho sobre eles já foi iniciado;
* **Pronto para QA:** itens que tenham sido concluídos e estejam aptos para avaliação do processo de qualidade;
* **QA em andamento:** itens que estejam sendo avaliados no processo de qualidade;
* **Pronto para homologar:** itens que tenham sido avaliados positivamente no processo de qualidade;
* **Em homologação:** itens que estejam sendo homologados pelo cliente;
* **Homologado:** itens homologados pelo cliente.
* **Impedido:** itens que estejam impedidos devido a alguma situação adversa e que não podem ser concluídos enquanto não foram removidos os ofensores;
* **Recusado:** Itens que tenham falhado no processo de qualidade **ou** que tenham sido recusados pelo cliente durante a homologação.

O fluxo de movimentação dos itens de trabalho é intuitivo e autoexplicativo. Ao mover um item de trabalho, ficam disponíveis apenas as colunas de origem/destino possíveis de acordo com o diagrama acima. Note que a cadeia de valor do quadro possui as mesmas situações do diagrama:

 ![Figura 2: possibildades de movimentação dos itens de trabalho](/api/attachments.redirect?id=21bbc3dd-d47b-47f9-a826-97537569232a)


:::tip
Caso tenha alguma dúvida sobre para onde mover o item, consulte o diagrama acima. :wink:

:::


:::warning
É de extrema importância que **TODOS** os itens de trabalho estejam atualizados e relação à sua situação. A situação do item é determinante para geração de relatórios íntegros e de indicadores que são monitorados, portanto, para evitar o recebimento de alertas indevidos ou descumprimento dos níveis de serviço, **mantenha atenção à manutenção do status de seus itens de trabalho**.

:::

Também é possível mover o card acessando-o diretamente, ou seja, ao invés de arrastá-lo pelo quadro, ao clicar sobre o item é possível acessá-lo diretamente e alterar a situação. Da mesma forma demonstrada no exemplo anterior, ficarão disponíveis somente as situações possíveis de origem/destino de acordo com o diagrama acima. Ao selecionar a nova situação, o card será movido para a coluna correspondente no quadro.

 ![Figura 3: possibilidades de movimentação dos itens de trabalho](/api/attachments.redirect?id=f3836a90-7af3-4e2c-b681-8cf940c24618)

## Exceções

Apesar de utilizarmos um fluxo simplificado de desenvolvimento de software, aproveitando-se de algumas características do ALM Jira, o processo sofreu algumas alterações para representar de maneira fiel a rotina de trabalho na Zello. Para tanto, existem duas exceções no fluxo de trabalho que auxiliam para a manutenção real do progresso dos itens de trabalho.

* **Fluxo de impedimentos;**
* **Fluxo de conclusão.**

Ambas estarão descritas nos tópicos subsequentes.