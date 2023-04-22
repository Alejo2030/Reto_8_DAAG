#10. Reto 8
import math #importar de math

def arctan_approx(x, n):
    if x < -1 or x > 1: # Aseguramos que el valor de x está en el rango [-1, 1]
        print("Error: el valor de x debe estar en el rango [-1, 1].")
        return

    # Inicializamos la variable approx en 0
    approx = 0
    for i in range(n):# Iteramos n veces, sumando cada término de la serie de Maclaurin para la arcotangente
        term = ((-1)**i * x**(2*i + 1)) / (2*i + 1) # Calculamos cada término de la serie de Maclaurin utilizando la fórmula correspondiente
        approx += term# Sumamos el término actual a la aproximación acumulada


    error = abs(math.atan(x) - approx)# Calculamos el error absoluto entre la aproximación y el valor real de la función arcotangente
    real = math.atan(x)
    p_error = error / real * 100

    # Imprimimos la aproximación, el valor real y el error en la pantalla
    print("Aproximación: ", approx)
    print("Valor real: ", math.atan(x))
    print("Error: ", error)
    print(f"Porciento de error: {p_error:.6f}%")  # Imprime la diferencia entre ambos


    # Condiciones para que el porcentaje de error sea mayor o menor a 0.1 %
    if p_error <= 0.1:
        print (f"el porcentaje de error es menor a 0.1%: {p_error:.6f}") 
    else:
        print (f"el porcentaje de error es mayor a 0.1%: {p_error:.6f}") 



x = float(input("Ingrese el valor de x para aproximar la función arcotangente: ")) #Ingresar el valor x
n = int(input("Ingrese el número de términos de la serie de Maclaurin que desea utilizar: ")) #Ingresar el valor de n 


arctan_approx(x, n)# Llamar a la función arctan_approx para utilizar los valores dados 
