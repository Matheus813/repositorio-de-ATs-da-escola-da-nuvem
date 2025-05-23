from datetime import date

def calcular_idade_em_dias():
    while True:
        nascimento = input("Digite o ano de nascimento (ou 'fim' para sair): ")

        if nascimento.lower() == "fim":
            break

        try:
            ano_nasc = int(nascimento)
            ano_atual = date.today().year
            idade_anos = ano_atual - ano_nasc
            idade_dias = idade_anos * 365
            print(f"Idade aproximada: {idade_dias} dias")

        except ValueError:
            print("Ano inválido. Tente novamente.")
            continue
        
calcular_idade_em_dias()