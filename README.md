# Bot Notification for Jira

## Overview

Este projeto é um bot que monitora issues do Jira no estado "Aberto" e envia notificações para o WhatsApp. Ele se integra com a API REST do Jira para buscar as issues e utiliza a biblioteca `whatsapp-web.js` para enviar mensagens para o WhatsApp.

## Features

- Monitora issues do Jira no estado "Aberto".
- Envia notificações para novas issues para um número e grupo do WhatsApp especificados.
- Gerencia reconexões com o WhatsApp Web automaticamente.
- Registra informações detalhadas para depuração.

## Pré-requisitos

- Node.js (v14 ou superior)
- Python (v3.8 ou superior)
- Uma conta no WhatsApp
- Conta no Jira com acesso à API

## Instalação

1. Clone o repositório:

   ```bash
   git clone <repository-url>
   cd botNotificationJira
   ```
2. Instale as dependências do Node.js:

   ```bash
   npm install
   ```
3. Crie um arquivo `.env` no diretório raiz e adicione as seguintes variáveis:

   ```env
   JIRA_USER=<seu-usuario-jira>
   JIRA_TOKEN=<seu-token-api-jira>
   JIRA_URL=<sua-url-api-jira>
   ```
4. Instale as dependências do Python (se houver):

   ```bash
   pip install -r requirements.txt
   ```

## Como obter o Token de API do Jira

1. Acesse [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Clique em "Create API token".
3. Dê um nome ao token e clique em "Create".
4. Copie o token gerado e utilize no campo `JIRA_TOKEN` do seu `.env`.

Mais detalhes na documentação oficial:
https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/

## Uso

1. Inicie o bot:

   ```bash
   node bot.js
   ```
2. Escaneie o código QR exibido no terminal com sua conta do WhatsApp.
3. O bot começará a monitorar as issues do Jira e enviar notificações para o WhatsApp.

## Bibliotecas Necessárias

É essencial instalar corretamente as bibliotecas necessárias para o funcionamento do bot. Certifique-se de executar o seguinte comando na raiz do projeto para instalar as dependências:

```bash
npm install whatsapp-web.js qrcode-terminal
```

Essas bibliotecas são fundamentais para a integração com o WhatsApp Web e para a exibição do QR Code no terminal.

### Exemplo de QR Code

Ao iniciar o bot, será exibido um QR Code no terminal. Use o aplicativo do WhatsApp para escanear o código e autenticar o bot. 

Certifique-se de que o QR Code seja escaneado rapidamente, pois ele expira após alguns segundos. Caso expire, reinicie o bot para gerar um novo QR Code.

## Deploy

Para implantar este projeto:

1. Certifique-se de que todas as dependências estão instaladas e o arquivo `.env` está configurado.
2. Use um gerenciador de processos como o `pm2` para manter o bot em execução:
   ```bash
   npm install -g pm2
   pm2 start bot.js --name botNotificationJira
   ```
3. Configure um servidor ou ambiente em nuvem para hospedar o bot.

## Licença

Este projeto está licenciado sob a Licença MIT.

---

**Atenção:** Nunca compartilhe seu arquivo `.env` ou seu token de API publicamente.
