import sys

A = []
paper_numbers = 0
N = int(sys.stdin.readline())
for _ in range (N) :
    A.append(list(map(int, sys.stdin.readline().split())))

def check(mat, n) :


    num_m1 = 0
    num_0 = 0
    num_1 = 0
    
    for i in range(n) :
        for j in range(n) :
            if mat[i][j] == -1 :
                num_m1 += 1
            elif mat[i][j] == 0 :
                num_0 += 1
            elif mat[i][j] == 1 :
                num_1 += 1
            if num_m1*num_0 != 0 or num_0*num_1 != 0 or num_1*num_m1 != 0 : break
        if num_m1*num_0 != 0 or num_0*num_1 != 0 or num_1*num_m1 != 0 : break

    if num_m1 == n*n : return 1, 0, 0
    elif num_0 == n*n : return 0, 1, 0
    elif num_1 == n*n : return 0, 0, 1


    else :
        a = []

        a.append(check([mat[i][0:n//3] for i in range(0,n//3)], n//3))
        a.append(check([mat[i][0:n//3] for i in range(n//3,n//3*2)], n//3))
        a.append(check([mat[i][0:n//3] for i in range(n//3*2,n)], n//3))

        a.append(check([mat[i][n//3:n//3*2] for i in range(0,n//3)], n//3))
        a.append(check([mat[i][n//3:n//3*2] for i in range(n//3,n//3*2)], n//3))
        a.append(check([mat[i][n//3:n//3*2] for i in range(n//3*2,n)], n//3))

        a.append(check([mat[i][n//3*2:] for i in range(0,n//3)], n//3))
        a.append(check([mat[i][n//3*2:] for i in range(n//3,n//3*2)], n//3))
        a.append(check([mat[i][n//3*2:] for i in range(n//3*2,n)], n//3))

        a1 = 0
        a2 = 0
        a3 = 0
        for i in a :
            a1 += i[0]
            a2 += i[1]
            a3 += i[2]

        return a1, a2, a3

result = check(A,N)
print(result[0])
print(result[1])
print(result[2])