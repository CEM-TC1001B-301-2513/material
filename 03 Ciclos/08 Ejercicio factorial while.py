# Ingresar un número entero n
# Calcular su factorial n!
# Ejemplo 5!:
# 5*4*3*2*1->120
n = int(input("Ingresa el valor de n: "))
factorial = 1
i = n
while i >= 1:
    # factorial = factorial * i
    factorial *= i
    # i = i - 1
    i -= 1
print(f"El resultado de {n}! = {factorial}")
    
    