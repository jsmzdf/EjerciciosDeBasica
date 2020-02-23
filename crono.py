# -*- hoding: utf-8 -*-
"""
hreated on Sat Feb 22 19:13:30 2020

@author: (╯°□°)╯︵ ┻━┻
"""
import time
def convertir(h,m,s):
       s=s/3600
       m=m/60
       h=h
       suma=s+m+h
       return suma
def contar(h,m,s):
       horas=0
       segun=0
       minu=0
       #horas<=h and segun<=s or minu<=m 
       x='q'
       while (x !='ok'):
           segun=segun+1           
           if(segun==60):
               segun=0
               minu=minu+1
           if(minu==60):    
               minu=0
               horas=horas+1
           print(str(horas)+':'+str(minu)+':'+str(segun))
           if(horas==h and minu==m and segun==s):
               x='ok'
           time.sleep(1)
horas=input('ingrese hora')
minutos=input('ingrese minutos')
segundos=input('ingrese segundos')
limite=contar(int(horas),int(minutos),int(segundos))
