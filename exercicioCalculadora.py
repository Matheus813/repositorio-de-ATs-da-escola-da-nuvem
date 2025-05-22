while True:
    try:
        numero1 = float(input("digite o primeiro numero:"))
        numero2 = float(input("digite o segundo numero:"))
        operation = str(input("digite uma operaçao (+, -, /, *):"))

        if operation == "+":
            resultado = numero1 + numero2

        elif operation == "-":
            resultado = numero1 - numero2

        elif operation == "/":
            resultado = numero1 / numero2

        elif operation == "*":
            resultado = numero1 * numero2
        
        else:
            print(f"{operation} nao e uma operacao valida")
        
        print(f"resultado: {resultado}")
        break
        
    except ValueError:
        print("digite um numero ou operaçao validos")

    except ZeroDivisionError:
        print("nao e possivel dividir um numero por zero")
