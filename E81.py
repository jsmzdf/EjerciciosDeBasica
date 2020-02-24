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
