'''
Created on 17 sept. 2019

@author: Inigo
'''
#Ejercicio1
import math
noAbsoluto = -23
print abs(noAbsoluto)

#Ejercicio2
suma1 = 23
suma2 = 45
print suma1 + suma2

#Ejercicio3
Celsius = 20
Fahr = ((9/5)*Celsius)+32
print Fahr,' grados fahrenheit'

#Ejercicio4
radio = 5.2
area = 4*math.pi*math.pow(5.2,2)
print area

#Ejercicio5
a=b=2
c=4
assert a == b
assert b < c
assert c > a

#Ejercicio6
x=[3,4]
y=[5,4]
d=math.sqrt(math.pow(x[0]-y[0],2)-math.pow(x[1]-y[1],2))
print d

#Ejercicio7
x,y=5,3
res = 5*math.pow(x,2)+math.sqrt(math.pow(x,2)+math.pow(y,2))+math.pow(math.e,math.log(x,math.e))
print res

#Ejercicio8
coleccion = [1,2,3,4,5]
#es un vector de Integers

#Ejercicio9
coleccionCon4 = [7,4,5,4,6,8,4,9]
#este for itera uno a uno por cada uno de la lista para cambiar los cuatros por dieces
for i in range(len(coleccionCon4)):
    if coleccionCon4[i] == 4:
        coleccionCon4[i] = 10
print coleccionCon4

#Ejercicio10
lista = [6,11,27,32,33]
NuevaLista=[]
#este for itera por cada uno de los objetos de la lista y el while los hace iterar hasta que se reduzcan
#a 1
for i in range(len(lista)):
    j = lista[i]
    cont = 0
    while j != 1:
        if j%2 == 0:
            j = j/2
            cont = cont+1
        else:
            j = (j*3)+1
            cont = cont+1
    NuevaLista.append(cont)
print NuevaLista

#Ejercicio11
matriz = [[2,3,4],[3,2,1],[-2,-3,-4],[-1,2,3],[-2,4,1],[3,-3,1]]

#Ejercicio12
x = -2
contador = 0
#el for anidado itera por cada uno de los elementos de la matriz anidada y luego se comprueba si el
#elemento actual es el mismo que el de entrada(x)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if x == matriz[i][j]:
            contador = contador +1
print contador

#Ejercicio13
contador = 0 
#el for anidado permite examinar si hay algun elemento de la matriz anidada entre 4 y 7
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if 4 <= matriz[i][j] and 7>= matriz[i][j]:
            contador = contador +1
if contador == 0:
    print 'hay numeros entre 4 y 7'
else:
    print 'no hay numeros entre 4 y 7'

#Ejercicio14
listaNumEnteros = [-2, 3, 4, -7, 10, -234]
listaBooleanos = [True,True,True,True,False,False]
#esta funcion calcula cuantos aciertos hay entre las dos matrices que indican si positivo o negativo
def numTrueFalse(parametro1,parametro2):
    contadorTrue = 0
    contadorFalse = 0
    #el for itera por los elementos de la lista para poder comprobar si corresponde True con positivo
    #y False con negativo
    for i in range(len(parametro1)):
        listaDevolver=[]
        if parametro1[i] >= 0 and parametro2[i] == True:
            contadorTrue = contadorTrue + 1
        if parametro1[i]<0 and parametro2[i] == False:
            contadorFalse = contadorFalse + 1
        
    listaDevolver.append(contadorTrue)
    listaDevolver.append(contadorFalse)
    return listaDevolver
#se llama a la funcion pasandole como parametros las dos listas y como respuesta se recive la lista de
#aciertos
numTrueFalse = numTrueFalse(listaNumEnteros,listaBooleanos)
print numTrueFalse
