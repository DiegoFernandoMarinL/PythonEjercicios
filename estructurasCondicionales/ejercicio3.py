dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

if dividendo % divisor == 0:
    print("La division es exacta")
else:
    print("La division no es exacta") 

print("Coeficiente: ",dividendo // divisor)
print("Residuo: ",dividendo % divisor)
