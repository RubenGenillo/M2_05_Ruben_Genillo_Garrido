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

#Pido tres numeros
num1 = inputfloat("Dame un número:\n")
num2 = inputfloat("Dame otro número\n")
num3 = inputfloat("Dane un último número\n")

#Compruebo si los numeros estan en orden ascendente
if num1<num2<num3:
    print("Estan en orden ascendente")
else:
    print("No estan en orden ascendente") 