#2. Reto 8
Pares = [] # Lista abierta de numeros pares
Impares = [] # Lista abierta de numeros impares
range(1,1001) # Definir el rango desde uno 
for l in range (1,1001):
    if l%2==0: #definir if si el residuo es 0
        Pares.append(l) #Agregar el dato a la lista pares si su resido es 0
    else:
        Impares.append(l) #Si el residuo no es cero agregarlo a la lista impares 
print(" Los numeros pares en el rango de 0 a 1000 son " + str(Pares)) #Imprimir la lista de los numeros pares
print("\n") #Dejar un espacio
print(" Los numeros pares en el rango de 0 a 1000 son " + str(Impares)) #Imprimir la lista de los numeros impares