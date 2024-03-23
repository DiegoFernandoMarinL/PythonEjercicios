limite = int(input("Digite limite: "))

potenciasDeDos = []
for i in range(limite + 1):
    potencia = 2 ** i
    potenciasDeDos.append(potencia)

print("Potencias de 2:")
for potencia in potenciasDeDos:
    print(potencia)

    