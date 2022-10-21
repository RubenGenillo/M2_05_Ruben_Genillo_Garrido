#Creo una función que recorra una lista, muestre cada palabra y compruebe cual es la palabra con más caracteres
def maxlen(lista):
 mayor = ""    
 for i in lista:
    print(i,"longitud:", len(i))
    if len(i) > len(mayor):
        mayor = i
 return mayor    

#Creo una lista de palabras
colores = ['Blanco', 'Azul', 'Naranja', 'Amarillo', 'Verde'] 
  
#Muestro los elementos de la lista junto a su longitud y la palabra con más caracteres
print("la palabra con mayor caracteres fue", maxlen(colores))