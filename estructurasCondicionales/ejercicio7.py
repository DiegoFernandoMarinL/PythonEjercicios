num1 = int(input("Digite numero: "))
operador = input("Operador: ")
num2 = int(input("Digite numero: "))

if operador == "+":
    operacion = num1 + num2
elif operador == "-":
    operacion = num1 - num2
elif operador == "x":
    operacion = num1 * num2
elif operador == "/":
    operacion = num1 / num2    
        
print(num1," ",operador," ",num2," = ",operacion)