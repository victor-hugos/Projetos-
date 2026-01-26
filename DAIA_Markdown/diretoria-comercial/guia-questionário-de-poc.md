# GUIA - Questionário de POC

> Objetivo deste documento: explicar **cada item** do formulário de POC de Observabilidade, o que significa, **quando marcar**, e dar **exemplos** de preenchimento.


---

## 1) Escopo & Objetivos

Esta seção define o **porquê** da POC e quais capacidades precisam ser provadas.

### ✅ Reduzir MTTR

* **MTTR (Mean Time To Repair/Resolve)** = tempo médio entre identificar um incidente e restaurar o serviço.
* Marque se a prioridade é **diagnosticar rápido** e **corrigir mais rápido**.
* Normalmente implica:
  * Alertas com menos ruído (reduzir falsos positivos)
  * Correlação de **logs + métricas + traces**
  * Dashboards orientados a **SLO/SLA**

**Exemplo:** “Hoje um incidente demora 2h para achar a causa. Queremos cair para 20min.”


---

### ✅ Observabilidade fim-a-fim

* É enxergar a jornada completa: **usuário → gateway → serviços → banco → filas → dependências externas**.
* Marque se você precisa correlacionar tudo na mesma investigação.
* Normalmente envolve:
  * APM/tracing distribuído
  * Logs correlacionados (com trace_id / request_id)
  * Métricas e SLOs
  * (Opcional) RUM

**Exemplo:** “Checkout está lento; quero ver qual serviço e qual query geraram a latência.”


---

### ✅ K8s/RKE2 visibilidade

* Visibilidade do **Kubernetes** (no caso, **RKE2**):
  * saúde de **pods/nodes**, eventos (OOMKilled, CrashLoopBackOff), throttling
  * deployments/replicas, HPA, consumo por namespace
  * DNS, rede, storage, etc.
* Marque se suas dores são “o app está ruim, mas é infra do cluster?”.

**Exemplo:** “Quero detectar quando um namespace está sofrendo CPU throttling.”


---

### ✅ Logs centralizados

* Unificar logs de apps/infra em um lugar para:
  * buscar e filtrar rápido
  * padronizar retenção
  * investigar incidentes sem “entrar em pod/VM”
* Marque se hoje os logs estão espalhados (pods, VMs, ferramentas diferentes).

**Exemplo:** “Quero fazer uma busca única e achar o erro do request em toda a cadeia.”


---

### ✅ Traces distribuídos

* Rastrear uma requisição atravessando múltiplos serviços (spans) e ver:
  * tempo gasto por etapa
  * dependências (HTTP, DB, filas)
  * erros com contexto
* Marque se você tem microserviços ou cadeia de chamadas longa.

**Exemplo:** “O endpoint leva 800ms; quero ver que 600ms foi no serviço X e 200ms no DB.”


---

### ✅ RUM (experiência real do usuário)

* **Real User Monitoring** mede a experiência real no navegador/app:
  * LCP/CLS/TTFB (web), erros JS, performance por região/dispositivo
* Marque se você quer entender percepção do usuário (não só backend).

**Exemplo:** “Backend ok, mas usuários no 4G reclamam; quero ver LCP e falhas por ISP.”


---

### ✅ Synthetic (uptime/fluxos)

* Testes automatizados (monitores) que simulam acesso:
  * **HTTP/API checks** (barato, simples)
  * **Browser journeys** (mais realista, mais caro): login → carrinho → pagamento
* Marque se você quer detectar falhas **antes** do usuário.

**Exemplo:** “Rodar a cada 1 minuto um check de login e checkout; se falhar, alertar.”


---

### ✅ Segurança de aplicações (runtime)

* Segurança em tempo de execução (às vezes RASP/Runtime Protection):
  * detecção de ataques (SQLi, RCE, SSRF)
  * sinais de abuso/anomalia
  * contexto de incidente junto do trace
* Marque se a POC também precisa validar observabilidade + segurança.

**Exemplo:** “Alertar tentativas de SQL injection com contexto do request e serviço.”


---

### ✅ FinOps (custo por serviço)

* Medir e atribuir custo por:
  * serviço, namespace, time, ambiente
* Marque se você quer **showback/chargeback** e eficiência.

**Exemplo:** “Quanto custa o checkout-service por 1.000 requests?”


---

### ✅ Migração de ferramentas

* Comparação lado-a-lado com solução atual (ELK, Prometheus+Grafana, etc.).
* Marque se a POC precisa provar:
  * paridade de dashboards/alertas
  * facilidade de operação
  * custo/benefício

**Exemplo:** “Migrar do ELK para uma plataforma integrada e validar equivalência.”


---

### Aplicações/serviços críticos (até 3)

Escolha os alvos do piloto. Critérios típicos:

* maior impacto no negócio
* maior volume
* mais incidentes
* cadeia de dependências relevante (bom para validar tracing)

