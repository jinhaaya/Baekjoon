import sys

A = []
paper_numbers = 0
N = int(sys.stdin.readline())
for _ in range (N) :
    A.append(list(map(int, sys.stdin.readline().split())))

def check(mat, n) :

    flag = 0
    for i in range(n) :
        for j in range(n) :
            if mat[i][j] == 1 :
                flag += 1
    if flag == 0 : return 1, 0
    elif flag == n*n : return 0, 1
    else :  
        a = check([mat[i][0:n//2] for i in range(0,n//2)], n//2)
        b = check([mat[i][0:n//2] for i in range(n//2,n)], n//2)
        c = check([mat[i][n//2:] for i in range(0,n//2)], n//2)
        d = check([mat[i][n//2:] for i in range(n//2,n)], n//2)
        return a[0]+b[0]+c[0]+d[0], a[1]+b[1]+c[1]+d[1]

result = check(A,N)
print(result[0])
print(result[1])