# Criação de usuário de VPN

## Gerar Credenciais no OpenVPN

This tutorial outlines the steps to generate credentials and connect a user to the OpenVPN.

**1. Acessar o servidor VPN**

* Connect via SSH:

  ```bash
  ssh ubuntu@177.136.241.236
  ```
* Password: use the default password

**2. Gerar as credenciais do usuário**

* Within the server, execute the script passing the user's `nome.sobrenome`:

  ```bash
  cd ~/openvpn
  sudo ./create-ovpn.sh nome.sobrenome
  ```
* Example:

  ```bash
  sudo ./create-ovpn.sh joao.silva
  ```

**3. Mover o arquivo gerado para a pasta de arquivos**

* To organize, move the `.ovpn` file to the `ovpn_archives` folder:

  ```bash
  mv ~/openvpn/joao.silva.ovpn ~/openvpn/ovpn_archives/
  ```
* If the folder doesn't exist, create it first:

  ```bash
  mkdir -p ~/openvpn/ovpn_archives
  ```

**4. Baixar o arquivo para sua máquina**

* On your local machine, execute:

  ```bash
  scp ubuntu@177.136.241.236:/home/ubuntu/openvpn/ovpn_archives/joao.silva.ovpn vpns/
  ```

**5. Importar no cliente OpenVPN**

* Steps:
  * Install the OpenVPN Connect (Windows, Mac, Linux, iOS or Android)
  * Open the application
  * Click on 'Import Profile'
  * Select the `.ovpn` file that you copied
  * Connect

\
