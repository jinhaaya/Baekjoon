import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
switches = {}
queue = deque()
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M) :
    x, y, a, b = map(int, sys.stdin.readline().split())
    if (x,y) not in switches :
        switches[(x,y)] = [(a,b)]
    else :
        switches[(x,y)].append((a,b))

if (1,1) not in switches :
    print(1)
    exit()
else :
    for s in switches[(1,1)] :
        queue.append(s)
    visited[1][1] = 1

result = 1

def isNeighbor(a, b) :
    if a > 1 and visited[a-1][b] : return True
    elif a < N-1 and visited[a+1][b] : return True
    elif b > 0 and visited[a][b-1] : return True
    elif b < N-1 and visited[a][b+1] : return True
    else : return False

i = 0
def BFS() :
    global result, i
    while queue :
        if i > len(queue) : break
        a, b = queue.popleft()
        if not isNeighbor(a,b) :
            queue.append((a,b))
            i += 1
            continue
        i = 0
        result += 1
        visited[a][b] = 1
        if (a,b) in switches :
            for s in switches[(a,b)] :
                if visited[s[0]][s[1]] == 0 :
                    queue.append(s)
        # print(a, b, queue)

BFS()
print(result)