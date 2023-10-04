import sys

N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
nutrient = [[5 for _ in range(N)] for _ in range(N)]

tree = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
tree.sort(key=lambda x:x[2])
for i in range(len(tree)) :
    tree[i][0] -= 1
    tree[i][1] -= 1

total_direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
def direction_around(y, x):
    result = []
    global total_direction
    for dy, dx in total_direction:
        if y+dy >= 0 and y+dy < N and x+dx >= 0 and x+dx < N:
            result.append([y+dy, x+dx])
    return result

around = [[direction_around(y, x) for x in range(N)] for y in range(N)]

for i in range(K):
    #spring
    next_tree = []
    dead_tree = []
    for y, x, age in tree:
        if nutrient[y][x] < age:
            dead_tree.append([y, x, age])
        else:
            next_tree.append([y, x, age])
            nutrient[y][x] -= age
    tree = next_tree

    for i in range(len(tree)):
        tree[i][2] += 1

    #summer
    for y, x, age in dead_tree:
        nutrient[y][x] += age//2

    #fall
    next_tree = []
    for y, x, age in tree:
        if age % 5 != 0: continue
        for around_y, around_x in around[y][x]:
            next_tree = [[around_y, around_x, 1]] + next_tree
    tree = next_tree + tree

    #winter
    for i in range(N):
        for j in range(N):
            nutrient[i][j] += A[i][j]

print(len(tree))
