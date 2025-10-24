frutas = {
    "Manzana": 3.50,
    "Banana": 2.80,
    "Naranja": 4.00,
    "Pera": 3.20
}
seguir = "si"
while seguir == "si":
    fruta = input("Escribe el nombre de la fruta: ").lower()
    if fruta in frutas:
        cantidad = float(input("¿Cuántos kilos se vendieron?: "))
        precio = frutas[fruta] * cantidad
        print("El precio total es:", precio)
    else:
        print("Lo siento, esa fruta no está en la lista.")
    seguir = input("¿Quieres hacer otra consulta? (si/no): ").lower()
print("Fin del programa")
