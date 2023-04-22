# 9. Reto 8
import math

def sin_approx(x, n):# Definimos la función sin_approx que toma dos argumentos: x y n
    approx = 0# Inicializamos la variable approx en 0
    for i in range(n):# Iteramos n veces, sumando cada término de la serie de Maclaurin para el seno
        term = ((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1)# Calculamos cada término de la serie de Maclaurin utilizando la fórmula correspondiente
        approx += term # Sumamos el término actual a la aproximación acumulada
    error = abs(math.sin(x) - approx)# Calculamos el error absoluto entre la aproximación y el valor real de la función seno
    real = math.sin(x)
    p_error = error / real * 100
    
    print("Aproximación: ", approx)# Imprir la aproximación
    print("Valor real: ", math.sin(x))# Imprimimos  el valor real 
    print("Error: ", error)# Imprimimos el error 
    print(f"Porciento de error: {p_error:.6f}%")  # Imprime la diferencia entre ambos

    # Condiciones para que el porcentaje de error sea mayor o menor a 0.1 %
    if p_error <= 0.1:
        print (f"el porcentaje de error es menor a 0.1%: {p_error:.6f}") 
    else:
        print (f"el porcentaje de error es mayor a 0.1%: {p_error:.6f}") 


x = float(input("Ingrese el valor de x para aproximar la función seno: ")) #Solicitar valor de x
n = int(input("Ingrese el número de términos de la serie de Maclaurin que desea utilizar: ")) #solicitar valor de n 

sin_approx(x, n) # Llamar a la función sin_approx con los valores dados
