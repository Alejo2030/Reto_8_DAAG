#4. Reto 8
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