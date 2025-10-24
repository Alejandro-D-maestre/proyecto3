cadena = input("Ingrese una cadena de texto: ")
def contar_caracteres(cadena):
    Con_cadena = {}
    for caracter in cadena:
        if caracter in Con_cadena:
            Con_cadena[caracter] += 1
        else:
            Con_cadena[caracter] = 1
    return Con_cadena
resultado = contar_caracteres(cadena)
print("Conteo de caracteres:", resultado)
