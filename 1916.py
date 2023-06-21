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
    # bus[a-1][b-1] = cost
start, goal = map(int, sys.stdin.readline().split())
start -= 1
goal -= 1

if start == goal :
    print(0)
    exit()

distance = [INF for _ in range(N)]
distance[start] = 0
visited = [0 for _ in range(N)]
temp = [0 for _ in range(N)]

i = 0
for i in range(N) :
    for j in range(N) :
        temp[j] = distance[j] + visited[j]
    mid = temp.index(min(temp))
    for j in range(N) :
        distance[j] = min(distance[j], distance[mid] + bus[mid][j])
    visited[mid] = math.inf
    # print(mid, distance)
print(distance[goal])
