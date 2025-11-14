# Sumatoria de 1 a n
# Ingresar n (número entero)
# Calcular con un ciclo la sumatoria de 1 hasta n
# Ejemplo si n = 5:
# 1+2+3+4+5->15
n = int(input("Ingrese el valor de n: "))
suma = 0
for i in range(1, n+1):
    suma = suma + i
print(f"La suma de 1 hasta {n} es: {suma}")
    
    