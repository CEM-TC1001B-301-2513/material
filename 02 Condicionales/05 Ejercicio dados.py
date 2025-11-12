# Simular la tirada de dos dados
# Preguntar al usuario que adivine el resultado
# Las opciones serán:
# 1) La suma de los dados es menor a 7
# 2) La suma de los dados es igual a 7
# 3) La suma de los dados es mayor a 7
# Mostrar al usuario la suma después de que adivinó
# Indicar al usuario si atinó o falló
import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma = dado1 + dado2
tiro = int(input("""Bienvenido al juego, selecciona:
1) La suma de los dados es menor a 7
2) La suma de los dados es igual a 7
3) La suma de los dados es mayor a 7
¿Cuál es tu selección?: """))
print(f"""El dado 1 cayó: {dado1}
El dado 2 cayó: {dado2}
La suma de los dados fue: {suma}""")
if suma < 7 and tiro == 1 or \
   suma == 7 and tiro == 2 or \
   suma > 7 and tiro == 3:
    print("Atinaste, has ganado.")
else:
    print("No atinaste, suerte para la próxima.")





