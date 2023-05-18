import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

dictionary = {}

def dp(n, k) :
    if k > (n+1)//2 or n <= 0 : return 0
    elif k == 1 : return n
    elif k == 0 : return 1
    else : 
        if (n-2, k-1) not in dictionary : dictionary[(n-2, k-1)] = dp(n-2, k-1) % 1000000003
        if (n-1, k) not in dictionary : dictionary[(n-1, k)] = dp(n-1, k) % 1000000003
        
        return (dictionary[(n-2, k-1)] + dictionary[(n-1, k)]) % 1000000003

print((dp(N-1, K) + dp(N-3, K-1))%1000000003)