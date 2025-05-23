#forma longa
arquivo = open("texto.txt", "r", encoding="utf8")
conteudo = arquivo.read()
arquivo .close
print(conteudo)

#forma boa e útil
with open("texto.txt", "w", encoding="utf8") as arquivo:
    arquivo.write("Nova linha de texto novamente")
    

with open("texto.txt", "r", encoding="utf8") as arquivo:
    print(conteudo)
    print(conteudo)
    print(conteudo)
    print(conteudo)

"""
readline ==== lê apena a primeira linha
readlines ==== lê como uma lista """

