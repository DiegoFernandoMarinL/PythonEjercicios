año = int(input("Digite año: "))

if año % 4 == 0:  # Divisible por 4
    if año % 100 == 0:  # Divisible por 100
        if año % 400 == 0:  # Divisible por 400
            print(f"El año {año} es bisiesto")
        else:
            print(f"El año {año} no es bisiesto")
    else:
        print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")