import sys
sys.setrecursionlimit(200000)

N, M, R = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(N+1)]
visited[R] = 1
edges = {}
for n in range(N+1) :
    edges[n] = []

for _ in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)
for v in edges :
    edges[v].sort()

depth = 1
def DFS(cur_point) :
    global depth
    for next_point in edges[cur_point] :
        if visited[next_point] == 0 :
            depth += 1
            visited[next_point] = depth
            DFS(next_point)
    return

DFS(R)
for v in visited[1:]: print(v)