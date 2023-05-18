import sys

N, K = map(int, sys.stdin.readline().split())

def Fac(n) :
    if n == 0 : return 1
    elif n == 1 : return 1
    else : return Fac(n-1) * n

def BC(n, k) :
    return Fac(n)//(Fac(k)*Fac(n-k))

print(BC(N,K))