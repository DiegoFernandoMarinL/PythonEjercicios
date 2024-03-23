flag = 1
numeros = []
while flag == 1:
    num = 0
    num = int(input("Digite numero: "))
    numeros.append(num)
    flag = int(input("1. Otro numero  0. Ordenar: "))

print(sorted(numeros))    