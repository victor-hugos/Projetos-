# Fluxo de Impedimentos

Os Impedimentos, representados pela situação “Impedido” do fluxo de trabalho, são nada mais que as **situações adversas,** que de acordo com a **Diretriz para o Gerenciamento do Processo de Ordem de Serviço** são:

> Eventos, incidentes ou problemas recorrentes cuja existência tendem a impactar no prazo, escopo, custo ou na qualidade das entregas \[…\]

Conforme já descrito no tópico [“Criação da Estrutura“](https://portal.zello.space/doc/criacao-da-estrutura-GDQZYJ2f3P#h-criando-uma-estrutura), os impedimentos geram itens de trabalho do tipo **“Ofensor“**. Esses por sua vez devem ser utilizados para o registro da situação adversa (**sim, no singular**), conforme descrito no tópico deste item de trabalho.

No fluxo de trabalho, **a criação deste item de trabalho ocorre de maneira automática**, bastando para tanto, mover um item para a coluna “Impedido“.

 ![Figura 1: movendo para Impedido para criação do ofensor](/api/attachments.redirect?id=7a166ad2-e804-4ca8-acb9-9289cf24b032)

Ao mover o item para “Impedido“, uma tela será exibida para o preenchimento dos campos necessários para a criação do Ofensor:

* **Motivo do Bloqueio:** Neste campo, deverá ser especificado o motivo do impedimento em relação ao item de origem. 
* **Natureza do Bloqueio:** Este campo deverá identificar se o bloqueio é causado pelo cliente ou pelo processo interno de trabalho;
* **Expectativa de desbloqueio:** Data em que se espera que o bloqueio seja removido, visando não impactar o prazo limite do item de origem;

 ![Figura 2: campos necessários para criação do Ofensor](/api/attachments.redirect?id=7fcbd77b-b569-46e3-a8a0-37fcc5e46791)

Prrenchidos esses campos, o item de origem irá repousar na coluna “Impedido“. Note que o item de origem foi comentado e que um item de trabalho do tipo Ofensor foi vinculado a ele.

 ![Figura 3: ofensor vinculado ao item de origem e comentários incluidos automaticamente](/api/attachments.redirect?id=8c118672-d16d-46e4-8764-0932090d2e10)

Este mesmo item que foi criado, consta agora do backlog do projeto, devendo ser incluído na mesma sprint do item de origem para que possa percorrer o mesmo fluxo dos demais itens de trabalho.

 ![Figura 4: ofensor criado automaticamente incluído no backlog do projeto](/api/attachments.redirect?id=4c38eee3-cf98-4348-b3e4-0547a036b739)

Uma vez incluído na sprint, o ofensor também ficará disponível para gestão visual através do quadro.

 ![Figura 5: ofensor incluído na sprint ativa para gestão pelo quadro](/api/attachments.redirect?id=0185d536-e697-4911-ac56-1d54147e8f99)

Ao percorrer o fluxo até sua conclusão, o item de origem que ora repousa na coluna “Impedido“, de maneira automática, será colocado novamente em andamento. Um novo comentário será adicionado informando da movimentação para que o responsável pela atividade seja notificado e tenha ciência de que o seu impedimento foi resolvido e que agora sua atividade poderá ser continuada.

 ![Figura 6: item de origem "Em andamento" e notificações inseridas automaticamente](/api/attachments.redirect?id=d3ae0613-1aff-469f-9eb8-09f588f4b060)


:::tip
Caso esse item tenha um novo impedimento, basta mover para “Impedido“ novamente, e um novo ofensor será criado! :wink:

:::

\
