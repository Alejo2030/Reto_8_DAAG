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