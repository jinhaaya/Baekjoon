import sys
from collections import deque

N = int(sys.stdin.readline())
like = [[] for _ in range(N**2+1)]
order = []
for _ in range(N**2):
    temp = list(map(int, sys.stdin.readline().split()))
    like[temp[0]] = temp[1:]
    like[temp[0]].sort()
    order.append(temp[0])
print(like)

# dict_empty_neighbor = {}
# for y in range(N):
#     for x in range(N):
#         dict_empty_neighbor[(y, x)] = 4
#         if y == 0 or y == N-1: dict_empty_neighbor[(y, x)] -= 1
#         if x == 0 or x == N-1: dict_empty_neighbor[(y, x)] -= 1

seat = [[0 for _ in range(N)] for _ in range(N)]
seat[1][1] = order[0]


def case_1(num):
    global like, seat, N
    max_list = []
    max_neighbor = 0
    for y in range(N) :
        for x in range(N) :
            if seat[y][x] != 0 : pass
            else :



for num in order[1:]:
    y, x = case_1(num)

print(seat)
