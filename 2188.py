import sys

N, M = map(int, sys.stdin.readline().split())
cow = {}
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    cow[i+1] = temp[1:]

def DFS(idx, connection, cow, visited) :
    for d in cow[idx] :
        if visited[d] == 1 :
            continue
        