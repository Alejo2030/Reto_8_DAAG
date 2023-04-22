# 8. Reto 8
import math  # Importamos el módulo math que contiene la función factorial.

def exp_approx(x, n):  # Definimos una función que toma dos argumentos: x y n.
    approx = 0  # Inicializamos la variable approx en 0.
    for i in range(n):  # Iteramos desde 0 hasta n-1.
        approx += (x**i) / math.factorial(i)  # Sumamos cada término de la serie de Maclaurin.
    real = math.exp(x)
    error = abs(math.exp(x) - approx)  # Calculamos el error absoluto entre la aproximación y el valor real.
    p_error = error / real * 100
    
    print(f"Aproximación: {approx:.6f}") # Imprime la aproximación
    print(f"Valor real: {real:.6f}") # Imprime  el valor real 
    print(f"Diferencia: {error:.6f}")  # Imprime la diferencia entre ambos
    print(f"Porciento de error: {p_error:.6f}%")  # Imprime la diferencia entre ambos

    # Condiciones para que el porcentaje de error sea mayor o menor a 0.1 %
    if p_error <= 0.1:
        print (f"el porcentaje de error es menor a 0.1%: {p_error:.6f}") 
    else:
        print (f"el porcentaje de error es mayor a 0.1%: {p_error:.6f}") 

x = float(input("Ingrese el valor de x para aproximar la función exponencial: "))# Solicitar el valor de x
n = int(input("Ingrese el número de términos de la serie de Maclaurin que desea utilizar: "))# Solicitar el valor de  n.

exp_approx(x, n)# Llamar a la función exp_approx con los valores dados
