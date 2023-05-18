import sys
from collections import deque

N = int(sys.stdin.readline())
edges = {} # start : [[end1, weight1], [end2, weight2], ...]

if N == 1 :
    print(0)
    exit()

for _ in range(N) :
    info = list(map(int, sys.stdin.readline().split()))
    node1 = info[0]
    for i in range(1, len(info)-1, 2) :
        node2 = info[i]
        weight = info[i+1]
        if node1 not in edges : edges[node1] = [[node2, weight]]
        else : edges[node1].append([node2, weight])
        if node2 not in edges : edges[node2] = [[node1, weight]]
        else : edges[node2].append([node1, weight])



def DFS(start_node) :
    max_weight = 0
    best_node = None

    # Initialize a stack with the start node and its weight
    stack = deque([(start_node, 0)])
    visited = set([start_node])

    while stack:
        cur_node, cur_weight = stack.pop()

        # Check if the current weight is greater than the maximum weight seen so far
        if cur_weight > max_weight:
            max_weight = cur_weight
            best_node = cur_node

        # Add unvisited children to the stack
        for child_node, child_weight in edges[cur_node]:
            if child_node not in visited:
                visited.add(child_node)
                stack.append((child_node, cur_weight+child_weight))

    return max_weight, best_node

result1 = DFS(node1)
result2 = DFS(result1[1])
print(result2[0])
