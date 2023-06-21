import sys

N, M = map(int, sys.stdin.readline().split())
     
parent = [i for i in range(N)]
rank = [0 for _ in range(N)]

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

flag = 0
for i in range(1, M+1):
    a, b = map(int, sys.stdin.readline().split())
    if root(a) == root(b) and flag == 0:
        print(i)
        flag = 1
    elif flag == 0 :
        union(a, b)

if flag == 0 : print(0)
    
