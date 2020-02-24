base = int(input("ingrese la base: "))
exponente = int(input ("ingrese el exponente: "))
def pot(num,exp):
    if exp ==0:return 1
    if exp ==1: return num
    return pot(num,exp-1)*num
print('la potencia'+pot(base,exponente))
