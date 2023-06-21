import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(N+1)]
visited[R] = 1
queue = deque()
edges = {}
for n in range(N+1) :
    edges[n] = []

for _ in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)
for v in edges :
    edges[v].sort()

def BFS() :
    queue.append(R)
    depth = 1
    while queue :
        cur_point = queue.popleft()
        for next_point in edges[cur_point] :
            if visited[next_point] == 0 :
                depth += 1
                visited[next_point] = depth
                queue.append(next_point)

BFS()
for v in visited[1:]: print(v)