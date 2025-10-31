
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Creamos la lista "números" y añadimos los valores

suma_total = sum(numeros) #Se realiza la suma total de los números
print(f"La suma total de los elementos es: {suma_total}\n")

num_mayor = max(numeros) #añade el numero mas grande
num_menor = min(numeros) #añade el numero mas pequeño
print(f"El numero más grande es: {num_mayor}")
print(f"El numero más pequeño es: {num_menor}\n")

promedio = suma_total / len(numeros) #se realiza la formula del promedio
print(f"El promedio de los numeros es: {promedio}\n") #lee el promedio
