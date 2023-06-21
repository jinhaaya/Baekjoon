import sys

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def isCross(a, b) :
    x1, y1, x2, y2 = a
    x3, y3, x4, y4 = b
    if ccw(x1, y1, x2, y2, x3, y3)==ccw(x1, y1, x2, y2, x4, y4)==ccw(x3, y3, x4, y4, x1, y1)==ccw(x3, y3, x4, y4, x2, y2)==0 :
        if x1 >= min(x3, x4) and x1 <= max(x3, x4) and y1 >= min(y3, y4) and y1 <= max(y3, y4) : return True
        elif x2 >= min(x3, x4) and x2 <= max(x3, x4) and y2 >= min(y3, y4) and y2 <= max(y3, y4) : return True
        elif x3 >= min(x1, x2) and x3 <= max(x1, x2) and y3 >= min(y1, y2) and y3 <= max(y1, y2) : return True
        elif x4 >= min(x1, x2) and x4 <= max(x1, x2) and y4 >= min(y1, y2) and y4 <= max(y1, y2) : return True
        else : return False
    elif ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) <= 0: return True
    else : return False

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

N = int(sys.stdin.readline())
point = [None]
parent = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]

for _ in range(N) :
    point.append(list(map(int, sys.stdin.readline().split())))

for n in range(2, N+1) :
    for i in range(1, n) :
        if isCross(point[n], point[i]) :
            union(n, i)

root_dict = {}
for i in range(N) :
    a = root(i+1)
    if a not in root_dict :
        root_dict[a] = 1
    else : root_dict[a] += 1

print(len(root_dict))
print(max(root_dict.values()))