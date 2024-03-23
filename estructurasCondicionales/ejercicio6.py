caracter = input("Ingrese caracter: ")

if caracter.isalpha():
    if caracter.isupper():
        print("La letra es mayuscula")
    else:
        print("La letra es minuscula")    
elif caracter.isdigit():
    print("El caracter es un numero")  
else:
    print("El caracter ingrasado no es numero ni letra")      
