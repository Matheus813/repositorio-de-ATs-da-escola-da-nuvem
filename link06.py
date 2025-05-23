try:
    peso = float(input("digite seu peso(em kilos): "))
    altura = float(input("digite sua altura(em metros): "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"

    elif imc < 25:
        classificacao = "Peso normal"

    elif imc < 30:
        classificacao = "Sobrepeso"

    elif imc < 35:
        classificacao = "Obesidade grau I"

    elif imc < 40:
        classificacao = "Obesidade grau II"
        
    else:
        classificacao = "Obesidade grau III"

    print(f"seu IMC é {imc} e voce está na classificação {classificacao}")

except ValueError:
    print("digite um valor valido")