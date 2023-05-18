import sys
import copy

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus = [0 for _ in range(N+1)]
for _ in range(M) :
    a, b, w = map(int, sys.stdin.readline().split())
    if bus[a] == 0 :
        bus[a] = [[b,w]]
    else :
        bus[a].append([b,w])

a, b = map(int, sys.stdin.readline().split())

def dfs(cur, visited) :
    if cur == b : return 0
    if bus[cur] == 0 : return 200000000
    min_weight = 200000000
    for way in bus[cur] :
        dest = way[0]
        weight = way[1]

        if dest in visited : continue

        temp_visited = copy.deepcopy(visited)
        temp_visited[cur] = 1
        next_weight = weight + dfs(dest, temp_visited)
        if next_weight >= 200000000 : continue

        min_weight = min(min_weight, next_weight)
    return min_weight

dictionary = {}
dictionary[a] = 1
print(dfs(a, dictionary))