import sys

N, M = map(int, sys.stdin.readline().split())

ways = []

def DFS(visited) :
    if len(visited) == M :
        ways.append(visited)
        return
    for i in range(1, N+1) :
        if len(visited) == 0 or visited[-1] < i :
            DFS(visited+[i])

DFS([])
for way in ways :
    for node in way :
        print(node, end = " ")
    print("")