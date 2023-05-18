import sys

A, B, C = map(int, sys.stdin.readline().split())

def mul(a, b, c) :
    a = a%c
    if b == 1 : return a
    elif b == 2 : return (a*a)%c
    else : 
        if b % 2 == 0 :
            return (mul(a, b//2, c)**2)%c
        else :
            return ((mul(a, b//2, c)**2)*a)%c


print(mul(A, B, C))