edades = [12, 17, 18, 20, 15, 22, 13] 
mayores = [] 

for edad in edades: 
    if edad >= 18: 
        mayores.append(edad) 
        
print(f"Las personas mayores de edad es: {len(mayores)}") 
print(f"Las edades mayores o iguales a 18 son: {mayores}")
