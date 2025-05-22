"""
Crie um programa que solicite ao usuário que insira números
inteiros. O programa deve continuar solicitando números até
que o usuário digite 'fim'. Para cada número inserido, o
programa deve informar se é par ou ímpar. Se o usuário
inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a
quantidade de números pares e ímpares inseridos.
"""
quant_pares = 0
numero_pares = []
quant_impares = 0
numero_impares = []
while True:
    try:
        entrada = input("digite um numero inteiro ou 'fim' para sair: ")
        

        if entrada.lower() == "fim":
            break

        numero = int(entrada)

        if numero % 2 == 0:
            print(f"{numero} é PAR")
            numero_pares.append(numero)
            quant_pares += 1

        else:
            print(f"{numero} é IMPAR")
            numero_impares.append(numero)
            quant_impares += 1

    except ValueError:
        input(f"{entrada} nao é uma entrada valida")
        continue

print(f"lista de {quant_pares} numeros pares: {numero_pares}")
print(f"lista de {quant_impares} numeros pares: {numero_impares}")