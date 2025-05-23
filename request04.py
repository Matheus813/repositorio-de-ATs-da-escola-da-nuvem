import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    
    chave = f"{moeda}BRL"
    if chave in dados:
        info = dados[chave]
        
        print("Moeda:           ", info['name'])
        print("Valor atual:     R$", info['bid'])
        print("Valor máximo:    R$", info['high'])
        print("Valor mínimo:    R$", info['low'])
        print("Data:            ", info['create_date'][:10])
        print("Hora:            ", info['create_date'][11:])
    else:
        print("Moeda não encontrada ou código inválido.")
else:
    print("Erro ao acessar a API:", resposta.status_code)
