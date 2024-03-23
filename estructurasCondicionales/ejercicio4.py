palabra1 = input("Primera palabra: ")
palabra2 = input("Segunda palabra: ")

cantidadLetras1 = len(palabra1)
cantidadLetras2 = len(palabra2)

if cantidadLetras1 > cantidadLetras2:
    dif = cantidadLetras1 - cantidadLetras2
    print("Esta palabra ",palabra1," es mas larga con diferencia de ",dif)
elif cantidadLetras1 < cantidadLetras2:
    dif = cantidadLetras2 - cantidadLetras1
    print("Esta palabra ",palabra2," es mas larga con diferencia de ",dif)
else:
    print("Las palabras tienen la mmisma longitud")       