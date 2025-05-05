import json
from utils import completar_data_com_ano
from servicos import mostrar_servicos, servicos

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

def agendar():
    nome = input("Nome: ")

    mostrar_servicos()
    codigo = input("Digite o número do serviço desejado: ").strip()

    if codigo not in servicos:
        print("Serviço inválido. Tente novamente.")
        return
    
    servico = codigo
    dia_mes = input("Data (dd/mm): ")
    data = completar_data_com_ano(dia_mes)
    hora = input("Horário (hh:mm): ")

    agendamentos = carregar_agendamentos()
    agendamentos.append({
        "nome": nome,
        "servico": servico,
        "data": data,
        "hora": hora
    })
    salvar_agendamentos(agendamentos)
    print("Agendamento realizado com sucesso!")
    input("Pressione Enter para voltar. ")

def cancelar():
    nome = input("Nome usado na reserva: ")
    data = input("Data do agendamento: ")

    agendamentos = carregar_agendamentos()
    atualizados = [a for a in agendamentos if not (a["nome"] == nome and a["data"] == data)]

    if len(atualizados) < len(agendamentos):
        salvar_agendamentos(atualizados)
        print("Agendamento cancelado.")
    else:
        print("Agendamento não encontrado.")

def consultar():
    nome = input("Digite seu nome para consultar seus agendamentos: ").strip().lower()
    agendamentos = carregar_agendamentos()
    encontrados = [a for a in agendamentos if a["nome"].strip().lower() == nome]

    if not encontrados:
        print("Nenhum agendamento encontrado.")
        input("Pressione Enter para voltar. ")
        return
    
    print(f"\nAgendamentos de {nome.title()}:")
    for ag in encontrados:
        print(f'{ag["nome"]} - {ag["servico"]} em {ag["data"]} às {ag["hora"]}')
        
    input("Pressione Enter para voltar. ")