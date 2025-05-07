from datetime import datetime, time

def dentro_horario_comercial():
    agora = datetime.now().time()
    inicio = time(9, 0)   # 09:00
    fim = time(23, 0)     # 23:00 (corrigido: antes estava escrito 19:00 no comentário)

    return inicio <= agora <= fim


from datetime import datetime

def completar_data_com_ano(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m")
        ano_atual = datetime.now().year
        data_com_ano = data.replace(year=ano_atual)
        return data_com_ano.strftime("%d/%m/%Y")
    except ValueError:
        return None
