import sys
     

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
            network_size[root_b] += network_size[root_a]
        elif rank[root_a] > rank[root_b] :
            parent[root_b] = root_a
            network_size[root_a] += network_size[root_b]
        elif rank[root_a] < rank[root_b] :
            parent[root_a] = root_b
            network_size[root_b] += network_size[root_a]

T = int(sys.stdin.readline())
for _ in range(T) :

    parent = [i for i in range(100000)]
    rank = [0 for _ in range(100000)]
    network_size = [1 for _ in range(100000)]
    names = []

    F = int(sys.stdin.readline())

    for f in range(F) :
        a, b = map(str, sys.stdin.readline().split())
        idx_a = 0
        idx_b = 0
        if a not in names :
            names.append(a)
            idx_a = len(names) - 1
        else : idx_a = names.index(a)
        if b not in names :
            names.append(b)
            idx_b = len(names) - 1
        else : idx_b = names.index(b)
        union(idx_a, idx_b)
        print(network_size[root(idx_a)])