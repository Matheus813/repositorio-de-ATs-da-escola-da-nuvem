try:
    entrada = int(input("digite sua idade: "))

    if entrada >= 60:
        print("voce é um idoso(a)")

    elif entrada >= 18:
        print("voce é um adulto(a)")

    elif entrada >= 13:
        print("voce é um adolecente")

    elif entrada >= 0:
        print("voce é uma criança")

    else:
        print("voce digitou uma entrada invalida")

except ValueError:
    print("voce digitou uma entrada invalida")