from datetime import datetime, time

def dentro_horario_comercial():
    agora = datetime.now().time()
    inicio = time(9, 0)   # 09:00
    fim = time(22, 0)     # 23:00

    return inicio <= agora <= fim

def completar_data_com_ano(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m")
        ano_atual = datetime.now().year
        data_com_ano = data.replace(year=ano_atual)
        return data_com_ano.strftime("%d/%m/%Y")
    except ValueError:
        return None

def hora_valida(hora_str):
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False