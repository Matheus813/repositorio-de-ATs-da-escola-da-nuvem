"""
Crie um programa que permita a um professor registrar as
notas de uma turma. O programa deve continuar solicitando
notas até que o professor digite 'fim'. Notas válidas são de 0 a
10. O programa deve ignorar notas inválidas e continuar
solicitando. No final, deve exibir a média da turma.
"""
lista_notas = []
while True:
    try:
        nota = input("digite a nota do aluno ou digite 'fim' para sair: ")
        
        if nota.lower() == "fim":
            break

        else:
            nota = float(nota)

        if nota >= 0 and nota <= 10:
            lista_notas.append(nota)
            print("nota salva")

        else:
            print("digite uma nota valida")

    except ValueError:
        print("digite uma entrada valida")

if len(lista_notas) != 0:
    quant_notas = len(lista_notas)
    media = sum(lista_notas) / quant_notas
    print(f"lista de notas: {lista_notas} e a media de notas da turma é {media}")