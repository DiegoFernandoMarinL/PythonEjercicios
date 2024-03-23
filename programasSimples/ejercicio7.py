horaActual = int(input("Digite hora actual: "))
horas = int(input("Digite cantidad de horas: "))

horaFinal = (horaActual + horas) % 24

print(f"En {horas} horas, el reloj marcara las {horaFinal}")
