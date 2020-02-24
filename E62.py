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
