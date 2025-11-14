# Tendremos una lista con nombres de alumnos
# Pedir como entrada el nombre de un alumno
# Usando ciclos y condicionales, revisar si el alumno
# está dentro de la lista
# Mostrar un mensaje si sí está
# Mostrar un mensaje si no está

alumnos = ["Juan", "Enrique", "Israel", "Lucio", "Axel"]
nombre = input("Ingrese el nombre a buscar: ")
presente = False
for alumno in alumnos:
    if nombre == alumno:
        presente = True
if presente == True:
    print(f"{nombre} está en la lista.")
else:
    print(f"{nombre} no está en la lista.")
    
# ------------------------------------------

for alumno in alumnos:
    if nombre == alumno:
        print(f"{nombre} está en la lista.")
        break
else: # Se ejecuta si el ciclo no se detuvo con un break
    print(f"{nombre} no está en la lista.")








