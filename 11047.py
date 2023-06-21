import sys

N, K = map(int, sys.stdin.readline().split())
A = []
for _ in range(N) : A.append(int(sys.stdin.readline()))
A.reverse()
i = 0
for a in A :
    print(K, a, i)
    i += K//a
    K -= K//a * a
print(i)