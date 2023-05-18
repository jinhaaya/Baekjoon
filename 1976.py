import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
     
parent = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]

def root(a) :
    while parent[a] != a :
        a = parent[a]
    return a

def union(a, b) :
    root_a = root(a)
    root_b = root(b)
    if root_a != root_b :
        if rank[root_a] == rank[root_b] :
            parent[root_a] = root_b
            rank[root_b] += 1
        elif rank[root_a] > rank[root_b] :
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b] :
            parent[root_a] = root_b

for i in range(1, N+1):
    connect = list(map(int, sys.stdin.readline().split()))
    for idx, is_connected in enumerate(connect) :
        if is_connected == 1 :
            union(i, idx+1)

way = list(map(int, sys.stdin.readline().split()))

if len(way) == 0 or len(way) == 1 :
    print('YES')
else :
    first_root = root(way[0])
    for w in way[1:] :
        if first_root != root(w) :
            print('NO')
            exit()
    print('YES')