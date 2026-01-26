# Criação de cluster kubernetes na Zello

## 1. Pré-requisitos

* Acesso ao Proxmox com permissões de criação de VMs;
* Acesso ao nó master do cluster

## 2. Criar a nova máquina virtual no Proxmox

Passos:


1. Acesse o Proxmox via interface web ou SSH.
2. Clone a VM a partir do template template-k8s.
3. Use a seguinte convenção de nome:

```
k8s-<nome-do-cluster>-<role>-<número>
```

Exemplo:

* k8s-akuma-worker-04
* k8s-akuma-master-02

## 3. Configurações customizadas da VM


1. Ao acessar a máquina execute o arquivo k8s-prepare.sh e preenchar os valores de ip da máquina e nome do host com o padrão do tópico anterior.

```sh
sudo ./k8s-prepare.sh
```

## 4. Fazer o join do cluster perfil Control Plane


1. Execute o seguinte comando em uma máquina master

```sh
sudo kubeadm token create --print-join-command --ttl 30m --control-plane --certificate-key $(sudo kubeadm init phase upload-certs --upload-certs | tail -n1)
```


2. Execute o resultado gerado no novo membro do cluster.

```sh
sudo kubeadm join 192.168.100.32:6443 --token di2o5y.hus2kwoq5pjhzqmy --discovery-token-ca-cert-hash sha256:690a0e77deea3bde44fbdb73195f0a35dbea2a5a83745dda95d25f70f43aeaa9 --control-plane --certificate-key b25fe63ae90ec56a9edff17a8b3e71456ec6f984e814378db035454773e12f40
```

## 5. Fazer o join do cluster perfil Worker


1. Para zerar o comando de join execute o seguinte comando se for worker

```sh
sudo kubeadm token create --print-join-command --ttl 30m
```


2. Execute o resultado gerado no novo membro do cluster.

```sh
sudo kubeadm join 192.168.100.31:6443 --token gfbf2m.tkiv3wrv5vj9yezu --discovery-token-ca-cert-hash sha256:690a0e77deea3bde44fbdb73195f0a35dbea2a5a83745dda95d25f70f43aeaa9
```

## 6. Instalar o metallb


1. Instalação do deployment

```sh
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.12/config/manifests/metallb-native.yaml
```


2. Crie um arquivo metallb-config.yaml com:

```yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: pool-local
  namespace: metallb-system
spec:
  addresses:
    - 192.168.100.121-192.168.100.130

---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: advert-local
  namespace: metallb-system
```

## 7. Instalar o kong


1. Adicionar o repo

```yaml
helm repo add kong https://charts.konghq.com
helm repo update
```


2. Instalar o kong

```yaml
helm install kong kong/kong --namespace kong --create-namespace \
  --set ingressController.installCRDs=false \
  --set proxy.type=LoadBalancer \
  --set ingressController.enabled=true \
  --set env.kong_DATABASE=off
```

## 7. Instalar o cloudflare


1. Mudar o svc do kubernetes para Load Balancer

```sh
kubectl edit svc kubernetes -n default #editer o tipo de serviço para LoadBalancer 
```


2. Gerar um cloud tunner com o comando:

```sh
cloudflared tunnel create kong-akuma
```


3. Aplicar o yaml alterando cloud tunnel id e o secret que é gerado na pasta local do usuário:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: cloudflare
---
apiVersion: v1
kind: Secret
metadata:
  name: cloudflared-creds
  namespace: cloudflare
type: Opaque
data:
  creds.json: eyJBY2NvdW50VGFnIjoiNWZlZjFiNDdlYjI1NmY4OTQwMWJhZGNhOTIyZWQ2ZmQiLCJUdW5uZWxTZWNyZXQiOiJwSnVqWlVRQUVob09hTXdCSE1qbi9jMFhuZ1M5Tm9uTmZaLzVkenJtcEl3PSIsIlR1bm5lbElEIjoiZTNhM2FjZmEtODVmNy00ZGRjLWIwMjUtYzc0MDU2OTIwM2U5IiwiRW5kcG9pbnQiOiIifQ==
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: cloudflared-config
  namespace: cloudflare
