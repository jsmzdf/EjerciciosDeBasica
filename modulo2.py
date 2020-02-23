# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:48:34 2020

@author: (╯°□°)╯︵ ┻━┻
"""
def convertbina( bina ):
     l = len(bina) - 1
     ente = 0
     for i in bina:
          Pow = 2 ** l
          ente = ente + ( int(i) * Pow)
          l = l - 1
     return ente
def convertente(num):
     bina = ""
     while (True):
          aux = str( num % 2 )
          num = int( num / 2 )
          bina = aux + bina
          if (num <= 1):
               bina = ( str( num ) if num > 0 else "" ) + bina
               break
     return bina
def suma(a,b):
    return convertente(convertbina(a)+ convertbina(b))
def multipicacion(a,b):
    return convertente(convertbina(a)* convertbina(b))
def divicion(a,b):
    return convertente(int(convertbina(a) // convertbina(b)))
def resta(a,b):
    return convertente(convertbina(a)- convertbina(b))
 