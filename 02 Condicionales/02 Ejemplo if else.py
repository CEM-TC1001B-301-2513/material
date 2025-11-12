edad = int(input("Indica tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    restante = 18 - edad
    print(f"Te faltan {restante} años para ser mayor de edad")