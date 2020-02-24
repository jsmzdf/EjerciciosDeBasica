imgresodenumfob=int(input('ingrese un numero para calcular fibo'))
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print('El numero de la serie de fibo: ',fib(imgresodenumfob))
