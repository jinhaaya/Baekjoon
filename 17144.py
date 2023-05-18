import sys

def direction(A) :
    dir = {}
    r = len(A)
    c = len(A[0])

    for ri in range(1, r-1) :
        for ci in range(1, c-1) :
            dir[(ri, ci)] = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for ri in range(1, r-1) :
        dir[(ri, 0)] = [[-1, 0], [1, 0], [0, 1]]
        dir[(ri, c-1)] = [[-1, 0], [1, 0], [0, -1]]
    for ci in range(1, c-1) :
        dir[(0, ci)] = [[1, 0], [0, -1], [0, 1]]
        dir[(r-1, ci)] = [[-1, 0], [0, -1], [0, 1]]

    dir[(0,0)] = [[1,0], [0,1]]
    dir[(0,c-1)] = [[1,0], [0,-1]]
    dir[(r-1,0)] = [[-1,0], [0,1]]
    dir[(r-1,c-1)] = [[-1,0], [0,-1]]

    dir[(conditioner[0], 0)] = []
    dir[(conditioner[0], 1)].remove([0, -1])
    dir[(conditioner[1], 0)] = []
    dir[(conditioner[1], 1)].remove([0, -1])

    try :
        dir[(conditioner[0]-1, 0)].remove([1, 0])
    except : pass
    try :
        dir[(conditioner[1]+1, 0)].remove([-1, 0])
    except : pass
    return dir



def diffusion(A) :
    additional = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R) :
        for j in range(C) :
            for d in dir[(i ,j)] :
                additional[i+d[0]][j+d[1]] += A[i][j]//5
            A[i][j] -= len(dir[(i, j)])*(A[i][j]//5)
    for i in range(R) :
        for j in range(C) :
            A[i][j] += additional[i][j]
    return A

def clean(A, conditioner) :

    # counterclockwise
    for i in range(conditioner[0]-1, 0, -1) :
        A[i][0] = A[i-1][0]
    for j in range(0, C-1) :
        A[0][j] = A[0][j+1]
    for i in range(0, conditioner[0]) :
        A[i][C-1] = A[i+1][C-1]
    for j in range(C-1, 1, -1) :
        A[conditioner[0]][j] = A[conditioner[0]][j-1]
    A[conditioner[0]][1] = 0

    # clockwise
    for i in range(conditioner[1]+1, R-1) :
        A[i][0] = A[i+1][0] 
    for j in range(0, C-1) :
        A[R-1][j] = A[R-1][j+1]
    for i in range(R-1, conditioner[1], -1) :
        A[i][C-1] = A[i-1][C-1]
    for j in range(C-1, 1, -1) :
        A[conditioner[1]][j] = A[conditioner[1]][j-1]
    A[conditioner[1]][1] = 0

    return A



R, C, T = map(int, sys.stdin.readline().split())
A = []
conditioner = []

for _ in range(R) :
    A.append(list(map(int, sys.stdin.readline().split())))

for i, a in enumerate(A) :
    if a[0] == -1 : conditioner.append(i)

dir = direction(A)

for t in range(T) :
    A = diffusion(A)
    # print(f"{t}초 후 :")
    # for a in A : print(a)
    # print("=============")
    A = clean(A, conditioner)
    # for a in A : print(a)
    # print("=============")

sum = 0
for i in range(R) :
    for j in range(C) :
        sum += A[i][j]


print(sum+2)