data:
  config.yaml: |
    tunnel: e3a3acfa-85f7-4ddc-b025-c740569203e9
    credentials-file: /etc/cloudflared/creds/creds.json
    no-autoupdate: true
    ingress:
      - hostname: "metabase-ryu.zello.space"
        service: http://192.168.100.100:80    
      - hostname: "api-extrata-backend-ryu.zello.space"
        service: http://192.168.100.100:80
      - hostname: "progressogov-ryu.zello.space"
        service: http://192.168.100.100:80
      - hostname: "api-progressogov-ryu.zello.space"
        service: http://192.168.100.100:80
      - hostname: "grafana-ryu.zello.space"
        service: http://192.168.100.100:80
      - hostname: "harbor.zello.space"
        service: https://192.168.100.100:443
        originRequest:
          noTLSVerify: true
      - hostname: "k8s-ryu.zello.space"
        service: https://192.168.100.101:443
        originRequest:
          noTLSVerify: true
      - service: http_status:404
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudflared
  namespace: cloudflare
spec:
  replicas: 2
  selector:
    matchLabels:
      app: cloudflared
  template:
    metadata:
      labels:
        app: cloudflared
    spec:
      containers:
        - name: cloudflared
          image: cloudflare/cloudflared:latest
          args:
            - tunnel
            - --config
            - /etc/cloudflared/config/config.yaml
            - run
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 200m
              memory: 256Mi
          volumeMounts:
            - name: config
              mountPath: /etc/cloudflared/config
            - name: credentials
              mountPath: /etc/cloudflared/creds
              readOnly: true
      volumes:
        - name: config
          configMap:
            name: cloudflared-config
        - name: credentials
          secret:
            secretName: cloudflared-creds
```

## 8. Instalar um storage class com nfs


1. é necessário já ter um servidor de nfs disponível
2. Instalar o helm:

```sh
helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
  --set nfs.server=192.168.100.47 \
  --set nfs.path=/mnt/nfs_share \
  --set storageClass.name=nfs-ryu \
  --set storageClass.defaultClass=true \
  --set storageClass.reclaimPolicy=Delete \
  --set storageClass.archiveOnDelete=false \
  --set nfs.mountOptions={vers=4.1} \
  --set resources.requests.memory=64Mi \
  --set resources.requests.cpu=50m
```

## 9. Instalar prometheus no ryu e akuma

* ryu

```sh
helm upgrade --install kube-prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace \
  --set prometheus.prometheusSpec.retention="45d" \
  --set prometheus.prometheusSpec.storageSpec.volumeClaimTemplate.spec.storageClassName="nfs-ryu" \
  --set prometheus.prometheusSpec.storageSpec.volumeClaimTemplate.spec.resources.requests.storage="50Gi" \
  --set grafana.persistence.enabled=true \
  --set grafana.persistence.storageClassName=nfs-ryu \
  --set grafana.persistence.size=5Gi \
  --set 'grafana.persistence.accessModes[0]=ReadWriteOnce' \
  --set grafana.ingress.enabled=true \
  --set 'grafana.ingress.hosts[0]=grafana-ryu.zello.space' \
  --set grafana.ingress.path=/ \
  --set grafana.ingress.pathType=Prefix \
  --set grafana.ingress.ingressClassName=kong
```

* akuma

```sh
helm upgrade --install kube-prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace \
  --set prometheus.prometheusSpec.retention="45d" \
  --set prometheus.prometheusSpec.storageSpec.volumeClaimTemplate.spec.storageClassName="nfs-client" \
  --set prometheus.prometheusSpec.storageSpec.volumeClaimTemplate.spec.resources.requests.storage="50Gi" \
  --set grafana.persistence.enabled=true \
  --set grafana.persistence.storageClassName=nfs-client \
  --set grafana.persistence.size=5Gi \
  --set 'grafana.persistence.accessModes[0]=ReadWriteOnce' \
  --set grafana.ingress.enabled=true \
  --set 'grafana.ingress.hosts[0]=grafana.zello.space' \
  --set grafana.ingress.path=/ \
  --set grafana.ingress.pathType=Prefix \
  --set grafana.ingress.ingressClassName=kong
```

You can now join any number of control-plane nodes running the following command on each as root:

\
