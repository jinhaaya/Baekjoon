import sys
from collections import deque
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = []
house = []
store = []
for i in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N) :
        if city[-1][j] == 1 :
            house.append([i, j])
        elif city[-1][j] == 2 :
            store.append([i, j])

total_chicken_distance = 0
combi = list(combinations(store, M))

min_val = 0
temp = []
for c in combi:
    chicken_distance = [9999999 for _ in range(len(house))]
    for dest in c:
        for i, v in enumerate(house):
            chicken_distance[i] = min(chicken_distance[i], abs(dest[0]-v[0])+abs(dest[1]-v[1]))
    temp.append(sum(chicken_distance))

print(min(temp))