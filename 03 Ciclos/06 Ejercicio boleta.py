udfs = int(input("¿Cuántas udfs cursaste en el semestre?: "))
promedio = 0
for i in range(1, udfs+1):
    udf = float(input(f"Ingresa la calificación de tu uf{i}: "))
    # promedio = promedio + udf
    promedio += udf
# promedio = promedio / udfs
promedio /= udfs

# f-strings (formated-strings)
# : -> formato especial
# , -> separador de miles
# .n -> redondear a n decimales
# f -> mostrar como float
print(f"El promedio de tu semestre fue: {promedio:,.2f}")

