servicos = {
    "1": "Corte - R$15",
    "2": "Barba - R$10",
    "3": "Corte + Barba - R$25",
    "4": "Sobrancelha - R$5",
    "5": "Corte + Sobrancelha - R$20",
    "6": "Luzes - R$50",
    "7": "Platinado - R$55"
}

def mostrar_servicos_terminal():
    print("\nServiços disponíveis:")
    for codigo, nome in servicos.items():
        print(f"{codigo}. {nome}")

def get_servicos_texto():
    return "\n".join([f"{codigo}. {nome}" for codigo, nome in servicos.items()])
