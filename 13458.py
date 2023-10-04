import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

result = 0

for a in A:
    result += 1
    if a-B <= 0 : continue
    result += (a-B)//C
    if (a-B)%C != 0 :
        result += 1

print(result)