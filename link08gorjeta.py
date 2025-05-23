def calcular_gorjeta():
    while True:
        try:
            valor = input("Digite o valor da conta (ou 'fim' para sair): ")

            if valor.lower() == "fim":
                break

            valor_conta = float(valor)
            porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))

            gorjeta = round(valor_conta * (porcentagem / 100), 2)
            print(f"Gorjeta calculada: R$ {gorjeta:.2f}")

        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

calcular_gorjeta()