def calcularDistancia(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
var1=float(input('ingrese x0\n'))
var2=float(input('ingrese x1\n'))
var3=float(input('ingrese y0\n'))
var4=float(input('ingrese y1\n'))
print('La distancia es \n'+ str(calcularDistancia(var2,var1,var4,var3)))
