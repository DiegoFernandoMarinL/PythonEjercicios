num1 = int(input("Ingrese numero inicio: "))
num2 = int(input("Ingrese numero final: "))

suma = 0

for i in range(num1 + 1,num2):
    suma += i

print("La suma es: ",suma)    