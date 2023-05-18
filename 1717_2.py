import sys

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

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

for _ in range(m):
    operator, a, b = map(int, sys.stdin.readline().split())
    if operator == 0:
        union(a, b)
    elif operator == 1:
        if root(a) == root(b):
            print("YES")
        else:
            print("NO")
# print(parent)
# print(rank)