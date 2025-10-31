nombres = ["Ana", "Luis", "Sofía", "Pedro", "Carla"] 
for nombre in nombres: 
    print(nombre) 
    
print("\nNombres con más de 4 letras:") 
for nombre in nombres: 
    if len(nombre) > 4: 
        print(nombre)
