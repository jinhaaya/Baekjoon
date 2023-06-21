import sys
from copy import deepcopy

N = int(sys.stdin.readline())
mat = []
for _ in range(N) :
    r, c = map(int, sys.stdin.readline().split())
    if not mat : 
        mat.append(r)
    mat.append(c)

DP_dict = {}
def DP(n, mat) :

    if n == 1 :
        return 0
    elif n == 2 :
        return mat[0]*mat[1]*mat[2]
    
    next = []
    for i in range(1, len(mat)-1) :
        a = mat[i-1]*mat[i]*mat[i+1]
        temp = deepcopy(mat)
        temp.pop(i)
        next.append(a+DP(n-1, temp))
    return min(next)

print(DP(N, mat))
## Memoization 해야됨