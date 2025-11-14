# Ciclo while

# for i in range(5)
i = 0 # inicio
while i < 5: # condición de salida o final
    print(f"El valor de i es: {i}")
    # i = i + 1
    i += 1 # paso
    
print("-" * 30)

lista = [7,4,5675,"hola",[6,4,2],True]
print(lista[3])
print(len(lista))
# for i in lista:
i = 0
while i < len(lista):
    # lista[i]
    print(f"lista[{i}] = {lista[i]}")
    i += 1
    
i = -1
while i >= -len(lista):
    # lista[i]
    print(f"lista[{i}] = {lista[i]}")
    i -= 1

print("-" * 30)

opción = 0
while opción != 3:
    # operaciones
    opción = int(input("""Menu:
1) Opción 1
2) Opción 2
3) Salir
Ingresa tu opción: """))
    #while opción != 1 and opción != 2 and opción != 3:
    while opción not in [1,2,3]:
        print("Error, debes elegir 1, 2 o 3")
        opción = int(input("""Menu:
1) Opción 1
2) Opción 2
3) Salir
Ingresa tu opción: """))

