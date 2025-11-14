import random
seguir_jugando = 1
while seguir_jugando != 2:
    aleatorio = random.randint(1,100)
    respuesta = 0
    intentos = 0
    while aleatorio != respuesta:
        respuesta = int(input("Adivina el número: "))
        if respuesta > aleatorio:
            print("El número que buscas es menor al ingresado.")
        elif respuesta < aleatorio:
            print("El número que buscas es mayor al ingresado.")
        intentos += 1
    print(f"Adivinaste, te tomó {intentos} intentos.")
    seguir_jugando = int(input("¿Volver a jugar? 1)Sí, 2)No: "))