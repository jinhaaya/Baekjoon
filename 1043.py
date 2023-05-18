import sys

N, M = map(int, sys.stdin.readline().split())
truth = list(map(int, sys.stdin.readline().split()))
N_true = truth[0]
dict_party = {}

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

if N_true != 0 :
    truth = truth[1:]

parties = []
for m in range(M) :
    party = list(map(int, sys.stdin.readline().split()))[1:]
    parties.append(party)
    for idx, p in enumerate(party[:-1]) :
        union(party[idx], party[idx+1])

root_list = []
for i in range(N+1) :
    root_list.append(root(i))

result = 0
for i, t in enumerate(truth) :
    truth[i] = root_list[t]
for members in parties :
    flag = 0
    for member in members :
        if root_list[member] in truth :
            flag += 1
            break
    if flag == 0 : result += 1
print(result)
