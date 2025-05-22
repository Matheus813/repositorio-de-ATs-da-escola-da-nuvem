"""
Crie um programa que verifique se uma senha é forte. Uma
senha forte deve ter pelo menos 8 caracteres e conter pelo
menos um número. O programa deve continuar pedindo
senhas até que uma válida seja inserida ou o usuário digite
'sair'.
"""
while True:
    try:
        senha =  input("digite sua senha: ")

        if senha.lower() == "sair":
            print("voce saiu do pograma")
            break

        elif len(senha) >= 8:
            print("sua senha tem oito ou mais caracteres")
            continue

        else:
            print("sua senha tem menos de 8 caracteres")

        temNumero = False

        for caractere in senha:
            if caractere in '1234567890':
                temNumero = True
                print("numero encontrado")
                break
                

        if not temNumero:
            print("sua senha precisa de pelo menos um numero")
            continue

        else:
            print("sua senha tem pelo menos um numero")  
            break 

    except ValueError:
        print("digite uma senha valida")