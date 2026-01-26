# Anatomia de um Prompt

Este guia foi pensado para ajudar qualquer pessoa a estruturar prompts claros, objetivos e reutilizáveis em qualquer contexto. Um bom prompt segue uma **anatomia lógica**, composta por diferentes partes que orientam a IA a entregar resultados mais consistentes.


---

## 1. 🎯 Função

Defina **o papel que a IA deve assumir**. Isso dá contexto e guia o comportamento esperado.

**Exemplo:**

* "Atue como um professor especializado em história medieval."
* "Você é um consultor financeiro focado em investimentos de longo prazo."


---

## 2. 📝 Tarefa

Explique de forma clara **o que a IA precisa fazer**. Use instruções específicas, divididas em tópicos quando necessário.

**Exemplo:**

* "Liste os principais eventos da Idade Média."
* "Crie um plano de investimentos para alguém com perfil conservador."


---

## 3. 🗂️ Contexto

Forneça **informações adicionais, restrições ou critérios** que a IA deve considerar para ajustar a resposta.

**Exemplo:**

* "Considere apenas eventos da Europa Ocidental."
* "Exclua opções de alto risco como criptomoedas."


---

## 4. 🔍 Raciocínio

Instrua a IA a **verificar, cruzar informações ou justificar** seu processo de resposta. Isso ajuda a melhorar a precisão e confiabilidade.

**Exemplo:**

* "Explique por que esses eventos foram marcantes."
* "Compare as opções apresentadas com dados reais de mercado."


---

## 5. 📊 Formato de Saída

Defina **como você deseja receber a resposta**. Isso garante clareza e padronização.

**Exemplo:**

* "Organize os eventos em uma linha do tempo em Markdown."
* "Apresente o plano de investimentos em uma tabela com colunas: Ativo | Risco | Retorno estimado."


---

## 6. ✅ Condições Finais

Estabeleça **quando a tarefa estará concluída**. Isso ajuda a IA a entender o critério de sucesso.

**Exemplo:**

* "A tarefa estará concluída quando forem listados ao menos 5 eventos com explicações de 2 a 3 frases cada."
* "O plano de investimentos deve conter pelo menos 3 opções validadas e justificadas."


---

# 🚀 Estrutura Genérica de Prompt

\
Aqui está um **modelo reutilizável**:

\
**Função:** Atue como \[papel desejado\].

**Tarefa:** \[Explique o que precisa ser feito, em etapas ou tópicos\].

**Contexto:** \[Inclua restrições, critérios e informações adicionais\].

**Raciocínio:** \[Peça verificação, comparação, validação ou explicação\].

**Formato de Saída:** \[Defina se quer lista, tabela, resumo, etc.\].

**Condições Finais:** \[Defina o que marca a conclusão da tarefa\].

\

---

# 📌 Exemplo Prático

\
**Função:** Atue como um guia de viagens especializado em recomendar trilhas ao ar livre menos conhecidas e exclusivas a até duas horas de São Francisco.

**Tarefa:**

* Comece com uma lista de verificação concisa (3–7 tópicos) dos passos que você seguirá para concluir essa tarefa, focando no planejamento conceitual em vez de detalhes.
* Identifique e apresente as 3 melhores trilhas de comprimento médio (não entre as mais populares) e até duas horas de carro de São Francisco.
* Garanta que cada trilha selecionada ofereça uma aventura única devido à sua paisagem, isolamento ou qualidades distintas.
* Exclua trilhas extremamente populares como Mount Tam, Golden Gate Park, Presidio e outras atrações principais da área de São Francisco.

**Contexto:**

* Priorize precisão: os nomes das trilhas devem corresponder às listas oficiais (ex.: AllTrails) e todas as estimativas de tempo e distância devem ser realistas e confiáveis.
* Destaque, de forma concisa, o que torna cada trilha uma aventura excepcional.

**Raciocínio:**

* Verifique internamente todas as trilhas sugeridas para garantir que sejam reais, pouco conhecidas e que se encaixem nos parâmetros especificados antes de responder.
* Cruze os nomes e detalhes das trilhas com fontes confiáveis de informações sobre atividades ao ar livre.
* Otimize para clareza, apresentação concisa e valor prático.

**Formato de Saída:** Apresente os resultados como **tabela formatada em Markdown** com as seguintes colunas:

```
| Nome da trilha | Endereço | Distância (km) | Tempo estimado | Resumo |
|----------------|----------|----------------|----------------|--------|
| [Trilha 1]     | [Endereço] | XX | X:XX | [Resumo] |
| [Trilha 2]     | [Endereço] | XX | X:XX | [Resumo] |
| [Trilha 3]     | [Endereço] | XX | X:XX | [Resumo] |
```

**Condições Finais:**

* A tarefa estará concluída quando três trilhas verificadas, únicas e de comprimento médio, excluindo opções populares, forem retornadas no formato especificado, e a validação confirmar o total cumprimento de todos os requisitos.

\
\
