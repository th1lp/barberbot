import json
from utils import completar_data_com_ano
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
    agendamentos.append({
        "nome": nome,
        "servico": servico,
        "data": data,
        "hora": hora
    })
    salvar_agendamentos(agendamentos)
    return f"✅ Agendamento confirmado para {nome} em {data} às {hora} para {servico}."

def cancelar_ws(nome, data):
    agendamentos = carregar_agendamentos()
    atualizados = [a for a in agendamentos if not (a["nome"] == nome and a["data"] == data)]

    if len(atualizados) < len(agendamentos):
        salvar_agendamentos(atualizados)
        return "❌ Agendamento cancelado com sucesso."
    else:
        return "⚠️ Agendamento não encontrado."

def consultar_ws(nome):
    agendamentos = carregar_agendamentos()
    encontrados = [a for a in agendamentos if a["nome"].strip().lower() == nome.strip().lower()]

    if not encontrados:
        return "📭 Nenhum agendamento encontrado."

    resposta = f"📋 Agendamentos de {nome.title()}:\n"
    for ag in encontrados:
        resposta += f'- {ag["servico"]} em {ag["data"]} às {ag["hora"]}\n'
    return resposta