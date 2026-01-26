# POC - Questionário de Definição de Escopo

> Use este documento para preencher e definir o escopo de uma POC de Observabilidade.

---

## 1) Escopo & Objetivos

Marque os objetivos da POC:

- [ ] Reduzir MTTR
- [ ] Observabilidade fim‑a‑fim
- [ ] K8s/RKE2 visibilidade
- [ ] Logs centralizados
- [ ] Traces distribuídos
- [ ] RUM (experiência real do usuário)
- [ ] Synthetic (uptime/fluxos)
- [ ] Segurança de aplicações (runtime)
- [ ] FinOps (custo por serviço)
- [ ] Migração de ferramentas

### Aplicações/serviços críticos (até 3)

1. _
2. _
3. _

### SLAs principais

Ex.: 99,9% uptime; latência p95 ≤ ___ ms

**SLAs:** _

---

## 2) Ambientes & Plataformas

### Ambientes

- [ ] Prod
- [ ] Hom
- [ ] Dev
- [ ] QA
- [ ] DR

### Kubernetes (se aplicável)

- [ ] RKE2
- [ ] EKS
- [ ] AKS
- [ ] GKE
- [ ] OpenShift
- [ ] k3s
- [ ] Outro: __

### Cluster sizing

- **# Clusters:** 
- **# Nodes (aprox):** 
- **Namespaces críticos:** _

### Hosts/VMs (aprox)

- **Linux:**  (distro: __)
- **Windows:** 
- **AIX/Outros:** 

### Bancos/filas

- [ ] PostgreSQL
- [ ] MySQL
- [ ] SQL Server
- [ ] Oracle
- [ ] Redis
- [ ] Kafka
- [ ] RabbitMQ
- [ ] Elastic
- [ ] Outros: __

---

## 3) Volumetria Rápida (Estimativas)

### Logs

- **Logs:**  GB/dia
- **Retenção desejada:**  dias

### Tráfego e traces

- **Tráfego app:**  req/s pico
- **Serviços com traces:** 

### RUM

- **RUM (web/mobile):**  sessões/mês

### Synthetic

- **Synthetic:**  checks (HTTP/API/Browser)
- **Locais:**
  - [ ] Global
  - [ ] Brasil
  - [ ] Private

### Métricas

- **Métricas:**  séries Prometheus (se houver)
- **Scrape interval:**  s

> Se não tiver números exatos, informe aproximações por aplicação/ambiente.

### Observações adicionais

__

__

__