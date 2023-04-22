#6. Reto 8

l = int(input("Ingresa un número natural: ")) #Ingrese un valor deseado entero que va ser por el que esté elevado s
s = float(input("Ingresa un número real: ")) #Ingrese número que quiere elevar a la l


resultado = 1 #Inicializar la variable resultado en 1

# Se utiliza un ciclo for para multiplicar x por sí mismo n veces
for i in range(l):
    resultado *= s

# Se imprime el resultado obtenido en la última iteración del ciclo for
print(" El resultado de " + str(s) + " elevado a la " + str(l) + " es " + str(resultado) )