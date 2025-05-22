idade = int(input("digite a sua idade: "))

if idade >= 18:
    print(f"Você tem {idade} anos de idade e você é de maior")

elif idade >= 0:
    print(f"Você tem {idade} anos de idade você é de menor")

else:
    print("Você ainda não nasceu")