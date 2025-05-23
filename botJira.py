import time
import requests
from requests.auth import HTTPBasicAuth
import base64
from dotenv import load_dotenv
import os
# Forçar o uso de encoding UTF-8 para evitar problemas com caracteres especiais
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Carregar variáveis do .env
load_dotenv()

# Configurações do Jira
JIRA_USER = os.getenv("JIRA_USER")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
JIRA_URL = os.getenv("JIRA_URL")
REFRESH_INTERVAL = 80  # segundos

# Codifica credenciais para Basic Auth
basic_auth = HTTPBasicAuth(JIRA_USER, JIRA_TOKEN)

# Histórico de issues já vistos
last_issue_ids = set()
# Histórico de issues já mostrados
shown_issue_ids = set()

def get_issues():
    response = requests.get(JIRA_URL, auth=basic_auth)
    response.raise_for_status()
    data = response.json()

    # Verificar se a resposta contém a chave 'issues'
    if 'issues' not in data or not isinstance(data['issues'], list):
        print("[botJira] Resposta inválida da API do Jira: 'issues' não encontrado ou não é uma lista.", flush=True)
        return []

    return data['issues']


print("[botJira] Monitoramento iniciado.", flush=True)

while True:
    try:
        issues = get_issues()

        if not issues:
            time.sleep(REFRESH_INTERVAL)
            continue

        # Filtrar e exibir todos os itens no estado "Aberto"
        for issue in issues:
            issue_id = issue["id"]
            status = issue["fields"].get("status", {}).get("name", "Desconhecido")
            if status == "Aberto" and issue_id not in shown_issue_ids:
                key = issue["key"]
                summary = issue["fields"]["summary"]
                created = issue["fields"]["created"]
                reporter = issue["fields"].get("reporter", {}).get("displayName", "Desconhecido")
                mensagem = (
                    "[botJira] Temos um Novo Card:\n"
                    f"Key: {key}\n"
                    f"Nome: {summary}\n"
                    f"Aberto por: {reporter}\n"
                    f"Criado em: {created}\n"
                )
                print(mensagem, flush=True)
                shown_issue_ids.add(issue_id)

        # Atualizar o conjunto de issues mostrados se houver alterações
        current_issue_ids = {issue["id"] for issue in issues if issue["fields"].get("status", {}).get("name", "") == "Aberto"}
        if shown_issue_ids != current_issue_ids:
            shown_issue_ids = current_issue_ids

    except KeyboardInterrupt:
        print("[botJira] Monitoramento encerrado.", flush=True)
        break
    except Exception as e:
        print(f"[botJira] Erro fatal: {e}", flush=True)
        break
