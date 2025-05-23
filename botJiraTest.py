# botJiraTest.py
# Simula a detecção de novo card do Jira e formata mensagem para WhatsApp

import time

# Dados de teste fixos simulando um novo card
issues = [
    {
        "id": "12345",
        "key": "STI-999",
        "fields": {
            "summary": "Exemplo de card para teste de WhatsApp",
            "created": "2025-05-22T10:00:00.000+0000",
            "reporter": {"displayName": "Usuário Teste"}
        }
    }
]

# Simula envio da mensagem formatada para WhatsApp
while True:
    for issue in issues:
        key = issue["key"]
        summary = issue["fields"]["summary"]
        created = issue["fields"]["created"]
        reporter = issue["fields"].get("reporter", {}).get("displayName", "Desconhecido")
        mensagem = (
            "Temos um novo card!\n"
            f"Key: {key}\n"
            f"Nome: {summary}\n"
            f"Aberto por: {reporter}"
        )
        print(mensagem, flush=True)
    time.sleep(120)
