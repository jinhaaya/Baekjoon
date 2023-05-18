import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
length = len(nums)

ways = []

def DFS(visited) :
    if len(visited) == M :
        ways.append(visited)
        return
    for n in nums :
        if len(visited) > 0 and n < visited[-1] : continue
        else :
            DFS(visited+[n])

DFS([])
for way in ways :
    for node in way :
        print(node, end = " ")
    print("")