from agendamentos import agendar, cancelar, consultar
from servicos import servicos, mostrar_servicos_terminal
from utils import dentro_horario_comercial

def menu():
    print("\n--- Bem-vindo à Barbearia Bot ---")
    print("1. Agendar horário")
    print("2. Cancelar agendamento")
    print("3. Consultar agendamentos")
    print("4. Ver serviços")
    print("5. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if dentro_horario_comercial():
                agendar()
            else:
                print("A barbearia está fora do horário comercial.")
                input("Pressione Enter para voltar. ")
        elif escolha == "2":
            cancelar()
        elif escolha == "3":
            consultar()
        elif escolha == "4":
            mostrar_servicos_terminal()
            input("Pressione Enter para continuar: ")
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
