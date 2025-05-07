import requests
import socketio
from agendamentos import agendar_ws, cancelar_ws, consultar_ws
from servicos import servicos, get_servicos_texto
from utils import completar_data_com_ano

# Função para enviar uma mensagem via API
def enviar_mensagem(id_sessao, numero, mensagem):
    url = 'http://localhost:3000/enviarMensagem'
    payload = {
        'idSessao': id_sessao,
        'numero': numero,
        'mensagem': mensagem
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        
        print(f"Mensagem enviada com sucesso para {numero}")
    else:
        print(f"Erro ao enviar mensagem: {response.text}")

# Conectar ao servidor WebSocket e reagir a mensagens
def ouvir_mensagens(id_sessao):
    sio = socketio.Client()
    estado_usuarios = {}  # Mantém o estado por usuário

    @sio.on("novaMensagem")
    def novaMensagem(data):
        if data['idSessao'] != id_sessao:
            return

        remetente = data['from']
        numero = remetente.replace('@c.us', '')
        mensagem = data['body'].strip().lower()

        if numero not in estado_usuarios:
            estado_usuarios[numero] = {"etapa": None, "dados": {}}

        estado = estado_usuarios[numero]

        if mensagem == "agendar":
            estado_usuarios[numero] = {"etapa": "nome", "dados": {}}
            enviar_mensagem(id_sessao, numero, "📛 Qual o seu nome?")
            return

        # Etapas do agendamento
        if estado["etapa"] == "nome":
            estado["dados"]["nome"] = mensagem
            estado["etapa"] = "servico"
            texto_servicos = "\n".join([f"{k} - {v}" for k, v in servicos.items()])
            enviar_mensagem(id_sessao, numero, f"💈 Escolha o serviço digitando o número:\n{texto_servicos}")
            return

        if estado["etapa"] == "servico":
            if mensagem not in servicos:
                enviar_mensagem(id_sessao, numero, "❌ Serviço inválido. Tente novamente.")
                return
            estado["dados"]["servico"] = mensagem
            estado["etapa"] = "data"
            enviar_mensagem(id_sessao, numero, "📅 Digite a data (dd/mm):")
            return

        if estado["etapa"] == "data":
            data_formatada = completar_data_com_ano(mensagem)
            if data_formatada is None:
                enviar_mensagem(id_sessao, numero, "❌ Data inválida. Use o formato dd/mm, ex: 05/07")
                return
            estado["dados"]["data"] = data_formatada
            estado["etapa"] = "hora"
            enviar_mensagem(id_sessao, numero, "🕒 Digite a hora (hh:mm):")
            return

        if estado["etapa"] == "hora":
            estado["dados"]["hora"] = mensagem
            dados = estado["dados"]
            resposta = agendar_ws(dados["nome"], dados["servico"], dados["data"], dados["hora"])
            enviar_mensagem(id_sessao, numero, resposta)
            estado_usuarios.pop(numero)  # Limpa o estado após o agendamento
            return

        # Menu e comandos avulsos
        if mensagem == "menu":
            menu_texto = (
                "👋 Bem-vindo à *Barbearia Bot*!\n"
                "Escolha uma opção:\n"
                "1️⃣ Agendar horário\n"
                "2️⃣ Cancelar agendamento\n"
                "3️⃣ Consultar agendamentos\n"
                "4️⃣ Ver serviços\n"
                "5️⃣ Sair"
            )
            enviar_mensagem(id_sessao, numero, menu_texto)
        elif mensagem == "1":
            estado_usuarios[numero] = {"etapa": "nome", "dados": {}}
            enviar_mensagem(id_sessao, numero, "📛 Qual o seu nome?")
        elif mensagem == "2":
            enviar_mensagem(id_sessao, numero, "Digite seu nome e a data do agendamento para cancelar. Ex: cancelar joao 12/05")
        elif mensagem.startswith("cancelar"):
            try:
                partes = mensagem.split()
                nome = partes[1]
                data_agendamento = partes[2]
                resposta = cancelar_ws(nome, data_agendamento)
            except:
                resposta = "❗Formato inválido. Use: cancelar joao 12/05"
            enviar_mensagem(id_sessao, numero, resposta)
        elif mensagem == "3":
            enviar_mensagem(id_sessao, numero, "Digite seu nome para consultar os agendamentos. Ex: consultar joao")
        elif mensagem.startswith("consultar"):
            try:
                nome = mensagem.split()[1]
                resposta = consultar_ws(nome)
            except:
                resposta = "❗Formato inválido. Use: consultar joao"
            enviar_mensagem(id_sessao, numero, resposta)
        elif mensagem == "4":
            texto_servicos = get_servicos_texto()
            enviar_mensagem(id_sessao, numero, f"💈 Serviços disponíveis:\n{texto_servicos}")
        elif mensagem == "5":
            enviar_mensagem(id_sessao, numero, "👋 Até logo!")
        else:
            enviar_mensagem(id_sessao, numero, "❓ Não entendi. Digite *menu* para ver as opções.")

        pass
    #Não mexer daqui em diante
    sio.connect('http://localhost:3000')
    print(f"Conectado ao servidor WebSocket para a sessão {id_sessao}")
    sio.wait()

# Função principal
def main():
    #Coloquem o número da sessão que foi definida no navegador
    id_sessao = '8113'
    ouvir_mensagens(id_sessao)

if __name__ == '__main__':
    main()
