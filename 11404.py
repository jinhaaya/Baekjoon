import sys
import math
INF = math.inf

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N) : bus[i][i] = 0
for _ in range(M) :
    a, b, cost = map(int, sys.stdin.readline().split())
    bus[a-1][b-1] = min(cost, bus[a-1][b-1])

# Floyd
for n in range(N) :
    for i in range(N) : 
        for j in range(N) :
            bus[i][j] = min(bus[i][j], bus[i][n] + bus[n][j])


for i in range(N) : 
    for j in range(N) :
        if bus[i][j] == math.inf : bus[i][j] = 0

for bu in bus :
    for b in bu :
        print(b, end = " ")
    print("")