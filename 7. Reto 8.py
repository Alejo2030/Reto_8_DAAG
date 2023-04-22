# 7. Reto 8

for i in range(1, 10): # Se recorre un ciclo for del 1 al 9
    print(f"Tabla del {i}") # Se imprime la cabecera de la tabla
    print("\n")
    # Se recorre otro ciclo for del 1 al 10 para mostrar los valores de la tabla
    for j in range(1, 11):
        # Se imprime el resultado de la multiplicación
        print(f"{i} x {j} = {i*j}")
    # Se imprime una línea en blanco para separar las tablas
    print()