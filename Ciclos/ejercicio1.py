num1 = input("Digite un número: ")
i = 0

print("Tabla del ",str(num1) )
for i in range(11) :
    num1 = int(num1)
    res = num1 * i
    print(str(num1)," x ",str(i)," = ",str(res) )
    i = i + 1   