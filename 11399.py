import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort()
sum = 0
for i, p in enumerate(P) :
    sum += (len(P)-i)*p
print(sum)