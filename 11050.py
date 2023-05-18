import sys

N, K = map(int, sys.stdin.readline().split())
fac_dictionary = {0:1, 1:1, 2:2}
exp_dictionary = {}
modula = 10007

cache = {0: 1}
def Fac(n):
    if n in cache:
        return cache[n]
    
    result = 1
    for i in range(1, n+1):
        result *= i
        cache[i] = result
    
    return result

def exp(n, d) :
    if d == 0 : return 1
    elif d == 1 : return n
    elif d % 2 == 0 :
        if (n, d//2) in exp_dictionary : 
            exp_dictionary[(n, d)] = exp_dictionary[(n, d//2)] ** 2
        else :
            exp_dictionary[(n, d)] = exp(n, d//2)**2
        return exp_dictionary[(n, d)]
    else : 
        if (n, d//2) in exp_dictionary : 
            exp_dictionary[(n, d)] = (exp_dictionary[(n, d//2)] ** 2) * n
        else :
            exp_dictionary[(n, d)] = (exp(n, d//2)**2) * n
        return exp_dictionary[(n, d)]

def BC(n, k) :
    return (Fac(n) % modula * exp(Fac(k)*Fac(n-k)%modula, modula-2) % modula) % modula

print(BC(N,K))