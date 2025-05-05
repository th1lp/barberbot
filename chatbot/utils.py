from datetime import datetime, time

def dentro_horario_comercial():
    agora = datetime.now().time()
    inicio = time(9, 0)   # 09:00
    fim = time(23, 0)     # 19:00

    return inicio <= agora <= fim

def completar_data_com_ano(dia_mes):
    """
    Recebe uma string no formato 'dd/mm' e retorna 'dd/mm/aaaa' com o ano atual.
    """
    ano_atual = datetime.now().year
    return f"{dia_mes}/{ano_atual}"
