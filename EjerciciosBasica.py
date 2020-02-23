# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:44:44 2020

@author: (╯°□°)╯︵ ┻━┻
"""

import math

#################################ejercicios simples
#vlumen de esfera

r=input("ingrese radio")
print("el volumen de la esfera es: ",(3/4)*math.pi*int(r)**3)
#perimetro y área de circulferencia
r=input("ingrese radio")
print("la longitud de la circunferencia es: ",2*math.pi*int(r)**2)
print("el área de la circunferencia es: ",math.pi*int(r)**2)
#################··################################condicional
#validar caracter si es vocal o no
er=input("ingrese caracter\n")
l=['a','e','i','o','u','A','E','I','O','U']
a=[x for x in l if er==x]
if(a ==[]):

    print('el caracter',er,'no es vocal')

if(a !=[]):

    print('el caracter',er,' es vocal')
#c celcius f fare
t=input('Ingrese la teperatura numero y la letra(c para celsius, f para fahrenheit)\n  Ejemplo 12 c\n')

tt=t.split(' ')
if(tt[1]=='c'):
    print('la temp en grados f es: ',((int(tt[0])*1.8)+32))
elif(tt[1]=='f'):
    print('la temp en grados c es: ',((int(tt[0])-32)/1.8))
else:
    print('error')
######################################################ciclos
#multiplos de 5 hasta 100
a=[x +1 for x in range(100) if (x+1)%5==0]
print(a)
num=input('num\n')
mul=[(x+1)*int(num) for x in range(10)]
print(mul)
#suma de los numeros dados por el usu
ing=input('ingrese un numero\n')
c=0
for i in range(int(ing)+1):
    c=c+i 
print(c)
##########################################################colescciones  
#20 primeros numeros pares y calcular la suma
pri20=[(x)*2 for x in range(20)]
c=0
for i in (pri20):
    c=c+i 
print(c)
#multitoplicar elemenots de una matriz 3*4 por elemento 2,2
matriz=[[1.0,2.0,3.0,4.0], [11.0,22.0,31.0,41.0], [14.0,25.0,36.0,47.0]]
matriz1=matriz.copy()
muneroselect=matriz[1][1]
for i in range(3):
    for j in range(4):
        matriz[i][j]=matriz[i][j]/muneroselect
        print(matriz[i][j])
print('la operacion de la matriz por el elemto M(2,2) es \n',matriz)
##################################################################cadenas
#quitar espacio
texto=input("ingrese texto\n")
print(texto.replace(" ",""))
#mostrar caracteres al revez
textoa=input("ingrese texto\n")
cadenab=[x for x in reversed(textoa)]

################################################################### fucniones y lo otro
#
def calcularDistancia(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
var1=float(input('ingrese x0\n'))
var2=float(input('ingrese x1\n'))
var3=float(input('ingrese y0\n'))
var4=float(input('ingrese y1\n'))
print('La distancia es \n'+ str(calcularDistancia(var2,var1,var4,var3)))
#es numero o no
t=input('Ingrese un caracter o diginto\n')
def num_o_no(v):
    es=''
    validar=[str(x+1) for x in range(10)]
    for i in validar:
        print(type(i),type(v))
        if(i==v):
            es= "es numero"
            break
        else:
            es= 'no es numero'
    return es
            
print('El caracter ingresado es: '+str(num_o_no(t)))
##############################################################################recursividad
base = int(input("ingrese la base: "))
exponente = int(input ("ingrese el exponente: "))
def pot(num,exp):
    if exp ==0:return 1
    if exp ==1: return num
    return pot(num,exp-1)*num
print('la potencia'+pot(base,exponente))
#
imgresodenumfob=int(input('ingrese un numero para calcular fibo'))
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print('El numero de la serie de fibo: ',fib(imgresodenumfob))
#################################################################################modulos
#suma resta dicision potencia enteres
import modulo1

a=float(input('ingrese valor a'))
b=float(input('ingrese valor b'))
print('la suma es:',modulo1.suma(a,b))
print('la multiplicación es:',modulo1.multipicacion(a,b))
print('la resta es:',modulo1.resta(a,b))
if(b>0):
    print('la divición es:',modulo1.divicion(a,b))
else:
    print('b es 0')
print('la potencia es:',modulo1.potencia(a,b))

#operaciones de binarios
import modulo2
a=(input('ingrese valor binario entero a'))
b=(input('ingrese valor binario entero b'))
print('la suma es:                 ',modulo2.suma(a,b))
print('la multiplicación es:       ',modulo2.multipicacion(a,b))
print('la resta es:                ',modulo2.resta(a,b))
aux=int(b)
if(aux>0):
    print('la divición entera es:  ',modulo2.divicion(a,b))
else:
    print('b es 0')
##############################################################################archivo
import codecs
archi1=codecs.open("datos.txt","w","utf-8") 
codigoAscii=[x for x in range(256) if x!=128]
for x in range(256):
    archi1.write(chr(x)+str(ord(chr(x)))+'\n')
archi1.close()
f=codecs.open("datos.txt","r","utf-8") 
for line in f.readlines():
    print(line)
################################################################################varos
#pica y fijas
