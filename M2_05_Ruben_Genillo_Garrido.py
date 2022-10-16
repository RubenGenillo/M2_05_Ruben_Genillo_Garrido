#Creo una función que me va servir para la mayoría de preguntas del ejercicio
def inputfloat(texto):
  while True:
    num = input(texto)
    try:
        num = float(num)
    except:
        print("no es un numero") 
    else:    
       return num


#1.

#Pido tres numeros
num1 = inputfloat("Dame un número:\n")
num2 = inputfloat("Dame otro número\n")
num3 = inputfloat("Dane un último número\n")

#Compruebo si los numeros estan en orden ascendente
if num1<num2<num3:
    print("Estan en orden ascendente")
else:
    print("No estan en orden ascendente")    


#2.

#Creo una función que pida y almacene un número de numeros en una lista 
def creatlist(texto,num):
    lista = []
    while len(lista) < num:
        num2 = inputfloat(texto)
        lista.append(num2)
    return lista    

#Creo una función que compruebe si lso números de una lista van en orden ascendente
def listOrdenAsc(lista):
 for i in range(len(lista)-1):
    if lista[i+1]<lista[i]:
        return False
 return True    

#pido tres numeros con creatlist y los almaceno en listanum
listanum = creatlist("Dame un número: ",3)

#Compruebo si los números de listanum están en orden ascendente con listOrdenAsc
print("La lista va en orden ascendente:", listOrdenAsc(listanum))


#3.

#Creo una función que lea las letras que escribas hasta un ".", y que cuente un caracter en específico y lo almacene en una variable
def contadorletr(x):
    contador = 0
    while True:
        texto = input()
        for i in texto:
            if i == x:
                contador +=1
            if i == ".":
                return contador

#Uso contadorletr para contar el número de "a" que se introduzcan
print("El número de 'a' escritas son: ", contadorletr("a"))              


#4

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