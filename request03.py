import requests

cep = input("Digite o CEP (somente números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    
    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("\n--- Endereço encontrado ---")
        print("Logradouro:", dados.get("logradouro", "Não informado"))
        print("Bairro:    ", dados.get("bairro", "Não informado"))
        print("Cidade:    ", dados.get("localidade", "Não informado"))
        print("Estado:    ", dados.get("uf", "Não informado"))
else:
    print("Erro ao acessar a API.")
