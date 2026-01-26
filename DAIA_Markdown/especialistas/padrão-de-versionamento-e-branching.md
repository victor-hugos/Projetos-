# Padrão de Versionamento e Branching

Este documento descreve o padrão de versionamento de software e a estratégia de branching a ser utilizada em nossos projetos, com o objetivo de manter um processo de desenvolvimento ágil, seguro e baseado em entrega contínua.

## 1. Versionamento Semântico (Semantic Versioning)

Adotamos o [Versionamento Semântico 2.0.0](https://semver.org/lang/pt-BR/). Todas as nossas versões seguirão o formato `MAJOR.MINOR.PATCH`.

* **MAJOR:** Para mudanças incompatíveis (breaking changes).
* **MINOR:** Para novas funcionalidades retrocompatíveis.
* **PATCH:** Para correções de bugs retrocompatíveis.

## 2. Estratégia de Branching: Deploy a partir da Feature Branch

Utilizamos um fluxo onde o artefato de software é gerado a partir de uma `feature branch` e promovido entre os ambientes. As branches principais (`main` e `develop`) são atualizadas *após* a validação e o deploy em produção.

### Branches Principais

* `main`: Espelha o código que está em **produção**. É uma branch de longa duração.
* `develop`: Branch de **integração** para as funcionalidades que já foram para produção. Também é de longa duração.

### Branches de Suporte

#### a. Branches de Funcionalidade (`feature/*`)

* **Propósito:** Desenvolver novas funcionalidades de forma isolada.
* **Origem:** Criadas a partir da `develop`.
* **Convenção:** `feature/<nome-da-funcionalidade>`.

#### b. Branches de Correção (`hotfix/*`)

* **Propósito:** Aplicar correções críticas em produção.
* **Origem:** Criadas a partir da `main`.
* **Convenção:** `hotfix/<descricao-do-bug>`.
* **Nota:** São branches de curta duração para correções rápidas (resolvidas em poucas horas). Não deve haver mais de uma branch de `hotfix` ativa em paralelo.

## 3. Fluxo de Deploy e Promoção de Artefato

O nosso processo de CI/CD é centrado na promoção do mesmo artefato (build) entre os ambientes, garantindo que o que foi testado é exatamente o que vai para produção. O fluxo se aplica tanto para `features` quanto para `hotfixes`.


1. **Criação da Tag e Deploy em Homologação (HLG):**
   * Ao final do desenvolvimento (seja em uma branch `feature/*` ou `hotfix/*`), uma **tag de versão** é criada diretamente na branch.
     * Para features: `v1.2.0`
     * Para hotfixes: `v1.1.1`
   * Esta tag aciona a esteira de CI/CD, que gera o artefato e o implanta no ambiente de **Homologação (HLG)**.
2. **Validação e Promoção para Produção (PRD):**
   * A equipe de QA e o Product Owner validam a mudança em HLG.
   * Se aprovada, a **mesma tag (e o mesmo artefato)** é usada para acionar o deploy para o ambiente de **Produção (PRD)**.
3. **Sincronização Pós-Deploy:**
   * **Somente após o deploy em produção ser bem-sucedido**, a branch de origem (`feature/*` ou `hotfix/*`) é mesclada (merged) nas branches principais.
     * `feature/*` é mesclada na `develop` e depois na `main`.
     * `hotfix/*` é mesclada na `main` e depois na `develop`.
   * Este passo garante que as branches principais reflitam o código exato que está em produção.
4. **Limpeza:**
   * Após o merge, a branch de origem (`feature/*` ou `hotfix/*`) **DEVE ser deletada**.

## 4. Resumo do Fluxo

### Cenário 1: Nova Funcionalidade (Feature)

```
# 1. Criação e desenvolvimento da feature
git checkout develop
git pull
git checkout -b feature/nova-api-pagamentos

# ... desenvolvimento ...

# 2. Criação da tag para gerar o build e implantar em HLG
git tag v1.2.0
git push origin v1.2.0  # Esteira de CI/CD faz o deploy em HLG

# ... testes e validação em HLG ...

# 3. Se aprovado, promover o mesmo build para PRD
# (Ação feita na ferramenta de CI/CD, promovendo o artefato da tag v1.2.0)

# 4. Após o deploy em PRD, sincronizar as branches
git checkout develop
git merge --no-ff feature/nova-api-pagamentos
git push

git checkout main
git merge --no-ff feature/nova-api-pagamentos
git push

# 5. Limpeza da branch
git branch -d feature/nova-api-pagamentos
git push origin --delete feature/nova-api-pagamentos
```

### Cenário 2: Correção Crítica (Hotfix)

```
# 1. Criação da branch de hotfix a partir da main
git checkout main
git pull
git checkout -b hotfix/correcao-login-nullpointer

# ... aplicação da correção ...

# 2. Criação da tag para gerar o build e implantar em HLG
git tag v1.1.1
git push origin v1.1.1  # Esteira de CI/CD faz o deploy em HLG

# ... testes e validação em HLG ...

# 3. Se aprovado, promover o mesmo build para PRD
# (Ação feita na ferramenta de CI/CD, promovendo o artefato da tag v1.1.1)

# 4. Após o deploy em PRD, sincronizar as branches
git checkout main
git merge --no-ff hotfix/correcao-login-nullpointer
git push

# A develop também precisa receber a correção
git checkout develop
git merge --no-ff hotfix/correcao-login-nullpointer
git push

# 5. Limpeza da branch
git branch -d hotfix/correcao-login-nullpointer
git push origin --delete hotfix/correcao-login-nullpointer
```

## 5. Diagramas de Fluxo

### Cenário 1: Nova Funcionalidade (Feature)

 ![](/api/attachments.redirect?id=2adb79cb-4f2b-4844-9949-8a7d58aa67ed " =1000x389")

### Cenário 2: Correção Crítica (Hotfix)

 ![](/api/attachments.redirect?id=a48c70dc-ea0f-43cf-87aa-161738b7b241 " =958x409")