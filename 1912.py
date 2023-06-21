import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

if N == 1 :
    print(A[0])
    exit()

max_val = A[0]
temp = A[0]

for a in A[1:] :
    temp = max(temp+a, a)
    max_val = max(max_val, temp)
print(max_val)