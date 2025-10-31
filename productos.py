produc = [] 
precios = [] 

for i in range(5): 
    nombre = input(f"Escriba el nombre de su producto {i+1}: ") 
    precio = float(input(f"Escriba el precio de {nombre}: ")) 
    produc.append(nombre) 
    precios.append(precio) 
total = sum(precios) 

indice_max = precios.index(max(precios)) 
indice_min = precios.index(min(precios)) 

print(f"\nEl precio total de los productos es: {total}") 
print(f"El producto más caro es: {produc[indice_max]} con un precio de {precios[indice_max]}") 
print(f"El producto más barato es: {produc[indice_min]} con un precio de {precios[indice_min]}")
