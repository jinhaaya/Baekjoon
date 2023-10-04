import sys
from collections import deque

dice = list(map(int, sys.stdin.readline().split()))
yoot_map_1 = [2*i for i in range(1, 21)]
yoot_map_2 = [10, 13, 16, 19, 25, 30, 35, 40]
yoot_map_3 = [20, 22, 24, 25, 30, 35, 40]
yoot_map_4 = [30, 28, 27, 26, 25, 30, 35, 40]
score = 0
dice_position = [(0, 1), (0, 1), (0, 1), (0, 1)] # (position, map)

yoot_dict = [{}, {}, {}, {}]
for i, v in enumerate(yoot_map_1):
    yoot_dict[1][i] = v
for i, v in enumerate(yoot_map_2):
    yoot_dict[2][i] = v
for i, v in enumerate(yoot_map_3):
    yoot_dict[3][i] = v
for i, v in enumerate(yoot_map_4):
    yoot_dict[4][i] = v

# if dice_position == 5, 10, 15 : move another way


print(yoot_dict)
heap = deque()
def BFS(num):
    for d in dice_position:
        cur_pos_score = 0
        d_pos = d[0]
        d_map_num = d[1]
        if d_pos+dice[num] >= len(yoot_dict[d_map_num]):
            cur_pos_score = 0
        elif d_pos+dice[num] < len(yoot_dict[d_map_num]):
            cur_pos_score = yoot_dict[d_map_num][d_pos+dice[num]]
        heap.append([])

