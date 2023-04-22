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

```





### :lock: PUNTO #6 
+ Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

#### :unlock: CODIGO DEL PROGRAMA


```ruby

```




### :lock: PUNTO #7 
+ Diseñe un programa que muestre las tablas de multiplicar del 1 al 9..

#### :unlock: CODIGO DEL PROGRAMA
```ruby

```







### :lock: PUNTO #8  
+ Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$

#### :unlock: CODIGO DEL PROGRAMA
```ruby

```




### :lock: PUNTO #9  
+ Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

#### :unlock: CODIGO DEL PROGRAMA
```ruby

```




### :lock: PUNTO #10 
+ Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$

#### :unlock: CODIGO DEL PROGRAMA
```ruby

```




## :sparkles: Esto es todo hoy amigos :blush:, espero poder haberlos ayudado he inspirado para encontar nuevas soluciones para nuevos retos :sparkles: 