**Exemplos:**


1. `api-gateway` / `bff`
2. `checkout-service`
3. `payments-service`


---

### SLAs principais

Defina as metas que a observabilidade precisa suportar.

* **Uptime**: ex. 99,9% (impacta disponibilidade)
* **Latência p95**: 95% das requisições abaixo de X ms
* **Taxa de erro**: ex. 5xx < 0,5%

**Exemplos:**

* “99,9% uptime do checkout”
* “Latência p95 do checkout ≤ 300ms”
* “Erro 5xx < 0,5%”


---

## 2) Ambientes & Plataformas

Esta seção define **onde** a POC vai rodar e quais componentes entram.

### Ambientes: Prod / Hom / Dev / QA / DR

* **Prod**: sinal real, melhor para incidentes e RUM, exige mais cuidado.
* **Hom**: excelente para validar instrumentação com menos risco.
* **Dev/QA**: útil para iterar rápido e ajustar integração.
* **DR**: se existir ambiente de contingência.

**Dica de POC:** Hom + (Prod parcial) costuma ser um bom equilíbrio.


---

### Kubernetes (se aplicável)

Marque o tipo do cluster (RKE2/EKS/AKS/GKE/OpenShift/k3s/outro). Isso impacta:

* modo de instalação do agente/collector (Helm/DaemonSet/Operator)
* integrações de métricas do cluster
* permissões e restrições (OpenShift costuma ser mais restrito)


---

### # Clusters / # Nodes / Namespaces críticos

* **# Clusters**: quantos clusters serão observados.
* **# Nodes**: tamanho aproximado (impacta agentes e custo).
* **Namespaces críticos**: onde ficam as apps alvo.

**Exemplo:**

* \
  # Clusters: 2 (prod/hom)
* \
  # Nodes: 40 (30 prod + 10 hom)
* Namespaces críticos: `gateway`, `checkout`, `payments`


---

### Hosts/VMs (aprox)

Se existir workload fora do K8s (VMs/bare metal), informe:

* Linux (e distro) — ex. Ubuntu, RHEL, Rocky, Amazon Linux
* Windows — ex. IIS/serviços legados
* AIX/Outros — ambientes específicos

**Exemplo:** Linux 20 (Ubuntu 22.04) | Windows 10 | AIX 0


---

### Bancos/filas

Marque os sistemas que fazem parte do caminho crítico e que você quer observar (métricas, logs e/ou traces).

**Sinais típicos por tecnologia:**

* **PostgreSQL/MySQL/SQL Server/Oracle**: conexões, locks, slow queries, replica lag
* **Redis**: hit rate, latência, memória, evictions
* **Kafka**: consumer lag, throughput, under-replicated partitions
* **RabbitMQ**: filas crescendo, consumidores lentos, redeliveries
* **Elastic**: latência de busca/indexação, uso de heap


---

## 3) Volumetria Rápida (Estimativas)

Serve para dimensionar a POC (infra, custo e retenção). Pode ser **aproximado**.

### Logs: GB/dia + retenção (dias)

* Volume diário total de logs (apps + infra) e por quanto tempo guardar.
* Impacta principalmente armazenamento e custo.

**Exemplo:** 60 GB/dia | retenção 14 dias.

**Como estimar rápido:**

* usar tamanho de índices diários se já existe ELK
* medir 1 serviço por hora e extrapolar


---

### Tráfego app: req/s pico + serviços com traces

* **req/s pico**: pico de tráfego (não a média).
* **serviços com traces**: quantos serviços serão instrumentados.

**Exemplo:** 1.200 req/s pico | 8 serviços com tracing.


---

### RUM: sessões/mês

* Sessões reais de usuários (web/mobile). Muitas ferramentas cobram por sessão.

**Exemplo:** 1,8M sessões/mês (web) + 0,5M (mobile).


---

### Synthetic: checks + locais

* Quantos monitores (HTTP/API/Browser) e de onde rodam:
  * **Global**: múltiplas regiões
  * **Brasil**: foco BR
  * **Private**: rodando dentro da sua rede (para endpoints internos)

**Exemplo:** 15 checks HTTP + 2 browser journeys | locais: Brasil + Private.


---

### Métricas: séries Prometheus + scrape interval

* **Séries** = cardinalidade (número de combinações de labels). É o que mais explode custo/perf.
* **Scrape interval**: 15s/30s/60s… (mais curto = mais detalhado = mais volume).

**Exemplo:** 1,2M séries | scrape 30s.


---

### Observações adicionais

Use este campo para restrições e contexto que mudam o desenho da POC:

* LGPD/PCI (mascarar dados em logs)
* restrições de rede (sem egress para SaaS)
* multi-tenant / separação por time
* janelas de mudança / freeze
* particularidades de instrumentação (OpenTelemetry, libs, etc.)

\
