import sys

def fibonacci_recursivo(n):
    if n==1 or n==0:
        return 1

    return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)

def fibonacci_dimanico(n, memo={}):
    if n==1 or n==0:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado=fibonacci_dimanico(n-1,memo) + fibonacci_dimanico(n-2, memo)
        memo[n]=resultado
        
        return resultado


if __name__=='__main__':
    sys.setrecursionlimit(10002)
    n= int(input("Escoge un numero: "))
    resultado=fibonacci_dimanico(n)
    print(resultado)

