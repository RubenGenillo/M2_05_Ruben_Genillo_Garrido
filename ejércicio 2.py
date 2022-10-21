#Creo una función que solo admita números
def inputfloat(texto):
  while True:
    num = input(texto)
    try:
        num = float(num)
    except:
        print("no es un numero") 
    else:    
       return num

#Creo una función que pida y almacene un número de numeros en una lista 
def creatlist(texto,num):
    lista = []
    while len(lista) < num:
        num2 = inputfloat(texto)
        lista.append(num2)
    return lista    

#Creo una función que compruebe si los números de una lista van en orden ascendente
def listOrdenAsc(lista):
 for i in range(len(lista)-1):
    if lista[i+1]<lista[i]:
        return False
 return True    

#pido tres numeros con creatlist y los almaceno en listanum
listanum = creatlist("Dame un número: ",3)

#Compruebo si los números de listanum están en orden ascendente con listOrdenAsc
print("La lista va en orden ascendente:", listOrdenAsc(listanum))