notaCertamen1 = int(input("Nota certamen 1: "))
notaCertamen2 = int(input("Nota certamen 2: "))
notaLaboratorio = int(input("Nota laboratorio: "))

promedio = (notaCertamen1 + notaCertamen2) / 2 
notaCertamen3 = round((60 - 0.3 * notaLaboratorio) / 0.7 - promedio * 3)


print(f"Necesita nota {notaCertamen3} en el certamen 3")