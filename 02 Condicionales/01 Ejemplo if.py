edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    #ine = input("¿Tienes tu INE? Sí o no: ").lower().strip()
    ine = int(input("¿Tienes INE?? 1)Sí, 2)No: "))
    print("Ya eres mayor de edad")
    #if ine == "sí":
    if ine == 1:
        print("Ya puedes votar")
    