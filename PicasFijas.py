# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:51:28 2020

@author: (╯°□°)╯︵ ┻━┻
"""
from random import randint
def crearNum():
    compu=[-1,-1,-1]
    primer=randint(0,9)
    compu[0]=primer
    while(compu[1]==-1 or compu[2]==-1):
        primer=randint(0,9)
        if(compu[0]!=primer and compu[1]==-1):
           compu[1]=primer
        if(compu[1]!=primer and compu[0]!=primer):
           compu[2]=primer
    return compu
prueba=crearNum()
def buscar(com,usu):
    sacarPicas=0
    fijas=0
    f=[(1,x) for x in range(len(usu)) if com[x]==usu[x]]
    preP=[ (com[x],usu[x]) for x in range(len(com)) if com[x]!=usu[x]]
    p=[(x,y)  for y in preP  for x in preP if x!=y and x[1]==y[0]]
    for i in range(0,len(f)+1):
        fijas=i
    for i in range(0,len(p)+1):        
        sacarPicas=i
    return sacarPicas,fijas
intentos=1
jugar='q'
menu=1
numerocom=crearNum()
print(numerocom)
while(jugar!='s'):    
    if(menu==1):
        print('Picas y fijas')
        print('salir: :   s ')
        print('jugar:   y')
        print('reiniciar: r')
        jugar=input('Ingrese accción\n')
        
        menu=0    
    if(jugar=='r'):
       numerocom=crearNum() 
       print(numerocom)
       intentos=1 
       jugar='y'
    if(jugar=='y'):
        print('ingrese el numero de 3 digitos sin repetir')
        num=str(input())
        picas,fijas=buscar([int(x) for x in num],numerocom)
        print('para el número ',num,' tiene ',picas,'picas y ',fijas,'fijas en el intento numero',intentos)
        if(fijas==3):
            print('ha adivinado el número')
            print('¡Felicidades!')
            menu=0
            jugar='q'
            numerocom=crearNum()
            intentos=0
    if(jugar!='r' and jugar!='y'and jugar!='q'):
        print('igrese valores válidos')
        menu=1
    intentos+=1
