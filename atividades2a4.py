import csv
import json
import os

try:
    pessoas_csv = [
        ["Nome", "Idade", "Cidade"],
        ["Ana", 28, "São Paulo"],
        ["Bruno", 35, "Curitiba"],
        ["Carlos", 22, "Salvador"]
    ]

    csv_path = "pessoas.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f_csv:
        escritor = csv.writer(f_csv)
        escritor.writerows(pessoas_csv)
    print("Arquivo CSV criado com sucesso.\n")

    arquivo_para_ler = input("Digite o nome do arquivo para leitura (.csv ou .json): ").strip()
    extensao = os.path.splitext(arquivo_para_ler)[1].lower()

    if not os.path.isfile(arquivo_para_ler):
        print("Arquivo não encontrado.")

    elif extensao == ".csv":
        print("\nConteúdo do CSV:")
        with open(arquivo_para_ler, "r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            
            for linha in leitor:
                print("Nome:", linha[0], "| Idade:", linha[1], "| Cidade:", linha[2])

    elif extensao == ".json":
        print("\nConteúdo do JSON:")
        with open(arquivo_para_ler, "r", encoding="utf-8") as f:
            dados = json.load(f)
            print("Nome:", dados['nome'])
            print("Idade:", dados['idade'])
            print("Cidade:", dados['cidade'])
    else:
        print("Tipo de arquivo não suportado. Use .csv ou .json.")

    pessoa_json = {
        "nome": "Julia",
        "idade": 30,
        "cidade": "Porto Alegre"
    }

    json_path = "pessoa.json"
    with open(json_path, "w", encoding="utf-8") as f_json:
        json.dump(pessoa_json, f_json, ensure_ascii=False, indent=4)
    print("\nArquivo JSON criado com sucesso.")

except Exception as e:
    print("\nErro durante a execução:")
    print("Detalhes:", str(e))  