import sys

A = []
paper_numbers = 0
N = int(sys.stdin.readline())
for _ in range (N) :
    str = sys.stdin.readline()
    A.append([int(c) for c in str[:-1]])

def check(mat, n) :

    flag = 0
    for i in range(n) :
        for j in range(n) :
            if mat[i][j] == 1 :
                flag += 1
    if flag == 0 : return "0"
    elif flag == n*n : return "1"
    else :  
        a = check([mat[i][0:n//2] for i in range(0,n//2)], n//2)
        b = check([mat[i][0:n//2] for i in range(n//2,n)], n//2)
        c = check([mat[i][n//2:] for i in range(0,n//2)], n//2)
        d = check([mat[i][n//2:] for i in range(n//2,n)], n//2)
        return f"({a}{c}{b}{d})"

print(check(A,N))