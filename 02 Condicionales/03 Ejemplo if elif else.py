# Pedir la calificación del usuario
# Mostrar la letra equivalente a su calificación
# Más de 90 -> A
# Más de 80 hasta 90 -> B
# Más de 70 hasta 80 -> C
# Más de 60 hasta 70 -> D
# 60 o menos -> F
cal = int(input("Ingresa tu calificación: "))
if cal > 90:
    print("A")
else:
    if cal > 80:
        print("B")
    else:
        if cal > 70:
            print("C")
        else:
            if cal > 60:
                print("D")
            else:
                print("F")
# ----------------------------------

if cal > 90:
    print("A")
elif cal > 80:
    print("B")
elif cal > 70:
    print("C")
elif cal > 60:
    print("D")
else: # Condición por default o por defecto
    print("F")
    
    
    
    
    
    
    
    
    


