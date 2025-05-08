from agendamentos import agendar_ws, cancelar_ws, consultar_ws
from servicos import mostrar_servicos_terminal
from utils import dentro_horario_comercial

def menu():
    print("\n--- Bem-vindo à Barbearia Bot ---")
    print("1. Agendar horário")
    print("2. Cancelar agendamento")
    print("3. Consultar agendamentos")
    print("4. Ver serviços")
    print("5. Ver localização da barbearia")  
    print("6. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if dentro_horario_comercial():
                agendar_ws()
            else:
                print("A barbearia está fora do horário comercial.")
                input("Pressione Enter para voltar. ")
        elif escolha == "2":
            cancelar_ws()
        elif escolha == "3":
            consultar_ws()
        elif escolha == "4":
            mostrar_servicos_terminal()
            input("Pressione Enter para continuar: ")
        elif escolha == "5":
            print("📍 Avenida Doutor Oliveira Brito, Galeria Bruna Center, Sala 1, Ribeira do Pombal 48400000.")
            input("Pressione Enter para voltar.")

        elif escolha == "6":
            print("📞 Você pode falar com o barbeiro diretamente pelo WhatsApp:")
            print("🔗 https://wa.me/5511912345678")
            input("Pressione Enter para voltar.")
            
        elif escolha == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
