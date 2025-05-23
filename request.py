import requests

name = input("digite o seu nome:")
resposta = requests.get(f"https://agify.io/?name={name}")

if resposta.status_code == 200:
    dados = resposta.json()
    print(dados['age'])

