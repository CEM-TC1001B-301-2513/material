# Generar una función de nombre número_primo(n) que
# reciba un número entero n y que como valor de retorno
# devuelva True o False en caso de que el número n
# sea un número primo o no
def número_primo(n : int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(número_primo(5))
print(número_primo(7))
print(número_primo(15))
print(número_primo(35))