def calculator():
    
    num1 = float(input("Ingresa el primer número: "))
    operator = input("Ingresa el operador (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))

    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Operador no válido.")
        return

   
    print("El resultado es:", result)

calculator()
