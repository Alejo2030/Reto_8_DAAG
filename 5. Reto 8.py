#5. reto 8
l = int(input("Ingrese un número entero al que quiera que este elevado el número 2: ")) # pedimos al usuario que introduzca el valor de n
result = 1 # valor inicial del resultado

for i in range(l): # Iniciamos un ciclo for que se ejecuta n veces
    result *= 2 # En cada iteración, multiplicamos resultado por 2 y lo asignamos a resultado

print("El resultado de 2 elevado a la " + str(l)+ " es " + str(result)) # resultado final: 2 elevado a la potencia n