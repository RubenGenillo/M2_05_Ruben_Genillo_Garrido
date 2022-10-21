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