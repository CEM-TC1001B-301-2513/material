# Entradas -> Parámetros
# Salida -> Valor de retorno

# Sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingresa x: "))
    y = float(input("Ingresa y: "))
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")

# suma1()

# Con parámetros y sin valor de retorno
def suma2(x : float, y : float) -> None:
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")
    
#suma2(15, 20)
#a = float(input("Ingresa x:"))
#b = float(input("Ingresa y: "))
#suma2(a,b)
#suma2("hola", "mundo")
    
# Con parámetros y valores de retorno
def suma3(x : float, y : float) -> float:
    resultado = x + y
    return resultado

print(suma2(5,7))
print(suma3(5,7))
#otra_operación = suma3(5,7) * 10
#print(f"Resultado: {otra_operación}")
    