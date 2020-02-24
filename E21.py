er=input("ingrese caracter\n")
l=['a','e','i','o','u','A','E','I','O','U']
a=[x for x in l if er==x]
if(a ==[]):

    print('el caracter',er,'no es vocal')

if(a !=[]):

    print('el caracter',er,' es vocal')
