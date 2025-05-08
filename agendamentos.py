import json
from servicos import servicos

ARQUIVO = "agendamentos.json"

def carregar_agendamentos():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_agendamentos(agendamentos):
    with open(ARQUIVO, "w") as f:
        json.dump(agendamentos, f, indent=4)

def agendar_ws(nome, servico, data, hora):
    agendamentos = carregar_agendamentos()

    # Verifica se já existe um agendamento com a mesma data e hora
    for agendamento in agendamentos:
        if agendamento['data'] == data and agendamento['hora'] == hora:
            return "⚠️ Esse horário já está agendado. Por favor, escolha outro."
    # Se não houver conflito, adiciona o novo agendamento
    agendamentos.append({
        "nome": nome,
        "servico": servico,
        "data": data,
        "hora": hora
    })
    salvar_agendamentos(agendamentos)
    return f"✅ Agendamento realizado com sucesso para {data} às {hora}."

def cancelar_ws(nome, data):
    agendamentos = carregar_agendamentos()
    atualizados = [a for a in agendamentos if not (a["nome"] == nome and a["data"] == data)]

    if len(atualizados) < len(agendamentos):
        salvar_agendamentos(atualizados)
        return "❌ Agendamento cancelado com sucesso.\n\nDigite menu para voltar para as opções"
    else:
        return "⚠️ Agendamento não encontrado."

def consultar_ws(nome):
    agendamentos = carregar_agendamentos()
    encontrados = [a for a in agendamentos if a["nome"].strip().lower() == nome.strip().lower()]

    if not encontrados:
        return "📭 Nenhum agendamento encontrado."

    resposta = f"📋 Agendamentos de {nome.title()}:\n"
    for ag in encontrados:
        # Obtém o nome do serviço baseado no código
        servico_desc = servicos.get(ag["servico"], "Serviço desconhecido")
        resposta += f'- {servico_desc} em {ag["data"]} às {ag["hora"]}\n'
    return resposta