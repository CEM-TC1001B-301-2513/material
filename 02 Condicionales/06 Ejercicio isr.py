# Pedir el salario de una persona
# Indicar cuánto se le descuenta de ISR
# Mostrar cuánto le queda como salario
salario = float(input("Ingresa tu salario: "))
if salario <= 578.52:
    inferior = 0.01
    porcentaje = 1.92
    cuota = 0
elif salario <= 4910.18:
    inferior = 578.53
    porcentaje = 6.4
    cuota = 11.11
elif salario <= 8629.20:
    inferior = 4910.19
    porcentaje = 10.88
    cuota = 288.33
isr = (salario - inferior) * porcentaje / 100 + cuota
salario_después_impuestos = salario - isr
print(f"El ISR que se te cobró fue de: ${isr:,.2f}")
print(f"Tu salario después de impuestos fue de: ${salario_después_impuestos:,.2f}")




