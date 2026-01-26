# OPA

## O que é OPA e Gatekeeper?

O **Open Policy Agent (OPA)** é um mecanismo de política de código aberto e de uso geral que permite unificar a aplicação de políticas em diferentes tecnologias.

Você pode usar o OPA para aplicar políticas em microserviços, pipelines de CI/CD, gateways de API e muito mais.

O **Gatekeeper** é um projeto que integra o OPA com o Kubernetes. Ele fornece um webhook de controle de admissão que impõe políticas em objetos do Kubernetes à medida que são criados, atualizados ou excluídos. 

## Por que usar OPA para Gerenciamento de Políticas?

Em um ambiente de Kubernetes, especialmente ao usar Helm para gerenciar aplicações, é crucial garantir que as implantações sigam as melhores práticas e as políticas de segurança da sua organização. O OPA, através do Gatekeeper, permite que você defina e aplique essas políticas de forma centralizada e declarativa.

Alguns exemplos de políticas que você pode aplicar:

* **Segurança:** Exigir que todos os contêineres rodem com um usuário não-root.
* **Consistência:** Garantir que todos os recursos tenham os rótulos (labels) necessários.
* **Boas Práticas:** Impedir o uso da tag `latest` em imagens de contêiner.
* **Governança:** Restringir a criação de `LoadBalancer` services a namespaces específicos.

## Benefícios do Uso do OPA

* **Prevenção de Erros:** Evita que configurações incorretas ou inseguras sejam aplicadas ao cluster.
* **Segurança Aprimorada:** Aplica políticas de segurança de forma consistente em todo o cluster.
* **Governança Centralizada:** Gerencia todas as políticas de um local central.
* **Flexibilidade:** As políticas são escritas em Rego, uma linguagem de consulta de alto nível que oferece grande flexibilidade.
* **Integração com o Ecossistema Kubernetes:** O Gatekeeper é um projeto nativo do Kubernetes, o que garante uma integração perfeita.

## Passos de Instalação usando Helm

A maneira mais fácil de instalar o OPA Gatekeeper é usando o Helm.


1. **Adicione o repositório do Gatekeeper:**

   ```bash
   helm repo add gatekeeper https://open-policy-agent.github.io/gatekeeper/charts
   ```
2. **Atualize o repositório:**

   ```bash
   helm repo update
   ```
3. **Instale o Gatekeeper:**

   ```bash
   helm install gatekeeper gatekeeper/gatekeeper --namespace gatekeeper-system --create-namespace
   ```

## Exemplo de uma Política

Aqui está um exemplo de uma política que exige que todos os namespaces tenham um rótulo `owner`.


1. **Crie um** `ConstraintTemplate`:

   ```yaml
   apiVersion: templates.gatekeeper.sh/v1
   kind: ConstraintTemplate
   metadata:
     name: k8srequiredlabels
   spec:
     crd:
       spec:
         names:
           kind: K8sRequiredLabels
         validation:
           openAPIV3Schema:
             type: object
             properties:
               labels:
                 type: array
                 items:
                   type: string
     targets:
       - target: admission.k8s.gatekeeper.sh
         rego: |
           package k8srequiredlabels
   
           violation[{"msg": msg, "details": {"missing_labels": missing}}] {
             provided := {label | input.review.object.metadata.labels[label]}
             required := {label | label := input.parameters.labels[_]}
             missing := required - provided
             count(missing) > 0
             msg := sprintf("you must provide labels: %v", [missing])
           }
   ```
2. **Crie uma** `Constraint`:

   ```yaml
   apiVersion: constraints.gatekeeper.sh/v1beta1
   kind: K8sRequiredLabels
   metadata:
     name: ns-must-have-owner
   spec:
     match:
       kinds:
         - apiGroups: [""]
           kinds: ["Namespace"]
     parameters:
       labels: ["owner"]
   ```

## Políticas atuais

### 1. Restringir Registro de Imagens

Esta política garante que apenas imagens do repositório `harbor.zello.space` possam ser implantadas.

**ConstraintTemplate:** `policies/imageregistry_template.yaml` **Constraint:** `policies/imageregistry_constraint.yaml`

### 2. Limitar Réplicas do HPA

Esta política impõe um limite máximo de 10 réplicas para os `HorizontalPodAutoscalers`.

**ConstraintTemplate:** `policies/hpa_max_replicas_template.yaml` **Constraint:** `policies/hpa_max_replicas_constraint.yaml`

### 3. Exigir Resource Requests

Esta política exige que todos os contêineres em um Pod tenham `requests` de CPU e memória definidos.

**ConstraintTemplate:** `policies/resource_requests_template.yaml` **Constraint:** `policies/resource_requests_constraint.yaml`

### 4. Política para Limites de Recursos Maiores que Solicitações

Esta política garante que os limites de recursos (CPU e memória) de um contêiner sejam sempre maiores ou iguais às suas solicitações.

**ConstraintTemplate:** `policies/resource_limits_greater_than_requests_template.yaml` **Constraint:** `policies/resource_limits_greater_than_requests_constraint.yaml`

### 5. Política de Proporção entre Limites e Solicitações de Recursos

Esta política garante que os limites de recursos (CPU e memória) de um contêiner não excedam as solicitações em mais de 30%.

**ConstraintTemplate:** `policies/resource_requests_limit_ratio_template.yaml` **Constraint:** `policies/resource_requests_limit_ratio_constraint.yaml`

### 6. Política para Exigir Labels Específicos

Esta política garante que todos os `Pods` tenham os labels `owner` e `app` especificados.

**ConstraintTemplate:** `policies/k8srequiredlabels_template.yaml` **Constraint:** `policies/k8srequiredlabels_constraint.yaml`

### 7. Política para Proibir a Tag `latest` em Imagens

Esta política impede que contêineres sejam implantados usando imagens com a tag `:latest`.

**ConstraintTemplate:** `policies/k8snotlatesttag_template.yaml` **Constraint:** `policies/k8snotlatesttag_constraint.yaml`

### 8. Política para Exigir Liveness e Readiness Probes

Esta política exige que todos os contêineres definam `livenessProbe` e `readinessProbe`.

**ConstraintTemplate:** `policies/k8srequiredprobes_template.yaml` **Constraint:** `policies/k8srequiredprobes_constraint.yaml`

### 9. Política para Restringir Contêineres Privilegiados

Esta política proíbe a execução de contêineres com privilégios de root.

**ConstraintTemplate:** `policies/k8sdisallowedprivilegedcontainers_template.yaml` **Constraint:** `policies/k8sdisallowedprivilegedcontainers_constraint.yaml`

\
**Se precisar sair do padrão definido de deploy, favor entrar em contato com o nível 2 de atendimento.**