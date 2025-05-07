from datetime import datetime, time

def dentro_horario_comercial():
    agora = datetime.now().time()
    inicio = time(9, 0)   # 09:00
    fim = time(23, 0)     # 23:00 (corrigido: antes estava escrito 19:00 no comentário)

    return inicio <= agora <= fim

def completar_data_com_ano(dia_mes):
    """
    Recebe uma string no formato 'dd/mm' e retorna 'dd/mm/aaaa' com o ano atual.
    """
    try:
        dia, mes = map(int, dia_mes.split('/'))
        data = datetime(datetime.now().year, mes, dia)
        return data.strftime('%d/%m/%Y')
    except (ValueError, IndexError):
        return None  # Importante para validar datas inválidas no chatbot
