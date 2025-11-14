# Tabla de multiplicar
# Ingresar un número n
# Mostrar su tabla de multiplicar hasta el 10 con formato:
# Por ejemplo, si n = 5
# 1 x 5 = 5
# 2 x 5 = 10
# ...
# 10 x 5 = 50

n = int(input("Ingrese el valor de n: "))
for i in range(1,11):
    mult = n * i
    print(f"{i} x {n} = {mult}")
