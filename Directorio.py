def crear_diccionario_cuadrados():
    numero = int(input("Ingresa un número entero positivo: "))
    if numero <= 0:
        print("El número debe ser positivo.")
        return
    diccionario = {i: i**2 for i in range(1, numero + 1)}
    print("Diccionario de cuadrados:", diccionario)