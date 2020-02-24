#validar caracter si es vocal o no

#c celcius f fare
t=input('Ingrese la teperatura numero y la letra(c para celsius, f para fahrenheit)\n  Ejemplo 12 c\n')

tt=t.split(' ')
if(tt[1]=='c'):
    print('la temp en grados f es: ',((int(tt[0])*1.8)+32))
elif(tt[1]=='f'):
    print('la temp en grados c es: ',((int(tt[0])-32)/1.8))
else:
    print('error')
