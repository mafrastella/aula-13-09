def pode_acessar(cargo, dia_semana=None):
    dias_uteis = {"segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"}
    
    cargo = cargo.lower()
    if dia_semana:
        dia_semana = dia_semana.lower()

    # Dicionário que mapeia cargos a permissões
    permissoes = {
        "gerente": True,  # Gerente tem acesso irrestrito
        "analista": dia_semana in dias_uteis if dia_semana else False,  # Analista tem acesso apenas em dias úteis
        "estagiário": dia_semana in dias_uteis if dia_semana else False  # Estagiário tem acesso apenas em dias úteis
    }

    # Retorna o acesso baseado no cargo; padrão é False se o cargo não estiver no dicionário
    return permissoes.get(cargo, False)

# Teste do programa
cargo = input("Digite o cargo do funcionário: ")

# Pergunta o dia da semana apenas se o cargo não for "gerente"
if cargo.lower() == "gerente":
    dia_semana = None
else:
    dia_semana = input("Digite o dia da semana: ")

if pode_acessar(cargo, dia_semana):
    print("Acesso Permitido.")
else:
    print("Acesso Negado.")