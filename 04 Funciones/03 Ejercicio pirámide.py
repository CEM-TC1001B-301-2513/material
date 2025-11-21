# Crear una función llamada pirámide que reciba como
# parámetro un número entero y que imprima una
# pirámide de asteriscos
# Ejemplo:
# pirámide(5)
# *
# **
# ***
# ****
# *****

def pirámide(n : int) -> None:
    for i in range(1, n+1):
        print("*" * i)
        
pirámide(5)


