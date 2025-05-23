def palindromo():
    while True:
        texto = input("Digite uma palavra ou frase (ou 'fim' para sair): ")

        if texto.lower() == "fim":
            break

        texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
        invertido = texto_limpo[::-1]

        if texto_limpo == invertido:
            print("Sim, é um palíndromo.")
        else:
            print("Não, não é um palíndromo.")

palindromo()