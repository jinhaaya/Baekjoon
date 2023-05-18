import sys

A = []
N, B = map(int, sys.stdin.readline().split())
for _ in range (N) :
    A.append(list(map(int, sys.stdin.readline().split())))

def mat_exp2(mat):
    N = len(mat)
    result = []
    for n in range(N):
        temp = []
        for k in range(N):
            a = 0
            for m in range(N):
                a += mat[n][m] * mat[m][k]
            temp.append(a%1000)
        result.append(temp)
    return result

def mat_mul(mat1, mat2) :
    N = len(mat1)
    result = []
    for n in range(N):
        temp = []
        for k in range(N):
            a = 0
            for m in range(N):
                a += mat1[n][m] * mat2[m][k]
            temp.append(a%1000)
        result.append(temp)
    return result

mat_exp_2 = mat_exp2(A)

def conquer(mat, exp) :
    N = len(mat)
    for row in range(N) :
        for col in range(N) :
            mat[row][col] %= 1000

    if exp == 1 : return mat
    elif exp == 2 : return mat_exp_2
    elif exp % 2 == 0 :
        return mat_exp2(conquer(mat, exp//2))
    else :
        return mat_mul(mat_exp2(conquer(mat, exp//2)), mat)

result = conquer(A, B)
for re in result :
    for r in re :
        print(r, end = " ")
    print("")