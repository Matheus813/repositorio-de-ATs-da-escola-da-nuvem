nome = input("Produto: ")
preco = float(input("Preço unitário (R$): "))
quantidade = int(input("Quantidade: "))

total = preco * quantidade

preco = round(preco, 2)
total = round(total, 2)


print("--- RECIBO DE COMPRA ---")
print("Produto:", nome)
print("Preço unitário: R$ " + str(preco))
print("Quantidade:", quantidade)
print("Total a pagar: R$ " + str(total))
print("------------------------")