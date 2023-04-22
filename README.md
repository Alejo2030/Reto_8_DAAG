# Reto_8_DAAG
## En este repositorio se encuentra el desarrollo del reto 8, vamos allá!!!
 ## :+1: Reto 8 :+1:

## 1.EJERCICIO DE CLASE
### :unlock: EJERCICIO #1 
+ Ejercicio: Qué se genera con range(-2)?

####  CODIGO DEL PROGRAMA

```ruby
range(-2) # No genera una secuencia
for num in range(-2): print(num) # No imprime el rango
```

### Codigo donde se obtiene un objeto de rango vacío. Esto se debe a que solo se da el primer argumento de la función range() que especifica el valor de inicio del rango, pero no el el segundo argumento que especifica el valor final del rango, lo que significa que el rango es indefinido y no se puede generar ningún número. x no ingresa al ciclo




## PUNTOS DEL RETO
### :lock: PUNTO #1 
+ Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

#### :unlock: CODIGO DEL PROGRAMA

```ruby
#1.Reto 8
range(0,101) #Dar el rango
for r in range (0,101): #Definir for en la variable r, en un rango hasta 100
    print("El cuadrado de " + str(r) + " es " + str(r**2)) #Definir que muestra el codigo
```





### :lock: PUNTO #2 
+ Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.


#### :unlock: CODIGO DEL PROGRAMA

```ruby
Pares=[]
Impares=[]
for i in range(1,1001):
    if i%2==0:
        Pares.append(i)
    else:
        Impares.append(i)
print("Los numeros pares en el rango de 0 a 1000 son " + str(Pares))
print("\n")
print("Los numeros impares en el rango de 0 a 1000 son " + str(Impares))
```




    
### :lock: PUNTO #3  
+ Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado


#### :unlock: CODIGO DEL PROGRAMA
```ruby
#3. Reto 8
s=int(input("Ingresar numero mayor igual que 2 del cual dese saber los numeros pares antes de el : "))  # Se pide un número entero cualquiera
def pares_hasta_el_numero(s): # Definimos unas función  para ir hasta s 
    l = [] # Hacemos una lista vacia 
    for i in range(1,s+1): # Establecemos el rango y lo unimos a la lista 
        if i%2==0: #si el residuo es igual a cero es par, unirlo a la lista 
            l.insert(0,i)
    return l
print(pares_hasta_el_numero(s)) # Imprimimos los numeros pares que se encuentran en el rango
print( "Estos son los numeros pares hasta " + str(s)) # Imprimir enunciado, para aclarar
```




### :lock: PUNTO #4 
+ Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial


#### :unlock: CODIGO DEL PROGRAMA
```ruby
def dar_factorial(l): # Definir una función para factorial 
    facto = 1 # Inicializar la variable factorial en 1
    for i in range(1,l+1):  # Bucle para multiplicar los números del 1 al n y calcular su respctivo factorial
        facto = i * facto # Dar el factorial de cada número en el bucle
        print(i, "! es igual a ", facto)
    # Devolver el factorial del número dado
    return facto

if __name__ == "__main__": #Ejecutar función
    l = int(input("Ingrese un número entero del cual desee conocer su factorial y sus factoriales antes de el : ")) #Pedir al usuario un numero l para hacer el factorial desde 1 hasta l
    fact = dar_factorial(l) #Solicitar la función y que plasta cada numero dado "facto"

```




### :lock: PUNTO #5  
+ Calcular el valor de 2 elevado a la potencia n usando ciclos for.


#### :unlock: CODIGO DEL PROGRAMA
```ruby
#5. reto 8
l = int(input("Ingrese un número entero al que quiera que este elevado el número 2: ")) # pedimos al usuario que introduzca el valor de n
result = 1 # valor inicial del resultado

for i in range(l): # Iniciamos un ciclo for que se ejecuta n veces
    result *= 2 # En cada iteración, multiplicamos resultado por 2 y lo asignamos a resultado

print("El resultado de 2 elevado a la " + str(l)+ " es " + str(result)) # resultado final: 2 elevado a la potencia n
```





### :lock: PUNTO #6 
+ Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

#### :unlock: CODIGO DEL PROGRAMA


```ruby
#6. Reto 8

l = int(input("Ingresa un número natural: ")) #Ingrese un valor deseado entero que va ser por el que esté elevado s
s = float(input("Ingresa un número real: ")) #Ingrese número que quiere elevar a la l


resultado = 1 #Inicializar la variable resultado en 1

# Se utiliza un ciclo for para multiplicar x por sí mismo n veces
for i in range(l):
    resultado *= s

# Se imprime el resultado obtenido en la última iteración del ciclo for
print(" El resultado de " + str(s) + " elevado a la " + str(l) + " es " + str(resultado) )
```




### :lock: PUNTO #7 
+ Diseñe un programa que muestre las tablas de multiplicar del 1 al 9..

#### :unlock: CODIGO DEL PROGRAMA
```ruby
# 7. Reto 8

for i in range(1, 10): # Se recorre un ciclo for del 1 al 9
    print(f"Tabla del {i}") # Se imprime la cabecera de la tabla
    print("\n")
    # Se recorre otro ciclo for del 1 al 10 para mostrar los valores de la tabla
    for j in range(1, 11):
        # Se imprime el resultado de la multiplicación
        print(f"{i} x {j} = {i*j}")
    
```







### :lock: PUNTO #8  
+ Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$

#### :unlock: CODIGO DEL PROGRAMA
```ruby
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
```




### :lock: PUNTO #9  
+ Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

#### :unlock: CODIGO DEL PROGRAMA
```ruby
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
```




### :lock: PUNTO #10 
+ Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$

#### :unlock: CODIGO DEL PROGRAMA
```ruby
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
```




## :file_folder: Este es el desarrollo del reto 8 en su totalidad, espero les sirva en su camino al aprendizaje!!!
## ¡¡ Vamos Manchester City!! :one::one::one::one::one::one::one:
