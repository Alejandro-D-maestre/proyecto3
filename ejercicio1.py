#crea una lista llamada frutas con los elementos: "manzana", "banano", "pera", "uva", "naranja". 
#Muestra el primer y el último elemento. Agrega la fruta "mango" al final. 
#Elimina "pera" de la lista. Imprime la lista final.

Fruta=["manzana", "banano", "pera", "uva", "naranja"]
print("Primera fruta:", Fruta[0])
print("Última fruta:", Fruta[-1])
Fruta.append("mango")
Fruta.remove("pera")
print("Lista final de frutas:", Fruta)