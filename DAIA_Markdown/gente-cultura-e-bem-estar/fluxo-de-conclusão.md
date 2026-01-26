# Fluxo de Conclusão

Foi implementado no fluxo de trabalho algumas validações relacionadas à conclusão dos itens.

## Vínculo de Bloqueio ou Predecessão

A primeira validação diz respeito à existências de itens com vínculo do tipo “Bloqueio“. Caso existam ofensores ou outros itens de trabalho vinculados à um card com o vínculo do tipo bloqueio, o ALM Jira não permitirá que o item seja concluído.

 ![Figura 1: concluindo um item com itens vinculados não resolvidos](/api/attachments.redirect?id=973813aa-48e9-4aba-b601-9d9c0e1c95af)

No exemplo acima, o item de trabalho possui um ofensor vinculado que não está concluído. 

Existe no entanto, a possibilidade de que um item seja vinculado a outro por predecessão, ou seja, alguma atividade mapeada como predecessora precisa ser concluída antes da atual.

 ![Figura 2: exemplo de dependência entre atividades no roteiro avançado](/api/attachments.redirect?id=6a16c95d-bb0e-44c7-a78d-a2ceccb0e75c)

 ![Figura 3: exemplo de dependência entre atividades na visualização do item](/api/attachments.redirect?id=9ec840ec-4cbe-49a5-8a6b-4b43b0b6e796)

No caso da tentativa de conclusão de um item que esteja bloqueado por uma atividade predecessora, o ALM Jira não permitirá que o item seja concluído.

 ![Figura 4: exemplo de item bloqueado por atividade predecessora](/api/attachments.redirect?id=2ef41ff9-f990-4f26-878f-cfb04f36604f)

## Concluindo itens “Pai“ pela conclusão dos itens “Filhos“

Ainda relacionada à conclusão dos itens associados, temos a conclusão automática do item “pai” vinculada à conclusão dos itens “filhos“.

No exemplo a seguir, observe que resta apenas um item da “Funcioanalidade 1“ em andamento:

 ![Figura 5: exemplo de itens "filhos" concluídos](/api/attachments.redirect?id=6d37c684-fa74-462c-9a27-02eb8d5dd283)

Ao concluir o item restante, o ALM Jira possibilitará que o item “Pai“ seja concluído automaticamente, desde que seja permitido pelo usuário.


:::info
Pode ser que não se queira concluir o item “Pai“ devido a possibilidade de inclusão de novos itens. Por isso a conclusão do item “Pai“ é opcional.

:::

 ![Figura 6: concluindo o item "Pai" a partir da conclusão dos itens "filhos"](/api/attachments.redirect?id=679baca9-58a7-4835-9cce-efd6352344cd)

Notem portanto, que essas validações estão presentes no fluxo de trabalho para todos os tipos de itens na hierarquia, portanto ocorrerão desde as subtarefas que estão no menor nível, até os épicos que estão no maior nível.


:::warning
É de extrema importância que **TODOS** os itens de trabalho estejam atualizados e relação à sua situação. A situação do item é determinante para geração de relatórios íntegros e de indicadores que são monitorados, portanto, para evitar o recebimento de alertas indevidos ou descumprimento dos níveis de serviço, **mantenha atenção à manutenção do status de seus itens de trabalho**.

:::

\
