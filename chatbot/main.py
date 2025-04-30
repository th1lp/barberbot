import json
import os
from datetime import datetime


ARQUIVO_AGENDAMENTOS = "agendamentos.json"

servicos = {
    1: "Corte Masculino",
    2: "Barba",
    3: "Corte + Barba",
    4: "Sobrancelha",
    5: "Hidratação Capilar"
}

def carregar_agendamentos():
    if os.path.exists(ARQUIVO_AGENDAMENTOS):
        with open(ARQUIVO_AGENDAMENTOS, "r") as f:
            return json.load(f)
    return []

# verifica se o formato da data esta correto 
def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# verifica se o formato do horario esta corretp
def validar_hora(hora_str):
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False

def salvar_agendamentos(agendamentos):
    with open(ARQUIVO_AGENDAMENTOS, "w") as f:
        json.dump(agendamentos, f, indent=4)

def mostrar_servicos():
    print("\nServiços disponíveis:")
    for codigo, nome in servicos.items():
        print(f"{codigo} - {nome}")


def agendar(agendamentos):
    nome = input("Digite seu nome: ")
    mostrar_servicos()
    
    try:
        servico_id = int(input("Escolha o serviço (número): "))
        if servico_id not in servicos:
            print("Serviço inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    data = input("Digite a data (dd/mm/aaaa): ")
    if not validar_data(data):
        print("Data inválida. Use o formato dd/mm/aaaa.")
        return

    hora = input("Digite a hora (hh:mm): ")
    if not validar_hora(hora):
        print("Hora inválida. Use o formato hh:mm (24h).")
        return

    # Verifica se já tem alguém nesse horário
    for ag in agendamentos:
        if ag["data"] == data and ag["hora"] == hora:
            print("Horário já está ocupado. Escolha outro.")
            return

    agendamento = {
        "nome": nome,
        "servico": servicos.get(servico_id, "Desconhecido"),
        "data": data,
        "hora": hora
    }
    agendamentos.append(agendamento)
    salvar_agendamentos(agendamentos)
    print("Agendamento realizado com sucesso!")

def menu():
    
    agendamentos = carregar_agendamentos()
    while True:
        print("\n--- ChatBot Barbearia ---")
        print("1 - Ver serviços")
        print("2 - Agendar horário")
        print("3 - Consultar agendamento")
        print("4 - Cancelar agendamento")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrar_servicos()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "2":
            agendar(agendamentos)
        elif opcao == "3":
            consultar(agendamentos)
        elif opcao == "4":
            cancelar(agendamentos)
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()