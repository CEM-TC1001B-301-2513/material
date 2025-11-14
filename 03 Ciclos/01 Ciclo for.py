# ciclo for
# range(final) -> Secuencia de números enteros que
# inicia en 0, termina antes de final
# y avanza de 1 en 1
for i in range(5):
    print(f"El valor de i es: {i}")

print("-" * 30)

# range(inicio, final) -> Secuencia de números enteros que
# inicia en inicio, termina antes de final
# y avanza de 1 en 1
for i in range(5,10):
    print(f"El valor de i es: {i}")
    
print("-" * 30)

# range(inicio, final, paso) -> Secuencia de números enteros que
# inicia en inicio, termina antes de final
# y avanza de paso en paso
for i in range(5, 15, 4):
    print(f"El valor de i es: {i}")
    
print("-" * 30)

for i in range(10, 1, -1):
    print(f"El valor de i es: {i}")
    
print("-" * 30)

texto = "Hola mundo"
for i in texto:
    print(f"El valor de i es: {i}")

print("-" * 30)

lista = [3,6,True,"hola",[1,2,3],False]
for i in lista:
    print(f"El valor de i es: {i}")
    