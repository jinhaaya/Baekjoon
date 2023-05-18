import sys

A = []
B = []
N, M = map(int, sys.stdin.readline().split())
for _ in range (N) :
    A.append(list(map(int, sys.stdin.readline().split())))
M, K = map(int, sys.stdin.readline().split())
for _ in range (M) :
    B.append(list(map(int, sys.stdin.readline().split())))


for n in range(N):
    temp = []
    for k in range(K) :
        a = 0
        for m in range(M) :
            a += A[n][m] * B[m][k]
        temp.append(a)
    print(*temp)
