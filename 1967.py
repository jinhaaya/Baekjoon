import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
edges = {} # start : [[end1, weight1], [end2, weight2], ...]

for _ in range(N-1) :
    try :
        node1, node2, weight = map(int, sys.stdin.readline().split())
    except :
        break
    if node1 not in edges : edges[node1] = [[node2, weight]]
    else : edges[node1].append([node2, weight])
    if node2 not in edges : edges[node2] = [[node1, weight]]
    else : edges[node2].append([node1, weight])

def DFS(cur_node, cur_weight, cur_visited) :
    child = edges[cur_node]
    max_weight = 0
    best_weight = None
    best_node = None
    best_visited = None

    for c in child :
        next_node = c[0]
        next_weight = c[1]
        if next_node in cur_visited : continue
        temp_visited = cur_visited.copy()
        temp_visited.append(next_node)
        next_weight, next_visited = DFS(next_node, cur_weight+next_weight, temp_visited)
        if next_weight > max_weight :
            max_weight = next_weight
            best_weight = next_weight
            best_node = next_node
            best_visited = next_visited
    if best_node == None :
        return cur_weight, cur_visited
    else :
        return best_weight, best_visited

result1 = DFS(node1, 0, [node1])
print(DFS(result1[1][-1], 0, [result1[1][-1]])[0])